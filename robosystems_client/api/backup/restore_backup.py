from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup_restore_request import BackupRestoreRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  backup_id: str,
  *,
  body: BackupRestoreRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/backups/{backup_id}/restore",
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
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  body: BackupRestoreRequest,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Restore Encrypted Backup

   Restore a graph database from an encrypted backup.

  Restores a complete graph database from an encrypted backup:
  - **Format**: Only full_dump backups can be restored
  - **Encryption**: Only encrypted backups can be restored (security requirement)
  - **System Backup**: Creates automatic backup of existing database before restore
  - **Verification**: Optionally verifies database integrity after restore

  **Restore Features:**
  - **Atomic Operation**: Complete replacement of database
  - **Rollback Protection**: System backup created before restore
  - **Data Integrity**: Verification ensures successful restore
  - **Security**: Only encrypted backups to prevent data tampering

  **Operation State Machine:**
  ```
  pending → backing_up_current → downloading → restoring → verifying → completed
                                                                     ↘ failed
  ```
  - **pending**: Restore queued, waiting to start
  - **backing_up_current**: Creating safety backup of existing database
  - **downloading**: Downloading backup from storage
  - **restoring**: Replacing database with backup contents
  - **verifying**: Verifying database integrity (if enabled)
  - **completed**: Restore successful, database operational
  - **failed**: Restore failed (rollback may be available)

  **Expected Durations:**
  Operation times vary by database size (includes backup + restore):
  - **Small** (<1GB): 1-3 minutes
  - **Medium** (1-10GB): 5-15 minutes
  - **Large** (10-100GB): 20-45 minutes
  - **Very Large** (>100GB): 45+ minutes

  Note: Restore operations take longer than backups due to safety backup step.

  **Progress Monitoring:**
  Use the returned operation_id to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.addEventListener('operation_progress', (event) => {
    const data = JSON.parse(event.data);
    console.log('Restore progress:', data.message);
    console.log('Status:', data.status); // Shows current state
  });
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Important Notes:**
  - Only encrypted backups can be restored (security measure)
  - Existing database is backed up to S3 before restore
  - Restore is a destructive operation - existing data is replaced
  - System backups are stored separately for recovery

  **Credit Consumption:**
  - Base cost: 100.0 credits
  - Large databases (>10GB): 200.0 credits
  - Multiplied by graph tier

  Returns operation details for SSE monitoring.

  Args:
      graph_id (str):
      backup_id (str): Backup identifier
      body (BackupRestoreRequest): Request model for restoring from a backup.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    backup_id=backup_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  body: BackupRestoreRequest,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Restore Encrypted Backup

   Restore a graph database from an encrypted backup.

  Restores a complete graph database from an encrypted backup:
  - **Format**: Only full_dump backups can be restored
  - **Encryption**: Only encrypted backups can be restored (security requirement)
  - **System Backup**: Creates automatic backup of existing database before restore
  - **Verification**: Optionally verifies database integrity after restore

  **Restore Features:**
  - **Atomic Operation**: Complete replacement of database
  - **Rollback Protection**: System backup created before restore
  - **Data Integrity**: Verification ensures successful restore
  - **Security**: Only encrypted backups to prevent data tampering

  **Operation State Machine:**
  ```
  pending → backing_up_current → downloading → restoring → verifying → completed
                                                                     ↘ failed
  ```
  - **pending**: Restore queued, waiting to start
  - **backing_up_current**: Creating safety backup of existing database
  - **downloading**: Downloading backup from storage
  - **restoring**: Replacing database with backup contents
  - **verifying**: Verifying database integrity (if enabled)
  - **completed**: Restore successful, database operational
  - **failed**: Restore failed (rollback may be available)

  **Expected Durations:**
  Operation times vary by database size (includes backup + restore):
  - **Small** (<1GB): 1-3 minutes
  - **Medium** (1-10GB): 5-15 minutes
  - **Large** (10-100GB): 20-45 minutes
  - **Very Large** (>100GB): 45+ minutes

  Note: Restore operations take longer than backups due to safety backup step.

  **Progress Monitoring:**
  Use the returned operation_id to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.addEventListener('operation_progress', (event) => {
    const data = JSON.parse(event.data);
    console.log('Restore progress:', data.message);
    console.log('Status:', data.status); // Shows current state
  });
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Important Notes:**
  - Only encrypted backups can be restored (security measure)
  - Existing database is backed up to S3 before restore
  - Restore is a destructive operation - existing data is replaced
  - System backups are stored separately for recovery

  **Credit Consumption:**
  - Base cost: 100.0 credits
  - Large databases (>10GB): 200.0 credits
  - Multiplied by graph tier

  Returns operation details for SSE monitoring.

  Args:
      graph_id (str):
      backup_id (str): Backup identifier
      body (BackupRestoreRequest): Request model for restoring from a backup.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    backup_id=backup_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  body: BackupRestoreRequest,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Restore Encrypted Backup

   Restore a graph database from an encrypted backup.

  Restores a complete graph database from an encrypted backup:
  - **Format**: Only full_dump backups can be restored
  - **Encryption**: Only encrypted backups can be restored (security requirement)
  - **System Backup**: Creates automatic backup of existing database before restore
  - **Verification**: Optionally verifies database integrity after restore

  **Restore Features:**
  - **Atomic Operation**: Complete replacement of database
  - **Rollback Protection**: System backup created before restore
  - **Data Integrity**: Verification ensures successful restore
  - **Security**: Only encrypted backups to prevent data tampering

  **Operation State Machine:**
  ```
  pending → backing_up_current → downloading → restoring → verifying → completed
                                                                     ↘ failed
  ```
  - **pending**: Restore queued, waiting to start
  - **backing_up_current**: Creating safety backup of existing database
  - **downloading**: Downloading backup from storage
  - **restoring**: Replacing database with backup contents
  - **verifying**: Verifying database integrity (if enabled)
  - **completed**: Restore successful, database operational
  - **failed**: Restore failed (rollback may be available)

  **Expected Durations:**
  Operation times vary by database size (includes backup + restore):
  - **Small** (<1GB): 1-3 minutes
  - **Medium** (1-10GB): 5-15 minutes
  - **Large** (10-100GB): 20-45 minutes
  - **Very Large** (>100GB): 45+ minutes

  Note: Restore operations take longer than backups due to safety backup step.

  **Progress Monitoring:**
  Use the returned operation_id to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.addEventListener('operation_progress', (event) => {
    const data = JSON.parse(event.data);
    console.log('Restore progress:', data.message);
    console.log('Status:', data.status); // Shows current state
  });
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Important Notes:**
  - Only encrypted backups can be restored (security measure)
  - Existing database is backed up to S3 before restore
  - Restore is a destructive operation - existing data is replaced
  - System backups are stored separately for recovery

  **Credit Consumption:**
  - Base cost: 100.0 credits
  - Large databases (>10GB): 200.0 credits
  - Multiplied by graph tier

  Returns operation details for SSE monitoring.

  Args:
      graph_id (str):
      backup_id (str): Backup identifier
      body (BackupRestoreRequest): Request model for restoring from a backup.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    backup_id=backup_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  backup_id: str,
  *,
  client: AuthenticatedClient,
  body: BackupRestoreRequest,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Restore Encrypted Backup

   Restore a graph database from an encrypted backup.

  Restores a complete graph database from an encrypted backup:
  - **Format**: Only full_dump backups can be restored
  - **Encryption**: Only encrypted backups can be restored (security requirement)
  - **System Backup**: Creates automatic backup of existing database before restore
  - **Verification**: Optionally verifies database integrity after restore

  **Restore Features:**
  - **Atomic Operation**: Complete replacement of database
  - **Rollback Protection**: System backup created before restore
  - **Data Integrity**: Verification ensures successful restore
  - **Security**: Only encrypted backups to prevent data tampering

  **Operation State Machine:**
  ```
  pending → backing_up_current → downloading → restoring → verifying → completed
                                                                     ↘ failed
  ```
  - **pending**: Restore queued, waiting to start
  - **backing_up_current**: Creating safety backup of existing database
  - **downloading**: Downloading backup from storage
  - **restoring**: Replacing database with backup contents
  - **verifying**: Verifying database integrity (if enabled)
  - **completed**: Restore successful, database operational
  - **failed**: Restore failed (rollback may be available)

  **Expected Durations:**
  Operation times vary by database size (includes backup + restore):
  - **Small** (<1GB): 1-3 minutes
  - **Medium** (1-10GB): 5-15 minutes
  - **Large** (10-100GB): 20-45 minutes
  - **Very Large** (>100GB): 45+ minutes

  Note: Restore operations take longer than backups due to safety backup step.

  **Progress Monitoring:**
  Use the returned operation_id to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.addEventListener('operation_progress', (event) => {
    const data = JSON.parse(event.data);
    console.log('Restore progress:', data.message);
    console.log('Status:', data.status); // Shows current state
  });
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Important Notes:**
  - Only encrypted backups can be restored (security measure)
  - Existing database is backed up to S3 before restore
  - Restore is a destructive operation - existing data is replaced
  - System backups are stored separately for recovery

  **Credit Consumption:**
  - Base cost: 100.0 credits
  - Large databases (>10GB): 200.0 credits
  - Multiplied by graph tier

  Returns operation details for SSE monitoring.

  Args:
      graph_id (str):
      backup_id (str): Backup identifier
      body (BackupRestoreRequest): Request model for restoring from a backup.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      backup_id=backup_id,
      client=client,
      body=body,
    )
  ).parsed
