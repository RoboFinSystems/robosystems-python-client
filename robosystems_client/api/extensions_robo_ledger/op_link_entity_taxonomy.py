from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.link_entity_taxonomy_request import LinkEntityTaxonomyRequest
from ...models.operation_envelope import OperationEnvelope
from ...models.operation_error import OperationError
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
) -> Any | HTTPValidationError | OperationEnvelope | OperationError | None:
  if response.status_code == 200:
    response_200 = OperationEnvelope.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = OperationError.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = cast(Any, None)
    return response_401

  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403

  if response.status_code == 404:
    response_404 = OperationError.from_dict(response.json())

    return response_404

  if response.status_code == 409:
    response_409 = OperationError.from_dict(response.json())

    return response_409

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = cast(Any, None)
    return response_429

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | OperationEnvelope | OperationError]:
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
) -> Response[Any | HTTPValidationError | OperationEnvelope | OperationError]:
  """Link Entity to Taxonomy

   Link the graph's entity to a taxonomy (creates the ENTITY_HAS_TAXONOMY edge). Idempotent — returns
  existing linkage if it already exists. Required after creating a CoA taxonomy so the platform knows
  which chart of accounts the entity reports under.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (LinkEntityTaxonomyRequest): Link an entity to a taxonomy (creates the
          ENTITY_HAS_TAXONOMY edge).

          This is how a graph declares "this entity reports under this taxonomy."
          For chart_of_accounts taxonomies, this tells the platform which CoA the
          entity uses. For reporting taxonomies, which standard (us-gaap, ifrs).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError | OperationEnvelope | OperationError]
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
) -> Any | HTTPValidationError | OperationEnvelope | OperationError | None:
  """Link Entity to Taxonomy

   Link the graph's entity to a taxonomy (creates the ENTITY_HAS_TAXONOMY edge). Idempotent — returns
  existing linkage if it already exists. Required after creating a CoA taxonomy so the platform knows
  which chart of accounts the entity reports under.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (LinkEntityTaxonomyRequest): Link an entity to a taxonomy (creates the
          ENTITY_HAS_TAXONOMY edge).

          This is how a graph declares "this entity reports under this taxonomy."
          For chart_of_accounts taxonomies, this tells the platform which CoA the
          entity uses. For reporting taxonomies, which standard (us-gaap, ifrs).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError | OperationEnvelope | OperationError
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
) -> Response[Any | HTTPValidationError | OperationEnvelope | OperationError]:
  """Link Entity to Taxonomy

   Link the graph's entity to a taxonomy (creates the ENTITY_HAS_TAXONOMY edge). Idempotent — returns
  existing linkage if it already exists. Required after creating a CoA taxonomy so the platform knows
  which chart of accounts the entity reports under.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (LinkEntityTaxonomyRequest): Link an entity to a taxonomy (creates the
          ENTITY_HAS_TAXONOMY edge).

          This is how a graph declares "this entity reports under this taxonomy."
          For chart_of_accounts taxonomies, this tells the platform which CoA the
          entity uses. For reporting taxonomies, which standard (us-gaap, ifrs).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError | OperationEnvelope | OperationError]
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
) -> Any | HTTPValidationError | OperationEnvelope | OperationError | None:
  """Link Entity to Taxonomy

   Link the graph's entity to a taxonomy (creates the ENTITY_HAS_TAXONOMY edge). Idempotent — returns
  existing linkage if it already exists. Required after creating a CoA taxonomy so the platform knows
  which chart of accounts the entity reports under.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (LinkEntityTaxonomyRequest): Link an entity to a taxonomy (creates the
          ENTITY_HAS_TAXONOMY edge).

          This is how a graph declares "this entity reports under this taxonomy."
          For chart_of_accounts taxonomies, this tells the platform which CoA the
          entity uses. For reporting taxonomies, which standard (us-gaap, ifrs).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError | OperationEnvelope | OperationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
