from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.sync_connection_request import SyncConnectionRequest
from ...models.sync_connection_response_syncconnection import (
  SyncConnectionResponseSyncconnection,
)
from ...types import Response


def _get_kwargs(
  graph_id: str,
  connection_id: str,
  *,
  body: SyncConnectionRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/connections/{connection_id}/sync",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]
]:
  if response.status_code == 200:
    response_200 = SyncConnectionResponseSyncconnection.from_dict(response.json())

    return response_200

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

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
) -> Response[
  Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]
]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SyncConnectionRequest,
) -> Response[
  Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]
]:
  """Sync Connection

   Trigger a data synchronization for the connection.

  Initiates data sync based on provider type:

  **SEC Sync**:
  - Downloads latest filings from EDGAR
  - Parses XBRL data and updates graph
  - Typically completes in 5-10 minutes

  **QuickBooks Sync**:
  - Fetches latest transactions and balances
  - Updates chart of accounts
  - Generates fresh trial balance
  - Duration depends on data volume

  **Plaid Sync**:
  - Retrieves recent bank transactions
  - Updates account balances
  - Categorizes new transactions

  Note:
  This operation is included - no credit consumption required.

  Returns a task ID for monitoring sync progress.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      body (SyncConnectionRequest): Request to sync a connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SyncConnectionRequest,
) -> Optional[
  Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]
]:
  """Sync Connection

   Trigger a data synchronization for the connection.

  Initiates data sync based on provider type:

  **SEC Sync**:
  - Downloads latest filings from EDGAR
  - Parses XBRL data and updates graph
  - Typically completes in 5-10 minutes

  **QuickBooks Sync**:
  - Fetches latest transactions and balances
  - Updates chart of accounts
  - Generates fresh trial balance
  - Duration depends on data volume

  **Plaid Sync**:
  - Retrieves recent bank transactions
  - Updates account balances
  - Categorizes new transactions

  Note:
  This operation is included - no credit consumption required.

  Returns a task ID for monitoring sync progress.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      body (SyncConnectionRequest): Request to sync a connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]
  """

  return sync_detailed(
    graph_id=graph_id,
    connection_id=connection_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SyncConnectionRequest,
) -> Response[
  Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]
]:
  """Sync Connection

   Trigger a data synchronization for the connection.

  Initiates data sync based on provider type:

  **SEC Sync**:
  - Downloads latest filings from EDGAR
  - Parses XBRL data and updates graph
  - Typically completes in 5-10 minutes

  **QuickBooks Sync**:
  - Fetches latest transactions and balances
  - Updates chart of accounts
  - Generates fresh trial balance
  - Duration depends on data volume

  **Plaid Sync**:
  - Retrieves recent bank transactions
  - Updates account balances
  - Categorizes new transactions

  Note:
  This operation is included - no credit consumption required.

  Returns a task ID for monitoring sync progress.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      body (SyncConnectionRequest): Request to sync a connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SyncConnectionRequest,
) -> Optional[
  Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]
]:
  """Sync Connection

   Trigger a data synchronization for the connection.

  Initiates data sync based on provider type:

  **SEC Sync**:
  - Downloads latest filings from EDGAR
  - Parses XBRL data and updates graph
  - Typically completes in 5-10 minutes

  **QuickBooks Sync**:
  - Fetches latest transactions and balances
  - Updates chart of accounts
  - Generates fresh trial balance
  - Duration depends on data volume

  **Plaid Sync**:
  - Retrieves recent bank transactions
  - Updates account balances
  - Categorizes new transactions

  Note:
  This operation is included - no credit consumption required.

  Returns a task ID for monitoring sync progress.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      body (SyncConnectionRequest): Request to sync a connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, SyncConnectionResponseSyncconnection]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      connection_id=connection_id,
      client=client,
      body=body,
    )
  ).parsed
