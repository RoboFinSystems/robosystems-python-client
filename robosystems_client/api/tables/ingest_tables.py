from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_ingest_request import BulkIngestRequest
from ...models.bulk_ingest_response import BulkIngestResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: BulkIngestRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/tables/ingest",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = BulkIngestResponse.from_dict(response.json())

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

  if response.status_code == 409:
    response_409 = ErrorResponse.from_dict(response.json())

    return response_409

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]]:
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
  body: BulkIngestRequest,
) -> Response[Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]]:
  """Ingest Tables to Graph

   Load all files from S3 into DuckDB staging tables and ingest into Kuzu graph database.

  Orchestrates the complete data pipeline from S3 staging files into the Kuzu graph database.
  Processes all tables in a single bulk operation with comprehensive error handling and metrics.

  **Use Cases:**
  - Initial graph population from uploaded data
  - Incremental data updates with new files
  - Complete database rebuild from source files
  - Recovery from failed ingestion attempts

  **Workflow:**
  1. Upload data files via `POST /tables/{table_name}/files`
  2. Files are validated and marked as 'uploaded'
  3. Trigger ingestion: `POST /tables/ingest`
  4. DuckDB staging tables created from S3 patterns
  5. Data copied from DuckDB to Kuzu
  6. Per-table results and metrics returned

  **Rebuild Feature:**
  Setting `rebuild=true` regenerates the entire graph database from scratch:
  - Deletes existing Kuzu database
  - Recreates with fresh schema from active GraphSchema
  - Ingests all data files
  - Safe operation - S3 is source of truth
  - Useful for schema changes or data corrections
  - Graph marked as 'rebuilding' during process

  **Error Handling:**
  - Per-table error isolation with `ignore_errors` flag
  - Partial success support (some tables succeed, some fail)
  - Detailed error reporting per table
  - Graph status tracking throughout process
  - Automatic failure recovery and cleanup

  **Performance:**
  - Processes all tables in sequence
  - Each table timed independently
  - Total execution metrics provided
  - Scales to thousands of files
  - Optimized for large datasets

  **Concurrency Control:**
  Only one ingestion can run per graph at a time. If another ingestion is in progress,
  you'll receive a 409 Conflict error. The distributed lock automatically expires after
  the configured TTL (default: 1 hour) to prevent deadlocks from failed ingestions.

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has independent staging tables and graph data. Ingestion operates
  on the specified graph/subgraph only and does not affect other subgraphs.

  **Important Notes:**
  - Only files with 'uploaded' status are processed
  - Tables with no uploaded files are skipped
  - Use `ignore_errors=false` for strict validation
  - Monitor progress via per-table results
  - Check graph metadata for rebuild status
  - Wait for current ingestion to complete before starting another
  - Table ingestion is included - no credit consumption

  Args:
      graph_id (str):
      body (BulkIngestRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]]
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
  body: BulkIngestRequest,
) -> Optional[Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]]:
  """Ingest Tables to Graph

   Load all files from S3 into DuckDB staging tables and ingest into Kuzu graph database.

  Orchestrates the complete data pipeline from S3 staging files into the Kuzu graph database.
  Processes all tables in a single bulk operation with comprehensive error handling and metrics.

  **Use Cases:**
  - Initial graph population from uploaded data
  - Incremental data updates with new files
  - Complete database rebuild from source files
  - Recovery from failed ingestion attempts

  **Workflow:**
  1. Upload data files via `POST /tables/{table_name}/files`
  2. Files are validated and marked as 'uploaded'
  3. Trigger ingestion: `POST /tables/ingest`
  4. DuckDB staging tables created from S3 patterns
  5. Data copied from DuckDB to Kuzu
  6. Per-table results and metrics returned

  **Rebuild Feature:**
  Setting `rebuild=true` regenerates the entire graph database from scratch:
  - Deletes existing Kuzu database
  - Recreates with fresh schema from active GraphSchema
  - Ingests all data files
  - Safe operation - S3 is source of truth
  - Useful for schema changes or data corrections
  - Graph marked as 'rebuilding' during process

  **Error Handling:**
  - Per-table error isolation with `ignore_errors` flag
  - Partial success support (some tables succeed, some fail)
  - Detailed error reporting per table
  - Graph status tracking throughout process
  - Automatic failure recovery and cleanup

  **Performance:**
  - Processes all tables in sequence
  - Each table timed independently
  - Total execution metrics provided
  - Scales to thousands of files
  - Optimized for large datasets

  **Concurrency Control:**
  Only one ingestion can run per graph at a time. If another ingestion is in progress,
  you'll receive a 409 Conflict error. The distributed lock automatically expires after
  the configured TTL (default: 1 hour) to prevent deadlocks from failed ingestions.

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has independent staging tables and graph data. Ingestion operates
  on the specified graph/subgraph only and does not affect other subgraphs.

  **Important Notes:**
  - Only files with 'uploaded' status are processed
  - Tables with no uploaded files are skipped
  - Use `ignore_errors=false` for strict validation
  - Monitor progress via per-table results
  - Check graph metadata for rebuild status
  - Wait for current ingestion to complete before starting another
  - Table ingestion is included - no credit consumption

  Args:
      graph_id (str):
      body (BulkIngestRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]
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
  body: BulkIngestRequest,
) -> Response[Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]]:
  """Ingest Tables to Graph

   Load all files from S3 into DuckDB staging tables and ingest into Kuzu graph database.

  Orchestrates the complete data pipeline from S3 staging files into the Kuzu graph database.
  Processes all tables in a single bulk operation with comprehensive error handling and metrics.

  **Use Cases:**
  - Initial graph population from uploaded data
  - Incremental data updates with new files
  - Complete database rebuild from source files
  - Recovery from failed ingestion attempts

  **Workflow:**
  1. Upload data files via `POST /tables/{table_name}/files`
  2. Files are validated and marked as 'uploaded'
  3. Trigger ingestion: `POST /tables/ingest`
  4. DuckDB staging tables created from S3 patterns
  5. Data copied from DuckDB to Kuzu
  6. Per-table results and metrics returned

  **Rebuild Feature:**
  Setting `rebuild=true` regenerates the entire graph database from scratch:
  - Deletes existing Kuzu database
  - Recreates with fresh schema from active GraphSchema
  - Ingests all data files
  - Safe operation - S3 is source of truth
  - Useful for schema changes or data corrections
  - Graph marked as 'rebuilding' during process

  **Error Handling:**
  - Per-table error isolation with `ignore_errors` flag
  - Partial success support (some tables succeed, some fail)
  - Detailed error reporting per table
  - Graph status tracking throughout process
  - Automatic failure recovery and cleanup

  **Performance:**
  - Processes all tables in sequence
  - Each table timed independently
  - Total execution metrics provided
  - Scales to thousands of files
  - Optimized for large datasets

  **Concurrency Control:**
  Only one ingestion can run per graph at a time. If another ingestion is in progress,
  you'll receive a 409 Conflict error. The distributed lock automatically expires after
  the configured TTL (default: 1 hour) to prevent deadlocks from failed ingestions.

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has independent staging tables and graph data. Ingestion operates
  on the specified graph/subgraph only and does not affect other subgraphs.

  **Important Notes:**
  - Only files with 'uploaded' status are processed
  - Tables with no uploaded files are skipped
  - Use `ignore_errors=false` for strict validation
  - Monitor progress via per-table results
  - Check graph metadata for rebuild status
  - Wait for current ingestion to complete before starting another
  - Table ingestion is included - no credit consumption

  Args:
      graph_id (str):
      body (BulkIngestRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]]
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
  body: BulkIngestRequest,
) -> Optional[Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]]:
  """Ingest Tables to Graph

   Load all files from S3 into DuckDB staging tables and ingest into Kuzu graph database.

  Orchestrates the complete data pipeline from S3 staging files into the Kuzu graph database.
  Processes all tables in a single bulk operation with comprehensive error handling and metrics.

  **Use Cases:**
  - Initial graph population from uploaded data
  - Incremental data updates with new files
  - Complete database rebuild from source files
  - Recovery from failed ingestion attempts

  **Workflow:**
  1. Upload data files via `POST /tables/{table_name}/files`
  2. Files are validated and marked as 'uploaded'
  3. Trigger ingestion: `POST /tables/ingest`
  4. DuckDB staging tables created from S3 patterns
  5. Data copied from DuckDB to Kuzu
  6. Per-table results and metrics returned

  **Rebuild Feature:**
  Setting `rebuild=true` regenerates the entire graph database from scratch:
  - Deletes existing Kuzu database
  - Recreates with fresh schema from active GraphSchema
  - Ingests all data files
  - Safe operation - S3 is source of truth
  - Useful for schema changes or data corrections
  - Graph marked as 'rebuilding' during process

  **Error Handling:**
  - Per-table error isolation with `ignore_errors` flag
  - Partial success support (some tables succeed, some fail)
  - Detailed error reporting per table
  - Graph status tracking throughout process
  - Automatic failure recovery and cleanup

  **Performance:**
  - Processes all tables in sequence
  - Each table timed independently
  - Total execution metrics provided
  - Scales to thousands of files
  - Optimized for large datasets

  **Concurrency Control:**
  Only one ingestion can run per graph at a time. If another ingestion is in progress,
  you'll receive a 409 Conflict error. The distributed lock automatically expires after
  the configured TTL (default: 1 hour) to prevent deadlocks from failed ingestions.

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has independent staging tables and graph data. Ingestion operates
  on the specified graph/subgraph only and does not affect other subgraphs.

  **Important Notes:**
  - Only files with 'uploaded' status are processed
  - Tables with no uploaded files are skipped
  - Use `ignore_errors=false` for strict validation
  - Monitor progress via per-table results
  - Check graph metadata for rebuild status
  - Wait for current ingestion to complete before starting another
  - Table ingestion is included - no credit consumption

  Args:
      graph_id (str):
      body (BulkIngestRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, BulkIngestResponse, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
