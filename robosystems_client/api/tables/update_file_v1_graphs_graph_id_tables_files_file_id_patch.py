from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.file_update_request import FileUpdateRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.update_file_v1_graphs_graph_id_tables_files_file_id_patch_response_update_file_v1_graphs_graph_id_tables_files_file_id_patch import (
  UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  file_id: str,
  *,
  body: FileUpdateRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "patch",
    "url": f"/v1/graphs/{graph_id}/tables/files/{file_id}",
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[
    Any,
    ErrorResponse,
    HTTPValidationError,
    UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch,
  ]
]:
  if response.status_code == 200:
    response_200 = UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch.from_dict(
      response.json()
    )

    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = cast(Any, None)
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

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
  Union[
    Any,
    ErrorResponse,
    HTTPValidationError,
    UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch,
  ]
]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileUpdateRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    Any,
    ErrorResponse,
    HTTPValidationError,
    UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch,
  ]
]:
  """Update File

   Update file metadata after upload (size, row count). Marks file as completed.

  Args:
      graph_id (str): Graph database identifier
      file_id (str): File identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (FileUpdateRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError, UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    body=body,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileUpdateRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    Any,
    ErrorResponse,
    HTTPValidationError,
    UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch,
  ]
]:
  """Update File

   Update file metadata after upload (size, row count). Marks file as completed.

  Args:
      graph_id (str): Graph database identifier
      file_id (str): File identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (FileUpdateRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError, UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch]
  """

  return sync_detailed(
    graph_id=graph_id,
    file_id=file_id,
    client=client,
    body=body,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileUpdateRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    Any,
    ErrorResponse,
    HTTPValidationError,
    UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch,
  ]
]:
  """Update File

   Update file metadata after upload (size, row count). Marks file as completed.

  Args:
      graph_id (str): Graph database identifier
      file_id (str): File identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (FileUpdateRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError, UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    body=body,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileUpdateRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    Any,
    ErrorResponse,
    HTTPValidationError,
    UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch,
  ]
]:
  """Update File

   Update file metadata after upload (size, row count). Marks file as completed.

  Args:
      graph_id (str): Graph database identifier
      file_id (str): File identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (FileUpdateRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError, UpdateFileV1GraphsGraphIdTablesFilesFileIdPatchResponseUpdateFileV1GraphsGraphIdTablesFilesFileIdPatch]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      file_id=file_id,
      client=client,
      body=body,
      token=token,
      authorization=authorization,
    )
  ).parsed
