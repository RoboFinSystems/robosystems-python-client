from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cypher_query_request import CypherQueryRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_mode import ResponseMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: CypherQueryRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
  chunk_size: Union[Unset, int] = 1000,
  test_mode: Union[Unset, bool] = False,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_mode: Union[None, Unset, str]
  if isinstance(mode, Unset):
    json_mode = UNSET
  elif isinstance(mode, ResponseMode):
    json_mode = mode.value
  else:
    json_mode = mode
  params["mode"] = json_mode

  params["chunk_size"] = chunk_size

  params["test_mode"] = test_mode

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/query",
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
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
  body: CypherQueryRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
  chunk_size: Union[Unset, int] = 1000,
  test_mode: Union[Unset, bool] = False,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
  """Execute Cypher Query

   Execute a Cypher query with intelligent response optimization.

  This endpoint automatically selects the best execution strategy based on:
  - Query characteristics (size, complexity)
  - Client capabilities (SSE, NDJSON, JSON)
  - System load (queue status, concurrent queries)
  - User preferences (mode parameter, headers)

  **Response Modes:**
  - `auto` (default): Intelligent automatic selection
  - `sync`: Force synchronous JSON response (best for testing)
  - `async`: Force queued response with SSE monitoring endpoints (no polling needed)
  - `stream`: Force streaming response (SSE or NDJSON)

  **Client Detection:**
  - Automatically detects testing tools (Postman, Swagger UI)
  - Adjusts behavior for better interactive experience
  - Respects Accept and Prefer headers for capabilities

  **Streaming Support (SSE):**
  - Real-time events with progress updates
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable
  - 30-second keepalive to prevent timeouts

  **Streaming Support (NDJSON):**
  - Efficient line-delimited JSON for large results
  - Automatic chunking (configurable 10-10000 rows)
  - No connection limits (stateless streaming)

  **Queue Management:**
  - Automatic queuing under high load
  - Real-time monitoring via SSE events (no polling needed)
  - Priority based on subscription tier
  - Queue position and progress updates pushed via SSE
  - Connect to returned `/v1/operations/{id}/stream` endpoint for updates

  **Error Handling:**
  - `429 Too Many Requests`: Rate limit or connection limit exceeded
  - `503 Service Unavailable`: Circuit breaker open or SSE disabled
  - Clients should implement exponential backoff

  **Note:**
  Query operations are FREE - no credit consumption required.
  Queue position is based on subscription tier for priority.

  Args:
      graph_id (str): Graph database identifier
      mode (Union[None, ResponseMode, Unset]): Response mode override
      chunk_size (Union[Unset, int]): Rows per chunk for streaming Default: 1000.
      test_mode (Union[Unset, bool]): Enable test mode for better debugging Default: False.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (CypherQueryRequest): Request model for Cypher query execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    mode=mode,
    chunk_size=chunk_size,
    test_mode=test_mode,
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
  body: CypherQueryRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
  chunk_size: Union[Unset, int] = 1000,
  test_mode: Union[Unset, bool] = False,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
  """Execute Cypher Query

   Execute a Cypher query with intelligent response optimization.

  This endpoint automatically selects the best execution strategy based on:
  - Query characteristics (size, complexity)
  - Client capabilities (SSE, NDJSON, JSON)
  - System load (queue status, concurrent queries)
  - User preferences (mode parameter, headers)

  **Response Modes:**
  - `auto` (default): Intelligent automatic selection
  - `sync`: Force synchronous JSON response (best for testing)
  - `async`: Force queued response with SSE monitoring endpoints (no polling needed)
  - `stream`: Force streaming response (SSE or NDJSON)

  **Client Detection:**
  - Automatically detects testing tools (Postman, Swagger UI)
  - Adjusts behavior for better interactive experience
  - Respects Accept and Prefer headers for capabilities

  **Streaming Support (SSE):**
  - Real-time events with progress updates
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable
  - 30-second keepalive to prevent timeouts

  **Streaming Support (NDJSON):**
  - Efficient line-delimited JSON for large results
  - Automatic chunking (configurable 10-10000 rows)
  - No connection limits (stateless streaming)

  **Queue Management:**
  - Automatic queuing under high load
  - Real-time monitoring via SSE events (no polling needed)
  - Priority based on subscription tier
  - Queue position and progress updates pushed via SSE
  - Connect to returned `/v1/operations/{id}/stream` endpoint for updates

  **Error Handling:**
  - `429 Too Many Requests`: Rate limit or connection limit exceeded
  - `503 Service Unavailable`: Circuit breaker open or SSE disabled
  - Clients should implement exponential backoff

  **Note:**
  Query operations are FREE - no credit consumption required.
  Queue position is based on subscription tier for priority.

  Args:
      graph_id (str): Graph database identifier
      mode (Union[None, ResponseMode, Unset]): Response mode override
      chunk_size (Union[Unset, int]): Rows per chunk for streaming Default: 1000.
      test_mode (Union[Unset, bool]): Enable test mode for better debugging Default: False.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (CypherQueryRequest): Request model for Cypher query execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
    mode=mode,
    chunk_size=chunk_size,
    test_mode=test_mode,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CypherQueryRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
  chunk_size: Union[Unset, int] = 1000,
  test_mode: Union[Unset, bool] = False,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
  """Execute Cypher Query

   Execute a Cypher query with intelligent response optimization.

  This endpoint automatically selects the best execution strategy based on:
  - Query characteristics (size, complexity)
  - Client capabilities (SSE, NDJSON, JSON)
  - System load (queue status, concurrent queries)
  - User preferences (mode parameter, headers)

  **Response Modes:**
  - `auto` (default): Intelligent automatic selection
  - `sync`: Force synchronous JSON response (best for testing)
  - `async`: Force queued response with SSE monitoring endpoints (no polling needed)
  - `stream`: Force streaming response (SSE or NDJSON)

  **Client Detection:**
  - Automatically detects testing tools (Postman, Swagger UI)
  - Adjusts behavior for better interactive experience
  - Respects Accept and Prefer headers for capabilities

  **Streaming Support (SSE):**
  - Real-time events with progress updates
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable
  - 30-second keepalive to prevent timeouts

  **Streaming Support (NDJSON):**
  - Efficient line-delimited JSON for large results
  - Automatic chunking (configurable 10-10000 rows)
  - No connection limits (stateless streaming)

  **Queue Management:**
  - Automatic queuing under high load
  - Real-time monitoring via SSE events (no polling needed)
  - Priority based on subscription tier
  - Queue position and progress updates pushed via SSE
  - Connect to returned `/v1/operations/{id}/stream` endpoint for updates

  **Error Handling:**
  - `429 Too Many Requests`: Rate limit or connection limit exceeded
  - `503 Service Unavailable`: Circuit breaker open or SSE disabled
  - Clients should implement exponential backoff

  **Note:**
  Query operations are FREE - no credit consumption required.
  Queue position is based on subscription tier for priority.

  Args:
      graph_id (str): Graph database identifier
      mode (Union[None, ResponseMode, Unset]): Response mode override
      chunk_size (Union[Unset, int]): Rows per chunk for streaming Default: 1000.
      test_mode (Union[Unset, bool]): Enable test mode for better debugging Default: False.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (CypherQueryRequest): Request model for Cypher query execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    mode=mode,
    chunk_size=chunk_size,
    test_mode=test_mode,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CypherQueryRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
  chunk_size: Union[Unset, int] = 1000,
  test_mode: Union[Unset, bool] = False,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
  """Execute Cypher Query

   Execute a Cypher query with intelligent response optimization.

  This endpoint automatically selects the best execution strategy based on:
  - Query characteristics (size, complexity)
  - Client capabilities (SSE, NDJSON, JSON)
  - System load (queue status, concurrent queries)
  - User preferences (mode parameter, headers)

  **Response Modes:**
  - `auto` (default): Intelligent automatic selection
  - `sync`: Force synchronous JSON response (best for testing)
  - `async`: Force queued response with SSE monitoring endpoints (no polling needed)
  - `stream`: Force streaming response (SSE or NDJSON)

  **Client Detection:**
  - Automatically detects testing tools (Postman, Swagger UI)
  - Adjusts behavior for better interactive experience
  - Respects Accept and Prefer headers for capabilities

  **Streaming Support (SSE):**
  - Real-time events with progress updates
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation if event system unavailable
  - 30-second keepalive to prevent timeouts

  **Streaming Support (NDJSON):**
  - Efficient line-delimited JSON for large results
  - Automatic chunking (configurable 10-10000 rows)
  - No connection limits (stateless streaming)

  **Queue Management:**
  - Automatic queuing under high load
  - Real-time monitoring via SSE events (no polling needed)
  - Priority based on subscription tier
  - Queue position and progress updates pushed via SSE
  - Connect to returned `/v1/operations/{id}/stream` endpoint for updates

  **Error Handling:**
  - `429 Too Many Requests`: Rate limit or connection limit exceeded
  - `503 Service Unavailable`: Circuit breaker open or SSE disabled
  - Clients should implement exponential backoff

  **Note:**
  Query operations are FREE - no credit consumption required.
  Queue position is based on subscription tier for priority.

  Args:
      graph_id (str): Graph database identifier
      mode (Union[None, ResponseMode, Unset]): Response mode override
      chunk_size (Union[Unset, int]): Rows per chunk for streaming Default: 1000.
      test_mode (Union[Unset, bool]): Enable test mode for better debugging Default: False.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (CypherQueryRequest): Request model for Cypher query execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      mode=mode,
      chunk_size=chunk_size,
      test_mode=test_mode,
      token=token,
      authorization=authorization,
    )
  ).parsed
