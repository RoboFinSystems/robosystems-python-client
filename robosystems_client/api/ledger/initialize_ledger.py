from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.initialize_ledger_request import InitializeLedgerRequest
from ...models.initialize_ledger_response import InitializeLedgerResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: InitializeLedgerRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/ledger/{graph_id}/initialize".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | InitializeLedgerResponse | None:
  if response.status_code == 201:
    response_201 = InitializeLedgerResponse.from_dict(response.json())

    return response_201

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | InitializeLedgerResponse]:
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
  body: InitializeLedgerRequest,
) -> Response[HTTPValidationError | InitializeLedgerResponse]:
  """Initialize Ledger

   One-time ledger initialization.

  Creates the fiscal calendar, seeds `FiscalPeriod` rows for the data window,
  and sets `closed_through` / `close_target`. Fails if the calendar already
  exists — use the reopen flow to undo prior closes instead of re-initializing.

  `auto_seed_schedules=true` is accepted but is a no-op in v1; schedule
  creation is deferred to the SchedulerAgent (Phase 5).

  Args:
      graph_id (str):
      body (InitializeLedgerRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | InitializeLedgerResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: InitializeLedgerRequest,
) -> HTTPValidationError | InitializeLedgerResponse | None:
  """Initialize Ledger

   One-time ledger initialization.

  Creates the fiscal calendar, seeds `FiscalPeriod` rows for the data window,
  and sets `closed_through` / `close_target`. Fails if the calendar already
  exists — use the reopen flow to undo prior closes instead of re-initializing.

  `auto_seed_schedules=true` is accepted but is a no-op in v1; schedule
  creation is deferred to the SchedulerAgent (Phase 5).

  Args:
      graph_id (str):
      body (InitializeLedgerRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | InitializeLedgerResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: InitializeLedgerRequest,
) -> Response[HTTPValidationError | InitializeLedgerResponse]:
  """Initialize Ledger

   One-time ledger initialization.

  Creates the fiscal calendar, seeds `FiscalPeriod` rows for the data window,
  and sets `closed_through` / `close_target`. Fails if the calendar already
  exists — use the reopen flow to undo prior closes instead of re-initializing.

  `auto_seed_schedules=true` is accepted but is a no-op in v1; schedule
  creation is deferred to the SchedulerAgent (Phase 5).

  Args:
      graph_id (str):
      body (InitializeLedgerRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | InitializeLedgerResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: InitializeLedgerRequest,
) -> HTTPValidationError | InitializeLedgerResponse | None:
  """Initialize Ledger

   One-time ledger initialization.

  Creates the fiscal calendar, seeds `FiscalPeriod` rows for the data window,
  and sets `closed_through` / `close_target`. Fails if the calendar already
  exists — use the reopen flow to undo prior closes instead of re-initializing.

  `auto_seed_schedules=true` is accepted but is a no-op in v1; schedule
  creation is deferred to the SchedulerAgent (Phase 5).

  Args:
      graph_id (str):
      body (InitializeLedgerRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | InitializeLedgerResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
