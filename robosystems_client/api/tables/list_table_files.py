from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_table_files_response import ListTableFilesResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  table_name: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/tables/{table_name}/files",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]]:
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

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  table_name: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]]:
  r""" List Files in Staging Table

     List all files uploaded to a staging table with comprehensive metadata.

    **Purpose:**
    Get a complete inventory of all files in a staging table, including upload status,
    file sizes, row counts, and S3 locations. Essential for monitoring upload progress
    and validating data before ingestion.

    **Use Cases:**
    - Monitor file upload progress
    - Verify files are ready for ingestion
    - Check file formats and sizes
    - Track storage usage per table
    - Identify failed or incomplete uploads
    - Pre-ingestion validation

    **What You Get:**
    - File ID and name
    - File format (parquet, csv, etc.)
    - Size in bytes
    - Row count (if available)
    - Upload status and method
    - Creation and upload timestamps
    - S3 key for reference

    **Upload Status Values:**
    - `created`: File record created, not yet uploaded
    - `uploading`: Upload in progress
    - `uploaded`: Successfully uploaded, ready for ingestion
    - `failed`: Upload failed

    **Example Response:**
    ```json
    {
      \"graph_id\": \"kg123\",
      \"table_name\": \"Entity\",
      \"files\": [
        {
          \"file_id\": \"f123\",
          \"file_name\": \"entities_batch1.parquet\",
          \"file_format\": \"parquet\",
          \"size_bytes\": 1048576,
          \"row_count\": 5000,
          \"upload_status\": \"uploaded\",
          \"upload_method\": \"presigned_url\",
          \"created_at\": \"2025-10-28T10:00:00Z\",
          \"uploaded_at\": \"2025-10-28T10:01:30Z\",
          \"s3_key\": \"user-staging/user123/kg123/Entity/entities_batch1.parquet\"
        }
      ],
      \"total_files\": 1,
      \"total_size_bytes\": 1048576
    }
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/Entity/files
    ```

    **Tips:**
    - Only `uploaded` files are ingested
    - Check `row_count` to estimate data volume
    - Use `total_size_bytes` for storage monitoring
    - Files with `failed` status should be deleted and re-uploaded

    **Note:**
    File listing is included - no credit consumption.

    Args:
        graph_id (str):
        table_name (str): Table name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]]
     """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    table_name=table_name,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  table_name: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]]:
  r""" List Files in Staging Table

     List all files uploaded to a staging table with comprehensive metadata.

    **Purpose:**
    Get a complete inventory of all files in a staging table, including upload status,
    file sizes, row counts, and S3 locations. Essential for monitoring upload progress
    and validating data before ingestion.

    **Use Cases:**
    - Monitor file upload progress
    - Verify files are ready for ingestion
    - Check file formats and sizes
    - Track storage usage per table
    - Identify failed or incomplete uploads
    - Pre-ingestion validation

    **What You Get:**
    - File ID and name
    - File format (parquet, csv, etc.)
    - Size in bytes
    - Row count (if available)
    - Upload status and method
    - Creation and upload timestamps
    - S3 key for reference

    **Upload Status Values:**
    - `created`: File record created, not yet uploaded
    - `uploading`: Upload in progress
    - `uploaded`: Successfully uploaded, ready for ingestion
    - `failed`: Upload failed

    **Example Response:**
    ```json
    {
      \"graph_id\": \"kg123\",
      \"table_name\": \"Entity\",
      \"files\": [
        {
          \"file_id\": \"f123\",
          \"file_name\": \"entities_batch1.parquet\",
          \"file_format\": \"parquet\",
          \"size_bytes\": 1048576,
          \"row_count\": 5000,
          \"upload_status\": \"uploaded\",
          \"upload_method\": \"presigned_url\",
          \"created_at\": \"2025-10-28T10:00:00Z\",
          \"uploaded_at\": \"2025-10-28T10:01:30Z\",
          \"s3_key\": \"user-staging/user123/kg123/Entity/entities_batch1.parquet\"
        }
      ],
      \"total_files\": 1,
      \"total_size_bytes\": 1048576
    }
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/Entity/files
    ```

    **Tips:**
    - Only `uploaded` files are ingested
    - Check `row_count` to estimate data volume
    - Use `total_size_bytes` for storage monitoring
    - Files with `failed` status should be deleted and re-uploaded

    **Note:**
    File listing is included - no credit consumption.

    Args:
        graph_id (str):
        table_name (str): Table name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]
     """

  return sync_detailed(
    graph_id=graph_id,
    table_name=table_name,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  table_name: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]]:
  r""" List Files in Staging Table

     List all files uploaded to a staging table with comprehensive metadata.

    **Purpose:**
    Get a complete inventory of all files in a staging table, including upload status,
    file sizes, row counts, and S3 locations. Essential for monitoring upload progress
    and validating data before ingestion.

    **Use Cases:**
    - Monitor file upload progress
    - Verify files are ready for ingestion
    - Check file formats and sizes
    - Track storage usage per table
    - Identify failed or incomplete uploads
    - Pre-ingestion validation

    **What You Get:**
    - File ID and name
    - File format (parquet, csv, etc.)
    - Size in bytes
    - Row count (if available)
    - Upload status and method
    - Creation and upload timestamps
    - S3 key for reference

    **Upload Status Values:**
    - `created`: File record created, not yet uploaded
    - `uploading`: Upload in progress
    - `uploaded`: Successfully uploaded, ready for ingestion
    - `failed`: Upload failed

    **Example Response:**
    ```json
    {
      \"graph_id\": \"kg123\",
      \"table_name\": \"Entity\",
      \"files\": [
        {
          \"file_id\": \"f123\",
          \"file_name\": \"entities_batch1.parquet\",
          \"file_format\": \"parquet\",
          \"size_bytes\": 1048576,
          \"row_count\": 5000,
          \"upload_status\": \"uploaded\",
          \"upload_method\": \"presigned_url\",
          \"created_at\": \"2025-10-28T10:00:00Z\",
          \"uploaded_at\": \"2025-10-28T10:01:30Z\",
          \"s3_key\": \"user-staging/user123/kg123/Entity/entities_batch1.parquet\"
        }
      ],
      \"total_files\": 1,
      \"total_size_bytes\": 1048576
    }
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/Entity/files
    ```

    **Tips:**
    - Only `uploaded` files are ingested
    - Check `row_count` to estimate data volume
    - Use `total_size_bytes` for storage monitoring
    - Files with `failed` status should be deleted and re-uploaded

    **Note:**
    File listing is included - no credit consumption.

    Args:
        graph_id (str):
        table_name (str): Table name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]]
     """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    table_name=table_name,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  table_name: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]]:
  r""" List Files in Staging Table

     List all files uploaded to a staging table with comprehensive metadata.

    **Purpose:**
    Get a complete inventory of all files in a staging table, including upload status,
    file sizes, row counts, and S3 locations. Essential for monitoring upload progress
    and validating data before ingestion.

    **Use Cases:**
    - Monitor file upload progress
    - Verify files are ready for ingestion
    - Check file formats and sizes
    - Track storage usage per table
    - Identify failed or incomplete uploads
    - Pre-ingestion validation

    **What You Get:**
    - File ID and name
    - File format (parquet, csv, etc.)
    - Size in bytes
    - Row count (if available)
    - Upload status and method
    - Creation and upload timestamps
    - S3 key for reference

    **Upload Status Values:**
    - `created`: File record created, not yet uploaded
    - `uploading`: Upload in progress
    - `uploaded`: Successfully uploaded, ready for ingestion
    - `failed`: Upload failed

    **Example Response:**
    ```json
    {
      \"graph_id\": \"kg123\",
      \"table_name\": \"Entity\",
      \"files\": [
        {
          \"file_id\": \"f123\",
          \"file_name\": \"entities_batch1.parquet\",
          \"file_format\": \"parquet\",
          \"size_bytes\": 1048576,
          \"row_count\": 5000,
          \"upload_status\": \"uploaded\",
          \"upload_method\": \"presigned_url\",
          \"created_at\": \"2025-10-28T10:00:00Z\",
          \"uploaded_at\": \"2025-10-28T10:01:30Z\",
          \"s3_key\": \"user-staging/user123/kg123/Entity/entities_batch1.parquet\"
        }
      ],
      \"total_files\": 1,
      \"total_size_bytes\": 1048576
    }
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/Entity/files
    ```

    **Tips:**
    - Only `uploaded` files are ingested
    - Check `row_count` to estimate data volume
    - Use `total_size_bytes` for storage monitoring
    - Files with `failed` status should be deleted and re-uploaded

    **Note:**
    File listing is included - no credit consumption.

    Args:
        graph_id (str):
        table_name (str): Table name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, HTTPValidationError, ListTableFilesResponse]
     """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      table_name=table_name,
      client=client,
    )
  ).parsed
