from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup_list_response import BackupListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  limit: Union[Unset, int] = 50,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  params["limit"] = limit

  params["offset"] = offset

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/backups",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BackupListResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = BackupListResponse.from_dict(response.json())

    return response_200
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BackupListResponse, HTTPValidationError]]:
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
  limit: Union[Unset, int] = 50,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[BackupListResponse, HTTPValidationError]]:
  """List Kuzu graph backups

   List all backups for the specified graph database

  Args:
      graph_id (str): Graph database identifier
      limit (Union[Unset, int]): Maximum number of backups to return Default: 50.
      offset (Union[Unset, int]): Number of backups to skip Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[BackupListResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    limit=limit,
    offset=offset,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  limit: Union[Unset, int] = 50,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[BackupListResponse, HTTPValidationError]]:
  """List Kuzu graph backups

   List all backups for the specified graph database

  Args:
      graph_id (str): Graph database identifier
      limit (Union[Unset, int]): Maximum number of backups to return Default: 50.
      offset (Union[Unset, int]): Number of backups to skip Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[BackupListResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    limit=limit,
    offset=offset,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  limit: Union[Unset, int] = 50,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[BackupListResponse, HTTPValidationError]]:
  """List Kuzu graph backups

   List all backups for the specified graph database

  Args:
      graph_id (str): Graph database identifier
      limit (Union[Unset, int]): Maximum number of backups to return Default: 50.
      offset (Union[Unset, int]): Number of backups to skip Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[BackupListResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    limit=limit,
    offset=offset,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  limit: Union[Unset, int] = 50,
  offset: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[BackupListResponse, HTTPValidationError]]:
  """List Kuzu graph backups

   List all backups for the specified graph database

  Args:
      graph_id (str): Graph database identifier
      limit (Union[Unset, int]): Maximum number of backups to return Default: 50.
      offset (Union[Unset, int]): Number of backups to skip Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[BackupListResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      limit=limit,
      offset=offset,
      token=token,
      authorization=authorization,
    )
  ).parsed
