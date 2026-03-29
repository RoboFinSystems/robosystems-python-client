from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.structure_list_response import StructureListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  taxonomy_id: None | str | Unset = UNSET,
  structure_type: None | str | Unset = UNSET,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_taxonomy_id: None | str | Unset
  if isinstance(taxonomy_id, Unset):
    json_taxonomy_id = UNSET
  else:
    json_taxonomy_id = taxonomy_id
  params["taxonomy_id"] = json_taxonomy_id

  json_structure_type: None | str | Unset
  if isinstance(structure_type, Unset):
    json_structure_type = UNSET
  else:
    json_structure_type = structure_type
  params["structure_type"] = json_structure_type

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/structures".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | StructureListResponse | None:
  if response.status_code == 200:
    response_200 = StructureListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | StructureListResponse]:
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
  taxonomy_id: None | str | Unset = UNSET,
  structure_type: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | StructureListResponse]:
  """List Structures

  Args:
      graph_id (str):
      taxonomy_id (None | str | Unset): Filter by taxonomy
      structure_type (None | str | Unset): Filter by type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | StructureListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    taxonomy_id=taxonomy_id,
    structure_type=structure_type,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  taxonomy_id: None | str | Unset = UNSET,
  structure_type: None | str | Unset = UNSET,
) -> HTTPValidationError | StructureListResponse | None:
  """List Structures

  Args:
      graph_id (str):
      taxonomy_id (None | str | Unset): Filter by taxonomy
      structure_type (None | str | Unset): Filter by type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | StructureListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    taxonomy_id=taxonomy_id,
    structure_type=structure_type,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  taxonomy_id: None | str | Unset = UNSET,
  structure_type: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | StructureListResponse]:
  """List Structures

  Args:
      graph_id (str):
      taxonomy_id (None | str | Unset): Filter by taxonomy
      structure_type (None | str | Unset): Filter by type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | StructureListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    taxonomy_id=taxonomy_id,
    structure_type=structure_type,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  taxonomy_id: None | str | Unset = UNSET,
  structure_type: None | str | Unset = UNSET,
) -> HTTPValidationError | StructureListResponse | None:
  """List Structures

  Args:
      graph_id (str):
      taxonomy_id (None | str | Unset): Filter by taxonomy
      structure_type (None | str | Unset): Filter by type

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | StructureListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      taxonomy_id=taxonomy_id,
      structure_type=structure_type,
    )
  ).parsed
