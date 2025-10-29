from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connection_response import ConnectionResponse
from ...models.create_connection_request import CreateConnectionRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: CreateConnectionRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/connections",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 201:
    response_201 = ConnectionResponse.from_dict(response.json())

    return response_201

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 409:
    response_409 = ErrorResponse.from_dict(response.json())

    return response_409

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
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
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
  body: CreateConnectionRequest,
) -> Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  """Create Connection

   Create a new data connection for external system integration.

  This endpoint initiates connections to external data sources:

  **SEC Connections**:
  - Provide entity CIK for automatic filing retrieval
  - No authentication needed
  - Begins immediate data sync

  **QuickBooks Connections**:
  - Returns OAuth URL for authorization
  - Requires admin permissions in QuickBooks
  - Complete with OAuth callback

  **Plaid Connections**:
  - Returns Plaid Link token
  - User completes bank authentication
  - Exchange public token for access

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      body (CreateConnectionRequest): Request to create a new connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateConnectionRequest,
) -> Optional[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  """Create Connection

   Create a new data connection for external system integration.

  This endpoint initiates connections to external data sources:

  **SEC Connections**:
  - Provide entity CIK for automatic filing retrieval
  - No authentication needed
  - Begins immediate data sync

  **QuickBooks Connections**:
  - Returns OAuth URL for authorization
  - Requires admin permissions in QuickBooks
  - Complete with OAuth callback

  **Plaid Connections**:
  - Returns Plaid Link token
  - User completes bank authentication
  - Exchange public token for access

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      body (CreateConnectionRequest): Request to create a new connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ConnectionResponse, ErrorResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateConnectionRequest,
) -> Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  """Create Connection

   Create a new data connection for external system integration.

  This endpoint initiates connections to external data sources:

  **SEC Connections**:
  - Provide entity CIK for automatic filing retrieval
  - No authentication needed
  - Begins immediate data sync

  **QuickBooks Connections**:
  - Returns OAuth URL for authorization
  - Requires admin permissions in QuickBooks
  - Complete with OAuth callback

  **Plaid Connections**:
  - Returns Plaid Link token
  - User completes bank authentication
  - Exchange public token for access

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      body (CreateConnectionRequest): Request to create a new connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateConnectionRequest,
) -> Optional[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  """Create Connection

   Create a new data connection for external system integration.

  This endpoint initiates connections to external data sources:

  **SEC Connections**:
  - Provide entity CIK for automatic filing retrieval
  - No authentication needed
  - Begins immediate data sync

  **QuickBooks Connections**:
  - Returns OAuth URL for authorization
  - Requires admin permissions in QuickBooks
  - Complete with OAuth callback

  **Plaid Connections**:
  - Returns Plaid Link token
  - User completes bank authentication
  - Exchange public token for access

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      body (CreateConnectionRequest): Request to create a new connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ConnectionResponse, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
