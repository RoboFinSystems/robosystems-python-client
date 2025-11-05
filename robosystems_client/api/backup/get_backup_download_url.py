from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup_download_url_response import BackupDownloadUrlResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  backup_id: str,
  *,
  expires_in: Union[Unset, int] = 3600,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  params["expires_in"] = expires_in

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/backups/{backup_id}/download",
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BackupDownloadUrlResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = BackupDownloadUrlResponse.from_dict(response.json())

    return response_200

  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403

  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BackupDownloadUrlResponse, HTTPValidationError]]:
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
) -> Response[Union[Any, BackupDownloadUrlResponse, HTTPValidationError]]:
  """Get temporary download URL for backup

   Generate a temporary download URL for a backup (unencrypted, compressed .kuzu files only)

  Args:
      graph_id (str):
      backup_id (str): Backup identifier
      expires_in (Union[Unset, int]): URL expiration time in seconds Default: 3600.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, BackupDownloadUrlResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    backup_id=backup_id,
    expires_in=expires_in,
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
) -> Optional[Union[Any, BackupDownloadUrlResponse, HTTPValidationError]]:
  """Get temporary download URL for backup

   Generate a temporary download URL for a backup (unencrypted, compressed .kuzu files only)

  Args:
      graph_id (str):
      backup_id (str): Backup identifier
      expires_in (Union[Unset, int]): URL expiration time in seconds Default: 3600.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, BackupDownloadUrlResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    backup_id=backup_id,
    client=client,
    expires_in=expires_in,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  expires_in: Union[Unset, int] = 3600,
) -> Response[Union[Any, BackupDownloadUrlResponse, HTTPValidationError]]:
  """Get temporary download URL for backup

   Generate a temporary download URL for a backup (unencrypted, compressed .kuzu files only)

  Args:
      graph_id (str):
      backup_id (str): Backup identifier
      expires_in (Union[Unset, int]): URL expiration time in seconds Default: 3600.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, BackupDownloadUrlResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    backup_id=backup_id,
    expires_in=expires_in,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  expires_in: Union[Unset, int] = 3600,
) -> Optional[Union[Any, BackupDownloadUrlResponse, HTTPValidationError]]:
  """Get temporary download URL for backup

   Generate a temporary download URL for a backup (unencrypted, compressed .kuzu files only)

  Args:
      graph_id (str):
      backup_id (str): Backup identifier
      expires_in (Union[Unset, int]): URL expiration time in seconds Default: 3600.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, BackupDownloadUrlResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      backup_id=backup_id,
      client=client,
      expires_in=expires_in,
    )
  ).parsed
