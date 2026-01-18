from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.materialize_request import MaterializeRequest
from ...models.materialize_response import MaterializeResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: MaterializeRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/materialize".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | MaterializeResponse | None:
  if response.status_code == 200:
    response_200 = MaterializeResponse.from_dict(response.json())

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

  if response.status_code == 409:
    response_409 = ErrorResponse.from_dict(response.json())

    return response_409

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
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | HTTPValidationError | MaterializeResponse]:
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
  body: MaterializeRequest,
) -> Response[Any | ErrorResponse | HTTPValidationError | MaterializeResponse]:
  """Materialize Graph from DuckDB

   Rebuild entire graph from DuckDB staging tables (materialized view pattern).

  This endpoint rebuilds the complete graph database from the current state of DuckDB
  staging tables. It automatically discovers all tables, ingests them in the correct
  order (nodes before relationships), and clears the staleness flag.

  **When to Use:**
  - After batch uploads (files uploaded with ingest_to_graph=false)
  - After cascade file deletions (graph marked stale)
  - To ensure graph consistency with DuckDB state
  - Periodic full refresh

  **What Happens:**
  1. Discovers all tables for the graph from PostgreSQL registry
  2. Sorts tables (nodes before relationships)
  3. Ingests all tables from DuckDB to graph in order
  4. Clears staleness flag on success
  5. Returns detailed materialization report

  **Staleness Check:**
  By default, only materializes if graph is stale (after deletions or missed ingestions).
  Use `force=true` to rebuild regardless of staleness.

  **Rebuild Feature:**
  Setting `rebuild=true` regenerates the entire graph database from scratch:
  - Deletes existing graph database
  - Recreates with fresh schema from active GraphSchema
  - Ingests all data files
  - Safe operation - DuckDB is source of truth
  - Useful for schema changes or data corrections
  - Graph marked as 'rebuilding' during process

  **Table Ordering:**
  Node tables (PascalCase) are ingested before relationship tables (UPPERCASE) to
  ensure referential integrity.

  **Error Handling:**
  With `ignore_errors=true` (default), continues materializing even if individual
  rows fail. Failed rows are logged but don't stop the process.

  **Concurrency Control:**
  Only one materialization can run per graph at a time. If another materialization is in progress,
  you'll receive a 409 Conflict error. The distributed lock automatically expires after
  the configured TTL (default: 1 hour) to prevent deadlocks from failed materializations.

  **Performance:**
  Full graph materialization can take minutes for large datasets. Consider running
  during off-peak hours for production systems.

  **Credits:**
  Materialization is included - no credit consumption

  Args:
      graph_id (str):
      body (MaterializeRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | MaterializeResponse]
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
  body: MaterializeRequest,
) -> Any | ErrorResponse | HTTPValidationError | MaterializeResponse | None:
  """Materialize Graph from DuckDB

   Rebuild entire graph from DuckDB staging tables (materialized view pattern).

  This endpoint rebuilds the complete graph database from the current state of DuckDB
  staging tables. It automatically discovers all tables, ingests them in the correct
  order (nodes before relationships), and clears the staleness flag.

  **When to Use:**
  - After batch uploads (files uploaded with ingest_to_graph=false)
  - After cascade file deletions (graph marked stale)
  - To ensure graph consistency with DuckDB state
  - Periodic full refresh

  **What Happens:**
  1. Discovers all tables for the graph from PostgreSQL registry
  2. Sorts tables (nodes before relationships)
  3. Ingests all tables from DuckDB to graph in order
  4. Clears staleness flag on success
  5. Returns detailed materialization report

  **Staleness Check:**
  By default, only materializes if graph is stale (after deletions or missed ingestions).
  Use `force=true` to rebuild regardless of staleness.

  **Rebuild Feature:**
  Setting `rebuild=true` regenerates the entire graph database from scratch:
  - Deletes existing graph database
  - Recreates with fresh schema from active GraphSchema
  - Ingests all data files
  - Safe operation - DuckDB is source of truth
  - Useful for schema changes or data corrections
  - Graph marked as 'rebuilding' during process

  **Table Ordering:**
  Node tables (PascalCase) are ingested before relationship tables (UPPERCASE) to
  ensure referential integrity.

  **Error Handling:**
  With `ignore_errors=true` (default), continues materializing even if individual
  rows fail. Failed rows are logged but don't stop the process.

  **Concurrency Control:**
  Only one materialization can run per graph at a time. If another materialization is in progress,
  you'll receive a 409 Conflict error. The distributed lock automatically expires after
  the configured TTL (default: 1 hour) to prevent deadlocks from failed materializations.

  **Performance:**
  Full graph materialization can take minutes for large datasets. Consider running
  during off-peak hours for production systems.

  **Credits:**
  Materialization is included - no credit consumption

  Args:
      graph_id (str):
      body (MaterializeRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | MaterializeResponse
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
  body: MaterializeRequest,
) -> Response[Any | ErrorResponse | HTTPValidationError | MaterializeResponse]:
  """Materialize Graph from DuckDB

   Rebuild entire graph from DuckDB staging tables (materialized view pattern).

  This endpoint rebuilds the complete graph database from the current state of DuckDB
  staging tables. It automatically discovers all tables, ingests them in the correct
  order (nodes before relationships), and clears the staleness flag.

  **When to Use:**
  - After batch uploads (files uploaded with ingest_to_graph=false)
  - After cascade file deletions (graph marked stale)
  - To ensure graph consistency with DuckDB state
  - Periodic full refresh

  **What Happens:**
  1. Discovers all tables for the graph from PostgreSQL registry
  2. Sorts tables (nodes before relationships)
  3. Ingests all tables from DuckDB to graph in order
  4. Clears staleness flag on success
  5. Returns detailed materialization report

  **Staleness Check:**
  By default, only materializes if graph is stale (after deletions or missed ingestions).
  Use `force=true` to rebuild regardless of staleness.

  **Rebuild Feature:**
  Setting `rebuild=true` regenerates the entire graph database from scratch:
  - Deletes existing graph database
  - Recreates with fresh schema from active GraphSchema
  - Ingests all data files
  - Safe operation - DuckDB is source of truth
  - Useful for schema changes or data corrections
  - Graph marked as 'rebuilding' during process

  **Table Ordering:**
  Node tables (PascalCase) are ingested before relationship tables (UPPERCASE) to
  ensure referential integrity.

  **Error Handling:**
  With `ignore_errors=true` (default), continues materializing even if individual
  rows fail. Failed rows are logged but don't stop the process.

  **Concurrency Control:**
  Only one materialization can run per graph at a time. If another materialization is in progress,
  you'll receive a 409 Conflict error. The distributed lock automatically expires after
  the configured TTL (default: 1 hour) to prevent deadlocks from failed materializations.

  **Performance:**
  Full graph materialization can take minutes for large datasets. Consider running
  during off-peak hours for production systems.

  **Credits:**
  Materialization is included - no credit consumption

  Args:
      graph_id (str):
      body (MaterializeRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | MaterializeResponse]
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
  body: MaterializeRequest,
) -> Any | ErrorResponse | HTTPValidationError | MaterializeResponse | None:
  """Materialize Graph from DuckDB

   Rebuild entire graph from DuckDB staging tables (materialized view pattern).

  This endpoint rebuilds the complete graph database from the current state of DuckDB
  staging tables. It automatically discovers all tables, ingests them in the correct
  order (nodes before relationships), and clears the staleness flag.

  **When to Use:**
  - After batch uploads (files uploaded with ingest_to_graph=false)
  - After cascade file deletions (graph marked stale)
  - To ensure graph consistency with DuckDB state
  - Periodic full refresh

  **What Happens:**
  1. Discovers all tables for the graph from PostgreSQL registry
  2. Sorts tables (nodes before relationships)
  3. Ingests all tables from DuckDB to graph in order
  4. Clears staleness flag on success
  5. Returns detailed materialization report

  **Staleness Check:**
  By default, only materializes if graph is stale (after deletions or missed ingestions).
  Use `force=true` to rebuild regardless of staleness.

  **Rebuild Feature:**
  Setting `rebuild=true` regenerates the entire graph database from scratch:
  - Deletes existing graph database
  - Recreates with fresh schema from active GraphSchema
  - Ingests all data files
  - Safe operation - DuckDB is source of truth
  - Useful for schema changes or data corrections
  - Graph marked as 'rebuilding' during process

  **Table Ordering:**
  Node tables (PascalCase) are ingested before relationship tables (UPPERCASE) to
  ensure referential integrity.

  **Error Handling:**
  With `ignore_errors=true` (default), continues materializing even if individual
  rows fail. Failed rows are logged but don't stop the process.

  **Concurrency Control:**
  Only one materialization can run per graph at a time. If another materialization is in progress,
  you'll receive a 409 Conflict error. The distributed lock automatically expires after
  the configured TTL (default: 1 hour) to prevent deadlocks from failed materializations.

  **Performance:**
  Full graph materialization can take minutes for large datasets. Consider running
  during off-peak hours for production systems.

  **Credits:**
  Materialization is included - no credit consumption

  Args:
      graph_id (str):
      body (MaterializeRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | MaterializeResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
