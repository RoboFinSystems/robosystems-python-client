from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.copy_response import CopyResponse
from ...models.data_frame_copy_request import DataFrameCopyRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.s3_copy_request import S3CopyRequest
from ...models.url_copy_request import URLCopyRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: Union["DataFrameCopyRequest", "S3CopyRequest", "URLCopyRequest"],
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
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/copy",
    "params": params,
  }

  _kwargs["json"]: dict[str, Any]
  if isinstance(body, S3CopyRequest):
    _kwargs["json"] = body.to_dict()
  elif isinstance(body, URLCopyRequest):
    _kwargs["json"] = body.to_dict()
  else:
    _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CopyResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = CopyResponse.from_dict(response.json())

    return response_200
  if response.status_code == 202:
    response_202 = cast(Any, None)
    return response_202
  if response.status_code == 400:
    response_400 = cast(Any, None)
    return response_400
  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403
  if response.status_code == 408:
    response_408 = cast(Any, None)
    return response_408
  if response.status_code == 429:
    response_429 = cast(Any, None)
    return response_429
  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500
  if response.status_code == 503:
    response_503 = cast(Any, None)
    return response_503
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CopyResponse, HTTPValidationError]]:
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
  body: Union["DataFrameCopyRequest", "S3CopyRequest", "URLCopyRequest"],
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, CopyResponse, HTTPValidationError]]:
  """Copy Data to Graph

   Copy data from external sources into the graph database.

  This endpoint supports multiple data sources through a unified interface:
  - **S3**: Copy from S3 buckets with user-provided credentials
  - **URL** (future): Copy from HTTP(S) URLs
  - **DataFrame** (future): Copy from uploaded DataFrames

  **Security:**
  - Requires write permissions to the target graph
  - **Not allowed on shared repositories** (sec, industry, economic) - these are read-only
  - User must provide their own AWS credentials for S3 access
  - All operations are logged for audit purposes

  **Tier Limits:**
  - Standard: 10GB max file size, 15 min timeout
  - Enterprise: 50GB max file size, 30 min timeout
  - Premium: 100GB max file size, 60 min timeout

  **Copy Options:**
  - `ignore_errors`: Skip duplicate/invalid rows (enables upsert-like behavior). Note: When enabled,
  row counts may not be accurately reported
  - `extended_timeout`: Use extended timeout for large datasets
  - `validate_schema`: Validate source schema against target table

  **Asynchronous Execution with SSE:**
  For large data imports, this endpoint returns immediately with an operation ID
  and SSE monitoring endpoint. Connect to the returned stream URL for real-time updates:

  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data.message);
  };
  ```

  **SSE Events Emitted:**
  - `operation_started`: Copy operation begins
  - `operation_progress`: Progress updates during data transfer
  - `operation_completed`: Copy successful with statistics
  - `operation_error`: Copy failed with error details

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Error Handling:**
  - `403 Forbidden`: Attempted copy to shared repository
  - `408 Request Timeout`: Operation exceeded timeout limit
  - `429 Too Many Requests`: Rate limit exceeded
  - `503 Service Unavailable`: Circuit breaker open or service unavailable
  - Clients should implement exponential backoff on errors

  **Note:**
  Copy operations are FREE - no credit consumption required.
  All copy operations are performed asynchronously with progress monitoring.

  Args:
      graph_id (str): Target graph identifier (user graphs only - shared repositories not
          allowed)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (Union['DataFrameCopyRequest', 'S3CopyRequest', 'URLCopyRequest']):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, CopyResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
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
  body: Union["DataFrameCopyRequest", "S3CopyRequest", "URLCopyRequest"],
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, CopyResponse, HTTPValidationError]]:
  """Copy Data to Graph

   Copy data from external sources into the graph database.

  This endpoint supports multiple data sources through a unified interface:
  - **S3**: Copy from S3 buckets with user-provided credentials
  - **URL** (future): Copy from HTTP(S) URLs
  - **DataFrame** (future): Copy from uploaded DataFrames

  **Security:**
  - Requires write permissions to the target graph
  - **Not allowed on shared repositories** (sec, industry, economic) - these are read-only
  - User must provide their own AWS credentials for S3 access
  - All operations are logged for audit purposes

  **Tier Limits:**
  - Standard: 10GB max file size, 15 min timeout
  - Enterprise: 50GB max file size, 30 min timeout
  - Premium: 100GB max file size, 60 min timeout

  **Copy Options:**
  - `ignore_errors`: Skip duplicate/invalid rows (enables upsert-like behavior). Note: When enabled,
  row counts may not be accurately reported
  - `extended_timeout`: Use extended timeout for large datasets
  - `validate_schema`: Validate source schema against target table

  **Asynchronous Execution with SSE:**
  For large data imports, this endpoint returns immediately with an operation ID
  and SSE monitoring endpoint. Connect to the returned stream URL for real-time updates:

  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data.message);
  };
  ```

  **SSE Events Emitted:**
  - `operation_started`: Copy operation begins
  - `operation_progress`: Progress updates during data transfer
  - `operation_completed`: Copy successful with statistics
  - `operation_error`: Copy failed with error details

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Error Handling:**
  - `403 Forbidden`: Attempted copy to shared repository
  - `408 Request Timeout`: Operation exceeded timeout limit
  - `429 Too Many Requests`: Rate limit exceeded
  - `503 Service Unavailable`: Circuit breaker open or service unavailable
  - Clients should implement exponential backoff on errors

  **Note:**
  Copy operations are FREE - no credit consumption required.
  All copy operations are performed asynchronously with progress monitoring.

  Args:
      graph_id (str): Target graph identifier (user graphs only - shared repositories not
          allowed)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (Union['DataFrameCopyRequest', 'S3CopyRequest', 'URLCopyRequest']):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, CopyResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: Union["DataFrameCopyRequest", "S3CopyRequest", "URLCopyRequest"],
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, CopyResponse, HTTPValidationError]]:
  """Copy Data to Graph

   Copy data from external sources into the graph database.

  This endpoint supports multiple data sources through a unified interface:
  - **S3**: Copy from S3 buckets with user-provided credentials
  - **URL** (future): Copy from HTTP(S) URLs
  - **DataFrame** (future): Copy from uploaded DataFrames

  **Security:**
  - Requires write permissions to the target graph
  - **Not allowed on shared repositories** (sec, industry, economic) - these are read-only
  - User must provide their own AWS credentials for S3 access
  - All operations are logged for audit purposes

  **Tier Limits:**
  - Standard: 10GB max file size, 15 min timeout
  - Enterprise: 50GB max file size, 30 min timeout
  - Premium: 100GB max file size, 60 min timeout

  **Copy Options:**
  - `ignore_errors`: Skip duplicate/invalid rows (enables upsert-like behavior). Note: When enabled,
  row counts may not be accurately reported
  - `extended_timeout`: Use extended timeout for large datasets
  - `validate_schema`: Validate source schema against target table

  **Asynchronous Execution with SSE:**
  For large data imports, this endpoint returns immediately with an operation ID
  and SSE monitoring endpoint. Connect to the returned stream URL for real-time updates:

  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data.message);
  };
  ```

  **SSE Events Emitted:**
  - `operation_started`: Copy operation begins
  - `operation_progress`: Progress updates during data transfer
  - `operation_completed`: Copy successful with statistics
  - `operation_error`: Copy failed with error details

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Error Handling:**
  - `403 Forbidden`: Attempted copy to shared repository
  - `408 Request Timeout`: Operation exceeded timeout limit
  - `429 Too Many Requests`: Rate limit exceeded
  - `503 Service Unavailable`: Circuit breaker open or service unavailable
  - Clients should implement exponential backoff on errors

  **Note:**
  Copy operations are FREE - no credit consumption required.
  All copy operations are performed asynchronously with progress monitoring.

  Args:
      graph_id (str): Target graph identifier (user graphs only - shared repositories not
          allowed)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (Union['DataFrameCopyRequest', 'S3CopyRequest', 'URLCopyRequest']):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, CopyResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: Union["DataFrameCopyRequest", "S3CopyRequest", "URLCopyRequest"],
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, CopyResponse, HTTPValidationError]]:
  """Copy Data to Graph

   Copy data from external sources into the graph database.

  This endpoint supports multiple data sources through a unified interface:
  - **S3**: Copy from S3 buckets with user-provided credentials
  - **URL** (future): Copy from HTTP(S) URLs
  - **DataFrame** (future): Copy from uploaded DataFrames

  **Security:**
  - Requires write permissions to the target graph
  - **Not allowed on shared repositories** (sec, industry, economic) - these are read-only
  - User must provide their own AWS credentials for S3 access
  - All operations are logged for audit purposes

  **Tier Limits:**
  - Standard: 10GB max file size, 15 min timeout
  - Enterprise: 50GB max file size, 30 min timeout
  - Premium: 100GB max file size, 60 min timeout

  **Copy Options:**
  - `ignore_errors`: Skip duplicate/invalid rows (enables upsert-like behavior). Note: When enabled,
  row counts may not be accurately reported
  - `extended_timeout`: Use extended timeout for large datasets
  - `validate_schema`: Validate source schema against target table

  **Asynchronous Execution with SSE:**
  For large data imports, this endpoint returns immediately with an operation ID
  and SSE monitoring endpoint. Connect to the returned stream URL for real-time updates:

  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data.message);
  };
  ```

  **SSE Events Emitted:**
  - `operation_started`: Copy operation begins
  - `operation_progress`: Progress updates during data transfer
  - `operation_completed`: Copy successful with statistics
  - `operation_error`: Copy failed with error details

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Error Handling:**
  - `403 Forbidden`: Attempted copy to shared repository
  - `408 Request Timeout`: Operation exceeded timeout limit
  - `429 Too Many Requests`: Rate limit exceeded
  - `503 Service Unavailable`: Circuit breaker open or service unavailable
  - Clients should implement exponential backoff on errors

  **Note:**
  Copy operations are FREE - no credit consumption required.
  All copy operations are performed asynchronously with progress monitoring.

  Args:
      graph_id (str): Target graph identifier (user graphs only - shared repositories not
          allowed)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (Union['DataFrameCopyRequest', 'S3CopyRequest', 'URLCopyRequest']):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, CopyResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      token=token,
      authorization=authorization,
    )
  ).parsed
