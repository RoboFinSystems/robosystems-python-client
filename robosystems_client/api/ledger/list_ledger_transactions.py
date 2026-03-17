import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ledger_transaction_list_response import LedgerTransactionListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  type_: None | str | Unset = UNSET,
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_type_: None | str | Unset
  if isinstance(type_, Unset):
    json_type_ = UNSET
  else:
    json_type_ = type_
  params["type"] = json_type_

  json_start_date: None | str | Unset
  if isinstance(start_date, Unset):
    json_start_date = UNSET
  elif isinstance(start_date, datetime.date):
    json_start_date = start_date.isoformat()
  else:
    json_start_date = start_date
  params["start_date"] = json_start_date

  json_end_date: None | str | Unset
  if isinstance(end_date, Unset):
    json_end_date = UNSET
  elif isinstance(end_date, datetime.date):
    json_end_date = end_date.isoformat()
  else:
    json_end_date = end_date
  params["end_date"] = json_end_date

  params["limit"] = limit

  params["offset"] = offset

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/transactions".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LedgerTransactionListResponse | None:
  if response.status_code == 200:
    response_200 = LedgerTransactionListResponse.from_dict(response.json())

    return response_200

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | LedgerTransactionListResponse]:
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
  type_: None | str | Unset = UNSET,
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[HTTPValidationError | LedgerTransactionListResponse]:
  """List Transactions

  Args:
      graph_id (str):
      type_ (None | str | Unset): Filter by transaction type
      start_date (datetime.date | None | Unset): Start date (inclusive)
      end_date (datetime.date | None | Unset): End date (inclusive)
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | LedgerTransactionListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    type_=type_,
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
  type_: None | str | Unset = UNSET,
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> HTTPValidationError | LedgerTransactionListResponse | None:
  """List Transactions

  Args:
      graph_id (str):
      type_ (None | str | Unset): Filter by transaction type
      start_date (datetime.date | None | Unset): Start date (inclusive)
      end_date (datetime.date | None | Unset): End date (inclusive)
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | LedgerTransactionListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    type_=type_,
    start_date=start_date,
    end_date=end_date,
    limit=limit,
    offset=offset,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  type_: None | str | Unset = UNSET,
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[HTTPValidationError | LedgerTransactionListResponse]:
  """List Transactions

  Args:
      graph_id (str):
      type_ (None | str | Unset): Filter by transaction type
      start_date (datetime.date | None | Unset): Start date (inclusive)
      end_date (datetime.date | None | Unset): End date (inclusive)
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | LedgerTransactionListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    type_=type_,
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
  type_: None | str | Unset = UNSET,
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> HTTPValidationError | LedgerTransactionListResponse | None:
  """List Transactions

  Args:
      graph_id (str):
      type_ (None | str | Unset): Filter by transaction type
      start_date (datetime.date | None | Unset): Start date (inclusive)
      end_date (datetime.date | None | Unset): End date (inclusive)
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | LedgerTransactionListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      type_=type_,
      start_date=start_date,
      end_date=end_date,
      limit=limit,
      offset=offset,
    )
  ).parsed
