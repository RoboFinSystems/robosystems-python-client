from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_mapping_association_operation import (
  CreateMappingAssociationOperation,
)
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_association_response import (
  OperationEnvelopeAssociationResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: CreateMappingAssociationOperation,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/create-mapping-association".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeAssociationResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeAssociationResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | OperationEnvelopeAssociationResponse]:
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
  body: CreateMappingAssociationOperation,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeAssociationResponse]:
  """Create Mapping Association

   Link a chart-of-accounts element to a US GAAP reporting concept. One mapping edge per call — use
  `auto-map-elements` for bulk AI-assisted mapping. Duplicate (from, to, type) tuples return 409.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (CreateMappingAssociationOperation): Create one CoA → reporting-concept mapping edge.

          This is the iterative, AI-assisted craft path. Each call adds a single
          association to the target mapping structure. Use `auto-map-elements`
          to create many at once via the MappingAgent. Reject duplicates: if
          the (from, to, type) tuple already exists, the call returns 409.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeAssociationResponse]
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
  body: CreateMappingAssociationOperation,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeAssociationResponse | None:
  """Create Mapping Association

   Link a chart-of-accounts element to a US GAAP reporting concept. One mapping edge per call — use
  `auto-map-elements` for bulk AI-assisted mapping. Duplicate (from, to, type) tuples return 409.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (CreateMappingAssociationOperation): Create one CoA → reporting-concept mapping edge.

          This is the iterative, AI-assisted craft path. Each call adds a single
          association to the target mapping structure. Use `auto-map-elements`
          to create many at once via the MappingAgent. Reject duplicates: if
          the (from, to, type) tuple already exists, the call returns 409.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeAssociationResponse
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
  body: CreateMappingAssociationOperation,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeAssociationResponse]:
  """Create Mapping Association

   Link a chart-of-accounts element to a US GAAP reporting concept. One mapping edge per call — use
  `auto-map-elements` for bulk AI-assisted mapping. Duplicate (from, to, type) tuples return 409.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (CreateMappingAssociationOperation): Create one CoA → reporting-concept mapping edge.

          This is the iterative, AI-assisted craft path. Each call adds a single
          association to the target mapping structure. Use `auto-map-elements`
          to create many at once via the MappingAgent. Reject duplicates: if
          the (from, to, type) tuple already exists, the call returns 409.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeAssociationResponse]
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
  body: CreateMappingAssociationOperation,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeAssociationResponse | None:
  """Create Mapping Association

   Link a chart-of-accounts element to a US GAAP reporting concept. One mapping edge per call — use
  `auto-map-elements` for bulk AI-assisted mapping. Duplicate (from, to, type) tuples return 409.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (CreateMappingAssociationOperation): Create one CoA → reporting-concept mapping edge.

          This is the iterative, AI-assisted craft path. Each call adds a single
          association to the target mapping structure. Use `auto-map-elements`
          to create many at once via the MappingAgent. Reject duplicates: if
          the (from, to, type) tuple already exists, the call returns 409.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeAssociationResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
