from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.operation_envelope import OperationEnvelope
from ...models.sync_connection_request import SyncConnectionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  connection_id: str,
  *,
  body: SyncConnectionRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/connections/{connection_id}/sync".format(
      graph_id=quote(str(graph_id), safe=""),
      connection_id=quote(str(connection_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | OperationEnvelope | None:
  if response.status_code == 202:
    response_202 = OperationEnvelope.from_dict(response.json())

    return response_202

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 409:
    response_409 = ErrorResponse.from_dict(response.json())

    return response_409

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if response.status_code == 504:
    response_504 = ErrorResponse.from_dict(response.json())

    return response_504

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | OperationEnvelope]:
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
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | OperationEnvelope]:
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

  Note:
  This operation is included - no credit consumption required.

  Returns an `OperationEnvelope` with an `operationId` for tracking sync progress.
  Supports `Idempotency-Key` header to safely retry without triggering duplicate syncs.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      idempotency_key (None | str | Unset):
      body (SyncConnectionRequest): Request to sync a connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | OperationEnvelope]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
    body=body,
    idempotency_key=idempotency_key,
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
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | OperationEnvelope | None:
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

  Note:
  This operation is included - no credit consumption required.

  Returns an `OperationEnvelope` with an `operationId` for tracking sync progress.
  Supports `Idempotency-Key` header to safely retry without triggering duplicate syncs.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      idempotency_key (None | str | Unset):
      body (SyncConnectionRequest): Request to sync a connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | OperationEnvelope
  """

  return sync_detailed(
    graph_id=graph_id,
    connection_id=connection_id,
    client=client,
    body=body,
    idempotency_key=idempotency_key,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SyncConnectionRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | OperationEnvelope]:
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

  Note:
  This operation is included - no credit consumption required.

  Returns an `OperationEnvelope` with an `operationId` for tracking sync progress.
  Supports `Idempotency-Key` header to safely retry without triggering duplicate syncs.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      idempotency_key (None | str | Unset):
      body (SyncConnectionRequest): Request to sync a connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | OperationEnvelope]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
    body=body,
    idempotency_key=idempotency_key,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SyncConnectionRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | OperationEnvelope | None:
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

  Note:
  This operation is included - no credit consumption required.

  Returns an `OperationEnvelope` with an `operationId` for tracking sync progress.
  Supports `Idempotency-Key` header to safely retry without triggering duplicate syncs.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      idempotency_key (None | str | Unset):
      body (SyncConnectionRequest): Request to sync a connection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | OperationEnvelope
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      connection_id=connection_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
