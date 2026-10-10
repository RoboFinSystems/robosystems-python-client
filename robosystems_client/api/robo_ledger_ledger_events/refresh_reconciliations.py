from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_reconciliation_list_response import (
  OperationEnvelopeReconciliationListResponse,
)
from ...models.refresh_reconciliations_request import RefreshReconciliationsRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: RefreshReconciliationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/refresh-reconciliations".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeReconciliationListResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeReconciliationListResponse.from_dict(
      response.json()
    )

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
) -> Response[ErrorResponse | OperationEnvelopeReconciliationListResponse]:
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
  body: RefreshReconciliationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeReconciliationListResponse]:
  """Refresh Reconciliations

   Run every reconciliation that applies at a period end and record each result on its block. A ledger
  synced from QuickBooks is compared with QuickBooks' own trial balance, on one block for the whole
  ledger. Each asset account a schedule carries a balance on is compared with what its schedules say
  it holds, on a block of its own. Each account with a statement covering the period (record-
  statement-balance; the latest within its statement cycle) is compared with that balance. A block
  reconciles for the period when its difference is within its materiality. Running it again replaces
  the period's comparison, so the answer is always as of the last run. A block is created the first
  time its check applies, and from then on the period's close waits on it until set-reconciliation-
  policy releases it. The one exception is an account block whose first comparison does not tie: it is
  created without holding the close, so a difference found on first contact is reported and becomes a
  close requirement only when you turn it on. Returns every reconciliation's standing for the period.
  Use preview-reconciliations to see a comparison without recording it.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RefreshReconciliationsRequest): Compare each reconciliation at a period end and
          record the result.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeReconciliationListResponse]
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
  body: RefreshReconciliationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeReconciliationListResponse | None:
  """Refresh Reconciliations

   Run every reconciliation that applies at a period end and record each result on its block. A ledger
  synced from QuickBooks is compared with QuickBooks' own trial balance, on one block for the whole
  ledger. Each asset account a schedule carries a balance on is compared with what its schedules say
  it holds, on a block of its own. Each account with a statement covering the period (record-
  statement-balance; the latest within its statement cycle) is compared with that balance. A block
  reconciles for the period when its difference is within its materiality. Running it again replaces
  the period's comparison, so the answer is always as of the last run. A block is created the first
  time its check applies, and from then on the period's close waits on it until set-reconciliation-
  policy releases it. The one exception is an account block whose first comparison does not tie: it is
  created without holding the close, so a difference found on first contact is reported and becomes a
  close requirement only when you turn it on. Returns every reconciliation's standing for the period.
  Use preview-reconciliations to see a comparison without recording it.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RefreshReconciliationsRequest): Compare each reconciliation at a period end and
          record the result.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeReconciliationListResponse
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
  body: RefreshReconciliationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeReconciliationListResponse]:
  """Refresh Reconciliations

   Run every reconciliation that applies at a period end and record each result on its block. A ledger
  synced from QuickBooks is compared with QuickBooks' own trial balance, on one block for the whole
  ledger. Each asset account a schedule carries a balance on is compared with what its schedules say
  it holds, on a block of its own. Each account with a statement covering the period (record-
  statement-balance; the latest within its statement cycle) is compared with that balance. A block
  reconciles for the period when its difference is within its materiality. Running it again replaces
  the period's comparison, so the answer is always as of the last run. A block is created the first
  time its check applies, and from then on the period's close waits on it until set-reconciliation-
  policy releases it. The one exception is an account block whose first comparison does not tie: it is
  created without holding the close, so a difference found on first contact is reported and becomes a
  close requirement only when you turn it on. Returns every reconciliation's standing for the period.
  Use preview-reconciliations to see a comparison without recording it.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RefreshReconciliationsRequest): Compare each reconciliation at a period end and
          record the result.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeReconciliationListResponse]
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
  body: RefreshReconciliationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeReconciliationListResponse | None:
  """Refresh Reconciliations

   Run every reconciliation that applies at a period end and record each result on its block. A ledger
  synced from QuickBooks is compared with QuickBooks' own trial balance, on one block for the whole
  ledger. Each asset account a schedule carries a balance on is compared with what its schedules say
  it holds, on a block of its own. Each account with a statement covering the period (record-
  statement-balance; the latest within its statement cycle) is compared with that balance. A block
  reconciles for the period when its difference is within its materiality. Running it again replaces
  the period's comparison, so the answer is always as of the last run. A block is created the first
  time its check applies, and from then on the period's close waits on it until set-reconciliation-
  policy releases it. The one exception is an account block whose first comparison does not tie: it is
  created without holding the close, so a difference found on first contact is reported and becomes a
  close requirement only when you turn it on. Returns every reconciliation's standing for the period.
  Use preview-reconciliations to see a comparison without recording it.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RefreshReconciliationsRequest): Compare each reconciliation at a period end and
          record the result.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeReconciliationListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
