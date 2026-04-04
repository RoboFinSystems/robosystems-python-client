import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.schedule_facts_response import ScheduleFactsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  structure_id: str,
  *,
  period_start: datetime.date | None | Unset = UNSET,
  period_end: datetime.date | None | Unset = UNSET,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_period_start: None | str | Unset
  if isinstance(period_start, Unset):
    json_period_start = UNSET
  elif isinstance(period_start, datetime.date):
    json_period_start = period_start.isoformat()
  else:
    json_period_start = period_start
  params["period_start"] = json_period_start

  json_period_end: None | str | Unset
  if isinstance(period_end, Unset):
    json_period_end = UNSET
  elif isinstance(period_end, datetime.date):
    json_period_end = period_end.isoformat()
  else:
    json_period_end = period_end
  params["period_end"] = json_period_end

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/schedules/{structure_id}/facts".format(
      graph_id=quote(str(graph_id), safe=""),
      structure_id=quote(str(structure_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ScheduleFactsResponse | None:
  if response.status_code == 200:
    response_200 = ScheduleFactsResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ScheduleFactsResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  structure_id: str,
  *,
  client: AuthenticatedClient,
  period_start: datetime.date | None | Unset = UNSET,
  period_end: datetime.date | None | Unset = UNSET,
) -> Response[HTTPValidationError | ScheduleFactsResponse]:
  """Get Schedule Facts

   Get facts for a schedule, optionally filtered by period.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      period_start (datetime.date | None | Unset): Filter: period start
      period_end (datetime.date | None | Unset): Filter: period end

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | ScheduleFactsResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    structure_id=structure_id,
    period_start=period_start,
    period_end=period_end,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  structure_id: str,
  *,
  client: AuthenticatedClient,
  period_start: datetime.date | None | Unset = UNSET,
  period_end: datetime.date | None | Unset = UNSET,
) -> HTTPValidationError | ScheduleFactsResponse | None:
  """Get Schedule Facts

   Get facts for a schedule, optionally filtered by period.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      period_start (datetime.date | None | Unset): Filter: period start
      period_end (datetime.date | None | Unset): Filter: period end

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | ScheduleFactsResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    structure_id=structure_id,
    client=client,
    period_start=period_start,
    period_end=period_end,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  structure_id: str,
  *,
  client: AuthenticatedClient,
  period_start: datetime.date | None | Unset = UNSET,
  period_end: datetime.date | None | Unset = UNSET,
) -> Response[HTTPValidationError | ScheduleFactsResponse]:
  """Get Schedule Facts

   Get facts for a schedule, optionally filtered by period.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      period_start (datetime.date | None | Unset): Filter: period start
      period_end (datetime.date | None | Unset): Filter: period end

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | ScheduleFactsResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    structure_id=structure_id,
    period_start=period_start,
    period_end=period_end,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  structure_id: str,
  *,
  client: AuthenticatedClient,
  period_start: datetime.date | None | Unset = UNSET,
  period_end: datetime.date | None | Unset = UNSET,
) -> HTTPValidationError | ScheduleFactsResponse | None:
  """Get Schedule Facts

   Get facts for a schedule, optionally filtered by period.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      period_start (datetime.date | None | Unset): Filter: period start
      period_end (datetime.date | None | Unset): Filter: period end

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | ScheduleFactsResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      structure_id=structure_id,
      client=client,
      period_start=period_start,
      period_end=period_end,
    )
  ).parsed
