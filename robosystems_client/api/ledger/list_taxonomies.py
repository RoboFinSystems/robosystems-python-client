from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.taxonomy_list_response import TaxonomyListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  taxonomy_type: None | str | Unset = UNSET,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_taxonomy_type: None | str | Unset
  if isinstance(taxonomy_type, Unset):
    json_taxonomy_type = UNSET
  else:
    json_taxonomy_type = taxonomy_type
  params["taxonomy_type"] = json_taxonomy_type

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/taxonomies".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TaxonomyListResponse | None:
  if response.status_code == 200:
    response_200 = TaxonomyListResponse.from_dict(response.json())

    return response_200

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | TaxonomyListResponse]:
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
  taxonomy_type: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TaxonomyListResponse]:
  """List Taxonomies

  Args:
      graph_id (str):
      taxonomy_type (None | str | Unset): Filter by type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | TaxonomyListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    taxonomy_type=taxonomy_type,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  taxonomy_type: None | str | Unset = UNSET,
) -> HTTPValidationError | TaxonomyListResponse | None:
  """List Taxonomies

  Args:
      graph_id (str):
      taxonomy_type (None | str | Unset): Filter by type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | TaxonomyListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    taxonomy_type=taxonomy_type,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  taxonomy_type: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TaxonomyListResponse]:
  """List Taxonomies

  Args:
      graph_id (str):
      taxonomy_type (None | str | Unset): Filter by type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | TaxonomyListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    taxonomy_type=taxonomy_type,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  taxonomy_type: None | str | Unset = UNSET,
) -> HTTPValidationError | TaxonomyListResponse | None:
  """List Taxonomies

  Args:
      graph_id (str):
      taxonomy_type (None | str | Unset): Filter by type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | TaxonomyListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      taxonomy_type=taxonomy_type,
    )
  ).parsed
