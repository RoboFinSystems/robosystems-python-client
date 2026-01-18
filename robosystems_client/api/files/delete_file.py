from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_file_response import DeleteFileResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  file_id: str,
  *,
  cascade: bool | Unset = False,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  params["cascade"] = cascade

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "delete",
    "url": "/v1/graphs/{graph_id}/files/{file_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      file_id=quote(str(file_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteFileResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = DeleteFileResponse.from_dict(response.json())

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
) -> Response[Any | DeleteFileResponse | ErrorResponse | HTTPValidationError]:
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
  cascade: bool | Unset = False,
) -> Response[Any | DeleteFileResponse | ErrorResponse | HTTPValidationError]:
  """Delete File

   Delete file from all layers.

  Remove file from S3, database tracking, and optionally from DuckDB and graph.
  Files are deleted by file_id, independent of table context.

  **Query Parameters:**
  - `cascade` (optional, default=false): Delete from all layers including DuckDB

  **What Happens (cascade=false):**
  1. File deleted from S3
  2. Database record removed
  3. Table statistics updated

  **What Happens (cascade=true):**
  1. File data deleted from all DuckDB tables (by file_id)
  2. Graph marked as stale
  3. File deleted from S3
  4. Database record removed
  5. Table statistics updated

  **Use Cases:**
  - Remove incorrect or duplicate files
  - Clean up failed uploads
  - Delete files before graph ingestion
  - Surgical data removal with cascade

  **Security:**
  - Write access required
  - Shared repositories block deletions
  - Full audit trail

  **Important:**
  - Use cascade=true for immediate DuckDB cleanup
  - Graph rebuild recommended after cascade deletion
  - File deletion is included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File ID
      cascade (bool | Unset): If true, delete from all layers including DuckDB and mark graph
          stale Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | DeleteFileResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    cascade=cascade,
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
  cascade: bool | Unset = False,
) -> Any | DeleteFileResponse | ErrorResponse | HTTPValidationError | None:
  """Delete File

   Delete file from all layers.

  Remove file from S3, database tracking, and optionally from DuckDB and graph.
  Files are deleted by file_id, independent of table context.

  **Query Parameters:**
  - `cascade` (optional, default=false): Delete from all layers including DuckDB

  **What Happens (cascade=false):**
  1. File deleted from S3
  2. Database record removed
  3. Table statistics updated

  **What Happens (cascade=true):**
  1. File data deleted from all DuckDB tables (by file_id)
  2. Graph marked as stale
  3. File deleted from S3
  4. Database record removed
  5. Table statistics updated

  **Use Cases:**
  - Remove incorrect or duplicate files
  - Clean up failed uploads
  - Delete files before graph ingestion
  - Surgical data removal with cascade

  **Security:**
  - Write access required
  - Shared repositories block deletions
  - Full audit trail

  **Important:**
  - Use cascade=true for immediate DuckDB cleanup
  - Graph rebuild recommended after cascade deletion
  - File deletion is included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File ID
      cascade (bool | Unset): If true, delete from all layers including DuckDB and mark graph
          stale Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | DeleteFileResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    file_id=file_id,
    client=client,
    cascade=cascade,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  cascade: bool | Unset = False,
) -> Response[Any | DeleteFileResponse | ErrorResponse | HTTPValidationError]:
  """Delete File

   Delete file from all layers.

  Remove file from S3, database tracking, and optionally from DuckDB and graph.
  Files are deleted by file_id, independent of table context.

  **Query Parameters:**
  - `cascade` (optional, default=false): Delete from all layers including DuckDB

  **What Happens (cascade=false):**
  1. File deleted from S3
  2. Database record removed
  3. Table statistics updated

  **What Happens (cascade=true):**
  1. File data deleted from all DuckDB tables (by file_id)
  2. Graph marked as stale
  3. File deleted from S3
  4. Database record removed
  5. Table statistics updated

  **Use Cases:**
  - Remove incorrect or duplicate files
  - Clean up failed uploads
  - Delete files before graph ingestion
  - Surgical data removal with cascade

  **Security:**
  - Write access required
  - Shared repositories block deletions
  - Full audit trail

  **Important:**
  - Use cascade=true for immediate DuckDB cleanup
  - Graph rebuild recommended after cascade deletion
  - File deletion is included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File ID
      cascade (bool | Unset): If true, delete from all layers including DuckDB and mark graph
          stale Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | DeleteFileResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    cascade=cascade,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  cascade: bool | Unset = False,
) -> Any | DeleteFileResponse | ErrorResponse | HTTPValidationError | None:
  """Delete File

   Delete file from all layers.

  Remove file from S3, database tracking, and optionally from DuckDB and graph.
  Files are deleted by file_id, independent of table context.

  **Query Parameters:**
  - `cascade` (optional, default=false): Delete from all layers including DuckDB

  **What Happens (cascade=false):**
  1. File deleted from S3
  2. Database record removed
  3. Table statistics updated

  **What Happens (cascade=true):**
  1. File data deleted from all DuckDB tables (by file_id)
  2. Graph marked as stale
  3. File deleted from S3
  4. Database record removed
  5. Table statistics updated

  **Use Cases:**
  - Remove incorrect or duplicate files
  - Clean up failed uploads
  - Delete files before graph ingestion
  - Surgical data removal with cascade

  **Security:**
  - Write access required
  - Shared repositories block deletions
  - Full audit trail

  **Important:**
  - Use cascade=true for immediate DuckDB cleanup
  - Graph rebuild recommended after cascade deletion
  - File deletion is included - no credit consumption

  Args:
      graph_id (str):
      file_id (str): File ID
      cascade (bool | Unset): If true, delete from all layers including DuckDB and mark graph
          stale Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | DeleteFileResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      file_id=file_id,
      client=client,
      cascade=cascade,
    )
  ).parsed
