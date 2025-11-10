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
  agent_type: str,
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
    "url": f"/v1/graphs/{graph_id}/agent/{agent_type}",
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

  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404

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
  agent_type: str,
  *,
  client: AuthenticatedClient,
  body: AgentRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
) -> Response[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
  """Execute specific agent

   Execute a specific agent type directly with intelligent execution strategy.

  Available agents:
  - **financial**: Financial analysis, SEC filings, accounting data
  - **research**: Deep research and comprehensive analysis
  - **rag**: Fast retrieval without AI (no credits required)

  **Execution Strategies (automatic):**
  - Fast operations (<5s): Immediate synchronous response
  - Medium operations (5-30s): SSE streaming with progress updates
  - Long operations (>30s): Async Celery worker with operation tracking

  **Response Mode Override:**
  Use query parameter `?mode=sync|async` to override automatic strategy selection.

  Use this endpoint when you know which agent you want to use.

  Args:
      graph_id (str):
      agent_type (str):
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
    agent_type=agent_type,
    body=body,
    mode=mode,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  agent_type: str,
  *,
  client: AuthenticatedClient,
  body: AgentRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
) -> Optional[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
  """Execute specific agent

   Execute a specific agent type directly with intelligent execution strategy.

  Available agents:
  - **financial**: Financial analysis, SEC filings, accounting data
  - **research**: Deep research and comprehensive analysis
  - **rag**: Fast retrieval without AI (no credits required)

  **Execution Strategies (automatic):**
  - Fast operations (<5s): Immediate synchronous response
  - Medium operations (5-30s): SSE streaming with progress updates
  - Long operations (>30s): Async Celery worker with operation tracking

  **Response Mode Override:**
  Use query parameter `?mode=sync|async` to override automatic strategy selection.

  Use this endpoint when you know which agent you want to use.

  Args:
      graph_id (str):
      agent_type (str):
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
    agent_type=agent_type,
    client=client,
    body=body,
    mode=mode,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  agent_type: str,
  *,
  client: AuthenticatedClient,
  body: AgentRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
) -> Response[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
  """Execute specific agent

   Execute a specific agent type directly with intelligent execution strategy.

  Available agents:
  - **financial**: Financial analysis, SEC filings, accounting data
  - **research**: Deep research and comprehensive analysis
  - **rag**: Fast retrieval without AI (no credits required)

  **Execution Strategies (automatic):**
  - Fast operations (<5s): Immediate synchronous response
  - Medium operations (5-30s): SSE streaming with progress updates
  - Long operations (>30s): Async Celery worker with operation tracking

  **Response Mode Override:**
  Use query parameter `?mode=sync|async` to override automatic strategy selection.

  Use this endpoint when you know which agent you want to use.

  Args:
      graph_id (str):
      agent_type (str):
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
    agent_type=agent_type,
    body=body,
    mode=mode,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  agent_type: str,
  *,
  client: AuthenticatedClient,
  body: AgentRequest,
  mode: Union[None, ResponseMode, Unset] = UNSET,
) -> Optional[Union[AgentResponse, Any, ErrorResponse, HTTPValidationError]]:
  """Execute specific agent

   Execute a specific agent type directly with intelligent execution strategy.

  Available agents:
  - **financial**: Financial analysis, SEC filings, accounting data
  - **research**: Deep research and comprehensive analysis
  - **rag**: Fast retrieval without AI (no credits required)

  **Execution Strategies (automatic):**
  - Fast operations (<5s): Immediate synchronous response
  - Medium operations (5-30s): SSE streaming with progress updates
  - Long operations (>30s): Async Celery worker with operation tracking

  **Response Mode Override:**
  Use query parameter `?mode=sync|async` to override automatic strategy selection.

  Use this endpoint when you know which agent you want to use.

  Args:
      graph_id (str):
      agent_type (str):
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
      agent_type=agent_type,
      client=client,
      body=body,
      mode=mode,
    )
  ).parsed
