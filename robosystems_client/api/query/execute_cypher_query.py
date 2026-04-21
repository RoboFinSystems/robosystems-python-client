from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cypher_query_request import CypherQueryRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.response_mode import ResponseMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: CypherQueryRequest,
  mode: None | ResponseMode | Unset = UNSET,
  chunk_size: int | None | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  params: dict[str, Any] = {}

  json_mode: None | str | Unset
  if isinstance(mode, Unset):
    json_mode = UNSET
  elif isinstance(mode, ResponseMode):
    json_mode = mode.value
  else:
    json_mode = mode
  params["mode"] = json_mode

  json_chunk_size: int | None | Unset
  if isinstance(chunk_size, Unset):
    json_chunk_size = UNSET
  else:
    json_chunk_size = chunk_size
  params["chunk_size"] = json_chunk_size

  params["test_mode"] = test_mode

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/query".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    content_type = response.headers.get("content-type", "")
    if (
      "application/x-ndjson" in content_type
      or response.headers.get("x-stream-format") == "ndjson"
    ):
      return None
    response_200 = response.json()
    return response_200

  if response.status_code == 202:
    response_202 = cast(Any, None)
    return response_202

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 408:
    response_408 = cast(Any, None)
    return response_408

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if response.status_code == 503:
    response_503 = cast(Any, None)
    return response_503

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CypherQueryRequest,
  mode: None | ResponseMode | Unset = UNSET,
  chunk_size: int | None | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  r"""Execute Cypher Query

   Main graphs are **read-only** — use the staging pipeline to ingest data. Subgraphs support full
  writes. Always use parameterized queries (`parameters: {\"key\": \"val\"}`) to prevent injection.
  Response modes: `auto` (default), `sync`, `async`, `stream`. Under load, queries are queued and emit
  an `operation_id` for SSE monitoring at `/v1/operations/{id}/stream`.

  Args:
      graph_id (str):
      mode (None | ResponseMode | Unset): Response mode override
      chunk_size (int | None | Unset): Rows per chunk for streaming
      test_mode (bool | Unset): Enable test mode for better debugging Default: False.
      body (CypherQueryRequest): Request model for Cypher query execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    mode=mode,
    chunk_size=chunk_size,
    test_mode=test_mode,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CypherQueryRequest,
  mode: None | ResponseMode | Unset = UNSET,
  chunk_size: int | None | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> Any | ErrorResponse | HTTPValidationError | None:
  r"""Execute Cypher Query

   Main graphs are **read-only** — use the staging pipeline to ingest data. Subgraphs support full
  writes. Always use parameterized queries (`parameters: {\"key\": \"val\"}`) to prevent injection.
  Response modes: `auto` (default), `sync`, `async`, `stream`. Under load, queries are queued and emit
  an `operation_id` for SSE monitoring at `/v1/operations/{id}/stream`.

  Args:
      graph_id (str):
      mode (None | ResponseMode | Unset): Response mode override
      chunk_size (int | None | Unset): Rows per chunk for streaming
      test_mode (bool | Unset): Enable test mode for better debugging Default: False.
      body (CypherQueryRequest): Request model for Cypher query execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
    mode=mode,
    chunk_size=chunk_size,
    test_mode=test_mode,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CypherQueryRequest,
  mode: None | ResponseMode | Unset = UNSET,
  chunk_size: int | None | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  r"""Execute Cypher Query

   Main graphs are **read-only** — use the staging pipeline to ingest data. Subgraphs support full
  writes. Always use parameterized queries (`parameters: {\"key\": \"val\"}`) to prevent injection.
  Response modes: `auto` (default), `sync`, `async`, `stream`. Under load, queries are queued and emit
  an `operation_id` for SSE monitoring at `/v1/operations/{id}/stream`.

  Args:
      graph_id (str):
      mode (None | ResponseMode | Unset): Response mode override
      chunk_size (int | None | Unset): Rows per chunk for streaming
      test_mode (bool | Unset): Enable test mode for better debugging Default: False.
      body (CypherQueryRequest): Request model for Cypher query execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    mode=mode,
    chunk_size=chunk_size,
    test_mode=test_mode,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CypherQueryRequest,
  mode: None | ResponseMode | Unset = UNSET,
  chunk_size: int | None | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> Any | ErrorResponse | HTTPValidationError | None:
  r"""Execute Cypher Query

   Main graphs are **read-only** — use the staging pipeline to ingest data. Subgraphs support full
  writes. Always use parameterized queries (`parameters: {\"key\": \"val\"}`) to prevent injection.
  Response modes: `auto` (default), `sync`, `async`, `stream`. Under load, queries are queued and emit
  an `operation_id` for SSE monitoring at `/v1/operations/{id}/stream`.

  Args:
      graph_id (str):
      mode (None | ResponseMode | Unset): Response mode override
      chunk_size (int | None | Unset): Rows per chunk for streaming
      test_mode (bool | Unset): Enable test mode for better debugging Default: False.
      body (CypherQueryRequest): Request model for Cypher query execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      mode=mode,
      chunk_size=chunk_size,
      test_mode=test_mode,
    )
  ).parsed
