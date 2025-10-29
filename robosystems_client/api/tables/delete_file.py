from http import HTTPStatus
from typing import Any, Optional, Union, cast

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
    "method": "delete",
    "url": f"/v1/graphs/{graph_id}/tables/files/{file_id}",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]]:
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

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]]:
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
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]]:
  r""" Delete File from Staging

     Delete a file from S3 storage and database tracking.

    **Purpose:**
    Remove unwanted, duplicate, or incorrect files from staging tables before ingestion.
    The file is deleted from both S3 and database tracking, and table statistics
    are automatically recalculated.

    **Use Cases:**
    - Remove duplicate uploads
    - Delete files with incorrect data
    - Clean up failed uploads
    - Fix data quality issues before ingestion
    - Manage storage usage

    **What Happens:**
    1. File deleted from S3 storage
    2. Database tracking record removed
    3. Table statistics recalculated (file count, size, row count)
    4. DuckDB automatically excludes file from future queries

    **Security:**
    - Write access required (verified via auth)
    - Shared repositories block file deletions
    - Full audit trail of deletion operations
    - Cannot delete after ingestion to graph

    **Example Response:**
    ```json
    {
      \"status\": \"deleted\",
      \"file_id\": \"f123\",
      \"file_name\": \"entities_batch1.parquet\",
      \"message\": \"File deleted successfully. DuckDB will automatically exclude it from queries.\"
    }
    ```

    **Example Usage:**
    ```bash
    curl -X DELETE -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/files/f123
    ```

    **Tips:**
    - Delete files before ingestion for best results
    - Table statistics update automatically
    - No need to refresh DuckDB - exclusion is automatic
    - Consider re-uploading corrected version after deletion

    **Note:**
    File deletion is included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        file_id (str): File ID
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]]
     """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    token=token,
    authorization=authorization,
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
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]]:
  r""" Delete File from Staging

     Delete a file from S3 storage and database tracking.

    **Purpose:**
    Remove unwanted, duplicate, or incorrect files from staging tables before ingestion.
    The file is deleted from both S3 and database tracking, and table statistics
    are automatically recalculated.

    **Use Cases:**
    - Remove duplicate uploads
    - Delete files with incorrect data
    - Clean up failed uploads
    - Fix data quality issues before ingestion
    - Manage storage usage

    **What Happens:**
    1. File deleted from S3 storage
    2. Database tracking record removed
    3. Table statistics recalculated (file count, size, row count)
    4. DuckDB automatically excludes file from future queries

    **Security:**
    - Write access required (verified via auth)
    - Shared repositories block file deletions
    - Full audit trail of deletion operations
    - Cannot delete after ingestion to graph

    **Example Response:**
    ```json
    {
      \"status\": \"deleted\",
      \"file_id\": \"f123\",
      \"file_name\": \"entities_batch1.parquet\",
      \"message\": \"File deleted successfully. DuckDB will automatically exclude it from queries.\"
    }
    ```

    **Example Usage:**
    ```bash
    curl -X DELETE -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/files/f123
    ```

    **Tips:**
    - Delete files before ingestion for best results
    - Table statistics update automatically
    - No need to refresh DuckDB - exclusion is automatic
    - Consider re-uploading corrected version after deletion

    **Note:**
    File deletion is included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        file_id (str): File ID
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]
     """

  return sync_detailed(
    graph_id=graph_id,
    file_id=file_id,
    client=client,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]]:
  r""" Delete File from Staging

     Delete a file from S3 storage and database tracking.

    **Purpose:**
    Remove unwanted, duplicate, or incorrect files from staging tables before ingestion.
    The file is deleted from both S3 and database tracking, and table statistics
    are automatically recalculated.

    **Use Cases:**
    - Remove duplicate uploads
    - Delete files with incorrect data
    - Clean up failed uploads
    - Fix data quality issues before ingestion
    - Manage storage usage

    **What Happens:**
    1. File deleted from S3 storage
    2. Database tracking record removed
    3. Table statistics recalculated (file count, size, row count)
    4. DuckDB automatically excludes file from future queries

    **Security:**
    - Write access required (verified via auth)
    - Shared repositories block file deletions
    - Full audit trail of deletion operations
    - Cannot delete after ingestion to graph

    **Example Response:**
    ```json
    {
      \"status\": \"deleted\",
      \"file_id\": \"f123\",
      \"file_name\": \"entities_batch1.parquet\",
      \"message\": \"File deleted successfully. DuckDB will automatically exclude it from queries.\"
    }
    ```

    **Example Usage:**
    ```bash
    curl -X DELETE -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/files/f123
    ```

    **Tips:**
    - Delete files before ingestion for best results
    - Table statistics update automatically
    - No need to refresh DuckDB - exclusion is automatic
    - Consider re-uploading corrected version after deletion

    **Note:**
    File deletion is included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        file_id (str): File ID
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]]
     """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]]:
  r""" Delete File from Staging

     Delete a file from S3 storage and database tracking.

    **Purpose:**
    Remove unwanted, duplicate, or incorrect files from staging tables before ingestion.
    The file is deleted from both S3 and database tracking, and table statistics
    are automatically recalculated.

    **Use Cases:**
    - Remove duplicate uploads
    - Delete files with incorrect data
    - Clean up failed uploads
    - Fix data quality issues before ingestion
    - Manage storage usage

    **What Happens:**
    1. File deleted from S3 storage
    2. Database tracking record removed
    3. Table statistics recalculated (file count, size, row count)
    4. DuckDB automatically excludes file from future queries

    **Security:**
    - Write access required (verified via auth)
    - Shared repositories block file deletions
    - Full audit trail of deletion operations
    - Cannot delete after ingestion to graph

    **Example Response:**
    ```json
    {
      \"status\": \"deleted\",
      \"file_id\": \"f123\",
      \"file_name\": \"entities_batch1.parquet\",
      \"message\": \"File deleted successfully. DuckDB will automatically exclude it from queries.\"
    }
    ```

    **Example Usage:**
    ```bash
    curl -X DELETE -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/files/f123
    ```

    **Tips:**
    - Delete files before ingestion for best results
    - Table statistics update automatically
    - No need to refresh DuckDB - exclusion is automatic
    - Consider re-uploading corrected version after deletion

    **Note:**
    File deletion is included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        file_id (str): File ID
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteFileResponse, ErrorResponse, HTTPValidationError]
     """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      file_id=file_id,
      client=client,
      token=token,
      authorization=authorization,
    )
  ).parsed
