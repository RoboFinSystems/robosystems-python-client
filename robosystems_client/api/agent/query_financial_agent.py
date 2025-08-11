from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_request import AgentRequest
from ...models.agent_response import AgentResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: AgentRequest,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  cookies = {}
  if auth_token is not UNSET:
    cookies["auth-token"] = auth_token

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/{graph_id}/agent",
    "cookies": cookies,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AgentResponse, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = AgentResponse.from_dict(response.json())

    return response_200
  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400
  if response.status_code == 402:
    response_402 = ErrorResponse.from_dict(response.json())

    return response_402
  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403
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
) -> Response[Union[AgentResponse, ErrorResponse, HTTPValidationError]]:
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
  body: AgentRequest,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[AgentResponse, ErrorResponse, HTTPValidationError]]:
  """Query Financial Agent

   AI-powered financial analysis with direct access to graph data.

  This endpoint provides intelligent financial analysis using an AI agent that can:
  - Analyze company financial statements and SEC filings
  - Review QuickBooks transactions and accounting data
  - Perform multi-period trend analysis
  - Generate insights from balance sheets and income statements
  - Answer complex financial queries with contextual understanding

  **Execution Modes:**
  - **Quick Analysis** (default): Synchronous responses for simple queries (1-2 tool calls)
  - **Extended Analysis**: Asynchronous processing for complex research (returns operation_id for SSE
  monitoring)

  **Extended Analysis Monitoring:**
  For complex queries, connect to the SSE stream for real-time progress:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Analysis:', data.message);
  };
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation with fallback to polling if SSE unavailable

  **Events Emitted:**
  - `operation_started`: Analysis begins
  - `operation_progress`: Tool calls, analysis steps
  - `operation_completed`: Final comprehensive analysis
  - `operation_error`: Analysis failed

  **Error Handling:**
  - `429 Too Many Requests`: SSE connection limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Fallback to status polling endpoint if SSE unavailable

  **Credit Consumption:**
  - Variable based on complexity: 3-60 credits
  - Simple queries: 3-15 credits
  - Complex analysis: 15-60 credits
  - Multiplied by graph tier (standard=1x, enterprise=2x, premium=4x)

  The agent automatically determines query complexity or you can force extended analysis.

  Args:
      graph_id (str):
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):
      body (AgentRequest): Request model for financial agent interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    authorization=authorization,
    auth_token=auth_token,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: AgentRequest,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[AgentResponse, ErrorResponse, HTTPValidationError]]:
  """Query Financial Agent

   AI-powered financial analysis with direct access to graph data.

  This endpoint provides intelligent financial analysis using an AI agent that can:
  - Analyze company financial statements and SEC filings
  - Review QuickBooks transactions and accounting data
  - Perform multi-period trend analysis
  - Generate insights from balance sheets and income statements
  - Answer complex financial queries with contextual understanding

  **Execution Modes:**
  - **Quick Analysis** (default): Synchronous responses for simple queries (1-2 tool calls)
  - **Extended Analysis**: Asynchronous processing for complex research (returns operation_id for SSE
  monitoring)

  **Extended Analysis Monitoring:**
  For complex queries, connect to the SSE stream for real-time progress:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Analysis:', data.message);
  };
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation with fallback to polling if SSE unavailable

  **Events Emitted:**
  - `operation_started`: Analysis begins
  - `operation_progress`: Tool calls, analysis steps
  - `operation_completed`: Final comprehensive analysis
  - `operation_error`: Analysis failed

  **Error Handling:**
  - `429 Too Many Requests`: SSE connection limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Fallback to status polling endpoint if SSE unavailable

  **Credit Consumption:**
  - Variable based on complexity: 3-60 credits
  - Simple queries: 3-15 credits
  - Complex analysis: 15-60 credits
  - Multiplied by graph tier (standard=1x, enterprise=2x, premium=4x)

  The agent automatically determines query complexity or you can force extended analysis.

  Args:
      graph_id (str):
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):
      body (AgentRequest): Request model for financial agent interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentResponse, ErrorResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
    authorization=authorization,
    auth_token=auth_token,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: AgentRequest,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[AgentResponse, ErrorResponse, HTTPValidationError]]:
  """Query Financial Agent

   AI-powered financial analysis with direct access to graph data.

  This endpoint provides intelligent financial analysis using an AI agent that can:
  - Analyze company financial statements and SEC filings
  - Review QuickBooks transactions and accounting data
  - Perform multi-period trend analysis
  - Generate insights from balance sheets and income statements
  - Answer complex financial queries with contextual understanding

  **Execution Modes:**
  - **Quick Analysis** (default): Synchronous responses for simple queries (1-2 tool calls)
  - **Extended Analysis**: Asynchronous processing for complex research (returns operation_id for SSE
  monitoring)

  **Extended Analysis Monitoring:**
  For complex queries, connect to the SSE stream for real-time progress:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Analysis:', data.message);
  };
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation with fallback to polling if SSE unavailable

  **Events Emitted:**
  - `operation_started`: Analysis begins
  - `operation_progress`: Tool calls, analysis steps
  - `operation_completed`: Final comprehensive analysis
  - `operation_error`: Analysis failed

  **Error Handling:**
  - `429 Too Many Requests`: SSE connection limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Fallback to status polling endpoint if SSE unavailable

  **Credit Consumption:**
  - Variable based on complexity: 3-60 credits
  - Simple queries: 3-15 credits
  - Complex analysis: 15-60 credits
  - Multiplied by graph tier (standard=1x, enterprise=2x, premium=4x)

  The agent automatically determines query complexity or you can force extended analysis.

  Args:
      graph_id (str):
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):
      body (AgentRequest): Request model for financial agent interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    authorization=authorization,
    auth_token=auth_token,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: AgentRequest,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[AgentResponse, ErrorResponse, HTTPValidationError]]:
  """Query Financial Agent

   AI-powered financial analysis with direct access to graph data.

  This endpoint provides intelligent financial analysis using an AI agent that can:
  - Analyze company financial statements and SEC filings
  - Review QuickBooks transactions and accounting data
  - Perform multi-period trend analysis
  - Generate insights from balance sheets and income statements
  - Answer complex financial queries with contextual understanding

  **Execution Modes:**
  - **Quick Analysis** (default): Synchronous responses for simple queries (1-2 tool calls)
  - **Extended Analysis**: Asynchronous processing for complex research (returns operation_id for SSE
  monitoring)

  **Extended Analysis Monitoring:**
  For complex queries, connect to the SSE stream for real-time progress:
  ```javascript
  const eventSource = new EventSource('/v1/operations/{operation_id}/stream');
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Analysis:', data.message);
  };
  ```

  **SSE Connection Limits:**
  - Maximum 5 concurrent SSE connections per user
  - Rate limited to 10 new connections per minute
  - Automatic circuit breaker for Redis failures
  - Graceful degradation with fallback to polling if SSE unavailable

  **Events Emitted:**
  - `operation_started`: Analysis begins
  - `operation_progress`: Tool calls, analysis steps
  - `operation_completed`: Final comprehensive analysis
  - `operation_error`: Analysis failed

  **Error Handling:**
  - `429 Too Many Requests`: SSE connection limit exceeded
  - `503 Service Unavailable`: SSE system temporarily disabled
  - Fallback to status polling endpoint if SSE unavailable

  **Credit Consumption:**
  - Variable based on complexity: 3-60 credits
  - Simple queries: 3-15 credits
  - Complex analysis: 15-60 credits
  - Multiplied by graph tier (standard=1x, enterprise=2x, premium=4x)

  The agent automatically determines query complexity or you can force extended analysis.

  Args:
      graph_id (str):
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):
      body (AgentRequest): Request model for financial agent interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentResponse, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      authorization=authorization,
      auth_token=auth_token,
    )
  ).parsed
