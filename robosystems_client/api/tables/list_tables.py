from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.table_list_response import TableListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
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
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/tables",
    "params": params,
  }

  _kwargs["headers"] = headers
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
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
  r""" List Staging Tables

     List all DuckDB staging tables with comprehensive metrics and status.

    **Purpose:**
    Get a complete inventory of all staging tables for a graph, including
    file counts, storage sizes, and row estimates. Essential for monitoring
    the data pipeline and determining which tables are ready for ingestion.

    **What You Get:**
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

    **Example Response:**
    ```json
    {
      \"tables\": [
        {
          \"table_name\": \"Entity\",
          \"row_count\": 5000,
          \"file_count\": 3,
          \"total_size_bytes\": 2457600,
          \"s3_location\": \"s3://bucket/user-staging/user123/graph456/Entity/**/*.parquet\"
        },
        {
          \"table_name\": \"Transaction\",
          \"row_count\": 15000,
          \"file_count\": 5,
          \"total_size_bytes\": 8192000,
          \"s3_location\": \"s3://bucket/user-staging/user123/graph456/Transaction/**/*.parquet\"
        }
      ],
      \"total_count\": 2
    }
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables
    ```

    **Tips:**
    - Tables with `file_count > 0` have data ready
    - Check `total_size_bytes` for storage monitoring
    - Use `s3_location` to verify upload paths
    - Empty tables (file_count=0) are skipped during ingestion

    **Note:**
    Table queries are included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]
     """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
  r""" List Staging Tables

     List all DuckDB staging tables with comprehensive metrics and status.

    **Purpose:**
    Get a complete inventory of all staging tables for a graph, including
    file counts, storage sizes, and row estimates. Essential for monitoring
    the data pipeline and determining which tables are ready for ingestion.

    **What You Get:**
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

    **Example Response:**
    ```json
    {
      \"tables\": [
        {
          \"table_name\": \"Entity\",
          \"row_count\": 5000,
          \"file_count\": 3,
          \"total_size_bytes\": 2457600,
          \"s3_location\": \"s3://bucket/user-staging/user123/graph456/Entity/**/*.parquet\"
        },
        {
          \"table_name\": \"Transaction\",
          \"row_count\": 15000,
          \"file_count\": 5,
          \"total_size_bytes\": 8192000,
          \"s3_location\": \"s3://bucket/user-staging/user123/graph456/Transaction/**/*.parquet\"
        }
      ],
      \"total_count\": 2
    }
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables
    ```

    **Tips:**
    - Tables with `file_count > 0` have data ready
    - Check `total_size_bytes` for storage monitoring
    - Use `s3_location` to verify upload paths
    - Empty tables (file_count=0) are skipped during ingestion

    **Note:**
    Table queries are included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]
     """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
  r""" List Staging Tables

     List all DuckDB staging tables with comprehensive metrics and status.

    **Purpose:**
    Get a complete inventory of all staging tables for a graph, including
    file counts, storage sizes, and row estimates. Essential for monitoring
    the data pipeline and determining which tables are ready for ingestion.

    **What You Get:**
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

    **Example Response:**
    ```json
    {
      \"tables\": [
        {
          \"table_name\": \"Entity\",
          \"row_count\": 5000,
          \"file_count\": 3,
          \"total_size_bytes\": 2457600,
          \"s3_location\": \"s3://bucket/user-staging/user123/graph456/Entity/**/*.parquet\"
        },
        {
          \"table_name\": \"Transaction\",
          \"row_count\": 15000,
          \"file_count\": 5,
          \"total_size_bytes\": 8192000,
          \"s3_location\": \"s3://bucket/user-staging/user123/graph456/Transaction/**/*.parquet\"
        }
      ],
      \"total_count\": 2
    }
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables
    ```

    **Tips:**
    - Tables with `file_count > 0` have data ready
    - Check `total_size_bytes` for storage monitoring
    - Use `s3_location` to verify upload paths
    - Empty tables (file_count=0) are skipped during ingestion

    **Note:**
    Table queries are included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]
     """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, TableListResponse]]:
  r""" List Staging Tables

     List all DuckDB staging tables with comprehensive metrics and status.

    **Purpose:**
    Get a complete inventory of all staging tables for a graph, including
    file counts, storage sizes, and row estimates. Essential for monitoring
    the data pipeline and determining which tables are ready for ingestion.

    **What You Get:**
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

    **Example Response:**
    ```json
    {
      \"tables\": [
        {
          \"table_name\": \"Entity\",
          \"row_count\": 5000,
          \"file_count\": 3,
          \"total_size_bytes\": 2457600,
          \"s3_location\": \"s3://bucket/user-staging/user123/graph456/Entity/**/*.parquet\"
        },
        {
          \"table_name\": \"Transaction\",
          \"row_count\": 15000,
          \"file_count\": 5,
          \"total_size_bytes\": 8192000,
          \"s3_location\": \"s3://bucket/user-staging/user123/graph456/Transaction/**/*.parquet\"
        }
      ],
      \"total_count\": 2
    }
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables
    ```

    **Tips:**
    - Tables with `file_count > 0` have data ready
    - Check `total_size_bytes` for storage monitoring
    - Use `s3_location` to verify upload paths
    - Empty tables (file_count=0) are skipped during ingestion

    **Note:**
    Table queries are included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

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
      token=token,
      authorization=authorization,
    )
  ).parsed
