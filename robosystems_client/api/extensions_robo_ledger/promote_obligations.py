from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_promote_obligations_response import (
  OperationEnvelopePromoteObligationsResponse,
)
from ...models.promote_obligations_request import PromoteObligationsRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: PromoteObligationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/promote-obligations".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopePromoteObligationsResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopePromoteObligationsResponse.from_dict(
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
) -> Response[ErrorResponse | OperationEnvelopePromoteObligationsResponse]:
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
  body: PromoteObligationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopePromoteObligationsResponse]:
  """Promote Due Schedule Obligations

   Promote matured pending schedule obligations (schedule_entry_due events whose period boundary has
  passed) to 'classified', and — when dispatch_handlers=true (default) — draft their closing entries
  in the same transaction. This is the on-demand form of the background obligation-promotion sweep;
  run it before close-period when a schedule was just created or when you can't wait for the Dagster
  sensor. Idempotent: re-running skips already-classified obligations and reconciles to existing
  drafts.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (PromoteObligationsRequest): On-demand trigger for the obligation-promotion sweep.

          Mirrors what the ``scheduled_obligation_promoter`` Dagster sensor does
          on its tick, but lets an interactive caller or an MCP close co-pilot
          run it now instead of waiting for the background cadence — required to
          drive a schedule-driven close to completion in a single session.
          Flips matured ``pending`` ``schedule_entry_due`` events (period boundary
          passed) to ``classified``; with ``dispatch_handlers`` it also drafts the
          closing entries in the same transaction (idempotent — reconciles to an
          existing draft).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopePromoteObligationsResponse]
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
  body: PromoteObligationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopePromoteObligationsResponse | None:
  """Promote Due Schedule Obligations

   Promote matured pending schedule obligations (schedule_entry_due events whose period boundary has
  passed) to 'classified', and — when dispatch_handlers=true (default) — draft their closing entries
  in the same transaction. This is the on-demand form of the background obligation-promotion sweep;
  run it before close-period when a schedule was just created or when you can't wait for the Dagster
  sensor. Idempotent: re-running skips already-classified obligations and reconciles to existing
  drafts.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (PromoteObligationsRequest): On-demand trigger for the obligation-promotion sweep.

          Mirrors what the ``scheduled_obligation_promoter`` Dagster sensor does
          on its tick, but lets an interactive caller or an MCP close co-pilot
          run it now instead of waiting for the background cadence — required to
          drive a schedule-driven close to completion in a single session.
          Flips matured ``pending`` ``schedule_entry_due`` events (period boundary
          passed) to ``classified``; with ``dispatch_handlers`` it also drafts the
          closing entries in the same transaction (idempotent — reconciles to an
          existing draft).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopePromoteObligationsResponse
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
  body: PromoteObligationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopePromoteObligationsResponse]:
  """Promote Due Schedule Obligations

   Promote matured pending schedule obligations (schedule_entry_due events whose period boundary has
  passed) to 'classified', and — when dispatch_handlers=true (default) — draft their closing entries
  in the same transaction. This is the on-demand form of the background obligation-promotion sweep;
  run it before close-period when a schedule was just created or when you can't wait for the Dagster
  sensor. Idempotent: re-running skips already-classified obligations and reconciles to existing
  drafts.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (PromoteObligationsRequest): On-demand trigger for the obligation-promotion sweep.

          Mirrors what the ``scheduled_obligation_promoter`` Dagster sensor does
          on its tick, but lets an interactive caller or an MCP close co-pilot
          run it now instead of waiting for the background cadence — required to
          drive a schedule-driven close to completion in a single session.
          Flips matured ``pending`` ``schedule_entry_due`` events (period boundary
          passed) to ``classified``; with ``dispatch_handlers`` it also drafts the
          closing entries in the same transaction (idempotent — reconciles to an
          existing draft).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopePromoteObligationsResponse]
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
  body: PromoteObligationsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopePromoteObligationsResponse | None:
  """Promote Due Schedule Obligations

   Promote matured pending schedule obligations (schedule_entry_due events whose period boundary has
  passed) to 'classified', and — when dispatch_handlers=true (default) — draft their closing entries
  in the same transaction. This is the on-demand form of the background obligation-promotion sweep;
  run it before close-period when a schedule was just created or when you can't wait for the Dagster
  sensor. Idempotent: re-running skips already-classified obligations and reconciles to existing
  drafts.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (PromoteObligationsRequest): On-demand trigger for the obligation-promotion sweep.

          Mirrors what the ``scheduled_obligation_promoter`` Dagster sensor does
          on its tick, but lets an interactive caller or an MCP close co-pilot
          run it now instead of waiting for the background cadence — required to
          drive a schedule-driven close to completion in a single session.
          Flips matured ``pending`` ``schedule_entry_due`` events (period boundary
          passed) to ``classified``; with ``dispatch_handlers`` it also drafts the
          closing entries in the same transaction (idempotent — reconciles to an
          existing draft).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopePromoteObligationsResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
