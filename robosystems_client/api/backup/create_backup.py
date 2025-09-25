from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup_create_request import BackupCreateRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: BackupCreateRequest,
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
    "url": f"/v1/graphs/{graph_id}/backups",
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 202:
    response_202 = response.json()
    return response_202
  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400
  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403
  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404
  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
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
  body: BackupCreateRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Create Backup

   Create a backup of the graph database.

  Creates a complete backup of the Kuzu database (.kuzu file) with:
  - **Format**: Full database backup only (complete .kuzu file)
  - **Compression**: Always enabled for optimal storage
  - **Encryption**: Optional AES-256 encryption for security
  - **Retention**: Configurable retention period (1-2555 days)

  **Backup Features:**
  - **Complete Backup**: Full database file backup
  - **Consistency**: Point-in-time consistent snapshot
  - **Download Support**: Unencrypted backups can be downloaded
  - **Restore Support**: Future support for encrypted backup restoration

  **Progress Monitoring:**
  Use the returned operation_id to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.addEventListener('operation_progress', (event) => {
    const data = JSON.parse(event.data);
    console.log('Backup progress:', data.progress_percent + '%');
  });
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Important Notes:**
  - Only full_dump format is supported (no CSV/JSON exports)
  - Compression is always enabled
  - Encrypted backups cannot be downloaded (security measure)
  - All backups are stored securely in cloud storage

  **Credit Consumption:**
  - Base cost: 25.0 credits
  - Large databases (>10GB): 50.0 credits
  - Multiplied by graph tier

  Returns operation details for SSE monitoring.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (BackupCreateRequest): Request model for creating a backup.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError]]
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
  body: BackupCreateRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Create Backup

   Create a backup of the graph database.

  Creates a complete backup of the Kuzu database (.kuzu file) with:
  - **Format**: Full database backup only (complete .kuzu file)
  - **Compression**: Always enabled for optimal storage
  - **Encryption**: Optional AES-256 encryption for security
  - **Retention**: Configurable retention period (1-2555 days)

  **Backup Features:**
  - **Complete Backup**: Full database file backup
  - **Consistency**: Point-in-time consistent snapshot
  - **Download Support**: Unencrypted backups can be downloaded
  - **Restore Support**: Future support for encrypted backup restoration

  **Progress Monitoring:**
  Use the returned operation_id to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.addEventListener('operation_progress', (event) => {
    const data = JSON.parse(event.data);
    console.log('Backup progress:', data.progress_percent + '%');
  });
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Important Notes:**
  - Only full_dump format is supported (no CSV/JSON exports)
  - Compression is always enabled
  - Encrypted backups cannot be downloaded (security measure)
  - All backups are stored securely in cloud storage

  **Credit Consumption:**
  - Base cost: 25.0 credits
  - Large databases (>10GB): 50.0 credits
  - Multiplied by graph tier

  Returns operation details for SSE monitoring.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (BackupCreateRequest): Request model for creating a backup.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError]
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
  body: BackupCreateRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Create Backup

   Create a backup of the graph database.

  Creates a complete backup of the Kuzu database (.kuzu file) with:
  - **Format**: Full database backup only (complete .kuzu file)
  - **Compression**: Always enabled for optimal storage
  - **Encryption**: Optional AES-256 encryption for security
  - **Retention**: Configurable retention period (1-2555 days)

  **Backup Features:**
  - **Complete Backup**: Full database file backup
  - **Consistency**: Point-in-time consistent snapshot
  - **Download Support**: Unencrypted backups can be downloaded
  - **Restore Support**: Future support for encrypted backup restoration

  **Progress Monitoring:**
  Use the returned operation_id to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.addEventListener('operation_progress', (event) => {
    const data = JSON.parse(event.data);
    console.log('Backup progress:', data.progress_percent + '%');
  });
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Important Notes:**
  - Only full_dump format is supported (no CSV/JSON exports)
  - Compression is always enabled
  - Encrypted backups cannot be downloaded (security measure)
  - All backups are stored securely in cloud storage

  **Credit Consumption:**
  - Base cost: 25.0 credits
  - Large databases (>10GB): 50.0 credits
  - Multiplied by graph tier

  Returns operation details for SSE monitoring.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (BackupCreateRequest): Request model for creating a backup.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError]]
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
  body: BackupCreateRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Create Backup

   Create a backup of the graph database.

  Creates a complete backup of the Kuzu database (.kuzu file) with:
  - **Format**: Full database backup only (complete .kuzu file)
  - **Compression**: Always enabled for optimal storage
  - **Encryption**: Optional AES-256 encryption for security
  - **Retention**: Configurable retention period (1-2555 days)

  **Backup Features:**
  - **Complete Backup**: Full database file backup
  - **Consistency**: Point-in-time consistent snapshot
  - **Download Support**: Unencrypted backups can be downloaded
  - **Restore Support**: Future support for encrypted backup restoration

  **Progress Monitoring:**
  Use the returned operation_id to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.addEventListener('operation_progress', (event) => {
    const data = JSON.parse(event.data);
    console.log('Backup progress:', data.progress_percent + '%');
  });
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Important Notes:**
  - Only full_dump format is supported (no CSV/JSON exports)
  - Compression is always enabled
  - Encrypted backups cannot be downloaded (security measure)
  - All backups are stored securely in cloud storage

  **Credit Consumption:**
  - Base cost: 25.0 credits
  - Large databases (>10GB): 50.0 credits
  - Multiplied by graph tier

  Returns operation details for SSE monitoring.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (BackupCreateRequest): Request model for creating a backup.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError]
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
