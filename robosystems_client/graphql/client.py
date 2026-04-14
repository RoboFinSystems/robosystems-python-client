"""Minimal GraphQL client wrapping httpx.

The Python client already depends on httpx, so we implement GraphQL POSTs
directly instead of pulling in a dedicated library like `gql`. Python's
GraphQL codegen ecosystem is weaker than TypeScript's, and since facade
methods reshape responses into existing generated Pydantic-style models,
we get end-to-end type safety without a codegen pipeline.

**Graph scoping.** The GraphQL endpoint is mounted per-graph at
`/extensions/{graph_id}/graphql`. Resolvers read the graph from the URL
path, never from GraphQL variables. `execute()` takes `graph_id` and
builds the per-request URL on each call.
"""

from __future__ import annotations

import re
from typing import Any

import httpx


class GraphQLError(Exception):
  """Raised when a GraphQL response contains errors or a non-2xx status.

  Attributes:
      message: Human-readable summary.
      errors: List of raw GraphQL error dicts from the response body
          (empty if the failure was an HTTP-level error).
      status_code: HTTP status code, or None if unknown.
  """

  def __init__(
    self,
    message: str,
    *,
    errors: list[dict[str, Any]] | None = None,
    status_code: int | None = None,
  ):
    super().__init__(message)
    self.errors = errors or []
    self.status_code = status_code


class GraphQLClient:
  """Synchronous GraphQL client for the per-graph `/extensions/{graph_id}/graphql` endpoint.

  Not a context manager — each `execute` call opens and closes its own
  httpx.Client, matching the existing facade convention of constructing
  a fresh `AuthenticatedClient` per request.
  """

  def __init__(
    self,
    base_url: str,
    *,
    token: str | None = None,
    headers: dict[str, str] | None = None,
    timeout: float = 60.0,
  ):
    self.base_url = base_url.rstrip("/")
    self.timeout = timeout
    self._headers: dict[str, str] = {"Content-Type": "application/json"}
    if headers:
      self._headers.update(headers)
    if token:
      # Match the existing facade convention: send the token as X-API-Key.
      self._headers["X-API-Key"] = token

  def _url_for(self, graph_id: str) -> str:
    if not graph_id:
      raise ValueError("graph_id must be a non-empty string")
    return f"{self.base_url}/extensions/{graph_id}/graphql"

  def execute(
    self,
    graph_id: str,
    query: str,
    variables: dict[str, Any] | None = None,
    *,
    operation_name: str | None = None,
  ) -> dict[str, Any]:
    """Execute a GraphQL query against the given graph and return the `data` dict.

    Raises:
        GraphQLError: If the HTTP response is non-2xx, or the body
            contains `errors[]`.
    """
    payload: dict[str, Any] = {"query": query}
    if variables is not None:
      payload["variables"] = variables
    if operation_name is not None:
      payload["operationName"] = operation_name

    url = self._url_for(graph_id)
    with httpx.Client(timeout=self.timeout) as client:
      response = client.post(url, json=payload, headers=self._headers)

    if response.status_code >= 400:
      raise GraphQLError(
        f"GraphQL request failed: HTTP {response.status_code}: {response.text[:500]}",
        status_code=response.status_code,
      )

    try:
      body = response.json()
    except ValueError as exc:
      raise GraphQLError(
        f"GraphQL response was not valid JSON: {exc}",
        status_code=response.status_code,
      ) from exc

    if body.get("errors"):
      errors = body["errors"]
      messages = ", ".join(e.get("message", "<unknown>") for e in errors)
      raise GraphQLError(
        f"GraphQL errors: {messages}",
        errors=errors,
        status_code=response.status_code,
      )

    return body.get("data") or {}


# ── Shared helpers for query parsers ──────────────────────────────────

_CAMEL_TO_SNAKE = re.compile(r"(?<!^)(?=[A-Z])")


def camel_to_snake(name: str) -> str:
  """Convert a camelCase field name to snake_case."""
  return _CAMEL_TO_SNAKE.sub("_", name).lower()


def keys_to_snake(value: Any) -> Any:
  """Recursively convert all dict keys from camelCase to snake_case.

  Preserves scalar values, lists, and nested dicts. Used at the GraphQL
  → Pydantic model boundary so the generated `from_dict` helpers (which
  expect snake_case) accept the camelCase JSON that Strawberry emits.
  """
  if isinstance(value, dict):
    return {camel_to_snake(k): keys_to_snake(v) for k, v in value.items()}
  if isinstance(value, list):
    return [keys_to_snake(item) for item in value]
  return value
