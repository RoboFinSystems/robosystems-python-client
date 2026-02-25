from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connection_response import ConnectionResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_connections_provider_type_0 import ListConnectionsProviderType0
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  entity_id: None | str | Unset = UNSET,
  provider: ListConnectionsProviderType0 | None | Unset = UNSET,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_entity_id: None | str | Unset
  if isinstance(entity_id, Unset):
    json_entity_id = UNSET
  else:
    json_entity_id = entity_id
  params["entity_id"] = json_entity_id

  json_provider: None | str | Unset
  if isinstance(provider, Unset):
    json_provider = UNSET
  elif isinstance(provider, ListConnectionsProviderType0):
    json_provider = provider.value
  else:
    json_provider = provider
  params["provider"] = json_provider

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/connections".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | list[ConnectionResponse] | None:
  if response.status_code == 200:
    response_200 = []
    _response_200 = response.json()
    for response_200_item_data in _response_200:
      response_200_item = ConnectionResponse.from_dict(response_200_item_data)

      response_200.append(response_200_item)

    return response_200

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | list[ConnectionResponse]]:
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
  entity_id: None | str | Unset = UNSET,
  provider: ListConnectionsProviderType0 | None | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | list[ConnectionResponse]]:
  """List Connections

   List all data connections in the graph.

  Returns active and inactive connections with their current status.
  Connections can be filtered by:
  - **Entity**: Show connections for a specific entity
  - **Provider**: Filter by connection type (sec, quickbooks, plaid)

  Each connection shows:
  - Current sync status and health
  - Last successful sync timestamp
  - Configuration metadata
  - Error messages if any

  No credits are consumed for listing connections.

  Args:
      graph_id (str):
      entity_id (None | str | Unset): Filter by entity ID
      provider (ListConnectionsProviderType0 | None | Unset): Filter by provider type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | list[ConnectionResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    entity_id=entity_id,
    provider=provider,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  entity_id: None | str | Unset = UNSET,
  provider: ListConnectionsProviderType0 | None | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | list[ConnectionResponse] | None:
  """List Connections

   List all data connections in the graph.

  Returns active and inactive connections with their current status.
  Connections can be filtered by:
  - **Entity**: Show connections for a specific entity
  - **Provider**: Filter by connection type (sec, quickbooks, plaid)

  Each connection shows:
  - Current sync status and health
  - Last successful sync timestamp
  - Configuration metadata
  - Error messages if any

  No credits are consumed for listing connections.

  Args:
      graph_id (str):
      entity_id (None | str | Unset): Filter by entity ID
      provider (ListConnectionsProviderType0 | None | Unset): Filter by provider type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | list[ConnectionResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    entity_id=entity_id,
    provider=provider,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  entity_id: None | str | Unset = UNSET,
  provider: ListConnectionsProviderType0 | None | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | list[ConnectionResponse]]:
  """List Connections

   List all data connections in the graph.

  Returns active and inactive connections with their current status.
  Connections can be filtered by:
  - **Entity**: Show connections for a specific entity
  - **Provider**: Filter by connection type (sec, quickbooks, plaid)

  Each connection shows:
  - Current sync status and health
  - Last successful sync timestamp
  - Configuration metadata
  - Error messages if any

  No credits are consumed for listing connections.

  Args:
      graph_id (str):
      entity_id (None | str | Unset): Filter by entity ID
      provider (ListConnectionsProviderType0 | None | Unset): Filter by provider type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | list[ConnectionResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    entity_id=entity_id,
    provider=provider,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  entity_id: None | str | Unset = UNSET,
  provider: ListConnectionsProviderType0 | None | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | list[ConnectionResponse] | None:
  """List Connections

   List all data connections in the graph.

  Returns active and inactive connections with their current status.
  Connections can be filtered by:
  - **Entity**: Show connections for a specific entity
  - **Provider**: Filter by connection type (sec, quickbooks, plaid)

  Each connection shows:
  - Current sync status and health
  - Last successful sync timestamp
  - Configuration metadata
  - Error messages if any

  No credits are consumed for listing connections.

  Args:
      graph_id (str):
      entity_id (None | str | Unset): Filter by entity ID
      provider (ListConnectionsProviderType0 | None | Unset): Filter by provider type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | list[ConnectionResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      entity_id=entity_id,
      provider=provider,
    )
  ).parsed
