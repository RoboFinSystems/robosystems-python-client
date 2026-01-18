from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_table_files_response import ListTableFilesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_table_name: None | str | Unset
  if isinstance(table_name, Unset):
    json_table_name = UNSET
  else:
    json_table_name = table_name
  params["table_name"] = json_table_name

  json_status: None | str | Unset
  if isinstance(status, Unset):
    json_status = UNSET
  else:
    json_status = status
  params["status"] = json_status

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/files".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse | None:
  if response.status_code == 200:
    response_200 = ListTableFilesResponse.from_dict(response.json())

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
) -> Response[Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse]:
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
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse]:
  """List Files in Graph

   List all files in the graph with optional filtering.

  Get a complete inventory of files across all tables or filtered by table name,
  status, or other criteria. Files are first-class resources with independent lifecycle.

  **Query Parameters:**
  - `table_name` (optional): Filter by table name
  - `status` (optional): Filter by upload status (uploaded, pending, failed, etc.)

  **Use Cases:**
  - Monitor file upload progress across all tables
  - Verify files are ready for ingestion
  - Check file metadata and sizes
  - Track storage usage per graph
  - Identify failed or incomplete uploads
  - Audit file provenance

  **Returned Metadata:**
  - File ID, name, and format (parquet, csv, json)
  - Size in bytes and row count (if available)
  - Upload status and timestamps
  - DuckDB and graph ingestion status
  - Table association

  **File Lifecycle Tracking:**
  Multi-layer status across S3 → DuckDB → Graph pipeline

  **Important Notes:**
  - Files are graph-scoped, not table-scoped
  - Use table_name parameter to filter by table
  - File listing is included - no credit consumption

  Args:
      graph_id (str):
      table_name (None | str | Unset): Filter by table name (optional)
      status (None | str | Unset): Filter by upload status (optional)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    table_name=table_name,
    status=status,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse | None:
  """List Files in Graph

   List all files in the graph with optional filtering.

  Get a complete inventory of files across all tables or filtered by table name,
  status, or other criteria. Files are first-class resources with independent lifecycle.

  **Query Parameters:**
  - `table_name` (optional): Filter by table name
  - `status` (optional): Filter by upload status (uploaded, pending, failed, etc.)

  **Use Cases:**
  - Monitor file upload progress across all tables
  - Verify files are ready for ingestion
  - Check file metadata and sizes
  - Track storage usage per graph
  - Identify failed or incomplete uploads
  - Audit file provenance

  **Returned Metadata:**
  - File ID, name, and format (parquet, csv, json)
  - Size in bytes and row count (if available)
  - Upload status and timestamps
  - DuckDB and graph ingestion status
  - Table association

  **File Lifecycle Tracking:**
  Multi-layer status across S3 → DuckDB → Graph pipeline

  **Important Notes:**
  - Files are graph-scoped, not table-scoped
  - Use table_name parameter to filter by table
  - File listing is included - no credit consumption

  Args:
      graph_id (str):
      table_name (None | str | Unset): Filter by table name (optional)
      status (None | str | Unset): Filter by upload status (optional)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    table_name=table_name,
    status=status,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse]:
  """List Files in Graph

   List all files in the graph with optional filtering.

  Get a complete inventory of files across all tables or filtered by table name,
  status, or other criteria. Files are first-class resources with independent lifecycle.

  **Query Parameters:**
  - `table_name` (optional): Filter by table name
  - `status` (optional): Filter by upload status (uploaded, pending, failed, etc.)

  **Use Cases:**
  - Monitor file upload progress across all tables
  - Verify files are ready for ingestion
  - Check file metadata and sizes
  - Track storage usage per graph
  - Identify failed or incomplete uploads
  - Audit file provenance

  **Returned Metadata:**
  - File ID, name, and format (parquet, csv, json)
  - Size in bytes and row count (if available)
  - Upload status and timestamps
  - DuckDB and graph ingestion status
  - Table association

  **File Lifecycle Tracking:**
  Multi-layer status across S3 → DuckDB → Graph pipeline

  **Important Notes:**
  - Files are graph-scoped, not table-scoped
  - Use table_name parameter to filter by table
  - File listing is included - no credit consumption

  Args:
      graph_id (str):
      table_name (None | str | Unset): Filter by table name (optional)
      status (None | str | Unset): Filter by upload status (optional)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    table_name=table_name,
    status=status,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse | None:
  """List Files in Graph

   List all files in the graph with optional filtering.

  Get a complete inventory of files across all tables or filtered by table name,
  status, or other criteria. Files are first-class resources with independent lifecycle.

  **Query Parameters:**
  - `table_name` (optional): Filter by table name
  - `status` (optional): Filter by upload status (uploaded, pending, failed, etc.)

  **Use Cases:**
  - Monitor file upload progress across all tables
  - Verify files are ready for ingestion
  - Check file metadata and sizes
  - Track storage usage per graph
  - Identify failed or incomplete uploads
  - Audit file provenance

  **Returned Metadata:**
  - File ID, name, and format (parquet, csv, json)
  - Size in bytes and row count (if available)
  - Upload status and timestamps
  - DuckDB and graph ingestion status
  - Table association

  **File Lifecycle Tracking:**
  Multi-layer status across S3 → DuckDB → Graph pipeline

  **Important Notes:**
  - Files are graph-scoped, not table-scoped
  - Use table_name parameter to filter by table
  - File listing is included - no credit consumption

  Args:
      graph_id (str):
      table_name (None | str | Unset): Filter by table name (optional)
      status (None | str | Unset): Filter by upload status (optional)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | ListTableFilesResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      table_name=table_name,
      status=status,
    )
  ).parsed
