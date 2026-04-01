from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.security_list_response import SecurityListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  entity_id: None | str | Unset = UNSET,
  security_type: None | str | Unset = UNSET,
  is_active: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_entity_id: None | str | Unset
  if isinstance(entity_id, Unset):
    json_entity_id = UNSET
  else:
    json_entity_id = entity_id
  params["entity_id"] = json_entity_id

  json_security_type: None | str | Unset
  if isinstance(security_type, Unset):
    json_security_type = UNSET
  else:
    json_security_type = security_type
  params["security_type"] = json_security_type

  json_is_active: bool | None | Unset
  if isinstance(is_active, Unset):
    json_is_active = UNSET
  else:
    json_is_active = is_active
  params["is_active"] = json_is_active

  params["limit"] = limit

  params["offset"] = offset

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/investor/{graph_id}/securities".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SecurityListResponse | None:
  if response.status_code == 200:
    response_200 = SecurityListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SecurityListResponse]:
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
  entity_id: None | str | Unset = UNSET,
  security_type: None | str | Unset = UNSET,
  is_active: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[HTTPValidationError | SecurityListResponse]:
  """List Securities

  Args:
      graph_id (str):
      entity_id (None | str | Unset): Filter by entity
      security_type (None | str | Unset): Filter by security type
      is_active (bool | None | Unset): Filter by active status
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | SecurityListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    entity_id=entity_id,
    security_type=security_type,
    is_active=is_active,
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
  entity_id: None | str | Unset = UNSET,
  security_type: None | str | Unset = UNSET,
  is_active: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> HTTPValidationError | SecurityListResponse | None:
  """List Securities

  Args:
      graph_id (str):
      entity_id (None | str | Unset): Filter by entity
      security_type (None | str | Unset): Filter by security type
      is_active (bool | None | Unset): Filter by active status
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | SecurityListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    entity_id=entity_id,
    security_type=security_type,
    is_active=is_active,
    limit=limit,
    offset=offset,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  entity_id: None | str | Unset = UNSET,
  security_type: None | str | Unset = UNSET,
  is_active: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[HTTPValidationError | SecurityListResponse]:
  """List Securities

  Args:
      graph_id (str):
      entity_id (None | str | Unset): Filter by entity
      security_type (None | str | Unset): Filter by security type
      is_active (bool | None | Unset): Filter by active status
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | SecurityListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    entity_id=entity_id,
    security_type=security_type,
    is_active=is_active,
    limit=limit,
    offset=offset,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  entity_id: None | str | Unset = UNSET,
  security_type: None | str | Unset = UNSET,
  is_active: bool | None | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> HTTPValidationError | SecurityListResponse | None:
  """List Securities

  Args:
      graph_id (str):
      entity_id (None | str | Unset): Filter by entity
      security_type (None | str | Unset): Filter by security type
      is_active (bool | None | Unset): Filter by active status
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | SecurityListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      entity_id=entity_id,
      security_type=security_type,
      is_active=is_active,
      limit=limit,
      offset=offset,
    )
  ).parsed
