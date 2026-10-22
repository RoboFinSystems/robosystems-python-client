from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_deconsolidation_response import (
  OperationEnvelopeDeconsolidationResponse,
)
from ...models.record_deconsolidation_request import RecordDeconsolidationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: RecordDeconsolidationRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/record-deconsolidation".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeDeconsolidationResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeDeconsolidationResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | OperationEnvelopeDeconsolidationResponse]:
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
  body: RecordDeconsolidationRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeDeconsolidationResponse]:
  """Record Deconsolidation

   Record a member's leaving the group, once `left_on` is set on it: what the parent received for its
  shares in cents (0 for a dissolution) and the basis. It writes a draft in the consolidation entity,
  dated the first day of the month after the member's last, that its close posts: what the
  consolidation entity still holds for the member on its balance-sheet accounts and as the outside
  owners' interest is taken off (goodwill, step-ups, the price above book of the investment, the
  outside owners' accumulated share), a member in full has the results it earned in the group put back
  into the group's equity as they leave with its books, and the difference is the gain or loss on its
  leaving: the group's adjustment to the gain the parent's own books took, so the consolidated gain is
  the consideration less the carrying amount of what left (ASC 810). The investment and intercompany
  eliminations go back on their own in that month's proposals. The parent's own sale entry stays on
  its books. Recording again replaces the draft; a posted deconsolidation is reversed first. A
  retained interest is not supported yet.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordDeconsolidationRequest): A member has left the group (`left_on` set): what the
          parent received
          for its shares, and the basis. The entry derecognizes what the
          consolidation entity still holds for the member and takes the gain or
          loss on its leaving; the parent's own sale entry stays on its books.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeDeconsolidationResponse]
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
  body: RecordDeconsolidationRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeDeconsolidationResponse | None:
  """Record Deconsolidation

   Record a member's leaving the group, once `left_on` is set on it: what the parent received for its
  shares in cents (0 for a dissolution) and the basis. It writes a draft in the consolidation entity,
  dated the first day of the month after the member's last, that its close posts: what the
  consolidation entity still holds for the member on its balance-sheet accounts and as the outside
  owners' interest is taken off (goodwill, step-ups, the price above book of the investment, the
  outside owners' accumulated share), a member in full has the results it earned in the group put back
  into the group's equity as they leave with its books, and the difference is the gain or loss on its
  leaving: the group's adjustment to the gain the parent's own books took, so the consolidated gain is
  the consideration less the carrying amount of what left (ASC 810). The investment and intercompany
  eliminations go back on their own in that month's proposals. The parent's own sale entry stays on
  its books. Recording again replaces the draft; a posted deconsolidation is reversed first. A
  retained interest is not supported yet.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordDeconsolidationRequest): A member has left the group (`left_on` set): what the
          parent received
          for its shares, and the basis. The entry derecognizes what the
          consolidation entity still holds for the member and takes the gain or
          loss on its leaving; the parent's own sale entry stays on its books.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeDeconsolidationResponse
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
  body: RecordDeconsolidationRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeDeconsolidationResponse]:
  """Record Deconsolidation

   Record a member's leaving the group, once `left_on` is set on it: what the parent received for its
  shares in cents (0 for a dissolution) and the basis. It writes a draft in the consolidation entity,
  dated the first day of the month after the member's last, that its close posts: what the
  consolidation entity still holds for the member on its balance-sheet accounts and as the outside
  owners' interest is taken off (goodwill, step-ups, the price above book of the investment, the
  outside owners' accumulated share), a member in full has the results it earned in the group put back
  into the group's equity as they leave with its books, and the difference is the gain or loss on its
  leaving: the group's adjustment to the gain the parent's own books took, so the consolidated gain is
  the consideration less the carrying amount of what left (ASC 810). The investment and intercompany
  eliminations go back on their own in that month's proposals. The parent's own sale entry stays on
  its books. Recording again replaces the draft; a posted deconsolidation is reversed first. A
  retained interest is not supported yet.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordDeconsolidationRequest): A member has left the group (`left_on` set): what the
          parent received
          for its shares, and the basis. The entry derecognizes what the
          consolidation entity still holds for the member and takes the gain or
          loss on its leaving; the parent's own sale entry stays on its books.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeDeconsolidationResponse]
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
  body: RecordDeconsolidationRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeDeconsolidationResponse | None:
  """Record Deconsolidation

   Record a member's leaving the group, once `left_on` is set on it: what the parent received for its
  shares in cents (0 for a dissolution) and the basis. It writes a draft in the consolidation entity,
  dated the first day of the month after the member's last, that its close posts: what the
  consolidation entity still holds for the member on its balance-sheet accounts and as the outside
  owners' interest is taken off (goodwill, step-ups, the price above book of the investment, the
  outside owners' accumulated share), a member in full has the results it earned in the group put back
  into the group's equity as they leave with its books, and the difference is the gain or loss on its
  leaving: the group's adjustment to the gain the parent's own books took, so the consolidated gain is
  the consideration less the carrying amount of what left (ASC 810). The investment and intercompany
  eliminations go back on their own in that month's proposals. The parent's own sale entry stays on
  its books. Recording again replaces the draft; a posted deconsolidation is reversed first. A
  retained interest is not supported yet.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordDeconsolidationRequest): A member has left the group (`left_on` set): what the
          parent received
          for its shares, and the basis. The entry derecognizes what the
          consolidation entity still holds for the member and takes the gain or
          loss on its leaving; the parent's own sale entry stays on its books.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeDeconsolidationResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
