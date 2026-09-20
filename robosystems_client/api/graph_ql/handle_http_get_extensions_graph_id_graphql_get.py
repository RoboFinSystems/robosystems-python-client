from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/extensions/{graph_id}/graphql".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = response.json()
    return response_200

  if response.status_code == 401:
    response_401 = cast(Any, None)
    return response_401

  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403

  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = cast(Any, None)
    return response_429

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
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
) -> Response[Any | HTTPValidationError]:
  """GraphQL explorer (development only)

   Serves the in-browser GraphiQL explorer on deployments that enable it, which is development only —
  it is not mounted on the hosted API. Run queries with `POST` to the same URL.

  Queries are scoped by the URL: `graph_id` is a path parameter and never a query argument, so a
  document cannot name a graph that disagrees with the path it was sent to. Reads hit the operational
  (OLTP) extensions database, so they reflect the books as they stand now; the analytical projection
  is Cypher at `POST /v1/graphs/{graph_id}/query/cypher`.

  The schema is composed per deployment: ledger fields require RoboLedger and investor fields require
  RoboInvestor, and a disabled domain is absent from introspection rather than failing at runtime.
  Every field carries a description, so introspection is the authoritative, deployment-specific
  reference.

  **Auth**: pass `X-API-Key` (or a JWT `Authorization: Bearer` header). Unauthenticated introspection
  queries are deliberately allowed for SDK codegen; data queries require credentials and raise
  `UNAUTHENTICATED`.

  **Error codes**: `LEDGER_NOT_INITIALIZED`, `INVESTOR_NOT_INITIALIZED`, and `UNAUTHENTICATED` surface
  in the GraphQL `errors[].extensions.code` field. GraphQL reports errors with HTTP 200 and a
  populated `errors[]`, so check that array rather than the status code.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
  """GraphQL explorer (development only)

   Serves the in-browser GraphiQL explorer on deployments that enable it, which is development only —
  it is not mounted on the hosted API. Run queries with `POST` to the same URL.

  Queries are scoped by the URL: `graph_id` is a path parameter and never a query argument, so a
  document cannot name a graph that disagrees with the path it was sent to. Reads hit the operational
  (OLTP) extensions database, so they reflect the books as they stand now; the analytical projection
  is Cypher at `POST /v1/graphs/{graph_id}/query/cypher`.

  The schema is composed per deployment: ledger fields require RoboLedger and investor fields require
  RoboInvestor, and a disabled domain is absent from introspection rather than failing at runtime.
  Every field carries a description, so introspection is the authoritative, deployment-specific
  reference.

  **Auth**: pass `X-API-Key` (or a JWT `Authorization: Bearer` header). Unauthenticated introspection
  queries are deliberately allowed for SDK codegen; data queries require credentials and raise
  `UNAUTHENTICATED`.

  **Error codes**: `LEDGER_NOT_INITIALIZED`, `INVESTOR_NOT_INITIALIZED`, and `UNAUTHENTICATED` surface
  in the GraphQL `errors[].extensions.code` field. GraphQL reports errors with HTTP 200 and a
  populated `errors[]`, so check that array rather than the status code.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
  """GraphQL explorer (development only)

   Serves the in-browser GraphiQL explorer on deployments that enable it, which is development only —
  it is not mounted on the hosted API. Run queries with `POST` to the same URL.

  Queries are scoped by the URL: `graph_id` is a path parameter and never a query argument, so a
  document cannot name a graph that disagrees with the path it was sent to. Reads hit the operational
  (OLTP) extensions database, so they reflect the books as they stand now; the analytical projection
  is Cypher at `POST /v1/graphs/{graph_id}/query/cypher`.

  The schema is composed per deployment: ledger fields require RoboLedger and investor fields require
  RoboInvestor, and a disabled domain is absent from introspection rather than failing at runtime.
  Every field carries a description, so introspection is the authoritative, deployment-specific
  reference.

  **Auth**: pass `X-API-Key` (or a JWT `Authorization: Bearer` header). Unauthenticated introspection
  queries are deliberately allowed for SDK codegen; data queries require credentials and raise
  `UNAUTHENTICATED`.

  **Error codes**: `LEDGER_NOT_INITIALIZED`, `INVESTOR_NOT_INITIALIZED`, and `UNAUTHENTICATED` surface
  in the GraphQL `errors[].extensions.code` field. GraphQL reports errors with HTTP 200 and a
  populated `errors[]`, so check that array rather than the status code.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
  """GraphQL explorer (development only)

   Serves the in-browser GraphiQL explorer on deployments that enable it, which is development only —
  it is not mounted on the hosted API. Run queries with `POST` to the same URL.

  Queries are scoped by the URL: `graph_id` is a path parameter and never a query argument, so a
  document cannot name a graph that disagrees with the path it was sent to. Reads hit the operational
  (OLTP) extensions database, so they reflect the books as they stand now; the analytical projection
  is Cypher at `POST /v1/graphs/{graph_id}/query/cypher`.

  The schema is composed per deployment: ledger fields require RoboLedger and investor fields require
  RoboInvestor, and a disabled domain is absent from introspection rather than failing at runtime.
  Every field carries a description, so introspection is the authoritative, deployment-specific
  reference.

  **Auth**: pass `X-API-Key` (or a JWT `Authorization: Bearer` header). Unauthenticated introspection
  queries are deliberately allowed for SDK codegen; data queries require credentials and raise
  `UNAUTHENTICATED`.

  **Error codes**: `LEDGER_NOT_INITIALIZED`, `INVESTOR_NOT_INITIALIZED`, and `UNAUTHENTICATED` surface
  in the GraphQL `errors[].extensions.code` field. GraphQL reports errors with HTTP 200 and a
  populated `errors[]`, so check that array rather than the status code.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
