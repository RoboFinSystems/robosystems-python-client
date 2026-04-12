from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.close_period_request import ClosePeriodRequest
from ...models.close_period_response import ClosePeriodResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  period: str,
  *,
  body: ClosePeriodRequest | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/ledger/{graph_id}/periods/{period}/close".format(
      graph_id=quote(str(graph_id), safe=""),
      period=quote(str(period), safe=""),
    ),
  }

  if not isinstance(body, Unset):
    _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClosePeriodResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = ClosePeriodResponse.from_dict(response.json())

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
) -> Response[ClosePeriodResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  period: str,
  *,
  client: AuthenticatedClient,
  body: ClosePeriodRequest | Unset = UNSET,
) -> Response[ClosePeriodResponse | HTTPValidationError]:
  """Close Fiscal Period

   Close a fiscal period — the final commit action.

  In a single transaction:
  1. Validates closeable gates
  2. Transitions all draft entries in the period to 'posted'
  3. Verifies BS equation balances
  4. Transitions the FiscalPeriod to 'closed'
  5. Advances closed_through; auto-advances close_target if reached

  This is synchronous in v1. With QB writeback (future) it will become async.

  Args:
      graph_id (str):
      period (str): Target period in YYYY-MM format
      body (ClosePeriodRequest | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ClosePeriodResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    period=period,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  period: str,
  *,
  client: AuthenticatedClient,
  body: ClosePeriodRequest | Unset = UNSET,
) -> ClosePeriodResponse | HTTPValidationError | None:
  """Close Fiscal Period

   Close a fiscal period — the final commit action.

  In a single transaction:
  1. Validates closeable gates
  2. Transitions all draft entries in the period to 'posted'
  3. Verifies BS equation balances
  4. Transitions the FiscalPeriod to 'closed'
  5. Advances closed_through; auto-advances close_target if reached

  This is synchronous in v1. With QB writeback (future) it will become async.

  Args:
      graph_id (str):
      period (str): Target period in YYYY-MM format
      body (ClosePeriodRequest | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ClosePeriodResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    period=period,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  period: str,
  *,
  client: AuthenticatedClient,
  body: ClosePeriodRequest | Unset = UNSET,
) -> Response[ClosePeriodResponse | HTTPValidationError]:
  """Close Fiscal Period

   Close a fiscal period — the final commit action.

  In a single transaction:
  1. Validates closeable gates
  2. Transitions all draft entries in the period to 'posted'
  3. Verifies BS equation balances
  4. Transitions the FiscalPeriod to 'closed'
  5. Advances closed_through; auto-advances close_target if reached

  This is synchronous in v1. With QB writeback (future) it will become async.

  Args:
      graph_id (str):
      period (str): Target period in YYYY-MM format
      body (ClosePeriodRequest | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ClosePeriodResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    period=period,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  period: str,
  *,
  client: AuthenticatedClient,
  body: ClosePeriodRequest | Unset = UNSET,
) -> ClosePeriodResponse | HTTPValidationError | None:
  """Close Fiscal Period

   Close a fiscal period — the final commit action.

  In a single transaction:
  1. Validates closeable gates
  2. Transitions all draft entries in the period to 'posted'
  3. Verifies BS equation balances
  4. Transitions the FiscalPeriod to 'closed'
  5. Advances closed_through; auto-advances close_target if reached

  This is synchronous in v1. With QB writeback (future) it will become async.

  Args:
      graph_id (str):
      period (str): Target period in YYYY-MM format
      body (ClosePeriodRequest | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ClosePeriodResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      period=period,
      client=client,
      body=body,
    )
  ).parsed
