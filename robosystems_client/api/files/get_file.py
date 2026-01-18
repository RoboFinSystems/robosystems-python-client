from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_file_info_response import GetFileInfoResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  file_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/files/{file_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      file_id=quote(str(file_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = GetFileInfoResponse.from_dict(response.json())

    return response_200

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
) -> Response[Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError]:
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
) -> Response[Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError]:
  """Get File Information

   Get detailed information about a specific file.

  Retrieve comprehensive metadata for a single file by file_id, independent of
  table context. Files are first-class resources with complete lifecycle tracking.

  **Returned Information:**
  - File ID, name, format, size
  - Upload status and timestamps
  - **Enhanced Multi-Layer Status** (new in this version):
    - S3 layer: upload_status, uploaded_at, size_bytes, row_count
    - DuckDB layer: duckdb_status, duckdb_staged_at, duckdb_row_count
    - Graph layer: graph_status, graph_ingested_at
  - Table association
  - S3 location

  **Multi-Layer Pipeline Visibility:**
  The `layers` object provides independent status tracking across the three-tier
  data pipeline:
  - **S3 (Immutable Source)**: File upload and validation
  - **DuckDB (Mutable Staging)**: Immediate queryability with file provenance
  - **Graph (Immutable View)**: Optional graph database materialization

  Each layer shows its own status, timestamp, and row count (where applicable),
  enabling precise debugging and monitoring of the data ingestion flow.

  **Use Cases:**
  - Validate file upload completion
  - Monitor multi-layer ingestion progress in real-time
  - Debug upload or staging issues at specific layers
  - Verify file metadata and row counts
  - Track file provenance through the pipeline
  - Identify bottlenecks in the ingestion process

  **Note:**
  File info retrieval is included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
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
) -> Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError | None:
  """Get File Information

   Get detailed information about a specific file.

  Retrieve comprehensive metadata for a single file by file_id, independent of
  table context. Files are first-class resources with complete lifecycle tracking.

  **Returned Information:**
  - File ID, name, format, size
  - Upload status and timestamps
  - **Enhanced Multi-Layer Status** (new in this version):
    - S3 layer: upload_status, uploaded_at, size_bytes, row_count
    - DuckDB layer: duckdb_status, duckdb_staged_at, duckdb_row_count
    - Graph layer: graph_status, graph_ingested_at
  - Table association
  - S3 location

  **Multi-Layer Pipeline Visibility:**
  The `layers` object provides independent status tracking across the three-tier
  data pipeline:
  - **S3 (Immutable Source)**: File upload and validation
  - **DuckDB (Mutable Staging)**: Immediate queryability with file provenance
  - **Graph (Immutable View)**: Optional graph database materialization

  Each layer shows its own status, timestamp, and row count (where applicable),
  enabling precise debugging and monitoring of the data ingestion flow.

  **Use Cases:**
  - Validate file upload completion
  - Monitor multi-layer ingestion progress in real-time
  - Debug upload or staging issues at specific layers
  - Verify file metadata and row counts
  - Track file provenance through the pipeline
  - Identify bottlenecks in the ingestion process

  **Note:**
  File info retrieval is included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    file_id=file_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError]:
  """Get File Information

   Get detailed information about a specific file.

  Retrieve comprehensive metadata for a single file by file_id, independent of
  table context. Files are first-class resources with complete lifecycle tracking.

  **Returned Information:**
  - File ID, name, format, size
  - Upload status and timestamps
  - **Enhanced Multi-Layer Status** (new in this version):
    - S3 layer: upload_status, uploaded_at, size_bytes, row_count
    - DuckDB layer: duckdb_status, duckdb_staged_at, duckdb_row_count
    - Graph layer: graph_status, graph_ingested_at
  - Table association
  - S3 location

  **Multi-Layer Pipeline Visibility:**
  The `layers` object provides independent status tracking across the three-tier
  data pipeline:
  - **S3 (Immutable Source)**: File upload and validation
  - **DuckDB (Mutable Staging)**: Immediate queryability with file provenance
  - **Graph (Immutable View)**: Optional graph database materialization

  Each layer shows its own status, timestamp, and row count (where applicable),
  enabling precise debugging and monitoring of the data ingestion flow.

  **Use Cases:**
  - Validate file upload completion
  - Monitor multi-layer ingestion progress in real-time
  - Debug upload or staging issues at specific layers
  - Verify file metadata and row counts
  - Track file provenance through the pipeline
  - Identify bottlenecks in the ingestion process

  **Note:**
  File info retrieval is included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
) -> Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError | None:
  """Get File Information

   Get detailed information about a specific file.

  Retrieve comprehensive metadata for a single file by file_id, independent of
  table context. Files are first-class resources with complete lifecycle tracking.

  **Returned Information:**
  - File ID, name, format, size
  - Upload status and timestamps
  - **Enhanced Multi-Layer Status** (new in this version):
    - S3 layer: upload_status, uploaded_at, size_bytes, row_count
    - DuckDB layer: duckdb_status, duckdb_staged_at, duckdb_row_count
    - Graph layer: graph_status, graph_ingested_at
  - Table association
  - S3 location

  **Multi-Layer Pipeline Visibility:**
  The `layers` object provides independent status tracking across the three-tier
  data pipeline:
  - **S3 (Immutable Source)**: File upload and validation
  - **DuckDB (Mutable Staging)**: Immediate queryability with file provenance
  - **Graph (Immutable View)**: Optional graph database materialization

  Each layer shows its own status, timestamp, and row count (where applicable),
  enabling precise debugging and monitoring of the data ingestion flow.

  **Use Cases:**
  - Validate file upload completion
  - Monitor multi-layer ingestion progress in real-time
  - Debug upload or staging issues at specific layers
  - Verify file metadata and row counts
  - Track file provenance through the pipeline
  - Identify bottlenecks in the ingestion process

  **Note:**
  File info retrieval is included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | GetFileInfoResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      file_id=file_id,
      client=client,
    )
  ).parsed
