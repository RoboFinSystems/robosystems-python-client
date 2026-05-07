from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_taxonomy_block_request import DeleteTaxonomyBlockRequest
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_delete_taxonomy_block_response import (
  OperationEnvelopeDeleteTaxonomyBlockResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: DeleteTaxonomyBlockRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/delete-taxonomy-block".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeDeleteTaxonomyBlockResponse.from_dict(
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
) -> Response[ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse]:
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
  body: DeleteTaxonomyBlockRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse]:
  """Delete Taxonomy Block

   Delete a taxonomy block and return a thin confirmation. `cascade_facts=True` also deletes Fact rows
  that reference the taxonomy's elements; default False fails the delete if such facts exist. Library-
  origin block types surface 501.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (DeleteTaxonomyBlockRequest): Request body for the ``delete-taxonomy-block``
          operation.

          ``cascade_facts=False`` (default) fails the delete if any Fact rows
          reference elements in this taxonomy. ``cascade_facts=True`` deletes the
          referencing facts alongside the taxonomy; the response reports
          ``facts_deleted``.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse]
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
  body: DeleteTaxonomyBlockRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse | None:
  """Delete Taxonomy Block

   Delete a taxonomy block and return a thin confirmation. `cascade_facts=True` also deletes Fact rows
  that reference the taxonomy's elements; default False fails the delete if such facts exist. Library-
  origin block types surface 501.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (DeleteTaxonomyBlockRequest): Request body for the ``delete-taxonomy-block``
          operation.

          ``cascade_facts=False`` (default) fails the delete if any Fact rows
          reference elements in this taxonomy. ``cascade_facts=True`` deletes the
          referencing facts alongside the taxonomy; the response reports
          ``facts_deleted``.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse
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
  body: DeleteTaxonomyBlockRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse]:
  """Delete Taxonomy Block

   Delete a taxonomy block and return a thin confirmation. `cascade_facts=True` also deletes Fact rows
  that reference the taxonomy's elements; default False fails the delete if such facts exist. Library-
  origin block types surface 501.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (DeleteTaxonomyBlockRequest): Request body for the ``delete-taxonomy-block``
          operation.

          ``cascade_facts=False`` (default) fails the delete if any Fact rows
          reference elements in this taxonomy. ``cascade_facts=True`` deletes the
          referencing facts alongside the taxonomy; the response reports
          ``facts_deleted``.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse]
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
  body: DeleteTaxonomyBlockRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse | None:
  """Delete Taxonomy Block

   Delete a taxonomy block and return a thin confirmation. `cascade_facts=True` also deletes Fact rows
  that reference the taxonomy's elements; default False fails the delete if such facts exist. Library-
  origin block types surface 501.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (DeleteTaxonomyBlockRequest): Request body for the ``delete-taxonomy-block``
          operation.

          ``cascade_facts=False`` (default) fails the delete if any Fact rows
          reference elements in this taxonomy. ``cascade_facts=True`` deletes the
          referencing facts alongside the taxonomy; the response reports
          ``facts_deleted``.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeDeleteTaxonomyBlockResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
