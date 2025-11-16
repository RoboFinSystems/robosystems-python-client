from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.table_query_request import TableQueryRequest
from ...models.table_query_response import TableQueryResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: TableQueryRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/tables/query",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]]:
  if response.status_code == 200:
    response_200 = TableQueryResponse.from_dict(response.json())

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

  if response.status_code == 408:
    response_408 = cast(Any, None)
    return response_408

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
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]]:
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
  body: TableQueryRequest,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]]:
  r"""Query Staging Tables with SQL

   Execute SQL queries on DuckDB staging tables for data inspection and validation.

  Query raw staging data directly with SQL before ingestion into the graph database.
  Useful for data quality checks, validation, and exploratory analysis.

  **Security Best Practice - Use Parameterized Queries:**
  ALWAYS use query parameters instead of string concatenation to prevent SQL injection:
  - ✅ SAFE: `SELECT * FROM Entity WHERE type = ? LIMIT ?` with `parameters: [\"Company\", 100]`
  - ❌ UNSAFE: `SELECT * FROM Entity WHERE type = 'Company' LIMIT 100` with user input concatenated
  into SQL string

  Query parameters provide automatic escaping and type safety. Use `?` placeholders with parameters
  array.

  **Use Cases:**
  - Validate data quality before graph ingestion
  - Inspect row-level data for debugging
  - Run analytics on staging tables
  - Check for duplicates, nulls, or data issues
  - Preview data transformations

  **Workflow:**
  1. Upload data files via `POST /tables/{table_name}/files`
  2. Query staging tables to validate: `POST /tables/query`
  3. Fix any data issues by re-uploading
  4. Ingest validated data: `POST /tables/ingest`

  **Supported SQL:**
  - Full DuckDB SQL syntax
  - SELECT, JOIN, WHERE, GROUP BY, ORDER BY
  - Aggregations, window functions, CTEs
  - Multiple table joins across staging area

  **Common Operations:**
  - Count rows: `SELECT COUNT(*) FROM Entity`
  - Filter by type: `SELECT * FROM Entity WHERE entity_type = ? LIMIT ?` with `parameters:
  [\"Company\", 100]`
  - Check for nulls: `SELECT * FROM Entity WHERE name IS NULL LIMIT 10`
  - Find duplicates: `SELECT identifier, COUNT(*) as cnt FROM Entity GROUP BY identifier HAVING
  COUNT(*) > 1`
  - Filter amounts: `SELECT * FROM Transaction WHERE amount > ? AND date >= ?` with `parameters:
  [1000, \"2024-01-01\"]`

  **Limits:**
  - Query timeout: 30 seconds
  - Result limit: 10,000 rows (use LIMIT clause)
  - Read-only: No INSERT, UPDATE, DELETE
  - User's tables only: Cannot query other users' data

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has its own independent staging tables.

  **Shared Repositories:**
  Shared repositories (SEC, etc.) do not allow direct SQL queries.
  Use the graph query endpoint instead: `POST /v1/graphs/{graph_id}/query`

  **Note:**
  Staging table queries are included - no credit consumption

  Args:
      graph_id (str):
      body (TableQueryRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]]
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
  body: TableQueryRequest,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]]:
  r"""Query Staging Tables with SQL

   Execute SQL queries on DuckDB staging tables for data inspection and validation.

  Query raw staging data directly with SQL before ingestion into the graph database.
  Useful for data quality checks, validation, and exploratory analysis.

  **Security Best Practice - Use Parameterized Queries:**
  ALWAYS use query parameters instead of string concatenation to prevent SQL injection:
  - ✅ SAFE: `SELECT * FROM Entity WHERE type = ? LIMIT ?` with `parameters: [\"Company\", 100]`
  - ❌ UNSAFE: `SELECT * FROM Entity WHERE type = 'Company' LIMIT 100` with user input concatenated
  into SQL string

  Query parameters provide automatic escaping and type safety. Use `?` placeholders with parameters
  array.

  **Use Cases:**
  - Validate data quality before graph ingestion
  - Inspect row-level data for debugging
  - Run analytics on staging tables
  - Check for duplicates, nulls, or data issues
  - Preview data transformations

  **Workflow:**
  1. Upload data files via `POST /tables/{table_name}/files`
  2. Query staging tables to validate: `POST /tables/query`
  3. Fix any data issues by re-uploading
  4. Ingest validated data: `POST /tables/ingest`

  **Supported SQL:**
  - Full DuckDB SQL syntax
  - SELECT, JOIN, WHERE, GROUP BY, ORDER BY
  - Aggregations, window functions, CTEs
  - Multiple table joins across staging area

  **Common Operations:**
  - Count rows: `SELECT COUNT(*) FROM Entity`
  - Filter by type: `SELECT * FROM Entity WHERE entity_type = ? LIMIT ?` with `parameters:
  [\"Company\", 100]`
  - Check for nulls: `SELECT * FROM Entity WHERE name IS NULL LIMIT 10`
  - Find duplicates: `SELECT identifier, COUNT(*) as cnt FROM Entity GROUP BY identifier HAVING
  COUNT(*) > 1`
  - Filter amounts: `SELECT * FROM Transaction WHERE amount > ? AND date >= ?` with `parameters:
  [1000, \"2024-01-01\"]`

  **Limits:**
  - Query timeout: 30 seconds
  - Result limit: 10,000 rows (use LIMIT clause)
  - Read-only: No INSERT, UPDATE, DELETE
  - User's tables only: Cannot query other users' data

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has its own independent staging tables.

  **Shared Repositories:**
  Shared repositories (SEC, etc.) do not allow direct SQL queries.
  Use the graph query endpoint instead: `POST /v1/graphs/{graph_id}/query`

  **Note:**
  Staging table queries are included - no credit consumption

  Args:
      graph_id (str):
      body (TableQueryRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]
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
  body: TableQueryRequest,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]]:
  r"""Query Staging Tables with SQL

   Execute SQL queries on DuckDB staging tables for data inspection and validation.

  Query raw staging data directly with SQL before ingestion into the graph database.
  Useful for data quality checks, validation, and exploratory analysis.

  **Security Best Practice - Use Parameterized Queries:**
  ALWAYS use query parameters instead of string concatenation to prevent SQL injection:
  - ✅ SAFE: `SELECT * FROM Entity WHERE type = ? LIMIT ?` with `parameters: [\"Company\", 100]`
  - ❌ UNSAFE: `SELECT * FROM Entity WHERE type = 'Company' LIMIT 100` with user input concatenated
  into SQL string

  Query parameters provide automatic escaping and type safety. Use `?` placeholders with parameters
  array.

  **Use Cases:**
  - Validate data quality before graph ingestion
  - Inspect row-level data for debugging
  - Run analytics on staging tables
  - Check for duplicates, nulls, or data issues
  - Preview data transformations

  **Workflow:**
  1. Upload data files via `POST /tables/{table_name}/files`
  2. Query staging tables to validate: `POST /tables/query`
  3. Fix any data issues by re-uploading
  4. Ingest validated data: `POST /tables/ingest`

  **Supported SQL:**
  - Full DuckDB SQL syntax
  - SELECT, JOIN, WHERE, GROUP BY, ORDER BY
  - Aggregations, window functions, CTEs
  - Multiple table joins across staging area

  **Common Operations:**
  - Count rows: `SELECT COUNT(*) FROM Entity`
  - Filter by type: `SELECT * FROM Entity WHERE entity_type = ? LIMIT ?` with `parameters:
  [\"Company\", 100]`
  - Check for nulls: `SELECT * FROM Entity WHERE name IS NULL LIMIT 10`
  - Find duplicates: `SELECT identifier, COUNT(*) as cnt FROM Entity GROUP BY identifier HAVING
  COUNT(*) > 1`
  - Filter amounts: `SELECT * FROM Transaction WHERE amount > ? AND date >= ?` with `parameters:
  [1000, \"2024-01-01\"]`

  **Limits:**
  - Query timeout: 30 seconds
  - Result limit: 10,000 rows (use LIMIT clause)
  - Read-only: No INSERT, UPDATE, DELETE
  - User's tables only: Cannot query other users' data

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has its own independent staging tables.

  **Shared Repositories:**
  Shared repositories (SEC, etc.) do not allow direct SQL queries.
  Use the graph query endpoint instead: `POST /v1/graphs/{graph_id}/query`

  **Note:**
  Staging table queries are included - no credit consumption

  Args:
      graph_id (str):
      body (TableQueryRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]]
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
  body: TableQueryRequest,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]]:
  r"""Query Staging Tables with SQL

   Execute SQL queries on DuckDB staging tables for data inspection and validation.

  Query raw staging data directly with SQL before ingestion into the graph database.
  Useful for data quality checks, validation, and exploratory analysis.

  **Security Best Practice - Use Parameterized Queries:**
  ALWAYS use query parameters instead of string concatenation to prevent SQL injection:
  - ✅ SAFE: `SELECT * FROM Entity WHERE type = ? LIMIT ?` with `parameters: [\"Company\", 100]`
  - ❌ UNSAFE: `SELECT * FROM Entity WHERE type = 'Company' LIMIT 100` with user input concatenated
  into SQL string

  Query parameters provide automatic escaping and type safety. Use `?` placeholders with parameters
  array.

  **Use Cases:**
  - Validate data quality before graph ingestion
  - Inspect row-level data for debugging
  - Run analytics on staging tables
  - Check for duplicates, nulls, or data issues
  - Preview data transformations

  **Workflow:**
  1. Upload data files via `POST /tables/{table_name}/files`
  2. Query staging tables to validate: `POST /tables/query`
  3. Fix any data issues by re-uploading
  4. Ingest validated data: `POST /tables/ingest`

  **Supported SQL:**
  - Full DuckDB SQL syntax
  - SELECT, JOIN, WHERE, GROUP BY, ORDER BY
  - Aggregations, window functions, CTEs
  - Multiple table joins across staging area

  **Common Operations:**
  - Count rows: `SELECT COUNT(*) FROM Entity`
  - Filter by type: `SELECT * FROM Entity WHERE entity_type = ? LIMIT ?` with `parameters:
  [\"Company\", 100]`
  - Check for nulls: `SELECT * FROM Entity WHERE name IS NULL LIMIT 10`
  - Find duplicates: `SELECT identifier, COUNT(*) as cnt FROM Entity GROUP BY identifier HAVING
  COUNT(*) > 1`
  - Filter amounts: `SELECT * FROM Transaction WHERE amount > ? AND date >= ?` with `parameters:
  [1000, \"2024-01-01\"]`

  **Limits:**
  - Query timeout: 30 seconds
  - Result limit: 10,000 rows (use LIMIT clause)
  - Read-only: No INSERT, UPDATE, DELETE
  - User's tables only: Cannot query other users' data

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has its own independent staging tables.

  **Shared Repositories:**
  Shared repositories (SEC, etc.) do not allow direct SQL queries.
  Use the graph query endpoint instead: `POST /v1/graphs/{graph_id}/query`

  **Note:**
  Staging table queries are included - no credit consumption

  Args:
      graph_id (str):
      body (TableQueryRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError, TableQueryResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
