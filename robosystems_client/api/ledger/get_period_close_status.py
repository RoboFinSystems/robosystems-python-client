import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.period_close_status_response import PeriodCloseStatusResponse
from ...types import UNSET, Response


def _get_kwargs(
  graph_id: str,
  *,
  period_start: datetime.date,
  period_end: datetime.date,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_period_start = period_start.isoformat()
  params["period_start"] = json_period_start

  json_period_end = period_end.isoformat()
  params["period_end"] = json_period_end

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/schedules/close-status".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PeriodCloseStatusResponse | None:
  if response.status_code == 200:
    response_200 = PeriodCloseStatusResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PeriodCloseStatusResponse]:
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
  period_start: datetime.date,
  period_end: datetime.date,
) -> Response[HTTPValidationError | PeriodCloseStatusResponse]:
  """Get Period Close Status

   Get close status for all schedules in a fiscal period.

  Args:
      graph_id (str):
      period_start (datetime.date): Fiscal period start
      period_end (datetime.date): Fiscal period end

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PeriodCloseStatusResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    period_start=period_start,
    period_end=period_end,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  period_start: datetime.date,
  period_end: datetime.date,
) -> HTTPValidationError | PeriodCloseStatusResponse | None:
  """Get Period Close Status

   Get close status for all schedules in a fiscal period.

  Args:
      graph_id (str):
      period_start (datetime.date): Fiscal period start
      period_end (datetime.date): Fiscal period end

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PeriodCloseStatusResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    period_start=period_start,
    period_end=period_end,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  period_start: datetime.date,
  period_end: datetime.date,
) -> Response[HTTPValidationError | PeriodCloseStatusResponse]:
  """Get Period Close Status

   Get close status for all schedules in a fiscal period.

  Args:
      graph_id (str):
      period_start (datetime.date): Fiscal period start
      period_end (datetime.date): Fiscal period end

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PeriodCloseStatusResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    period_start=period_start,
    period_end=period_end,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  period_start: datetime.date,
  period_end: datetime.date,
) -> HTTPValidationError | PeriodCloseStatusResponse | None:
  """Get Period Close Status

   Get close status for all schedules in a fiscal period.

  Args:
      graph_id (str):
      period_start (datetime.date): Fiscal period start
      period_end (datetime.date): Fiscal period end

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PeriodCloseStatusResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      period_start=period_start,
      period_end=period_end,
    )
  ).parsed
