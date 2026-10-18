from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_propose_consolidation_entries_response import (
  OperationEnvelopeProposeConsolidationEntriesResponse,
)
from ...models.propose_consolidation_entries_request import (
  ProposeConsolidationEntriesRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: ProposeConsolidationEntriesRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/propose-consolidation-entries".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeProposeConsolidationEntriesResponse.from_dict(
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
) -> Response[ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse]:
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
  body: ProposeConsolidationEntriesRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse]:
  """Propose Consolidation Entries

   Draft a month's consolidating entries in the group's consolidation entity: what preview-
  consolidation-entries computes, written as drafts that the consolidation entity's close posts.
  Proposing the month again replaces the drafts it wrote before, so it can be run after any member's
  books change; a person's own entries are never touched. Lines that eliminate a cash flow carry the
  row they offset. A residual or a disagreement is returned beside the drafts, never plugged; a month
  the consolidation entity has closed is left as posted.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ProposeConsolidationEntriesRequest): The month to draft the consolidating entries
          for.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse]
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
  body: ProposeConsolidationEntriesRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse | None:
  """Propose Consolidation Entries

   Draft a month's consolidating entries in the group's consolidation entity: what preview-
  consolidation-entries computes, written as drafts that the consolidation entity's close posts.
  Proposing the month again replaces the drafts it wrote before, so it can be run after any member's
  books change; a person's own entries are never touched. Lines that eliminate a cash flow carry the
  row they offset. A residual or a disagreement is returned beside the drafts, never plugged; a month
  the consolidation entity has closed is left as posted.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ProposeConsolidationEntriesRequest): The month to draft the consolidating entries
          for.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse
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
  body: ProposeConsolidationEntriesRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse]:
  """Propose Consolidation Entries

   Draft a month's consolidating entries in the group's consolidation entity: what preview-
  consolidation-entries computes, written as drafts that the consolidation entity's close posts.
  Proposing the month again replaces the drafts it wrote before, so it can be run after any member's
  books change; a person's own entries are never touched. Lines that eliminate a cash flow carry the
  row they offset. A residual or a disagreement is returned beside the drafts, never plugged; a month
  the consolidation entity has closed is left as posted.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ProposeConsolidationEntriesRequest): The month to draft the consolidating entries
          for.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse]
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
  body: ProposeConsolidationEntriesRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse | None:
  """Propose Consolidation Entries

   Draft a month's consolidating entries in the group's consolidation entity: what preview-
  consolidation-entries computes, written as drafts that the consolidation entity's close posts.
  Proposing the month again replaces the drafts it wrote before, so it can be run after any member's
  books change; a person's own entries are never touched. Lines that eliminate a cash flow carry the
  row they offset. A residual or a disagreement is returned beside the drafts, never plugged; a month
  the consolidation entity has closed is left as posted.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ProposeConsolidationEntriesRequest): The month to draft the consolidating entries
          for.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeProposeConsolidationEntriesResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
