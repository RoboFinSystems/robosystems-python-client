from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_allocation_override_response import (
  OperationEnvelopeAllocationOverrideResponse,
)
from ...models.set_allocation_override_request import SetAllocationOverrideRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: SetAllocationOverrideRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/set-allocation-override".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeAllocationOverrideResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeAllocationOverrideResponse.from_dict(
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
) -> Response[ErrorResponse | OperationEnvelopeAllocationOverrideResponse]:
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
  body: SetAllocationOverrideRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeAllocationOverrideResponse]:
  """Set Allocation Override

   Set the outside owners' share of a member's result for one month in place of the pro-rata share its
  ownership percentage gives: a preferred return, a waterfall, a special allocation. Give the share as
  an amount in cents (negative for a share of a loss) or as a percentage of the month's result, with
  the basis; `clear` removes it. preview- and propose-consolidation-entries then use it for that
  month, and their basis says so. Only for a member consolidated in full, and refused in a month the
  consolidation entity has closed.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (SetAllocationOverrideRequest): The outside owners' share of a member's result for
          one month, set by a
          person in place of the pro-rata share: a preferred return, a waterfall, a
          special allocation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeAllocationOverrideResponse]
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
  body: SetAllocationOverrideRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeAllocationOverrideResponse | None:
  """Set Allocation Override

   Set the outside owners' share of a member's result for one month in place of the pro-rata share its
  ownership percentage gives: a preferred return, a waterfall, a special allocation. Give the share as
  an amount in cents (negative for a share of a loss) or as a percentage of the month's result, with
  the basis; `clear` removes it. preview- and propose-consolidation-entries then use it for that
  month, and their basis says so. Only for a member consolidated in full, and refused in a month the
  consolidation entity has closed.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (SetAllocationOverrideRequest): The outside owners' share of a member's result for
          one month, set by a
          person in place of the pro-rata share: a preferred return, a waterfall, a
          special allocation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeAllocationOverrideResponse
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
  body: SetAllocationOverrideRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeAllocationOverrideResponse]:
  """Set Allocation Override

   Set the outside owners' share of a member's result for one month in place of the pro-rata share its
  ownership percentage gives: a preferred return, a waterfall, a special allocation. Give the share as
  an amount in cents (negative for a share of a loss) or as a percentage of the month's result, with
  the basis; `clear` removes it. preview- and propose-consolidation-entries then use it for that
  month, and their basis says so. Only for a member consolidated in full, and refused in a month the
  consolidation entity has closed.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (SetAllocationOverrideRequest): The outside owners' share of a member's result for
          one month, set by a
          person in place of the pro-rata share: a preferred return, a waterfall, a
          special allocation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeAllocationOverrideResponse]
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
  body: SetAllocationOverrideRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeAllocationOverrideResponse | None:
  """Set Allocation Override

   Set the outside owners' share of a member's result for one month in place of the pro-rata share its
  ownership percentage gives: a preferred return, a waterfall, a special allocation. Give the share as
  an amount in cents (negative for a share of a loss) or as a percentage of the month's result, with
  the basis; `clear` removes it. preview- and propose-consolidation-entries then use it for that
  month, and their basis says so. Only for a member consolidated in full, and refused in a month the
  consolidation entity has closed.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (SetAllocationOverrideRequest): The outside owners' share of a member's result for
          one month, set by a
          person in place of the pro-rata share: a preferred return, a waterfall, a
          special allocation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeAllocationOverrideResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
