from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_ownership_change_response import (
  OperationEnvelopeOwnershipChangeResponse,
)
from ...models.record_ownership_change_request import RecordOwnershipChangeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: RecordOwnershipChangeRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/record-ownership-change".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeOwnershipChangeResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeOwnershipChangeResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | OperationEnvelopeOwnershipChangeResponse]:
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
  body: RecordOwnershipChangeRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeOwnershipChangeResponse]:
  """Record Ownership Change

   Record the parent buying more of a member consolidated in full from its outside owners, or selling
  some of it to them while keeping control: the share it holds from a month (`ownership_pct`, staying
  50 or more) and the price in cents, with the basis. It sets the member's share from that month and
  writes a draft in the consolidation entity, dated the month's first day, that its close posts: ASC
  810 makes it an equity transaction with no gain or loss. Buying, the price above the book value of
  the capital bought goes against the investment, the share bought of the member's results since it
  joined comes out of the outside owners' interest, and the difference is the parent's equity.
  Selling, the parent's own entry takes the proceeds against the carrying amount of the shares sold
  and books its gain or loss; the draft reverses that gain, releases the parent's cost above book on
  those shares, credits the outside owners their larger share of the member's results, and takes the
  difference to the parent's equity. preview-consolidation-entries then reads the price paid, net of
  what a sale released, as part of the parent's investment, and the new share from that month. Changes
  are recorded in order; recording a month again replaces its draft, and a posted one is reversed
  first. A change across consolidation methods is not supported yet.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordOwnershipChangeRequest): The parent buys more of a member from its outside
          owners, or sells some
          of it to them while keeping control: the share it holds from a month, and
          the price. ASC 810 makes it an equity transaction, never a gain or loss.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeOwnershipChangeResponse]
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
  body: RecordOwnershipChangeRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeOwnershipChangeResponse | None:
  """Record Ownership Change

   Record the parent buying more of a member consolidated in full from its outside owners, or selling
  some of it to them while keeping control: the share it holds from a month (`ownership_pct`, staying
  50 or more) and the price in cents, with the basis. It sets the member's share from that month and
  writes a draft in the consolidation entity, dated the month's first day, that its close posts: ASC
  810 makes it an equity transaction with no gain or loss. Buying, the price above the book value of
  the capital bought goes against the investment, the share bought of the member's results since it
  joined comes out of the outside owners' interest, and the difference is the parent's equity.
  Selling, the parent's own entry takes the proceeds against the carrying amount of the shares sold
  and books its gain or loss; the draft reverses that gain, releases the parent's cost above book on
  those shares, credits the outside owners their larger share of the member's results, and takes the
  difference to the parent's equity. preview-consolidation-entries then reads the price paid, net of
  what a sale released, as part of the parent's investment, and the new share from that month. Changes
  are recorded in order; recording a month again replaces its draft, and a posted one is reversed
  first. A change across consolidation methods is not supported yet.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordOwnershipChangeRequest): The parent buys more of a member from its outside
          owners, or sells some
          of it to them while keeping control: the share it holds from a month, and
          the price. ASC 810 makes it an equity transaction, never a gain or loss.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeOwnershipChangeResponse
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
  body: RecordOwnershipChangeRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeOwnershipChangeResponse]:
  """Record Ownership Change

   Record the parent buying more of a member consolidated in full from its outside owners, or selling
  some of it to them while keeping control: the share it holds from a month (`ownership_pct`, staying
  50 or more) and the price in cents, with the basis. It sets the member's share from that month and
  writes a draft in the consolidation entity, dated the month's first day, that its close posts: ASC
  810 makes it an equity transaction with no gain or loss. Buying, the price above the book value of
  the capital bought goes against the investment, the share bought of the member's results since it
  joined comes out of the outside owners' interest, and the difference is the parent's equity.
  Selling, the parent's own entry takes the proceeds against the carrying amount of the shares sold
  and books its gain or loss; the draft reverses that gain, releases the parent's cost above book on
  those shares, credits the outside owners their larger share of the member's results, and takes the
  difference to the parent's equity. preview-consolidation-entries then reads the price paid, net of
  what a sale released, as part of the parent's investment, and the new share from that month. Changes
  are recorded in order; recording a month again replaces its draft, and a posted one is reversed
  first. A change across consolidation methods is not supported yet.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordOwnershipChangeRequest): The parent buys more of a member from its outside
          owners, or sells some
          of it to them while keeping control: the share it holds from a month, and
          the price. ASC 810 makes it an equity transaction, never a gain or loss.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeOwnershipChangeResponse]
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
  body: RecordOwnershipChangeRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeOwnershipChangeResponse | None:
  """Record Ownership Change

   Record the parent buying more of a member consolidated in full from its outside owners, or selling
  some of it to them while keeping control: the share it holds from a month (`ownership_pct`, staying
  50 or more) and the price in cents, with the basis. It sets the member's share from that month and
  writes a draft in the consolidation entity, dated the month's first day, that its close posts: ASC
  810 makes it an equity transaction with no gain or loss. Buying, the price above the book value of
  the capital bought goes against the investment, the share bought of the member's results since it
  joined comes out of the outside owners' interest, and the difference is the parent's equity.
  Selling, the parent's own entry takes the proceeds against the carrying amount of the shares sold
  and books its gain or loss; the draft reverses that gain, releases the parent's cost above book on
  those shares, credits the outside owners their larger share of the member's results, and takes the
  difference to the parent's equity. preview-consolidation-entries then reads the price paid, net of
  what a sale released, as part of the parent's investment, and the new share from that month. Changes
  are recorded in order; recording a month again replaces its draft, and a posted one is reversed
  first. A change across consolidation methods is not supported yet.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordOwnershipChangeRequest): The parent buys more of a member from its outside
          owners, or sells some
          of it to them while keeping control: the share it holds from a month, and
          the price. ASC 810 makes it an equity transaction, never a gain or loss.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeOwnershipChangeResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
