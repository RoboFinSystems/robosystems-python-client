from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.memory_list_response import MemoryListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  memory_type: None | str | Unset = UNSET,
  source: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  json_memory_type: None | str | Unset
  if isinstance(memory_type, Unset):
    json_memory_type = UNSET
  else:
    json_memory_type = memory_type
  params["memory_type"] = json_memory_type

  json_source: None | str | Unset
  if isinstance(source, Unset):
    json_source = UNSET
  else:
    json_source = source
  params["source"] = json_source

  params["limit"] = limit

  params["offset"] = offset

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/memory".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | MemoryListResponse | None:
  if response.status_code == 200:
    response_200 = MemoryListResponse.from_dict(response.json())

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

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | MemoryListResponse]:
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
  memory_type: None | str | Unset = UNSET,
  source: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[ErrorResponse | HTTPValidationError | MemoryListResponse]:
  """List Memories

  Args:
      graph_id (str):
      memory_type (None | str | Unset): Filter by memory type
      source (None | str | Unset): Filter by source
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | MemoryListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    memory_type=memory_type,
    source=source,
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
  memory_type: None | str | Unset = UNSET,
  source: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> ErrorResponse | HTTPValidationError | MemoryListResponse | None:
  """List Memories

  Args:
      graph_id (str):
      memory_type (None | str | Unset): Filter by memory type
      source (None | str | Unset): Filter by source
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | MemoryListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    memory_type=memory_type,
    source=source,
    limit=limit,
    offset=offset,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  memory_type: None | str | Unset = UNSET,
  source: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[ErrorResponse | HTTPValidationError | MemoryListResponse]:
  """List Memories

  Args:
      graph_id (str):
      memory_type (None | str | Unset): Filter by memory type
      source (None | str | Unset): Filter by source
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | MemoryListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    memory_type=memory_type,
    source=source,
    limit=limit,
    offset=offset,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  memory_type: None | str | Unset = UNSET,
  source: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> ErrorResponse | HTTPValidationError | MemoryListResponse | None:
  """List Memories

  Args:
      graph_id (str):
      memory_type (None | str | Unset): Filter by memory type
      source (None | str | Unset): Filter by source
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | MemoryListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      memory_type=memory_type,
      source=source,
      limit=limit,
      offset=offset,
    )
  ).parsed
