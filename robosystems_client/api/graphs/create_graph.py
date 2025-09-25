from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_graph_request import CreateGraphRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  *,
  body: CreateGraphRequest,
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
    "url": "/v1/graphs",
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
  if response.status_code == 202:
    response_202 = response.json()
    return response_202
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
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
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
  """Create New Graph Database

   Create a new graph database with specified schema and optionally an initial entity.

  This endpoint starts an asynchronous graph creation operation and returns
  connection details for monitoring progress via Server-Sent Events (SSE).

  **Operation Types:**
  - **Generic Graph**: Creates empty graph with schema extensions
  - **Entity Graph**: Creates graph with initial entity data

  **Monitoring Progress:**
  Use the returned `operation_id` to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data.progress_percent + '%');
  };
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Events Emitted:**
  - `operation_started`: Graph creation begins
  - `operation_progress`: Schema loading, database setup, etc.
  - `operation_completed`: Graph ready with connection details
  - `operation_error`: Creation failed with error details

  **Error Handling:**
  - `429 Too Many Requests`: SSE connection limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Clients should implement exponential backoff on errors

  **Response includes:**
  - `operation_id`: Unique identifier for monitoring
  - `_links.stream`: SSE endpoint for real-time updates
  - `_links.status`: Point-in-time status check endpoint

  Args:
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (CreateGraphRequest): Request model for creating a new graph. Example:
          {'initial_entity': {'cik': '0001234567', 'name': 'Acme Corp', 'uri': 'https://acme.com'},
          'instance_tier': 'standard', 'metadata': {'description': 'Main production graph',
          'graph_name': 'Production System', 'schema_extensions': ['roboledger']}, 'tags':
          ['production', 'finance']}.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    body=body,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
  """Create New Graph Database

   Create a new graph database with specified schema and optionally an initial entity.

  This endpoint starts an asynchronous graph creation operation and returns
  connection details for monitoring progress via Server-Sent Events (SSE).

  **Operation Types:**
  - **Generic Graph**: Creates empty graph with schema extensions
  - **Entity Graph**: Creates graph with initial entity data

  **Monitoring Progress:**
  Use the returned `operation_id` to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data.progress_percent + '%');
  };
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Events Emitted:**
  - `operation_started`: Graph creation begins
  - `operation_progress`: Schema loading, database setup, etc.
  - `operation_completed`: Graph ready with connection details
  - `operation_error`: Creation failed with error details

  **Error Handling:**
  - `429 Too Many Requests`: SSE connection limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Clients should implement exponential backoff on errors

  **Response includes:**
  - `operation_id`: Unique identifier for monitoring
  - `_links.stream`: SSE endpoint for real-time updates
  - `_links.status`: Point-in-time status check endpoint

  Args:
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (CreateGraphRequest): Request model for creating a new graph. Example:
          {'initial_entity': {'cik': '0001234567', 'name': 'Acme Corp', 'uri': 'https://acme.com'},
          'instance_tier': 'standard', 'metadata': {'description': 'Main production graph',
          'graph_name': 'Production System', 'schema_extensions': ['roboledger']}, 'tags':
          ['production', 'finance']}.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError]
  """

  return sync_detailed(
    client=client,
    body=body,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
  """Create New Graph Database

   Create a new graph database with specified schema and optionally an initial entity.

  This endpoint starts an asynchronous graph creation operation and returns
  connection details for monitoring progress via Server-Sent Events (SSE).

  **Operation Types:**
  - **Generic Graph**: Creates empty graph with schema extensions
  - **Entity Graph**: Creates graph with initial entity data

  **Monitoring Progress:**
  Use the returned `operation_id` to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data.progress_percent + '%');
  };
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Events Emitted:**
  - `operation_started`: Graph creation begins
  - `operation_progress`: Schema loading, database setup, etc.
  - `operation_completed`: Graph ready with connection details
  - `operation_error`: Creation failed with error details

  **Error Handling:**
  - `429 Too Many Requests`: SSE connection limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Clients should implement exponential backoff on errors

  **Response includes:**
  - `operation_id`: Unique identifier for monitoring
  - `_links.stream`: SSE endpoint for real-time updates
  - `_links.status`: Point-in-time status check endpoint

  Args:
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (CreateGraphRequest): Request model for creating a new graph. Example:
          {'initial_entity': {'cik': '0001234567', 'name': 'Acme Corp', 'uri': 'https://acme.com'},
          'instance_tier': 'standard', 'metadata': {'description': 'Main production graph',
          'graph_name': 'Production System', 'schema_extensions': ['roboledger']}, 'tags':
          ['production', 'finance']}.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    body=body,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
  """Create New Graph Database

   Create a new graph database with specified schema and optionally an initial entity.

  This endpoint starts an asynchronous graph creation operation and returns
  connection details for monitoring progress via Server-Sent Events (SSE).

  **Operation Types:**
  - **Generic Graph**: Creates empty graph with schema extensions
  - **Entity Graph**: Creates graph with initial entity data

  **Monitoring Progress:**
  Use the returned `operation_id` to connect to the SSE stream:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Progress:', data.progress_percent + '%');
  };
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable

  **Events Emitted:**
  - `operation_started`: Graph creation begins
  - `operation_progress`: Schema loading, database setup, etc.
  - `operation_completed`: Graph ready with connection details
  - `operation_error`: Creation failed with error details

  **Error Handling:**
  - `429 Too Many Requests`: SSE connection limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Clients should implement exponential backoff on errors

  **Response includes:**
  - `operation_id`: Unique identifier for monitoring
  - `_links.stream`: SSE endpoint for real-time updates
  - `_links.status`: Point-in-time status check endpoint

  Args:
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (CreateGraphRequest): Request model for creating a new graph. Example:
          {'initial_entity': {'cik': '0001234567', 'name': 'Acme Corp', 'uri': 'https://acme.com'},
          'instance_tier': 'standard', 'metadata': {'description': 'Main production graph',
          'graph_name': 'Production System', 'schema_extensions': ['roboledger']}, 'tags':
          ['production', 'finance']}.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
      token=token,
      authorization=authorization,
    )
  ).parsed
