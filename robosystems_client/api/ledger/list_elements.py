from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.element_list_response import ElementListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  taxonomy_id: None | str | Unset = UNSET,
  source: None | str | Unset = UNSET,
  classification: None | str | Unset = UNSET,
  is_abstract: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_taxonomy_id: None | str | Unset
  if isinstance(taxonomy_id, Unset):
    json_taxonomy_id = UNSET
  else:
    json_taxonomy_id = taxonomy_id
  params["taxonomy_id"] = json_taxonomy_id

  json_source: None | str | Unset
  if isinstance(source, Unset):
    json_source = UNSET
  else:
    json_source = source
  params["source"] = json_source

  json_classification: None | str | Unset
  if isinstance(classification, Unset):
    json_classification = UNSET
  else:
    json_classification = classification
  params["classification"] = json_classification

  json_is_abstract: bool | None | Unset
  if isinstance(is_abstract, Unset):
    json_is_abstract = UNSET
  else:
    json_is_abstract = is_abstract
  params["is_abstract"] = json_is_abstract

  params["limit"] = limit

  params["offset"] = offset

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/elements".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ElementListResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = ElementListResponse.from_dict(response.json())

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
) -> Response[ElementListResponse | HTTPValidationError]:
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
  source: None | str | Unset = UNSET,
  classification: None | str | Unset = UNSET,
  is_abstract: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[ElementListResponse | HTTPValidationError]:
  """List Elements

  Args:
      graph_id (str):
      taxonomy_id (None | str | Unset): Filter by taxonomy
      source (None | str | Unset): Filter by source
      classification (None | str | Unset): Filter by classification
      is_abstract (bool | None | Unset): Filter by abstract
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ElementListResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    taxonomy_id=taxonomy_id,
    source=source,
    classification=classification,
    is_abstract=is_abstract,
    limit=limit,
    offset=offset,
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
  source: None | str | Unset = UNSET,
  classification: None | str | Unset = UNSET,
  is_abstract: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> ElementListResponse | HTTPValidationError | None:
  """List Elements

  Args:
      graph_id (str):
      taxonomy_id (None | str | Unset): Filter by taxonomy
      source (None | str | Unset): Filter by source
      classification (None | str | Unset): Filter by classification
      is_abstract (bool | None | Unset): Filter by abstract
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ElementListResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    taxonomy_id=taxonomy_id,
    source=source,
    classification=classification,
    is_abstract=is_abstract,
    limit=limit,
    offset=offset,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  taxonomy_id: None | str | Unset = UNSET,
  source: None | str | Unset = UNSET,
  classification: None | str | Unset = UNSET,
  is_abstract: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[ElementListResponse | HTTPValidationError]:
  """List Elements

  Args:
      graph_id (str):
      taxonomy_id (None | str | Unset): Filter by taxonomy
      source (None | str | Unset): Filter by source
      classification (None | str | Unset): Filter by classification
      is_abstract (bool | None | Unset): Filter by abstract
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ElementListResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    taxonomy_id=taxonomy_id,
    source=source,
    classification=classification,
    is_abstract=is_abstract,
    limit=limit,
    offset=offset,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  taxonomy_id: None | str | Unset = UNSET,
  source: None | str | Unset = UNSET,
  classification: None | str | Unset = UNSET,
  is_abstract: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> ElementListResponse | HTTPValidationError | None:
  """List Elements

  Args:
      graph_id (str):
      taxonomy_id (None | str | Unset): Filter by taxonomy
      source (None | str | Unset): Filter by source
      classification (None | str | Unset): Filter by classification
      is_abstract (bool | None | Unset): Filter by abstract
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ElementListResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      taxonomy_id=taxonomy_id,
      source=source,
      classification=classification,
      is_abstract=is_abstract,
      limit=limit,
      offset=offset,
    )
  ).parsed
