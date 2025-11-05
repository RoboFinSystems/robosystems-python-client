from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_graph_request import CreateGraphRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  *,
  body: CreateGraphRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs",
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
) -> Response[Union[Any, HTTPValidationError]]:
  """Create New Graph Database

   Create a new graph database with specified schema and optionally an initial entity.

  This endpoint starts an asynchronous graph creation operation and returns
  connection details for monitoring progress via Server-Sent Events (SSE).

  **Graph Creation Options:**

  1. **Entity Graph with Initial Entity** (`initial_entity` provided, `create_entity=True`):
     - Creates graph structure with entity schema extensions
     - Populates an initial entity node with provided data
     - Useful when you want a pre-configured entity to start with
     - Example: Creating a company graph with the company already populated

  2. **Entity Graph without Initial Entity** (`initial_entity=None`, `create_entity=False`):
     - Creates graph structure with entity schema extensions
     - Graph starts empty, ready for data import
     - Useful for bulk data imports or custom workflows
     - Example: Creating a graph structure before importing from CSV/API

  3. **Generic Graph** (no `initial_entity` provided):
     - Creates empty graph with custom schema extensions
     - General-purpose knowledge graph
     - Example: Analytics graphs, custom data models

  **Required Fields:**
  - `metadata.graph_name`: Unique name for the graph
  - `instance_tier`: Resource tier (kuzu-standard, kuzu-large, kuzu-xlarge)

  **Optional Fields:**
  - `metadata.description`: Human-readable description of the graph's purpose
  - `metadata.schema_extensions`: List of schema extensions (roboledger, roboinvestor, etc.)
  - `tags`: Organizational tags (max 10)
  - `initial_entity`: Entity data (required for entity graphs with initial data)
  - `create_entity`: Whether to populate initial entity (default: true when initial_entity provided)

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
      body (CreateGraphRequest): Request model for creating a new graph.

          Use this to create either:
          - **Entity graphs**: Standard graphs with entity schema and optional extensions
          - **Custom graphs**: Generic graphs with fully custom schema definitions

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
) -> Optional[Union[Any, HTTPValidationError]]:
  """Create New Graph Database

   Create a new graph database with specified schema and optionally an initial entity.

  This endpoint starts an asynchronous graph creation operation and returns
  connection details for monitoring progress via Server-Sent Events (SSE).

  **Graph Creation Options:**

  1. **Entity Graph with Initial Entity** (`initial_entity` provided, `create_entity=True`):
     - Creates graph structure with entity schema extensions
     - Populates an initial entity node with provided data
     - Useful when you want a pre-configured entity to start with
     - Example: Creating a company graph with the company already populated

  2. **Entity Graph without Initial Entity** (`initial_entity=None`, `create_entity=False`):
     - Creates graph structure with entity schema extensions
     - Graph starts empty, ready for data import
     - Useful for bulk data imports or custom workflows
     - Example: Creating a graph structure before importing from CSV/API

  3. **Generic Graph** (no `initial_entity` provided):
     - Creates empty graph with custom schema extensions
     - General-purpose knowledge graph
     - Example: Analytics graphs, custom data models

  **Required Fields:**
  - `metadata.graph_name`: Unique name for the graph
  - `instance_tier`: Resource tier (kuzu-standard, kuzu-large, kuzu-xlarge)

  **Optional Fields:**
  - `metadata.description`: Human-readable description of the graph's purpose
  - `metadata.schema_extensions`: List of schema extensions (roboledger, roboinvestor, etc.)
  - `tags`: Organizational tags (max 10)
  - `initial_entity`: Entity data (required for entity graphs with initial data)
  - `create_entity`: Whether to populate initial entity (default: true when initial_entity provided)

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
      body (CreateGraphRequest): Request model for creating a new graph.

          Use this to create either:
          - **Entity graphs**: Standard graphs with entity schema and optional extensions
          - **Custom graphs**: Generic graphs with fully custom schema definitions

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError]
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
) -> Response[Union[Any, HTTPValidationError]]:
  """Create New Graph Database

   Create a new graph database with specified schema and optionally an initial entity.

  This endpoint starts an asynchronous graph creation operation and returns
  connection details for monitoring progress via Server-Sent Events (SSE).

  **Graph Creation Options:**

  1. **Entity Graph with Initial Entity** (`initial_entity` provided, `create_entity=True`):
     - Creates graph structure with entity schema extensions
     - Populates an initial entity node with provided data
     - Useful when you want a pre-configured entity to start with
     - Example: Creating a company graph with the company already populated

  2. **Entity Graph without Initial Entity** (`initial_entity=None`, `create_entity=False`):
     - Creates graph structure with entity schema extensions
     - Graph starts empty, ready for data import
     - Useful for bulk data imports or custom workflows
     - Example: Creating a graph structure before importing from CSV/API

  3. **Generic Graph** (no `initial_entity` provided):
     - Creates empty graph with custom schema extensions
     - General-purpose knowledge graph
     - Example: Analytics graphs, custom data models

  **Required Fields:**
  - `metadata.graph_name`: Unique name for the graph
  - `instance_tier`: Resource tier (kuzu-standard, kuzu-large, kuzu-xlarge)

  **Optional Fields:**
  - `metadata.description`: Human-readable description of the graph's purpose
  - `metadata.schema_extensions`: List of schema extensions (roboledger, roboinvestor, etc.)
  - `tags`: Organizational tags (max 10)
  - `initial_entity`: Entity data (required for entity graphs with initial data)
  - `create_entity`: Whether to populate initial entity (default: true when initial_entity provided)

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
      body (CreateGraphRequest): Request model for creating a new graph.

          Use this to create either:
          - **Entity graphs**: Standard graphs with entity schema and optional extensions
          - **Custom graphs**: Generic graphs with fully custom schema definitions

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
) -> Optional[Union[Any, HTTPValidationError]]:
  """Create New Graph Database

   Create a new graph database with specified schema and optionally an initial entity.

  This endpoint starts an asynchronous graph creation operation and returns
  connection details for monitoring progress via Server-Sent Events (SSE).

  **Graph Creation Options:**

  1. **Entity Graph with Initial Entity** (`initial_entity` provided, `create_entity=True`):
     - Creates graph structure with entity schema extensions
     - Populates an initial entity node with provided data
     - Useful when you want a pre-configured entity to start with
     - Example: Creating a company graph with the company already populated

  2. **Entity Graph without Initial Entity** (`initial_entity=None`, `create_entity=False`):
     - Creates graph structure with entity schema extensions
     - Graph starts empty, ready for data import
     - Useful for bulk data imports or custom workflows
     - Example: Creating a graph structure before importing from CSV/API

  3. **Generic Graph** (no `initial_entity` provided):
     - Creates empty graph with custom schema extensions
     - General-purpose knowledge graph
     - Example: Analytics graphs, custom data models

  **Required Fields:**
  - `metadata.graph_name`: Unique name for the graph
  - `instance_tier`: Resource tier (kuzu-standard, kuzu-large, kuzu-xlarge)

  **Optional Fields:**
  - `metadata.description`: Human-readable description of the graph's purpose
  - `metadata.schema_extensions`: List of schema extensions (roboledger, roboinvestor, etc.)
  - `tags`: Organizational tags (max 10)
  - `initial_entity`: Entity data (required for entity graphs with initial data)
  - `create_entity`: Whether to populate initial entity (default: true when initial_entity provided)

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
      body (CreateGraphRequest): Request model for creating a new graph.

          Use this to create either:
          - **Entity graphs**: Standard graphs with entity schema and optional extensions
          - **Custom graphs**: Generic graphs with fully custom schema definitions

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
    )
  ).parsed
