from http import HTTPStatus
from typing import Any, Optional, Union

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
  entity_id: Union[None, Unset, str] = UNSET,
  provider: Union[ListConnectionsProviderType0, None, Unset] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_entity_id: Union[None, Unset, str]
  if isinstance(entity_id, Unset):
    json_entity_id = UNSET
  else:
    json_entity_id = entity_id
  params["entity_id"] = json_entity_id

  json_provider: Union[None, Unset, str]
  if isinstance(provider, Unset):
    json_provider = UNSET
  elif isinstance(provider, ListConnectionsProviderType0):
    json_provider = provider.value
  else:
    json_provider = provider
  params["provider"] = json_provider

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/connections",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, HTTPValidationError, list["ConnectionResponse"]]]:
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
  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, HTTPValidationError, list["ConnectionResponse"]]]:
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
  entity_id: Union[None, Unset, str] = UNSET,
  provider: Union[ListConnectionsProviderType0, None, Unset] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, HTTPValidationError, list["ConnectionResponse"]]]:
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
      graph_id (str): Graph database identifier
      entity_id (Union[None, Unset, str]): Filter by entity ID
      provider (Union[ListConnectionsProviderType0, None, Unset]): Filter by provider type
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, list['ConnectionResponse']]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    entity_id=entity_id,
    provider=provider,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  entity_id: Union[None, Unset, str] = UNSET,
  provider: Union[ListConnectionsProviderType0, None, Unset] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, HTTPValidationError, list["ConnectionResponse"]]]:
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
      graph_id (str): Graph database identifier
      entity_id (Union[None, Unset, str]): Filter by entity ID
      provider (Union[ListConnectionsProviderType0, None, Unset]): Filter by provider type
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, list['ConnectionResponse']]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    entity_id=entity_id,
    provider=provider,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  entity_id: Union[None, Unset, str] = UNSET,
  provider: Union[ListConnectionsProviderType0, None, Unset] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, HTTPValidationError, list["ConnectionResponse"]]]:
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
      graph_id (str): Graph database identifier
      entity_id (Union[None, Unset, str]): Filter by entity ID
      provider (Union[ListConnectionsProviderType0, None, Unset]): Filter by provider type
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, list['ConnectionResponse']]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    entity_id=entity_id,
    provider=provider,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  entity_id: Union[None, Unset, str] = UNSET,
  provider: Union[ListConnectionsProviderType0, None, Unset] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, HTTPValidationError, list["ConnectionResponse"]]]:
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
      graph_id (str): Graph database identifier
      entity_id (Union[None, Unset, str]): Filter by entity ID
      provider (Union[ListConnectionsProviderType0, None, Unset]): Filter by provider type
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, list['ConnectionResponse']]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      entity_id=entity_id,
      provider=provider,
      token=token,
      authorization=authorization,
    )
  ).parsed
