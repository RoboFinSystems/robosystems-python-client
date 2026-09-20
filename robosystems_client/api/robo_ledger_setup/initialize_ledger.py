from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.initialize_ledger_request import InitializeLedgerRequest
from ...models.operation_envelope_initialize_ledger_response import (
  OperationEnvelopeInitializeLedgerResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: InitializeLedgerRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/initialize".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeInitializeLedgerResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeInitializeLedgerResponse.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401

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
    response_422 = ErrorResponse.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | OperationEnvelopeInitializeLedgerResponse]:
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
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeInitializeLedgerResponse]:
  """Initialize Ledger

   One-time setup: creates the fiscal calendar and seeds periods. Returns 409 if already initialized.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (InitializeLedgerRequest): One-time setup for a graph's fiscal calendar.

          Creates the `FiscalCalendar` row, seeds `FiscalPeriod` rows from
          ``earliest_data_period`` (or 24 months ago) through the current month,
          and stamps periods on or before ``closed_through`` as already closed.
          Subsequent calls return 409 — there's no re-initialize.

          The two pointers it sets up:

          - ``closed_through`` (system-maintained): the latest period whose
            books are locked. Set on init for businesses with prior close
            history; null for a fresh start.
          - ``close_target`` (user-controlled): the goal date the user is
            closing toward. Set independently via `set-close-target`.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeInitializeLedgerResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    idempotency_key=idempotency_key,
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
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeInitializeLedgerResponse | None:
  """Initialize Ledger

   One-time setup: creates the fiscal calendar and seeds periods. Returns 409 if already initialized.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (InitializeLedgerRequest): One-time setup for a graph's fiscal calendar.

          Creates the `FiscalCalendar` row, seeds `FiscalPeriod` rows from
          ``earliest_data_period`` (or 24 months ago) through the current month,
          and stamps periods on or before ``closed_through`` as already closed.
          Subsequent calls return 409 — there's no re-initialize.

          The two pointers it sets up:

          - ``closed_through`` (system-maintained): the latest period whose
            books are locked. Set on init for businesses with prior close
            history; null for a fresh start.
          - ``close_target`` (user-controlled): the goal date the user is
            closing toward. Set independently via `set-close-target`.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeInitializeLedgerResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
    idempotency_key=idempotency_key,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: InitializeLedgerRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeInitializeLedgerResponse]:
  """Initialize Ledger

   One-time setup: creates the fiscal calendar and seeds periods. Returns 409 if already initialized.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (InitializeLedgerRequest): One-time setup for a graph's fiscal calendar.

          Creates the `FiscalCalendar` row, seeds `FiscalPeriod` rows from
          ``earliest_data_period`` (or 24 months ago) through the current month,
          and stamps periods on or before ``closed_through`` as already closed.
          Subsequent calls return 409 — there's no re-initialize.

          The two pointers it sets up:

          - ``closed_through`` (system-maintained): the latest period whose
            books are locked. Set on init for businesses with prior close
            history; null for a fresh start.
          - ``close_target`` (user-controlled): the goal date the user is
            closing toward. Set independently via `set-close-target`.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeInitializeLedgerResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    idempotency_key=idempotency_key,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: InitializeLedgerRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeInitializeLedgerResponse | None:
  """Initialize Ledger

   One-time setup: creates the fiscal calendar and seeds periods. Returns 409 if already initialized.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (InitializeLedgerRequest): One-time setup for a graph's fiscal calendar.

          Creates the `FiscalCalendar` row, seeds `FiscalPeriod` rows from
          ``earliest_data_period`` (or 24 months ago) through the current month,
          and stamps periods on or before ``closed_through`` as already closed.
          Subsequent calls return 409 — there's no re-initialize.

          The two pointers it sets up:

          - ``closed_through`` (system-maintained): the latest period whose
            books are locked. Set on init for businesses with prior close
            history; null for a fresh start.
          - ``close_target`` (user-controlled): the goal date the user is
            closing toward. Set independently via `set-close-target`.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeInitializeLedgerResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
