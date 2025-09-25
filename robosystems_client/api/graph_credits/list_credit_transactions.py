from http import HTTPStatus
from typing import Any, Optional, Union

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
  transaction_type: Union[None, Unset, str] = UNSET,
  operation_type: Union[None, Unset, str] = UNSET,
  start_date: Union[None, Unset, str] = UNSET,
  end_date: Union[None, Unset, str] = UNSET,
  limit: Union[Unset, int] = 100,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_transaction_type: Union[None, Unset, str]
  if isinstance(transaction_type, Unset):
    json_transaction_type = UNSET
  else:
    json_transaction_type = transaction_type
  params["transaction_type"] = json_transaction_type

  json_operation_type: Union[None, Unset, str]
  if isinstance(operation_type, Unset):
    json_operation_type = UNSET
  else:
    json_operation_type = operation_type
  params["operation_type"] = json_operation_type

  json_start_date: Union[None, Unset, str]
  if isinstance(start_date, Unset):
    json_start_date = UNSET
  else:
    json_start_date = start_date
  params["start_date"] = json_start_date

  json_end_date: Union[None, Unset, str]
  if isinstance(end_date, Unset):
    json_end_date = UNSET
  else:
    json_end_date = end_date
  params["end_date"] = json_end_date

  params["limit"] = limit

  params["offset"] = offset

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/credits/transactions",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = DetailedTransactionsResponse.from_dict(response.json())

    return response_200
  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400
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
) -> Response[Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]]:
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
  transaction_type: Union[None, Unset, str] = UNSET,
  operation_type: Union[None, Unset, str] = UNSET,
  start_date: Union[None, Unset, str] = UNSET,
  end_date: Union[None, Unset, str] = UNSET,
  limit: Union[Unset, int] = 100,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]]:
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
      transaction_type (Union[None, Unset, str]): Filter by transaction type (allocation,
          consumption, bonus, refund)
      operation_type (Union[None, Unset, str]): Filter by operation type (e.g., entity_lookup,
          cypher_query)
      start_date (Union[None, Unset, str]): Start date for filtering (ISO format: YYYY-MM-DD)
      end_date (Union[None, Unset, str]): End date for filtering (ISO format: YYYY-MM-DD)
      limit (Union[Unset, int]): Maximum number of transactions to return Default: 100.
      offset (Union[Unset, int]): Number of transactions to skip Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    transaction_type=transaction_type,
    operation_type=operation_type,
    start_date=start_date,
    end_date=end_date,
    limit=limit,
    offset=offset,
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
  transaction_type: Union[None, Unset, str] = UNSET,
  operation_type: Union[None, Unset, str] = UNSET,
  start_date: Union[None, Unset, str] = UNSET,
  end_date: Union[None, Unset, str] = UNSET,
  limit: Union[Unset, int] = 100,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]]:
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
      transaction_type (Union[None, Unset, str]): Filter by transaction type (allocation,
          consumption, bonus, refund)
      operation_type (Union[None, Unset, str]): Filter by operation type (e.g., entity_lookup,
          cypher_query)
      start_date (Union[None, Unset, str]): Start date for filtering (ISO format: YYYY-MM-DD)
      end_date (Union[None, Unset, str]): End date for filtering (ISO format: YYYY-MM-DD)
      limit (Union[Unset, int]): Maximum number of transactions to return Default: 100.
      offset (Union[Unset, int]): Number of transactions to skip Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]
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
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  transaction_type: Union[None, Unset, str] = UNSET,
  operation_type: Union[None, Unset, str] = UNSET,
  start_date: Union[None, Unset, str] = UNSET,
  end_date: Union[None, Unset, str] = UNSET,
  limit: Union[Unset, int] = 100,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]]:
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
      transaction_type (Union[None, Unset, str]): Filter by transaction type (allocation,
          consumption, bonus, refund)
      operation_type (Union[None, Unset, str]): Filter by operation type (e.g., entity_lookup,
          cypher_query)
      start_date (Union[None, Unset, str]): Start date for filtering (ISO format: YYYY-MM-DD)
      end_date (Union[None, Unset, str]): End date for filtering (ISO format: YYYY-MM-DD)
      limit (Union[Unset, int]): Maximum number of transactions to return Default: 100.
      offset (Union[Unset, int]): Number of transactions to skip Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    transaction_type=transaction_type,
    operation_type=operation_type,
    start_date=start_date,
    end_date=end_date,
    limit=limit,
    offset=offset,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  transaction_type: Union[None, Unset, str] = UNSET,
  operation_type: Union[None, Unset, str] = UNSET,
  start_date: Union[None, Unset, str] = UNSET,
  end_date: Union[None, Unset, str] = UNSET,
  limit: Union[Unset, int] = 100,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]]:
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
      transaction_type (Union[None, Unset, str]): Filter by transaction type (allocation,
          consumption, bonus, refund)
      operation_type (Union[None, Unset, str]): Filter by operation type (e.g., entity_lookup,
          cypher_query)
      start_date (Union[None, Unset, str]): Start date for filtering (ISO format: YYYY-MM-DD)
      end_date (Union[None, Unset, str]): End date for filtering (ISO format: YYYY-MM-DD)
      limit (Union[Unset, int]): Maximum number of transactions to return Default: 100.
      offset (Union[Unset, int]): Number of transactions to skip Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[DetailedTransactionsResponse, ErrorResponse, HTTPValidationError]
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
      token=token,
      authorization=authorization,
    )
  ).parsed
