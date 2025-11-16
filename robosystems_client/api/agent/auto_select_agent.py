from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_request import AgentRequest
from ...models.agent_response import AgentResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.response_mode import ResponseMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: AgentRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  params: dict[str, Any] = {}

  json_mode: Union[None, Unset, str]
  if isinstance(mode, Unset):
    json_mode = UNSET
  elif isinstance(mode, ResponseMode):
    json_mode = mode.value
  else:
    json_mode = mode
  params["mode"] = json_mode

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/agent",
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = AgentResponse.from_dict(response.json())

    return response_200

  if response.status_code == 202:
    response_202 = cast(Any, None)
    return response_202

  if response.status_code == 400:
    response_400 = cast(Any, None)
    return response_400

  if response.status_code == 402:
    response_402 = cast(Any, None)
    return response_402

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = cast(Any, None)
    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
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
  mode: Union[None, ResponseMode, Unset] = UNSET,
) -> Response[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
  r"""Auto-select agent for query

   Automatically select the best agent for your query with intelligent execution strategy.

  **Agent Selection Process:**

  The orchestrator intelligently routes your query by:
  1. Analyzing query intent and complexity
  2. Enriching context with RAG if enabled
  3. Evaluating all available agents against selection criteria
  4. Selecting the best match based on confidence scores
  5. Choosing execution strategy (sync/SSE/async) based on expected time
  6. Executing the query with the selected agent

  **Available Agent Types:**
  - `financial`: Financial analysis, SEC filings, company metrics
  - `research`: General research, data exploration, trend analysis
  - `rag`: Knowledge base search using RAG enrichment

  **Execution Modes:**
  - `quick`: Fast responses (~2-5s), suitable for simple queries
  - `standard`: Balanced approach (~5-15s), default mode
  - `extended`: Comprehensive analysis (~15-60s), deep research
  - `streaming`: Real-time response streaming

  **Execution Strategies (automatic):**
  - Fast operations (<5s): Immediate synchronous response
  - Medium operations (5-30s): SSE streaming with progress updates
  - Long operations (>30s): Async Celery worker with operation tracking

  **Response Mode Override:**
  Use query parameter `?mode=sync|async` to override automatic strategy selection.

  **Confidence Score Interpretation:**
  - `0.9-1.0`: High confidence, agent is ideal match
  - `0.7-0.9`: Good confidence, agent is suitable
  - `0.5-0.7`: Moderate confidence, agent can handle but may not be optimal
  - `0.3-0.5`: Low confidence, fallback agent used
  - `<0.3`: Very low confidence, consider using specific agent endpoint

  **Credit Costs:**
  - Quick mode: 5-10 credits per query
  - Standard mode: 15-25 credits per query
  - Extended mode: 30-75 credits per query
  - RAG enrichment: +5-15 credits (if enabled)

  **Use Cases:**
  - Ask questions without specifying agent type
  - Get intelligent routing for complex multi-domain queries
  - Leverage conversation history for contextual understanding
  - Enable RAG for knowledge base enrichment

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Agents operate on the specified graph/subgraph's data independently. RAG enrichment
  and knowledge base search are scoped to the specific graph/subgraph.

  See request/response examples in the \"Examples\" dropdown below.

  Args:
      graph_id (str):
      mode (Union[None, ResponseMode, Unset]): Override execution mode: sync, async, stream, or
          auto
      body (AgentRequest): Request model for agent interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    mode=mode,
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
  mode: Union[None, ResponseMode, Unset] = UNSET,
) -> Optional[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
  r"""Auto-select agent for query

   Automatically select the best agent for your query with intelligent execution strategy.

  **Agent Selection Process:**

  The orchestrator intelligently routes your query by:
  1. Analyzing query intent and complexity
  2. Enriching context with RAG if enabled
  3. Evaluating all available agents against selection criteria
  4. Selecting the best match based on confidence scores
  5. Choosing execution strategy (sync/SSE/async) based on expected time
  6. Executing the query with the selected agent

  **Available Agent Types:**
  - `financial`: Financial analysis, SEC filings, company metrics
  - `research`: General research, data exploration, trend analysis
  - `rag`: Knowledge base search using RAG enrichment

  **Execution Modes:**
  - `quick`: Fast responses (~2-5s), suitable for simple queries
  - `standard`: Balanced approach (~5-15s), default mode
  - `extended`: Comprehensive analysis (~15-60s), deep research
  - `streaming`: Real-time response streaming

  **Execution Strategies (automatic):**
  - Fast operations (<5s): Immediate synchronous response
  - Medium operations (5-30s): SSE streaming with progress updates
  - Long operations (>30s): Async Celery worker with operation tracking

  **Response Mode Override:**
  Use query parameter `?mode=sync|async` to override automatic strategy selection.

  **Confidence Score Interpretation:**
  - `0.9-1.0`: High confidence, agent is ideal match
  - `0.7-0.9`: Good confidence, agent is suitable
  - `0.5-0.7`: Moderate confidence, agent can handle but may not be optimal
  - `0.3-0.5`: Low confidence, fallback agent used
  - `<0.3`: Very low confidence, consider using specific agent endpoint

  **Credit Costs:**
  - Quick mode: 5-10 credits per query
  - Standard mode: 15-25 credits per query
  - Extended mode: 30-75 credits per query
  - RAG enrichment: +5-15 credits (if enabled)

  **Use Cases:**
  - Ask questions without specifying agent type
  - Get intelligent routing for complex multi-domain queries
  - Leverage conversation history for contextual understanding
  - Enable RAG for knowledge base enrichment

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Agents operate on the specified graph/subgraph's data independently. RAG enrichment
  and knowledge base search are scoped to the specific graph/subgraph.

  See request/response examples in the \"Examples\" dropdown below.

  Args:
      graph_id (str):
      mode (Union[None, ResponseMode, Unset]): Override execution mode: sync, async, stream, or
          auto
      body (AgentRequest): Request model for agent interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
    mode=mode,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: AgentRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
) -> Response[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
  r"""Auto-select agent for query

   Automatically select the best agent for your query with intelligent execution strategy.

  **Agent Selection Process:**

  The orchestrator intelligently routes your query by:
  1. Analyzing query intent and complexity
  2. Enriching context with RAG if enabled
  3. Evaluating all available agents against selection criteria
  4. Selecting the best match based on confidence scores
  5. Choosing execution strategy (sync/SSE/async) based on expected time
  6. Executing the query with the selected agent

  **Available Agent Types:**
  - `financial`: Financial analysis, SEC filings, company metrics
  - `research`: General research, data exploration, trend analysis
  - `rag`: Knowledge base search using RAG enrichment

  **Execution Modes:**
  - `quick`: Fast responses (~2-5s), suitable for simple queries
  - `standard`: Balanced approach (~5-15s), default mode
  - `extended`: Comprehensive analysis (~15-60s), deep research
  - `streaming`: Real-time response streaming

  **Execution Strategies (automatic):**
  - Fast operations (<5s): Immediate synchronous response
  - Medium operations (5-30s): SSE streaming with progress updates
  - Long operations (>30s): Async Celery worker with operation tracking

  **Response Mode Override:**
  Use query parameter `?mode=sync|async` to override automatic strategy selection.

  **Confidence Score Interpretation:**
  - `0.9-1.0`: High confidence, agent is ideal match
  - `0.7-0.9`: Good confidence, agent is suitable
  - `0.5-0.7`: Moderate confidence, agent can handle but may not be optimal
  - `0.3-0.5`: Low confidence, fallback agent used
  - `<0.3`: Very low confidence, consider using specific agent endpoint

  **Credit Costs:**
  - Quick mode: 5-10 credits per query
  - Standard mode: 15-25 credits per query
  - Extended mode: 30-75 credits per query
  - RAG enrichment: +5-15 credits (if enabled)

  **Use Cases:**
  - Ask questions without specifying agent type
  - Get intelligent routing for complex multi-domain queries
  - Leverage conversation history for contextual understanding
  - Enable RAG for knowledge base enrichment

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Agents operate on the specified graph/subgraph's data independently. RAG enrichment
  and knowledge base search are scoped to the specific graph/subgraph.

  See request/response examples in the \"Examples\" dropdown below.

  Args:
      graph_id (str):
      mode (Union[None, ResponseMode, Unset]): Override execution mode: sync, async, stream, or
          auto
      body (AgentRequest): Request model for agent interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    mode=mode,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: AgentRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
) -> Optional[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
  r"""Auto-select agent for query

   Automatically select the best agent for your query with intelligent execution strategy.

  **Agent Selection Process:**

  The orchestrator intelligently routes your query by:
  1. Analyzing query intent and complexity
  2. Enriching context with RAG if enabled
  3. Evaluating all available agents against selection criteria
  4. Selecting the best match based on confidence scores
  5. Choosing execution strategy (sync/SSE/async) based on expected time
  6. Executing the query with the selected agent

  **Available Agent Types:**
  - `financial`: Financial analysis, SEC filings, company metrics
  - `research`: General research, data exploration, trend analysis
  - `rag`: Knowledge base search using RAG enrichment

  **Execution Modes:**
  - `quick`: Fast responses (~2-5s), suitable for simple queries
  - `standard`: Balanced approach (~5-15s), default mode
  - `extended`: Comprehensive analysis (~15-60s), deep research
  - `streaming`: Real-time response streaming

  **Execution Strategies (automatic):**
  - Fast operations (<5s): Immediate synchronous response
  - Medium operations (5-30s): SSE streaming with progress updates
  - Long operations (>30s): Async Celery worker with operation tracking

  **Response Mode Override:**
  Use query parameter `?mode=sync|async` to override automatic strategy selection.

  **Confidence Score Interpretation:**
  - `0.9-1.0`: High confidence, agent is ideal match
  - `0.7-0.9`: Good confidence, agent is suitable
  - `0.5-0.7`: Moderate confidence, agent can handle but may not be optimal
  - `0.3-0.5`: Low confidence, fallback agent used
  - `<0.3`: Very low confidence, consider using specific agent endpoint

  **Credit Costs:**
  - Quick mode: 5-10 credits per query
  - Standard mode: 15-25 credits per query
  - Extended mode: 30-75 credits per query
  - RAG enrichment: +5-15 credits (if enabled)

  **Use Cases:**
  - Ask questions without specifying agent type
  - Get intelligent routing for complex multi-domain queries
  - Leverage conversation history for contextual understanding
  - Enable RAG for knowledge base enrichment

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Agents operate on the specified graph/subgraph's data independently. RAG enrichment
  and knowledge base search are scoped to the specific graph/subgraph.

  See request/response examples in the \"Examples\" dropdown below.

  Args:
      graph_id (str):
      mode (Union[None, ResponseMode, Unset]): Override execution mode: sync, async, stream, or
          auto
      body (AgentRequest): Request model for agent interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      mode=mode,
    )
  ).parsed
