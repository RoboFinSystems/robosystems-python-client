from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  operation_id: str,
  *,
  from_sequence: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  params["from_sequence"] = from_sequence

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/operations/{operation_id}/stream",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = response.json()
    return response_200

  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403

  if response.status_code == 404:
    response_404 = cast(Any, None)
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
) -> Response[Union[Any, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  operation_id: str,
  *,
  client: AuthenticatedClient,
  from_sequence: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
  """Stream Operation Events

   Stream real-time events for an operation using Server-Sent Events (SSE).

  This endpoint provides real-time monitoring for all non-immediate operations including:
  - Graph creation and management
  - Agent analysis processing
  - Database backups and restores
  - Data synchronization tasks

  **Event Types:**
  - `operation_started`: Operation began execution
  - `operation_progress`: Progress update with details
  - `operation_completed`: Operation finished successfully
  - `operation_error`: Operation failed with error details
  - `operation_cancelled`: Operation was cancelled

  **Features:**
  - **Event Replay**: Use `from_sequence` parameter to replay missed events
  - **Automatic Reconnection**: Client can reconnect and resume from last seen event
  - **Real-time Updates**: Live progress updates during execution
  - **Timeout Handling**: 30-second keepalive messages prevent connection timeouts
  - **Graceful Degradation**: Automatic fallback if Redis is unavailable

  **Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic cleanup of stale connections
  - Circuit breaker protection for Redis failures

  **Client Usage:**
  ```javascript
  const eventSource = new EventSource('/v1/operations/abc123/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data);
  };
  eventSource.onerror = (error) => {
    // Handle connection errors or rate limits
    console.error('SSE Error:', error);
  };
  ```

  **Error Handling:**
  - `429 Too Many Requests`: Connection limit or rate limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Clients should implement exponential backoff on errors

  **No credits are consumed for SSE connections.**

  Args:
      operation_id (str): Operation identifier from initial submission
      from_sequence (Union[Unset, int]): Start streaming from this sequence number (0 = from
          beginning) Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    operation_id=operation_id,
    from_sequence=from_sequence,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  operation_id: str,
  *,
  client: AuthenticatedClient,
  from_sequence: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
  """Stream Operation Events

   Stream real-time events for an operation using Server-Sent Events (SSE).

  This endpoint provides real-time monitoring for all non-immediate operations including:
  - Graph creation and management
  - Agent analysis processing
  - Database backups and restores
  - Data synchronization tasks

  **Event Types:**
  - `operation_started`: Operation began execution
  - `operation_progress`: Progress update with details
  - `operation_completed`: Operation finished successfully
  - `operation_error`: Operation failed with error details
  - `operation_cancelled`: Operation was cancelled

  **Features:**
  - **Event Replay**: Use `from_sequence` parameter to replay missed events
  - **Automatic Reconnection**: Client can reconnect and resume from last seen event
  - **Real-time Updates**: Live progress updates during execution
  - **Timeout Handling**: 30-second keepalive messages prevent connection timeouts
  - **Graceful Degradation**: Automatic fallback if Redis is unavailable

  **Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic cleanup of stale connections
  - Circuit breaker protection for Redis failures

  **Client Usage:**
  ```javascript
  const eventSource = new EventSource('/v1/operations/abc123/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data);
  };
  eventSource.onerror = (error) => {
    // Handle connection errors or rate limits
    console.error('SSE Error:', error);
  };
  ```

  **Error Handling:**
  - `429 Too Many Requests`: Connection limit or rate limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Clients should implement exponential backoff on errors

  **No credits are consumed for SSE connections.**

  Args:
      operation_id (str): Operation identifier from initial submission
      from_sequence (Union[Unset, int]): Start streaming from this sequence number (0 = from
          beginning) Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError]
  """

  return sync_detailed(
    operation_id=operation_id,
    client=client,
    from_sequence=from_sequence,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  operation_id: str,
  *,
  client: AuthenticatedClient,
  from_sequence: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
  """Stream Operation Events

   Stream real-time events for an operation using Server-Sent Events (SSE).

  This endpoint provides real-time monitoring for all non-immediate operations including:
  - Graph creation and management
  - Agent analysis processing
  - Database backups and restores
  - Data synchronization tasks

  **Event Types:**
  - `operation_started`: Operation began execution
  - `operation_progress`: Progress update with details
  - `operation_completed`: Operation finished successfully
  - `operation_error`: Operation failed with error details
  - `operation_cancelled`: Operation was cancelled

  **Features:**
  - **Event Replay**: Use `from_sequence` parameter to replay missed events
  - **Automatic Reconnection**: Client can reconnect and resume from last seen event
  - **Real-time Updates**: Live progress updates during execution
  - **Timeout Handling**: 30-second keepalive messages prevent connection timeouts
  - **Graceful Degradation**: Automatic fallback if Redis is unavailable

  **Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic cleanup of stale connections
  - Circuit breaker protection for Redis failures

  **Client Usage:**
  ```javascript
  const eventSource = new EventSource('/v1/operations/abc123/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data);
  };
  eventSource.onerror = (error) => {
    // Handle connection errors or rate limits
    console.error('SSE Error:', error);
  };
  ```

  **Error Handling:**
  - `429 Too Many Requests`: Connection limit or rate limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Clients should implement exponential backoff on errors

  **No credits are consumed for SSE connections.**

  Args:
      operation_id (str): Operation identifier from initial submission
      from_sequence (Union[Unset, int]): Start streaming from this sequence number (0 = from
          beginning) Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    operation_id=operation_id,
    from_sequence=from_sequence,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  operation_id: str,
  *,
  client: AuthenticatedClient,
  from_sequence: Union[Unset, int] = 0,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
  """Stream Operation Events

   Stream real-time events for an operation using Server-Sent Events (SSE).

  This endpoint provides real-time monitoring for all non-immediate operations including:
  - Graph creation and management
  - Agent analysis processing
  - Database backups and restores
  - Data synchronization tasks

  **Event Types:**
  - `operation_started`: Operation began execution
  - `operation_progress`: Progress update with details
  - `operation_completed`: Operation finished successfully
  - `operation_error`: Operation failed with error details
  - `operation_cancelled`: Operation was cancelled

  **Features:**
  - **Event Replay**: Use `from_sequence` parameter to replay missed events
  - **Automatic Reconnection**: Client can reconnect and resume from last seen event
  - **Real-time Updates**: Live progress updates during execution
  - **Timeout Handling**: 30-second keepalive messages prevent connection timeouts
  - **Graceful Degradation**: Automatic fallback if Redis is unavailable

  **Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic cleanup of stale connections
  - Circuit breaker protection for Redis failures

  **Client Usage:**
  ```javascript
  const eventSource = new EventSource('/v1/operations/abc123/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data);
  };
  eventSource.onerror = (error) => {
    // Handle connection errors or rate limits
    console.error('SSE Error:', error);
  };
  ```

  **Error Handling:**
  - `429 Too Many Requests`: Connection limit or rate limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Clients should implement exponential backoff on errors

  **No credits are consumed for SSE connections.**

  Args:
      operation_id (str): Operation identifier from initial submission
      from_sequence (Union[Unset, int]): Start streaming from this sequence number (0 = from
          beginning) Default: 0.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      operation_id=operation_id,
      client=client,
      from_sequence=from_sequence,
      token=token,
      authorization=authorization,
    )
  ).parsed
