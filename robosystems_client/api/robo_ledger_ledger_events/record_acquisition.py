from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_acquisition_response import (
  OperationEnvelopeAcquisitionResponse,
)
from ...models.record_acquisition_request import RecordAcquisitionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: RecordAcquisitionRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/record-acquisition".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeAcquisitionResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeAcquisitionResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | OperationEnvelopeAcquisitionResponse]:
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
  body: RecordAcquisitionRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeAcquisitionResponse]:
  """Record Acquisition

   Record a member the parent bought from its outside owners, for a member that joined mid-life
  (`joined_on` set) with its balance sheet at acquisition recorded by record-opening-balance. Give the
  consideration paid to the sellers in cents and the basis (the purchase agreement, a valuation);
  optionally the fair value of the outside owners' interest (`nci_fair_value`, for goodwill on the
  whole business) and fair-value step-ups (`allocations`). It writes a draft in the consolidation
  entity, dated the join, that its close posts: the excess of the consideration over the parent's
  share of the member's equity at acquisition goes to the step-ups and the rest to goodwill. preview-
  consolidation-entries then reads the consideration as the parent's investment, so the pre-
  acquisition residual clears. A bargain purchase is refused until `confirm_bargain_purchase` is set
  after the reassessment ASC 805 asks for. Recording again replaces the draft; a posted acquisition is
  reversed first.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordAcquisitionRequest): A member bought from its outside owners: what the parent
          paid them,
          and how the excess over its share of the member's equity at acquisition is
          allocated. The engine never invents a fair value; each comes from the
          person, with the basis.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeAcquisitionResponse]
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
  body: RecordAcquisitionRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeAcquisitionResponse | None:
  """Record Acquisition

   Record a member the parent bought from its outside owners, for a member that joined mid-life
  (`joined_on` set) with its balance sheet at acquisition recorded by record-opening-balance. Give the
  consideration paid to the sellers in cents and the basis (the purchase agreement, a valuation);
  optionally the fair value of the outside owners' interest (`nci_fair_value`, for goodwill on the
  whole business) and fair-value step-ups (`allocations`). It writes a draft in the consolidation
  entity, dated the join, that its close posts: the excess of the consideration over the parent's
  share of the member's equity at acquisition goes to the step-ups and the rest to goodwill. preview-
  consolidation-entries then reads the consideration as the parent's investment, so the pre-
  acquisition residual clears. A bargain purchase is refused until `confirm_bargain_purchase` is set
  after the reassessment ASC 805 asks for. Recording again replaces the draft; a posted acquisition is
  reversed first.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordAcquisitionRequest): A member bought from its outside owners: what the parent
          paid them,
          and how the excess over its share of the member's equity at acquisition is
          allocated. The engine never invents a fair value; each comes from the
          person, with the basis.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeAcquisitionResponse
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
  body: RecordAcquisitionRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeAcquisitionResponse]:
  """Record Acquisition

   Record a member the parent bought from its outside owners, for a member that joined mid-life
  (`joined_on` set) with its balance sheet at acquisition recorded by record-opening-balance. Give the
  consideration paid to the sellers in cents and the basis (the purchase agreement, a valuation);
  optionally the fair value of the outside owners' interest (`nci_fair_value`, for goodwill on the
  whole business) and fair-value step-ups (`allocations`). It writes a draft in the consolidation
  entity, dated the join, that its close posts: the excess of the consideration over the parent's
  share of the member's equity at acquisition goes to the step-ups and the rest to goodwill. preview-
  consolidation-entries then reads the consideration as the parent's investment, so the pre-
  acquisition residual clears. A bargain purchase is refused until `confirm_bargain_purchase` is set
  after the reassessment ASC 805 asks for. Recording again replaces the draft; a posted acquisition is
  reversed first.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordAcquisitionRequest): A member bought from its outside owners: what the parent
          paid them,
          and how the excess over its share of the member's equity at acquisition is
          allocated. The engine never invents a fair value; each comes from the
          person, with the basis.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeAcquisitionResponse]
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
  body: RecordAcquisitionRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeAcquisitionResponse | None:
  """Record Acquisition

   Record a member the parent bought from its outside owners, for a member that joined mid-life
  (`joined_on` set) with its balance sheet at acquisition recorded by record-opening-balance. Give the
  consideration paid to the sellers in cents and the basis (the purchase agreement, a valuation);
  optionally the fair value of the outside owners' interest (`nci_fair_value`, for goodwill on the
  whole business) and fair-value step-ups (`allocations`). It writes a draft in the consolidation
  entity, dated the join, that its close posts: the excess of the consideration over the parent's
  share of the member's equity at acquisition goes to the step-ups and the rest to goodwill. preview-
  consolidation-entries then reads the consideration as the parent's investment, so the pre-
  acquisition residual clears. A bargain purchase is refused until `confirm_bargain_purchase` is set
  after the reassessment ASC 805 asks for. Recording again replaces the draft; a posted acquisition is
  reversed first.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (RecordAcquisitionRequest): A member bought from its outside owners: what the parent
          paid them,
          and how the excess over its share of the member's equity at acquisition is
          allocated. The engine never invents a fair value; each comes from the
          person, with the basis.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeAcquisitionResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
