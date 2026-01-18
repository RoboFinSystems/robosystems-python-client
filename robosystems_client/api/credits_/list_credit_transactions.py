from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detailed_transactions_response import DetailedTransactionsResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  transaction_type: None | str | Unset = UNSET,
  operation_type: None | str | Unset = UNSET,
  start_date: None | str | Unset = UNSET,
  end_date: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_transaction_type: None | str | Unset
  if isinstance(transaction_type, Unset):
    json_transaction_type = UNSET
  else:
    json_transaction_type = transaction_type
  params["transaction_type"] = json_transaction_type

  json_operation_type: None | str | Unset
  if isinstance(operation_type, Unset):
    json_operation_type = UNSET
  else:
    json_operation_type = operation_type
  params["operation_type"] = json_operation_type

  json_start_date: None | str | Unset
  if isinstance(start_date, Unset):
    json_start_date = UNSET
  else:
    json_start_date = start_date
  params["start_date"] = json_start_date

  json_end_date: None | str | Unset
  if isinstance(end_date, Unset):
    json_end_date = UNSET
  else:
    json_end_date = end_date
  params["end_date"] = json_end_date

  params["limit"] = limit

  params["offset"] = offset

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/credits/transactions".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DetailedTransactionsResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = DetailedTransactionsResponse.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

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
) -> Response[DetailedTransactionsResponse | ErrorResponse | HTTPValidationError]:
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
  transaction_type: None | str | Unset = UNSET,
  operation_type: None | str | Unset = UNSET,
  start_date: None | str | Unset = UNSET,
  end_date: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[DetailedTransactionsResponse | ErrorResponse | HTTPValidationError]:
  """List Credit Transactions

   Retrieve detailed credit transaction history for the specified graph.

  This enhanced endpoint provides:
  - Detailed transaction records with idempotency information
  - Summary by operation type to identify high-consumption operations
  - Date range filtering for analysis
  - Metadata search capabilities

  Transaction types include:
  - ALLOCATION: Monthly credit allocations
  - CONSUMPTION: Credit usage for operations
  - BONUS: Bonus credits added by admins
  - REFUND: Credit refunds

  No credits are consumed for viewing transaction history.

  Args:
      graph_id (str): Graph database identifier
      transaction_type (None | str | Unset): Filter by transaction type (allocation,
          consumption, bonus, refund)
      operation_type (None | str | Unset): Filter by operation type (e.g., entity_lookup,
          cypher_query)
      start_date (None | str | Unset): Start date for filtering (ISO format: YYYY-MM-DD)
      end_date (None | str | Unset): End date for filtering (ISO format: YYYY-MM-DD)
      limit (int | Unset): Maximum number of transactions to return Default: 100.
      offset (int | Unset): Number of transactions to skip Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[DetailedTransactionsResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    transaction_type=transaction_type,
    operation_type=operation_type,
    start_date=start_date,
    end_date=end_date,
    limit=limit,
    offset=offset,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  transaction_type: None | str | Unset = UNSET,
  operation_type: None | str | Unset = UNSET,
  start_date: None | str | Unset = UNSET,
  end_date: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> DetailedTransactionsResponse | ErrorResponse | HTTPValidationError | None:
  """List Credit Transactions

   Retrieve detailed credit transaction history for the specified graph.

  This enhanced endpoint provides:
  - Detailed transaction records with idempotency information
  - Summary by operation type to identify high-consumption operations
  - Date range filtering for analysis
  - Metadata search capabilities

  Transaction types include:
  - ALLOCATION: Monthly credit allocations
  - CONSUMPTION: Credit usage for operations
  - BONUS: Bonus credits added by admins
  - REFUND: Credit refunds

  No credits are consumed for viewing transaction history.

  Args:
      graph_id (str): Graph database identifier
      transaction_type (None | str | Unset): Filter by transaction type (allocation,
          consumption, bonus, refund)
      operation_type (None | str | Unset): Filter by operation type (e.g., entity_lookup,
          cypher_query)
      start_date (None | str | Unset): Start date for filtering (ISO format: YYYY-MM-DD)
      end_date (None | str | Unset): End date for filtering (ISO format: YYYY-MM-DD)
      limit (int | Unset): Maximum number of transactions to return Default: 100.
      offset (int | Unset): Number of transactions to skip Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      DetailedTransactionsResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    transaction_type=transaction_type,
    operation_type=operation_type,
    start_date=start_date,
    end_date=end_date,
    limit=limit,
    offset=offset,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  transaction_type: None | str | Unset = UNSET,
  operation_type: None | str | Unset = UNSET,
  start_date: None | str | Unset = UNSET,
  end_date: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[DetailedTransactionsResponse | ErrorResponse | HTTPValidationError]:
  """List Credit Transactions

   Retrieve detailed credit transaction history for the specified graph.

  This enhanced endpoint provides:
  - Detailed transaction records with idempotency information
  - Summary by operation type to identify high-consumption operations
  - Date range filtering for analysis
  - Metadata search capabilities

  Transaction types include:
  - ALLOCATION: Monthly credit allocations
  - CONSUMPTION: Credit usage for operations
  - BONUS: Bonus credits added by admins
  - REFUND: Credit refunds

  No credits are consumed for viewing transaction history.

  Args:
      graph_id (str): Graph database identifier
      transaction_type (None | str | Unset): Filter by transaction type (allocation,
          consumption, bonus, refund)
      operation_type (None | str | Unset): Filter by operation type (e.g., entity_lookup,
          cypher_query)
      start_date (None | str | Unset): Start date for filtering (ISO format: YYYY-MM-DD)
      end_date (None | str | Unset): End date for filtering (ISO format: YYYY-MM-DD)
      limit (int | Unset): Maximum number of transactions to return Default: 100.
      offset (int | Unset): Number of transactions to skip Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[DetailedTransactionsResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    transaction_type=transaction_type,
    operation_type=operation_type,
    start_date=start_date,
    end_date=end_date,
    limit=limit,
    offset=offset,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  transaction_type: None | str | Unset = UNSET,
  operation_type: None | str | Unset = UNSET,
  start_date: None | str | Unset = UNSET,
  end_date: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> DetailedTransactionsResponse | ErrorResponse | HTTPValidationError | None:
  """List Credit Transactions

   Retrieve detailed credit transaction history for the specified graph.

  This enhanced endpoint provides:
  - Detailed transaction records with idempotency information
  - Summary by operation type to identify high-consumption operations
  - Date range filtering for analysis
  - Metadata search capabilities

  Transaction types include:
  - ALLOCATION: Monthly credit allocations
  - CONSUMPTION: Credit usage for operations
  - BONUS: Bonus credits added by admins
  - REFUND: Credit refunds

  No credits are consumed for viewing transaction history.

  Args:
      graph_id (str): Graph database identifier
      transaction_type (None | str | Unset): Filter by transaction type (allocation,
          consumption, bonus, refund)
      operation_type (None | str | Unset): Filter by operation type (e.g., entity_lookup,
          cypher_query)
      start_date (None | str | Unset): Start date for filtering (ISO format: YYYY-MM-DD)
      end_date (None | str | Unset): End date for filtering (ISO format: YYYY-MM-DD)
      limit (int | Unset): Maximum number of transactions to return Default: 100.
      offset (int | Unset): Number of transactions to skip Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      DetailedTransactionsResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      transaction_type=transaction_type,
      operation_type=operation_type,
      start_date=start_date,
      end_date=end_date,
      limit=limit,
      offset=offset,
    )
  ).parsed
