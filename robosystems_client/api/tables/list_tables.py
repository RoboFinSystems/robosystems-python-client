from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.table_list_response import TableListResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/tables",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
  if response.status_code == 200:
    response_200 = TableListResponse.from_dict(response.json())

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

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
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
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
  """List Staging Tables

   List all DuckDB staging tables with comprehensive metrics and status.

  Get a complete inventory of all staging tables for a graph, including
  file counts, storage sizes, and row estimates. Essential for monitoring
  the data pipeline and determining which tables are ready for ingestion.

  **Returned Metrics:**
  - Table name and type (node/relationship)
  - File count per table
  - Total storage size in bytes
  - Estimated row count
  - S3 location pattern
  - Ready-for-ingestion status

  **Use Cases:**
  - Monitor data upload progress
  - Check which tables have files ready
  - Track storage consumption
  - Validate pipeline before ingestion
  - Capacity planning

  **Workflow:**
  1. List tables to see current state
  2. Upload files to empty tables
  3. Re-list to verify uploads
  4. Check file counts and sizes
  5. Ingest when ready

  **Important Notes:**
  - Tables with `file_count > 0` have data ready
  - Check `total_size_bytes` for storage monitoring
  - Use `s3_location` to verify upload paths
  - Empty tables (file_count=0) are skipped during ingestion
  - Table queries are included - no credit consumption

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
  """List Staging Tables

   List all DuckDB staging tables with comprehensive metrics and status.

  Get a complete inventory of all staging tables for a graph, including
  file counts, storage sizes, and row estimates. Essential for monitoring
  the data pipeline and determining which tables are ready for ingestion.

  **Returned Metrics:**
  - Table name and type (node/relationship)
  - File count per table
  - Total storage size in bytes
  - Estimated row count
  - S3 location pattern
  - Ready-for-ingestion status

  **Use Cases:**
  - Monitor data upload progress
  - Check which tables have files ready
  - Track storage consumption
  - Validate pipeline before ingestion
  - Capacity planning

  **Workflow:**
  1. List tables to see current state
  2. Upload files to empty tables
  3. Re-list to verify uploads
  4. Check file counts and sizes
  5. Ingest when ready

  **Important Notes:**
  - Tables with `file_count > 0` have data ready
  - Check `total_size_bytes` for storage monitoring
  - Use `s3_location` to verify upload paths
  - Empty tables (file_count=0) are skipped during ingestion
  - Table queries are included - no credit consumption

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
  """List Staging Tables

   List all DuckDB staging tables with comprehensive metrics and status.

  Get a complete inventory of all staging tables for a graph, including
  file counts, storage sizes, and row estimates. Essential for monitoring
  the data pipeline and determining which tables are ready for ingestion.

  **Returned Metrics:**
  - Table name and type (node/relationship)
  - File count per table
  - Total storage size in bytes
  - Estimated row count
  - S3 location pattern
  - Ready-for-ingestion status

  **Use Cases:**
  - Monitor data upload progress
  - Check which tables have files ready
  - Track storage consumption
  - Validate pipeline before ingestion
  - Capacity planning

  **Workflow:**
  1. List tables to see current state
  2. Upload files to empty tables
  3. Re-list to verify uploads
  4. Check file counts and sizes
  5. Ingest when ready

  **Important Notes:**
  - Tables with `file_count > 0` have data ready
  - Check `total_size_bytes` for storage monitoring
  - Use `s3_location` to verify upload paths
  - Empty tables (file_count=0) are skipped during ingestion
  - Table queries are included - no credit consumption

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
  """List Staging Tables

   List all DuckDB staging tables with comprehensive metrics and status.

  Get a complete inventory of all staging tables for a graph, including
  file counts, storage sizes, and row estimates. Essential for monitoring
  the data pipeline and determining which tables are ready for ingestion.

  **Returned Metrics:**
  - Table name and type (node/relationship)
  - File count per table
  - Total storage size in bytes
  - Estimated row count
  - S3 location pattern
  - Ready-for-ingestion status

  **Use Cases:**
  - Monitor data upload progress
  - Check which tables have files ready
  - Track storage consumption
  - Validate pipeline before ingestion
  - Capacity planning

  **Workflow:**
  1. List tables to see current state
  2. Upload files to empty tables
  3. Re-list to verify uploads
  4. Check file counts and sizes
  5. Ingest when ready

  **Important Notes:**
  - Tables with `file_count > 0` have data ready
  - Check `total_size_bytes` for storage monitoring
  - Use `s3_location` to verify upload paths
  - Empty tables (file_count=0) are skipped during ingestion
  - Table queries are included - no credit consumption

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
