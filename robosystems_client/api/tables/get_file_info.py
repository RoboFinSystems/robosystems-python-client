from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_file_info_response import GetFileInfoResponse
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
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/tables/files/{file_id}",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]]:
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
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]]:
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
) -> Response[Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]]:
  r""" Get File Information

     Get detailed information about a specific file.

    **Purpose:**
    Retrieve comprehensive metadata for a single file, including upload status,
    size, row count, and timestamps. Useful for validating individual files
    before ingestion.

    **Use Cases:**
    - Validate file upload completion
    - Check file metadata before ingestion
    - Debug upload issues
    - Verify file format and size
    - Track file lifecycle

    **Example Response:**
    ```json
    {
      \"file_id\": \"f123\",
      \"graph_id\": \"kg123\",
      \"table_id\": \"t456\",
      \"table_name\": \"Entity\",
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
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/files/f123
    ```

    **Note:**
    File info retrieval is included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        file_id (str): File ID
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]]
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
) -> Optional[Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]]:
  r""" Get File Information

     Get detailed information about a specific file.

    **Purpose:**
    Retrieve comprehensive metadata for a single file, including upload status,
    size, row count, and timestamps. Useful for validating individual files
    before ingestion.

    **Use Cases:**
    - Validate file upload completion
    - Check file metadata before ingestion
    - Debug upload issues
    - Verify file format and size
    - Track file lifecycle

    **Example Response:**
    ```json
    {
      \"file_id\": \"f123\",
      \"graph_id\": \"kg123\",
      \"table_id\": \"t456\",
      \"table_name\": \"Entity\",
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
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/files/f123
    ```

    **Note:**
    File info retrieval is included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        file_id (str): File ID
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]
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
) -> Response[Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]]:
  r""" Get File Information

     Get detailed information about a specific file.

    **Purpose:**
    Retrieve comprehensive metadata for a single file, including upload status,
    size, row count, and timestamps. Useful for validating individual files
    before ingestion.

    **Use Cases:**
    - Validate file upload completion
    - Check file metadata before ingestion
    - Debug upload issues
    - Verify file format and size
    - Track file lifecycle

    **Example Response:**
    ```json
    {
      \"file_id\": \"f123\",
      \"graph_id\": \"kg123\",
      \"table_id\": \"t456\",
      \"table_name\": \"Entity\",
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
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/files/f123
    ```

    **Note:**
    File info retrieval is included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        file_id (str): File ID
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]]
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
) -> Optional[Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]]:
  r""" Get File Information

     Get detailed information about a specific file.

    **Purpose:**
    Retrieve comprehensive metadata for a single file, including upload status,
    size, row count, and timestamps. Useful for validating individual files
    before ingestion.

    **Use Cases:**
    - Validate file upload completion
    - Check file metadata before ingestion
    - Debug upload issues
    - Verify file format and size
    - Track file lifecycle

    **Example Response:**
    ```json
    {
      \"file_id\": \"f123\",
      \"graph_id\": \"kg123\",
      \"table_id\": \"t456\",
      \"table_name\": \"Entity\",
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
    ```

    **Example Usage:**
    ```bash
    curl -H \"Authorization: Bearer YOUR_TOKEN\" \
      https://api.robosystems.ai/v1/graphs/kg123/tables/files/f123
    ```

    **Note:**
    File info retrieval is included - no credit consumption.

    Args:
        graph_id (str): Graph database identifier
        file_id (str): File ID
        token (Union[None, Unset, str]): JWT token for SSE authentication
        authorization (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, GetFileInfoResponse, HTTPValidationError]
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
