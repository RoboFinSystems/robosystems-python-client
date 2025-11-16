from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.mcp_tool_call import MCPToolCall
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: MCPToolCall,
  format_: Union[None, Unset, str] = UNSET,
  test_mode: Union[Unset, bool] = False,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  params: dict[str, Any] = {}

  json_format_: Union[None, Unset, str]
  if isinstance(format_, Unset):
    json_format_ = UNSET
  else:
    json_format_ = format_
  params["format"] = json_format_

  params["test_mode"] = test_mode

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/mcp/call-tool",
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = response.json()
    return response_200

  if response.status_code == 202:
    response_202 = cast(Any, None)
    return response_202

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 402:
    response_402 = ErrorResponse.from_dict(response.json())

    return response_402

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 408:
    response_408 = ErrorResponse.from_dict(response.json())

    return response_408

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if response.status_code == 503:
    response_503 = ErrorResponse.from_dict(response.json())

    return response_503

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
  body: MCPToolCall,
  format_: Union[None, Unset, str] = UNSET,
  test_mode: Union[Unset, bool] = False,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Execute MCP Tool

   Execute an MCP tool with intelligent response optimization.

  This endpoint automatically selects the best execution strategy based on:
  - Tool type and estimated complexity
  - Client capabilities (AI agent detection)
  - System load and queue status
  - Graph type (shared repository vs user graph)

  **Response Formats:**
  - **JSON**: Direct response for small/fast operations
  - **SSE**: Server-Sent Events for progress monitoring
  - **NDJSON**: Newline-delimited JSON for streaming
  - **Queued**: Asynchronous execution with status monitoring

  **SSE Streaming Support:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation to direct response if SSE unavailable
  - Progress events for long-running operations

  **AI Agent Optimization:**
  The Node.js MCP client transparently handles all response formats,
  presenting a unified interface to AI agents. Streaming responses are
  automatically aggregated for seamless consumption.

  **Error Handling:**
  - `429 Too Many Requests`: Connection limit or rate limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - `408 Request Timeout`: Tool execution exceeded timeout
  - Clients should implement exponential backoff on errors

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  MCP tools operate on the specified graph/subgraph independently. Each subgraph
  has its own schema, data, and can be queried separately via MCP.

  **Credit Model:**
  MCP tool execution is included - no credit consumption required. Database
  operations (queries, schema inspection, analytics) are completely free.
  Only AI operations that invoke Claude or other LLM APIs consume credits,
  which happens at the AI agent layer, not the MCP tool layer.

  Args:
      graph_id (str):
      format_ (Union[None, Unset, str]): Response format override (json, sse, ndjson)
      test_mode (Union[Unset, bool]): Enable test mode for debugging Default: False.
      body (MCPToolCall): Request model for MCP tool execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    format_=format_,
    test_mode=test_mode,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: MCPToolCall,
  format_: Union[None, Unset, str] = UNSET,
  test_mode: Union[Unset, bool] = False,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Execute MCP Tool

   Execute an MCP tool with intelligent response optimization.

  This endpoint automatically selects the best execution strategy based on:
  - Tool type and estimated complexity
  - Client capabilities (AI agent detection)
  - System load and queue status
  - Graph type (shared repository vs user graph)

  **Response Formats:**
  - **JSON**: Direct response for small/fast operations
  - **SSE**: Server-Sent Events for progress monitoring
  - **NDJSON**: Newline-delimited JSON for streaming
  - **Queued**: Asynchronous execution with status monitoring

  **SSE Streaming Support:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation to direct response if SSE unavailable
  - Progress events for long-running operations

  **AI Agent Optimization:**
  The Node.js MCP client transparently handles all response formats,
  presenting a unified interface to AI agents. Streaming responses are
  automatically aggregated for seamless consumption.

  **Error Handling:**
  - `429 Too Many Requests`: Connection limit or rate limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - `408 Request Timeout`: Tool execution exceeded timeout
  - Clients should implement exponential backoff on errors

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  MCP tools operate on the specified graph/subgraph independently. Each subgraph
  has its own schema, data, and can be queried separately via MCP.

  **Credit Model:**
  MCP tool execution is included - no credit consumption required. Database
  operations (queries, schema inspection, analytics) are completely free.
  Only AI operations that invoke Claude or other LLM APIs consume credits,
  which happens at the AI agent layer, not the MCP tool layer.

  Args:
      graph_id (str):
      format_ (Union[None, Unset, str]): Response format override (json, sse, ndjson)
      test_mode (Union[Unset, bool]): Enable test mode for debugging Default: False.
      body (MCPToolCall): Request model for MCP tool execution.

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
    format_=format_,
    test_mode=test_mode,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: MCPToolCall,
  format_: Union[None, Unset, str] = UNSET,
  test_mode: Union[Unset, bool] = False,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Execute MCP Tool

   Execute an MCP tool with intelligent response optimization.

  This endpoint automatically selects the best execution strategy based on:
  - Tool type and estimated complexity
  - Client capabilities (AI agent detection)
  - System load and queue status
  - Graph type (shared repository vs user graph)

  **Response Formats:**
  - **JSON**: Direct response for small/fast operations
  - **SSE**: Server-Sent Events for progress monitoring
  - **NDJSON**: Newline-delimited JSON for streaming
  - **Queued**: Asynchronous execution with status monitoring

  **SSE Streaming Support:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation to direct response if SSE unavailable
  - Progress events for long-running operations

  **AI Agent Optimization:**
  The Node.js MCP client transparently handles all response formats,
  presenting a unified interface to AI agents. Streaming responses are
  automatically aggregated for seamless consumption.

  **Error Handling:**
  - `429 Too Many Requests`: Connection limit or rate limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - `408 Request Timeout`: Tool execution exceeded timeout
  - Clients should implement exponential backoff on errors

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  MCP tools operate on the specified graph/subgraph independently. Each subgraph
  has its own schema, data, and can be queried separately via MCP.

  **Credit Model:**
  MCP tool execution is included - no credit consumption required. Database
  operations (queries, schema inspection, analytics) are completely free.
  Only AI operations that invoke Claude or other LLM APIs consume credits,
  which happens at the AI agent layer, not the MCP tool layer.

  Args:
      graph_id (str):
      format_ (Union[None, Unset, str]): Response format override (json, sse, ndjson)
      test_mode (Union[Unset, bool]): Enable test mode for debugging Default: False.
      body (MCPToolCall): Request model for MCP tool execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    format_=format_,
    test_mode=test_mode,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: MCPToolCall,
  format_: Union[None, Unset, str] = UNSET,
  test_mode: Union[Unset, bool] = False,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Execute MCP Tool

   Execute an MCP tool with intelligent response optimization.

  This endpoint automatically selects the best execution strategy based on:
  - Tool type and estimated complexity
  - Client capabilities (AI agent detection)
  - System load and queue status
  - Graph type (shared repository vs user graph)

  **Response Formats:**
  - **JSON**: Direct response for small/fast operations
  - **SSE**: Server-Sent Events for progress monitoring
  - **NDJSON**: Newline-delimited JSON for streaming
  - **Queued**: Asynchronous execution with status monitoring

  **SSE Streaming Support:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation to direct response if SSE unavailable
  - Progress events for long-running operations

  **AI Agent Optimization:**
  The Node.js MCP client transparently handles all response formats,
  presenting a unified interface to AI agents. Streaming responses are
  automatically aggregated for seamless consumption.

  **Error Handling:**
  - `429 Too Many Requests`: Connection limit or rate limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - `408 Request Timeout`: Tool execution exceeded timeout
  - Clients should implement exponential backoff on errors

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  MCP tools operate on the specified graph/subgraph independently. Each subgraph
  has its own schema, data, and can be queried separately via MCP.

  **Credit Model:**
  MCP tool execution is included - no credit consumption required. Database
  operations (queries, schema inspection, analytics) are completely free.
  Only AI operations that invoke Claude or other LLM APIs consume credits,
  which happens at the AI agent layer, not the MCP tool layer.

  Args:
      graph_id (str):
      format_ (Union[None, Unset, str]): Response format override (json, sse, ndjson)
      test_mode (Union[Unset, bool]): Enable test mode for debugging Default: False.
      body (MCPToolCall): Request model for MCP tool execution.

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
      format_=format_,
      test_mode=test_mode,
    )
  ).parsed
