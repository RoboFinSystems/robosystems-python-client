from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.file_upload_request import FileUploadRequest
from ...models.file_upload_response import FileUploadResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: FileUploadRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/files".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | FileUploadResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = FileUploadResponse.from_dict(response.json())

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
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | FileUploadResponse | HTTPValidationError]:
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
  body: FileUploadRequest,
) -> Response[Any | ErrorResponse | FileUploadResponse | HTTPValidationError]:
  """Create File Upload

   Generate presigned S3 URL for file upload.

  Initiate file upload by generating a secure, time-limited presigned S3 URL.
  Files are first-class resources uploaded directly to S3.

  **Request Body:**
  - `file_name`: Name of the file (1-255 characters)
  - `file_format`: Format (parquet, csv, json)
  - `table_name`: Table to associate file with

  **Upload Workflow:**
  1. Call this endpoint to get presigned URL
  2. PUT file directly to S3 URL
  3. Call PATCH /files/{file_id} with status='uploaded'
  4. Backend validates and stages in DuckDB immediately
  5. Background task ingests to graph

  **Supported Formats:**
  - Parquet, CSV, JSON

  **Auto-Table Creation:**
  Tables are automatically created if they don't exist.

  **Important Notes:**
  - Presigned URLs expire (default: 1 hour)
  - Files are graph-scoped, independent resources
  - Upload URL generation is included - no credit consumption

  Args:
      graph_id (str):
      body (FileUploadRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | FileUploadResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: FileUploadRequest,
) -> Any | ErrorResponse | FileUploadResponse | HTTPValidationError | None:
  """Create File Upload

   Generate presigned S3 URL for file upload.

  Initiate file upload by generating a secure, time-limited presigned S3 URL.
  Files are first-class resources uploaded directly to S3.

  **Request Body:**
  - `file_name`: Name of the file (1-255 characters)
  - `file_format`: Format (parquet, csv, json)
  - `table_name`: Table to associate file with

  **Upload Workflow:**
  1. Call this endpoint to get presigned URL
  2. PUT file directly to S3 URL
  3. Call PATCH /files/{file_id} with status='uploaded'
  4. Backend validates and stages in DuckDB immediately
  5. Background task ingests to graph

  **Supported Formats:**
  - Parquet, CSV, JSON

  **Auto-Table Creation:**
  Tables are automatically created if they don't exist.

  **Important Notes:**
  - Presigned URLs expire (default: 1 hour)
  - Files are graph-scoped, independent resources
  - Upload URL generation is included - no credit consumption

  Args:
      graph_id (str):
      body (FileUploadRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | FileUploadResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: FileUploadRequest,
) -> Response[Any | ErrorResponse | FileUploadResponse | HTTPValidationError]:
  """Create File Upload

   Generate presigned S3 URL for file upload.

  Initiate file upload by generating a secure, time-limited presigned S3 URL.
  Files are first-class resources uploaded directly to S3.

  **Request Body:**
  - `file_name`: Name of the file (1-255 characters)
  - `file_format`: Format (parquet, csv, json)
  - `table_name`: Table to associate file with

  **Upload Workflow:**
  1. Call this endpoint to get presigned URL
  2. PUT file directly to S3 URL
  3. Call PATCH /files/{file_id} with status='uploaded'
  4. Backend validates and stages in DuckDB immediately
  5. Background task ingests to graph

  **Supported Formats:**
  - Parquet, CSV, JSON

  **Auto-Table Creation:**
  Tables are automatically created if they don't exist.

  **Important Notes:**
  - Presigned URLs expire (default: 1 hour)
  - Files are graph-scoped, independent resources
  - Upload URL generation is included - no credit consumption

  Args:
      graph_id (str):
      body (FileUploadRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | FileUploadResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: FileUploadRequest,
) -> Any | ErrorResponse | FileUploadResponse | HTTPValidationError | None:
  """Create File Upload

   Generate presigned S3 URL for file upload.

  Initiate file upload by generating a secure, time-limited presigned S3 URL.
  Files are first-class resources uploaded directly to S3.

  **Request Body:**
  - `file_name`: Name of the file (1-255 characters)
  - `file_format`: Format (parquet, csv, json)
  - `table_name`: Table to associate file with

  **Upload Workflow:**
  1. Call this endpoint to get presigned URL
  2. PUT file directly to S3 URL
  3. Call PATCH /files/{file_id} with status='uploaded'
  4. Backend validates and stages in DuckDB immediately
  5. Background task ingests to graph

  **Supported Formats:**
  - Parquet, CSV, JSON

  **Auto-Table Creation:**
  Tables are automatically created if they don't exist.

  **Important Notes:**
  - Presigned URLs expire (default: 1 hour)
  - Files are graph-scoped, independent resources
  - Upload URL generation is included - no credit consumption

  Args:
      graph_id (str):
      body (FileUploadRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | FileUploadResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
