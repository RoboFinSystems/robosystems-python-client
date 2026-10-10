from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_reconciliation_summary import (
  OperationEnvelopeReconciliationSummary,
)
from ...models.record_statement_balance_request import RecordStatementBalanceRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: RecordStatementBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/record-statement-balance".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeReconciliationSummary | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeReconciliationSummary.from_dict(response.json())

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
) -> Response[ErrorResponse | OperationEnvelopeReconciliationSummary]:
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
  body: RecordStatementBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeReconciliationSummary]:
  """Record Statement Balance

   Record the ending balance of a statement (a bank, card or loan statement) for one balance-sheet
  account, and reconcile the account to it. Give the balance as the statement shows it, as a positive
  number in the account's normal direction, with the statement's ending date. The ledger's balance at
  that date is set beside it, counting the drafts the close will post, and the result is recorded on
  the account's statement reconciliation for the period the statement ends in. Attach the statement as
  evidence by passing the `document_id` of its stored file (create-document-upload, then complete-
  document-upload); recording it again with another document lapses a sign-off. Writes no books. The
  first statement recorded for an account creates its reconciliation, which does not hold the close:
  turn `required_for_close` on with set-reconciliation-policy to make every period's close wait for a
  statement on that account. Recording the same account and date again replaces the earlier balance;
  when more than one statement ends in a period, the one with the latest date stands. Recording a
  balance that differs from one already signed off lapses that sign-off. A difference is not explained
  here: it is activity one side has and the other does not yet, or an error on either. Returns the
  reconciliation's standing for the period.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordStatementBalanceRequest): Record the ending balance of a statement for one
          account.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeReconciliationSummary]
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
  body: RecordStatementBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeReconciliationSummary | None:
  """Record Statement Balance

   Record the ending balance of a statement (a bank, card or loan statement) for one balance-sheet
  account, and reconcile the account to it. Give the balance as the statement shows it, as a positive
  number in the account's normal direction, with the statement's ending date. The ledger's balance at
  that date is set beside it, counting the drafts the close will post, and the result is recorded on
  the account's statement reconciliation for the period the statement ends in. Attach the statement as
  evidence by passing the `document_id` of its stored file (create-document-upload, then complete-
  document-upload); recording it again with another document lapses a sign-off. Writes no books. The
  first statement recorded for an account creates its reconciliation, which does not hold the close:
  turn `required_for_close` on with set-reconciliation-policy to make every period's close wait for a
  statement on that account. Recording the same account and date again replaces the earlier balance;
  when more than one statement ends in a period, the one with the latest date stands. Recording a
  balance that differs from one already signed off lapses that sign-off. A difference is not explained
  here: it is activity one side has and the other does not yet, or an error on either. Returns the
  reconciliation's standing for the period.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordStatementBalanceRequest): Record the ending balance of a statement for one
          account.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeReconciliationSummary
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
  body: RecordStatementBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeReconciliationSummary]:
  """Record Statement Balance

   Record the ending balance of a statement (a bank, card or loan statement) for one balance-sheet
  account, and reconcile the account to it. Give the balance as the statement shows it, as a positive
  number in the account's normal direction, with the statement's ending date. The ledger's balance at
  that date is set beside it, counting the drafts the close will post, and the result is recorded on
  the account's statement reconciliation for the period the statement ends in. Attach the statement as
  evidence by passing the `document_id` of its stored file (create-document-upload, then complete-
  document-upload); recording it again with another document lapses a sign-off. Writes no books. The
  first statement recorded for an account creates its reconciliation, which does not hold the close:
  turn `required_for_close` on with set-reconciliation-policy to make every period's close wait for a
  statement on that account. Recording the same account and date again replaces the earlier balance;
  when more than one statement ends in a period, the one with the latest date stands. Recording a
  balance that differs from one already signed off lapses that sign-off. A difference is not explained
  here: it is activity one side has and the other does not yet, or an error on either. Returns the
  reconciliation's standing for the period.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordStatementBalanceRequest): Record the ending balance of a statement for one
          account.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeReconciliationSummary]
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
  body: RecordStatementBalanceRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeReconciliationSummary | None:
  """Record Statement Balance

   Record the ending balance of a statement (a bank, card or loan statement) for one balance-sheet
  account, and reconcile the account to it. Give the balance as the statement shows it, as a positive
  number in the account's normal direction, with the statement's ending date. The ledger's balance at
  that date is set beside it, counting the drafts the close will post, and the result is recorded on
  the account's statement reconciliation for the period the statement ends in. Attach the statement as
  evidence by passing the `document_id` of its stored file (create-document-upload, then complete-
  document-upload); recording it again with another document lapses a sign-off. Writes no books. The
  first statement recorded for an account creates its reconciliation, which does not hold the close:
  turn `required_for_close` on with set-reconciliation-policy to make every period's close wait for a
  statement on that account. Recording the same account and date again replaces the earlier balance;
  when more than one statement ends in a period, the one with the latest date stands. Recording a
  balance that differs from one already signed off lapses that sign-off. A difference is not explained
  here: it is activity one side has and the other does not yet, or an error on either. Returns the
  reconciliation's standing for the period.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordStatementBalanceRequest): Record the ending balance of a statement for one
          account.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeReconciliationSummary
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
