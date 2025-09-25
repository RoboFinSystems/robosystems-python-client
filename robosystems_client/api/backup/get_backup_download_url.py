from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_backup_download_url_response_getbackupdownloadurl import (
  GetBackupDownloadUrlResponseGetbackupdownloadurl,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  backup_id: str,
  *,
  expires_in: Union[Unset, int] = 3600,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  params["expires_in"] = expires_in

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/backups/{backup_id}/download",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]
]:
  if response.status_code == 200:
    response_200 = GetBackupDownloadUrlResponseGetbackupdownloadurl.from_dict(
      response.json()
    )

    return response_200
  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403
  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404
  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
  Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]
]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  expires_in: Union[Unset, int] = 3600,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]
]:
  """Get temporary download URL for backup

   Generate a temporary download URL for a backup (unencrypted, compressed .kuzu files only)

  Args:
      graph_id (str): Graph database identifier
      backup_id (str): Backup identifier
      expires_in (Union[Unset, int]): URL expiration time in seconds Default: 3600.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    backup_id=backup_id,
    expires_in=expires_in,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  expires_in: Union[Unset, int] = 3600,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]
]:
  """Get temporary download URL for backup

   Generate a temporary download URL for a backup (unencrypted, compressed .kuzu files only)

  Args:
      graph_id (str): Graph database identifier
      backup_id (str): Backup identifier
      expires_in (Union[Unset, int]): URL expiration time in seconds Default: 3600.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    backup_id=backup_id,
    client=client,
    expires_in=expires_in,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  expires_in: Union[Unset, int] = 3600,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]
]:
  """Get temporary download URL for backup

   Generate a temporary download URL for a backup (unencrypted, compressed .kuzu files only)

  Args:
      graph_id (str): Graph database identifier
      backup_id (str): Backup identifier
      expires_in (Union[Unset, int]): URL expiration time in seconds Default: 3600.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    backup_id=backup_id,
    expires_in=expires_in,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  expires_in: Union[Unset, int] = 3600,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]
]:
  """Get temporary download URL for backup

   Generate a temporary download URL for a backup (unencrypted, compressed .kuzu files only)

  Args:
      graph_id (str): Graph database identifier
      backup_id (str): Backup identifier
      expires_in (Union[Unset, int]): URL expiration time in seconds Default: 3600.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GetBackupDownloadUrlResponseGetbackupdownloadurl, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      backup_id=backup_id,
      client=client,
      expires_in=expires_in,
      token=token,
      authorization=authorization,
    )
  ).parsed
