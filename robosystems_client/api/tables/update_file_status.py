from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.file_status_update import FileStatusUpdate
from ...models.http_validation_error import HTTPValidationError
from ...models.update_file_status_response_updatefilestatus import (
  UpdateFileStatusResponseUpdatefilestatus,
)
from ...types import Response


def _get_kwargs(
  graph_id: str,
  file_id: str,
  *,
  body: FileStatusUpdate,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "patch",
    "url": f"/v1/graphs/{graph_id}/tables/files/{file_id}",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[
    Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus
  ]
]:
  if response.status_code == 200:
    response_200 = UpdateFileStatusResponseUpdatefilestatus.from_dict(response.json())

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

  if response.status_code == 413:
    response_413 = ErrorResponse.from_dict(response.json())

    return response_413

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
) -> Response[
  Union[
    Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus
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
  body: FileStatusUpdate,
) -> Response[
  Union[
    Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus
  ]
]:
  """Update File Upload Status

   Update file status after upload completes.

  Marks files as uploaded after successful S3 upload. The backend validates
  the file, calculates size and row count, enforces storage limits, and
  registers the DuckDB table for queries.

  **Status Values:**
  - `uploaded`: File successfully uploaded to S3 (triggers validation)
  - `disabled`: Exclude file from ingestion
  - `archived`: Soft delete file

  **What Happens on 'uploaded' Status:**
  1. Verify file exists in S3
  2. Calculate actual file size
  3. Enforce tier storage limits
  4. Calculate or estimate row count
  5. Update table statistics
  6. Register DuckDB external table
  7. File ready for ingestion

  **Row Count Calculation:**
  - **Parquet**: Exact count from file metadata
  - **CSV**: Count rows (minus header)
  - **JSON**: Count array elements
  - **Fallback**: Estimate from file size if reading fails

  **Storage Limits:**
  Enforced per subscription tier. Returns HTTP 413 if limit exceeded.
  Check current usage before large uploads.

  **Important Notes:**
  - Always call this after S3 upload completes
  - Check response for actual row count
  - Storage limit errors (413) mean tier upgrade needed
  - DuckDB registration failures are non-fatal (retried later)
  - Status updates are included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File identifier
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    body=body,
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
  body: FileStatusUpdate,
) -> Optional[
  Union[
    Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus
  ]
]:
  """Update File Upload Status

   Update file status after upload completes.

  Marks files as uploaded after successful S3 upload. The backend validates
  the file, calculates size and row count, enforces storage limits, and
  registers the DuckDB table for queries.

  **Status Values:**
  - `uploaded`: File successfully uploaded to S3 (triggers validation)
  - `disabled`: Exclude file from ingestion
  - `archived`: Soft delete file

  **What Happens on 'uploaded' Status:**
  1. Verify file exists in S3
  2. Calculate actual file size
  3. Enforce tier storage limits
  4. Calculate or estimate row count
  5. Update table statistics
  6. Register DuckDB external table
  7. File ready for ingestion

  **Row Count Calculation:**
  - **Parquet**: Exact count from file metadata
  - **CSV**: Count rows (minus header)
  - **JSON**: Count array elements
  - **Fallback**: Estimate from file size if reading fails

  **Storage Limits:**
  Enforced per subscription tier. Returns HTTP 413 if limit exceeded.
  Check current usage before large uploads.

  **Important Notes:**
  - Always call this after S3 upload completes
  - Check response for actual row count
  - Storage limit errors (413) mean tier upgrade needed
  - DuckDB registration failures are non-fatal (retried later)
  - Status updates are included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File identifier
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus]
  """

  return sync_detailed(
    graph_id=graph_id,
    file_id=file_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileStatusUpdate,
) -> Response[
  Union[
    Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus
  ]
]:
  """Update File Upload Status

   Update file status after upload completes.

  Marks files as uploaded after successful S3 upload. The backend validates
  the file, calculates size and row count, enforces storage limits, and
  registers the DuckDB table for queries.

  **Status Values:**
  - `uploaded`: File successfully uploaded to S3 (triggers validation)
  - `disabled`: Exclude file from ingestion
  - `archived`: Soft delete file

  **What Happens on 'uploaded' Status:**
  1. Verify file exists in S3
  2. Calculate actual file size
  3. Enforce tier storage limits
  4. Calculate or estimate row count
  5. Update table statistics
  6. Register DuckDB external table
  7. File ready for ingestion

  **Row Count Calculation:**
  - **Parquet**: Exact count from file metadata
  - **CSV**: Count rows (minus header)
  - **JSON**: Count array elements
  - **Fallback**: Estimate from file size if reading fails

  **Storage Limits:**
  Enforced per subscription tier. Returns HTTP 413 if limit exceeded.
  Check current usage before large uploads.

  **Important Notes:**
  - Always call this after S3 upload completes
  - Check response for actual row count
  - Storage limit errors (413) mean tier upgrade needed
  - DuckDB registration failures are non-fatal (retried later)
  - Status updates are included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File identifier
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileStatusUpdate,
) -> Optional[
  Union[
    Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus
  ]
]:
  """Update File Upload Status

   Update file status after upload completes.

  Marks files as uploaded after successful S3 upload. The backend validates
  the file, calculates size and row count, enforces storage limits, and
  registers the DuckDB table for queries.

  **Status Values:**
  - `uploaded`: File successfully uploaded to S3 (triggers validation)
  - `disabled`: Exclude file from ingestion
  - `archived`: Soft delete file

  **What Happens on 'uploaded' Status:**
  1. Verify file exists in S3
  2. Calculate actual file size
  3. Enforce tier storage limits
  4. Calculate or estimate row count
  5. Update table statistics
  6. Register DuckDB external table
  7. File ready for ingestion

  **Row Count Calculation:**
  - **Parquet**: Exact count from file metadata
  - **CSV**: Count rows (minus header)
  - **JSON**: Count array elements
  - **Fallback**: Estimate from file size if reading fails

  **Storage Limits:**
  Enforced per subscription tier. Returns HTTP 413 if limit exceeded.
  Check current usage before large uploads.

  **Important Notes:**
  - Always call this after S3 upload completes
  - Check response for actual row count
  - Storage limit errors (413) mean tier upgrade needed
  - DuckDB registration failures are non-fatal (retried later)
  - Status updates are included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File identifier
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError, UpdateFileStatusResponseUpdatefilestatus]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      file_id=file_id,
      client=client,
      body=body,
    )
  ).parsed
