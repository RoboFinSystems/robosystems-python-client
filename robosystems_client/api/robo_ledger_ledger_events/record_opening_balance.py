from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_journal_entry_response import (
  OperationEnvelopeJournalEntryResponse,
)
from ...models.record_opening_balance_request import RecordOpeningBalanceRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: RecordOpeningBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/record-opening-balance".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeJournalEntryResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeJournalEntryResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | OperationEnvelopeJournalEntryResponse]:
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
  body: RecordOpeningBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeJournalEntryResponse]:
  """Record Opening Balance

   Record the balance sheet an entity's books start from, when its history does not come with them: one
  balance per balance-sheet account (assets, liabilities, equity), in cents, debit or credit in the
  account's normal direction. It posts as one `opening` entry dated the day before the entity's first
  fiscal month, so every month's opening balances include it and no month's activity does: the cash
  flow and the equity statement start from it rather than counting it. Name the equity account that
  takes any difference between debits and credits (`equity_element_id`, usually Opening Balance
  Equity); unbalanced balances without one are refused, and an income or expense account is refused,
  since income before the books begin is in retained earnings. One per entity: recording it again
  replaces it, until the entity's first close, after which a correction is an adjusting entry in an
  open month. Set up the fiscal calendar first; moving its start (change-calendar-start) moves the
  opening with it.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordOpeningBalanceRequest): The balance sheet a ledger starts from.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeJournalEntryResponse]
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
  body: RecordOpeningBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeJournalEntryResponse | None:
  """Record Opening Balance

   Record the balance sheet an entity's books start from, when its history does not come with them: one
  balance per balance-sheet account (assets, liabilities, equity), in cents, debit or credit in the
  account's normal direction. It posts as one `opening` entry dated the day before the entity's first
  fiscal month, so every month's opening balances include it and no month's activity does: the cash
  flow and the equity statement start from it rather than counting it. Name the equity account that
  takes any difference between debits and credits (`equity_element_id`, usually Opening Balance
  Equity); unbalanced balances without one are refused, and an income or expense account is refused,
  since income before the books begin is in retained earnings. One per entity: recording it again
  replaces it, until the entity's first close, after which a correction is an adjusting entry in an
  open month. Set up the fiscal calendar first; moving its start (change-calendar-start) moves the
  opening with it.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordOpeningBalanceRequest): The balance sheet a ledger starts from.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeJournalEntryResponse
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
  body: RecordOpeningBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeJournalEntryResponse]:
  """Record Opening Balance

   Record the balance sheet an entity's books start from, when its history does not come with them: one
  balance per balance-sheet account (assets, liabilities, equity), in cents, debit or credit in the
  account's normal direction. It posts as one `opening` entry dated the day before the entity's first
  fiscal month, so every month's opening balances include it and no month's activity does: the cash
  flow and the equity statement start from it rather than counting it. Name the equity account that
  takes any difference between debits and credits (`equity_element_id`, usually Opening Balance
  Equity); unbalanced balances without one are refused, and an income or expense account is refused,
  since income before the books begin is in retained earnings. One per entity: recording it again
  replaces it, until the entity's first close, after which a correction is an adjusting entry in an
  open month. Set up the fiscal calendar first; moving its start (change-calendar-start) moves the
  opening with it.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordOpeningBalanceRequest): The balance sheet a ledger starts from.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeJournalEntryResponse]
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
  body: RecordOpeningBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeJournalEntryResponse | None:
  """Record Opening Balance

   Record the balance sheet an entity's books start from, when its history does not come with them: one
  balance per balance-sheet account (assets, liabilities, equity), in cents, debit or credit in the
  account's normal direction. It posts as one `opening` entry dated the day before the entity's first
  fiscal month, so every month's opening balances include it and no month's activity does: the cash
  flow and the equity statement start from it rather than counting it. Name the equity account that
  takes any difference between debits and credits (`equity_element_id`, usually Opening Balance
  Equity); unbalanced balances without one are refused, and an income or expense account is refused,
  since income before the books begin is in retained earnings. One per entity: recording it again
  replaces it, until the entity's first close, after which a correction is an adjusting entry in an
  open month. Set up the fiscal calendar first; moving its start (change-calendar-start) moves the
  opening with it.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordOpeningBalanceRequest): The balance sheet a ledger starts from.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeJournalEntryResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
