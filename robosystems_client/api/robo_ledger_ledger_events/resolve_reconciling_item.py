from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_resolve_reconciling_item_response import (
  OperationEnvelopeResolveReconcilingItemResponse,
)
from ...models.resolve_reconciling_item_request import ResolveReconcilingItemRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: ResolveReconcilingItemRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/resolve-reconciling-item".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeResolveReconcilingItemResponse.from_dict(
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
) -> Response[ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse]:
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
  body: ResolveReconcilingItemRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse]:
  """Resolve Reconciling Item

   Dispose of one reconciling item and clear its flag. Three treatments: 'restate' regenerates the
  event's entries from the accepted payload in place (prior months' figures change — right when
  nothing external binds them); 'catch_up' leaves history alone and posts the difference as an
  alignment entry in an open period, local-only so it cannot travel back to the source system and
  apply the change twice; 'acknowledge' records that the difference was handled elsewhere and clears
  the flag without touching the ledger (a note is required, and reference_event_id should name the
  entry that handled it). Omit disposition to take the default from preview-reconciling-item. Clearing
  the flag means the item stays cleared: the event's payload is set to the accepted one, so the next
  sync no longer sees a difference.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ResolveReconcilingItemRequest): Dispose of one reconciling item and clear its flag.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse]
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
  body: ResolveReconcilingItemRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse | None:
  """Resolve Reconciling Item

   Dispose of one reconciling item and clear its flag. Three treatments: 'restate' regenerates the
  event's entries from the accepted payload in place (prior months' figures change — right when
  nothing external binds them); 'catch_up' leaves history alone and posts the difference as an
  alignment entry in an open period, local-only so it cannot travel back to the source system and
  apply the change twice; 'acknowledge' records that the difference was handled elsewhere and clears
  the flag without touching the ledger (a note is required, and reference_event_id should name the
  entry that handled it). Omit disposition to take the default from preview-reconciling-item. Clearing
  the flag means the item stays cleared: the event's payload is set to the accepted one, so the next
  sync no longer sees a difference.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ResolveReconcilingItemRequest): Dispose of one reconciling item and clear its flag.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse
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
  body: ResolveReconcilingItemRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse]:
  """Resolve Reconciling Item

   Dispose of one reconciling item and clear its flag. Three treatments: 'restate' regenerates the
  event's entries from the accepted payload in place (prior months' figures change — right when
  nothing external binds them); 'catch_up' leaves history alone and posts the difference as an
  alignment entry in an open period, local-only so it cannot travel back to the source system and
  apply the change twice; 'acknowledge' records that the difference was handled elsewhere and clears
  the flag without touching the ledger (a note is required, and reference_event_id should name the
  entry that handled it). Omit disposition to take the default from preview-reconciling-item. Clearing
  the flag means the item stays cleared: the event's payload is set to the accepted one, so the next
  sync no longer sees a difference.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ResolveReconcilingItemRequest): Dispose of one reconciling item and clear its flag.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse]
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
  body: ResolveReconcilingItemRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse | None:
  """Resolve Reconciling Item

   Dispose of one reconciling item and clear its flag. Three treatments: 'restate' regenerates the
  event's entries from the accepted payload in place (prior months' figures change — right when
  nothing external binds them); 'catch_up' leaves history alone and posts the difference as an
  alignment entry in an open period, local-only so it cannot travel back to the source system and
  apply the change twice; 'acknowledge' records that the difference was handled elsewhere and clears
  the flag without touching the ledger (a note is required, and reference_event_id should name the
  entry that handled it). Omit disposition to take the default from preview-reconciling-item. Clearing
  the flag means the item stays cleared: the event's payload is set to the accepted one, so the next
  sync no longer sees a difference.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ResolveReconcilingItemRequest): Dispose of one reconciling item and clear its flag.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeResolveReconcilingItemResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
