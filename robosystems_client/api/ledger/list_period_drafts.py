from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.period_drafts_response import PeriodDraftsResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  period: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/periods/{period}/drafts".format(
      graph_id=quote(str(graph_id), safe=""),
      period=quote(str(period), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PeriodDraftsResponse | None:
  if response.status_code == 200:
    response_200 = PeriodDraftsResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PeriodDraftsResponse]:
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
) -> Response[HTTPValidationError | PeriodDraftsResponse]:
  """List Draft Entries For Review

   List all draft entries in a fiscal period for review before close.

  Returns every draft entry whose `posting_date` falls within the period,
  fully expanded with line items, element names/codes, source schedule
  structure name, and per-entry balance check.

  Use this to review exactly what `close-period` will commit. Typical flow:

  1. Draft entries via `create-closing-entry` (one per schedule)
  2. Call this endpoint to review the full set
  3. Call `POST /periods/{period}/close` to atomically post + close

  This is a pure read — no side effects. It can be called repeatedly.

  Args:
      graph_id (str):
      period (str): Period in YYYY-MM format

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PeriodDraftsResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    period=period,
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
) -> HTTPValidationError | PeriodDraftsResponse | None:
  """List Draft Entries For Review

   List all draft entries in a fiscal period for review before close.

  Returns every draft entry whose `posting_date` falls within the period,
  fully expanded with line items, element names/codes, source schedule
  structure name, and per-entry balance check.

  Use this to review exactly what `close-period` will commit. Typical flow:

  1. Draft entries via `create-closing-entry` (one per schedule)
  2. Call this endpoint to review the full set
  3. Call `POST /periods/{period}/close` to atomically post + close

  This is a pure read — no side effects. It can be called repeatedly.

  Args:
      graph_id (str):
      period (str): Period in YYYY-MM format

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PeriodDraftsResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    period=period,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  period: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | PeriodDraftsResponse]:
  """List Draft Entries For Review

   List all draft entries in a fiscal period for review before close.

  Returns every draft entry whose `posting_date` falls within the period,
  fully expanded with line items, element names/codes, source schedule
  structure name, and per-entry balance check.

  Use this to review exactly what `close-period` will commit. Typical flow:

  1. Draft entries via `create-closing-entry` (one per schedule)
  2. Call this endpoint to review the full set
  3. Call `POST /periods/{period}/close` to atomically post + close

  This is a pure read — no side effects. It can be called repeatedly.

  Args:
      graph_id (str):
      period (str): Period in YYYY-MM format

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PeriodDraftsResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    period=period,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  period: str,
  *,
  client: AuthenticatedClient,
) -> HTTPValidationError | PeriodDraftsResponse | None:
  """List Draft Entries For Review

   List all draft entries in a fiscal period for review before close.

  Returns every draft entry whose `posting_date` falls within the period,
  fully expanded with line items, element names/codes, source schedule
  structure name, and per-entry balance check.

  Use this to review exactly what `close-period` will commit. Typical flow:

  1. Draft entries via `create-closing-entry` (one per schedule)
  2. Call this endpoint to review the full set
  3. Call `POST /periods/{period}/close` to atomically post + close

  This is a pure read — no side effects. It can be called repeatedly.

  Args:
      graph_id (str):
      period (str): Period in YYYY-MM format

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PeriodDraftsResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      period=period,
      client=client,
    )
  ).parsed
