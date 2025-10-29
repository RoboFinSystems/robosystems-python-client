from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.file_upload_request import FileUploadRequest
from ...models.file_upload_response import FileUploadResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  table_name: str,
  *,
  body: FileUploadRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/tables/{table_name}/files",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = FileUploadResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]]:
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
  body: FileUploadRequest,
) -> Response[Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]]:
  r""" Get File Upload URL

     Generate a presigned S3 URL for secure file upload.

    **Purpose:**
    Initiate file upload to a staging table by generating a secure, time-limited
    presigned S3 URL. Files are uploaded directly to S3, bypassing the API for
    optimal performance.

    **Upload Workflow:**
    1. Call this endpoint to get presigned URL
    2. PUT file directly to S3 URL (using curl, axios, etc.)
    3. Call PATCH /tables/files/{file_id} with status='uploaded'
    4. Backend validates file and calculates metrics
    5. File ready for ingestion

    **Supported Formats:**
    - Parquet (`application/x-parquet` with `.parquet` extension)
    - CSV (`text/csv` with `.csv` extension)
    - JSON (`application/json` with `.json` extension)

    **Validation:**
    - File extension must match content type
    - File name 1-255 characters
    - No path traversal characters (.. / \)
    - Auto-creates table if it doesn't exist

    **Auto-Table Creation:**
    If the table doesn't exist, it's automatically created with:
    - Type inferred from name (e.g., \"Transaction\" → relationship)
    - Empty schema (populated on ingestion)
    - Ready for file uploads

    **Example Response:**
    ```json
    {
      \"upload_url\": \"https://bucket.s3.amazonaws.com/path?X-Amz-Algorithm=...\",
      \"expires_in\": 3600,
      \"file_id\": \"f123-456-789\",
      \"s3_key\": \"user-staging/user123/kg456/Entity/f123.../data.parquet\"
    }
    ```

    **Example Usage:**
    ```bash
    # Step 1: Get upload URL
    curl -X POST \"https://api.robosystems.ai/v1/graphs/kg123/tables/Entity/files\" \
      -H \"Authorization: Bearer YOUR_TOKEN\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"file_name\": \"entities.parquet\",
        \"content_type\": \"application/x-parquet\"
      }'

    # Step 2: Upload file directly to S3
    curl -X PUT \"$UPLOAD_URL\" \
      -H \"Content-Type: application/x-parquet\" \
      --data-binary \"@entities.parquet\"

    # Step 3: Mark as uploaded
    curl -X PATCH \"https://api.robosystems.ai/v1/graphs/kg123/tables/files/$FILE_ID\" \
      -H \"Authorization: Bearer YOUR_TOKEN\" \
      -H \"Content-Type: application/json\" \
      -d '{\"status\": \"uploaded\"}'
    ```

    **Tips:**
    - Presigned URLs expire (default: 1 hour)
    - Use appropriate Content-Type header when uploading to S3
    - File extension must match content type
    - Large files benefit from direct S3 upload

    **Note:**
    Upload URL generation is included - no credit consumption.

    Args:
        graph_id (str):
        table_name (str): Table name
        body (FileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]]
     """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    table_name=table_name,
    body=body,
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
  body: FileUploadRequest,
) -> Optional[Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]]:
  r""" Get File Upload URL

     Generate a presigned S3 URL for secure file upload.

    **Purpose:**
    Initiate file upload to a staging table by generating a secure, time-limited
    presigned S3 URL. Files are uploaded directly to S3, bypassing the API for
    optimal performance.

    **Upload Workflow:**
    1. Call this endpoint to get presigned URL
    2. PUT file directly to S3 URL (using curl, axios, etc.)
    3. Call PATCH /tables/files/{file_id} with status='uploaded'
    4. Backend validates file and calculates metrics
    5. File ready for ingestion

    **Supported Formats:**
    - Parquet (`application/x-parquet` with `.parquet` extension)
    - CSV (`text/csv` with `.csv` extension)
    - JSON (`application/json` with `.json` extension)

    **Validation:**
    - File extension must match content type
    - File name 1-255 characters
    - No path traversal characters (.. / \)
    - Auto-creates table if it doesn't exist

    **Auto-Table Creation:**
    If the table doesn't exist, it's automatically created with:
    - Type inferred from name (e.g., \"Transaction\" → relationship)
    - Empty schema (populated on ingestion)
    - Ready for file uploads

    **Example Response:**
    ```json
    {
      \"upload_url\": \"https://bucket.s3.amazonaws.com/path?X-Amz-Algorithm=...\",
      \"expires_in\": 3600,
      \"file_id\": \"f123-456-789\",
      \"s3_key\": \"user-staging/user123/kg456/Entity/f123.../data.parquet\"
    }
    ```

    **Example Usage:**
    ```bash
    # Step 1: Get upload URL
    curl -X POST \"https://api.robosystems.ai/v1/graphs/kg123/tables/Entity/files\" \
      -H \"Authorization: Bearer YOUR_TOKEN\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"file_name\": \"entities.parquet\",
        \"content_type\": \"application/x-parquet\"
      }'

    # Step 2: Upload file directly to S3
    curl -X PUT \"$UPLOAD_URL\" \
      -H \"Content-Type: application/x-parquet\" \
      --data-binary \"@entities.parquet\"

    # Step 3: Mark as uploaded
    curl -X PATCH \"https://api.robosystems.ai/v1/graphs/kg123/tables/files/$FILE_ID\" \
      -H \"Authorization: Bearer YOUR_TOKEN\" \
      -H \"Content-Type: application/json\" \
      -d '{\"status\": \"uploaded\"}'
    ```

    **Tips:**
    - Presigned URLs expire (default: 1 hour)
    - Use appropriate Content-Type header when uploading to S3
    - File extension must match content type
    - Large files benefit from direct S3 upload

    **Note:**
    Upload URL generation is included - no credit consumption.

    Args:
        graph_id (str):
        table_name (str): Table name
        body (FileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]
     """

  return sync_detailed(
    graph_id=graph_id,
    table_name=table_name,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  table_name: str,
  *,
  client: AuthenticatedClient,
  body: FileUploadRequest,
) -> Response[Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]]:
  r""" Get File Upload URL

     Generate a presigned S3 URL for secure file upload.

    **Purpose:**
    Initiate file upload to a staging table by generating a secure, time-limited
    presigned S3 URL. Files are uploaded directly to S3, bypassing the API for
    optimal performance.

    **Upload Workflow:**
    1. Call this endpoint to get presigned URL
    2. PUT file directly to S3 URL (using curl, axios, etc.)
    3. Call PATCH /tables/files/{file_id} with status='uploaded'
    4. Backend validates file and calculates metrics
    5. File ready for ingestion

    **Supported Formats:**
    - Parquet (`application/x-parquet` with `.parquet` extension)
    - CSV (`text/csv` with `.csv` extension)
    - JSON (`application/json` with `.json` extension)

    **Validation:**
    - File extension must match content type
    - File name 1-255 characters
    - No path traversal characters (.. / \)
    - Auto-creates table if it doesn't exist

    **Auto-Table Creation:**
    If the table doesn't exist, it's automatically created with:
    - Type inferred from name (e.g., \"Transaction\" → relationship)
    - Empty schema (populated on ingestion)
    - Ready for file uploads

    **Example Response:**
    ```json
    {
      \"upload_url\": \"https://bucket.s3.amazonaws.com/path?X-Amz-Algorithm=...\",
      \"expires_in\": 3600,
      \"file_id\": \"f123-456-789\",
      \"s3_key\": \"user-staging/user123/kg456/Entity/f123.../data.parquet\"
    }
    ```

    **Example Usage:**
    ```bash
    # Step 1: Get upload URL
    curl -X POST \"https://api.robosystems.ai/v1/graphs/kg123/tables/Entity/files\" \
      -H \"Authorization: Bearer YOUR_TOKEN\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"file_name\": \"entities.parquet\",
        \"content_type\": \"application/x-parquet\"
      }'

    # Step 2: Upload file directly to S3
    curl -X PUT \"$UPLOAD_URL\" \
      -H \"Content-Type: application/x-parquet\" \
      --data-binary \"@entities.parquet\"

    # Step 3: Mark as uploaded
    curl -X PATCH \"https://api.robosystems.ai/v1/graphs/kg123/tables/files/$FILE_ID\" \
      -H \"Authorization: Bearer YOUR_TOKEN\" \
      -H \"Content-Type: application/json\" \
      -d '{\"status\": \"uploaded\"}'
    ```

    **Tips:**
    - Presigned URLs expire (default: 1 hour)
    - Use appropriate Content-Type header when uploading to S3
    - File extension must match content type
    - Large files benefit from direct S3 upload

    **Note:**
    Upload URL generation is included - no credit consumption.

    Args:
        graph_id (str):
        table_name (str): Table name
        body (FileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]]
     """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    table_name=table_name,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  table_name: str,
  *,
  client: AuthenticatedClient,
  body: FileUploadRequest,
) -> Optional[Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]]:
  r""" Get File Upload URL

     Generate a presigned S3 URL for secure file upload.

    **Purpose:**
    Initiate file upload to a staging table by generating a secure, time-limited
    presigned S3 URL. Files are uploaded directly to S3, bypassing the API for
    optimal performance.

    **Upload Workflow:**
    1. Call this endpoint to get presigned URL
    2. PUT file directly to S3 URL (using curl, axios, etc.)
    3. Call PATCH /tables/files/{file_id} with status='uploaded'
    4. Backend validates file and calculates metrics
    5. File ready for ingestion

    **Supported Formats:**
    - Parquet (`application/x-parquet` with `.parquet` extension)
    - CSV (`text/csv` with `.csv` extension)
    - JSON (`application/json` with `.json` extension)

    **Validation:**
    - File extension must match content type
    - File name 1-255 characters
    - No path traversal characters (.. / \)
    - Auto-creates table if it doesn't exist

    **Auto-Table Creation:**
    If the table doesn't exist, it's automatically created with:
    - Type inferred from name (e.g., \"Transaction\" → relationship)
    - Empty schema (populated on ingestion)
    - Ready for file uploads

    **Example Response:**
    ```json
    {
      \"upload_url\": \"https://bucket.s3.amazonaws.com/path?X-Amz-Algorithm=...\",
      \"expires_in\": 3600,
      \"file_id\": \"f123-456-789\",
      \"s3_key\": \"user-staging/user123/kg456/Entity/f123.../data.parquet\"
    }
    ```

    **Example Usage:**
    ```bash
    # Step 1: Get upload URL
    curl -X POST \"https://api.robosystems.ai/v1/graphs/kg123/tables/Entity/files\" \
      -H \"Authorization: Bearer YOUR_TOKEN\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"file_name\": \"entities.parquet\",
        \"content_type\": \"application/x-parquet\"
      }'

    # Step 2: Upload file directly to S3
    curl -X PUT \"$UPLOAD_URL\" \
      -H \"Content-Type: application/x-parquet\" \
      --data-binary \"@entities.parquet\"

    # Step 3: Mark as uploaded
    curl -X PATCH \"https://api.robosystems.ai/v1/graphs/kg123/tables/files/$FILE_ID\" \
      -H \"Authorization: Bearer YOUR_TOKEN\" \
      -H \"Content-Type: application/json\" \
      -d '{\"status\": \"uploaded\"}'
    ```

    **Tips:**
    - Presigned URLs expire (default: 1 hour)
    - Use appropriate Content-Type header when uploading to S3
    - File extension must match content type
    - Large files benefit from direct S3 upload

    **Note:**
    Upload URL generation is included - no credit consumption.

    Args:
        graph_id (str):
        table_name (str): Table name
        body (FileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, FileUploadResponse, HTTPValidationError]
     """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      table_name=table_name,
      client=client,
      body=body,
    )
  ).parsed
