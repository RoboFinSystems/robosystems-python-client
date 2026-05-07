from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.link_entity_taxonomy_request import LinkEntityTaxonomyRequest
from ...models.operation_envelope_entity_taxonomy_response import (
  OperationEnvelopeEntityTaxonomyResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: LinkEntityTaxonomyRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/link-entity-taxonomy".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeEntityTaxonomyResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeEntityTaxonomyResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | OperationEnvelopeEntityTaxonomyResponse]:
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
  body: LinkEntityTaxonomyRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeEntityTaxonomyResponse]:
  """Link Entity to Taxonomy

   Link the graph's entity to a taxonomy. Idempotent — returns existing linkage if it already exists.
  CoA blocks auto-link at create time; use this only to switch the primary CoA or link a reporting
  extension / custom ontology explicitly.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (LinkEntityTaxonomyRequest): Link an entity to a taxonomy (creates the
          ENTITY_HAS_TAXONOMY edge).

          This is how a graph declares "this entity reports under this taxonomy."
          For ``chart_of_accounts`` taxonomies, this tells the platform which CoA
          the entity uses. For reporting taxonomies, which standard (us-gaap,
          ifrs). Idempotent — re-linking returns the existing edge unchanged.

          CoA blocks auto-link at create time; use this to switch the primary
          CoA, link a reporting extension, or attach a custom ontology
          explicitly.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeEntityTaxonomyResponse]
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
  body: LinkEntityTaxonomyRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeEntityTaxonomyResponse | None:
  """Link Entity to Taxonomy

   Link the graph's entity to a taxonomy. Idempotent — returns existing linkage if it already exists.
  CoA blocks auto-link at create time; use this only to switch the primary CoA or link a reporting
  extension / custom ontology explicitly.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (LinkEntityTaxonomyRequest): Link an entity to a taxonomy (creates the
          ENTITY_HAS_TAXONOMY edge).

          This is how a graph declares "this entity reports under this taxonomy."
          For ``chart_of_accounts`` taxonomies, this tells the platform which CoA
          the entity uses. For reporting taxonomies, which standard (us-gaap,
          ifrs). Idempotent — re-linking returns the existing edge unchanged.

          CoA blocks auto-link at create time; use this to switch the primary
          CoA, link a reporting extension, or attach a custom ontology
          explicitly.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeEntityTaxonomyResponse
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
  body: LinkEntityTaxonomyRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeEntityTaxonomyResponse]:
  """Link Entity to Taxonomy

   Link the graph's entity to a taxonomy. Idempotent — returns existing linkage if it already exists.
  CoA blocks auto-link at create time; use this only to switch the primary CoA or link a reporting
  extension / custom ontology explicitly.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (LinkEntityTaxonomyRequest): Link an entity to a taxonomy (creates the
          ENTITY_HAS_TAXONOMY edge).

          This is how a graph declares "this entity reports under this taxonomy."
          For ``chart_of_accounts`` taxonomies, this tells the platform which CoA
          the entity uses. For reporting taxonomies, which standard (us-gaap,
          ifrs). Idempotent — re-linking returns the existing edge unchanged.

          CoA blocks auto-link at create time; use this to switch the primary
          CoA, link a reporting extension, or attach a custom ontology
          explicitly.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeEntityTaxonomyResponse]
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
  body: LinkEntityTaxonomyRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeEntityTaxonomyResponse | None:
  """Link Entity to Taxonomy

   Link the graph's entity to a taxonomy. Idempotent — returns existing linkage if it already exists.
  CoA blocks auto-link at create time; use this only to switch the primary CoA or link a reporting
  extension / custom ontology explicitly.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (LinkEntityTaxonomyRequest): Link an entity to a taxonomy (creates the
          ENTITY_HAS_TAXONOMY edge).

          This is how a graph declares "this entity reports under this taxonomy."
          For ``chart_of_accounts`` taxonomies, this tells the platform which CoA
          the entity uses. For reporting taxonomies, which standard (us-gaap,
          ifrs). Idempotent — re-linking returns the existing edge unchanged.

          CoA blocks auto-link at create time; use this to switch the primary
          CoA, link a reporting extension, or attach a custom ontology
          explicitly.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeEntityTaxonomyResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
