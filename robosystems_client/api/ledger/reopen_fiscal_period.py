from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fiscal_calendar_response import FiscalCalendarResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.reopen_period_request import ReopenPeriodRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  period: str,
  *,
  body: ReopenPeriodRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/ledger/{graph_id}/periods/{period}/reopen".format(
      graph_id=quote(str(graph_id), safe=""),
      period=quote(str(period), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FiscalCalendarResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = FiscalCalendarResponse.from_dict(response.json())

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
) -> Response[FiscalCalendarResponse | HTTPValidationError]:
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
  body: ReopenPeriodRequest,
) -> Response[FiscalCalendarResponse | HTTPValidationError]:
  """Reopen Fiscal Period

   Reopen a closed fiscal period.

  Transitions the period status from 'closed' to 'closing' (drafts may still
  exist for this period after reopening). If the reopened period is the
  current `closed_through`, decrements the pointer. Requires a non-empty
  `reason` for the audit log. Does NOT modify `close_target` — that's a
  separate user decision.

  Posted entries in the reopened period stay posted. The user can then post
  additional adjustments, review, and close the period again.

  Args:
      graph_id (str):
      period (str): Period to reopen (YYYY-MM)
      body (ReopenPeriodRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[FiscalCalendarResponse | HTTPValidationError]
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
  body: ReopenPeriodRequest,
) -> FiscalCalendarResponse | HTTPValidationError | None:
  """Reopen Fiscal Period

   Reopen a closed fiscal period.

  Transitions the period status from 'closed' to 'closing' (drafts may still
  exist for this period after reopening). If the reopened period is the
  current `closed_through`, decrements the pointer. Requires a non-empty
  `reason` for the audit log. Does NOT modify `close_target` — that's a
  separate user decision.

  Posted entries in the reopened period stay posted. The user can then post
  additional adjustments, review, and close the period again.

  Args:
      graph_id (str):
      period (str): Period to reopen (YYYY-MM)
      body (ReopenPeriodRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      FiscalCalendarResponse | HTTPValidationError
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
  body: ReopenPeriodRequest,
) -> Response[FiscalCalendarResponse | HTTPValidationError]:
  """Reopen Fiscal Period

   Reopen a closed fiscal period.

  Transitions the period status from 'closed' to 'closing' (drafts may still
  exist for this period after reopening). If the reopened period is the
  current `closed_through`, decrements the pointer. Requires a non-empty
  `reason` for the audit log. Does NOT modify `close_target` — that's a
  separate user decision.

  Posted entries in the reopened period stay posted. The user can then post
  additional adjustments, review, and close the period again.

  Args:
      graph_id (str):
      period (str): Period to reopen (YYYY-MM)
      body (ReopenPeriodRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[FiscalCalendarResponse | HTTPValidationError]
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
  body: ReopenPeriodRequest,
) -> FiscalCalendarResponse | HTTPValidationError | None:
  """Reopen Fiscal Period

   Reopen a closed fiscal period.

  Transitions the period status from 'closed' to 'closing' (drafts may still
  exist for this period after reopening). If the reopened period is the
  current `closed_through`, decrements the pointer. Requires a non-empty
  `reason` for the audit log. Does NOT modify `close_target` — that's a
  separate user decision.

  Posted entries in the reopened period stay posted. The user can then post
  additional adjustments, review, and close the period again.

  Args:
      graph_id (str):
      period (str): Period to reopen (YYYY-MM)
      body (ReopenPeriodRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      FiscalCalendarResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      period=period,
      client=client,
      body=body,
    )
  ).parsed
