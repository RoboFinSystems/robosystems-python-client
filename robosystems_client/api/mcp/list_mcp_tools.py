from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.mcp_tools_response import MCPToolsResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/mcp/tools".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | MCPToolsResponse | None:
  if response.status_code == 200:
    response_200 = MCPToolsResponse.from_dict(response.json())

    return response_200

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

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
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | MCPToolsResponse]:
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
) -> Response[ErrorResponse | HTTPValidationError | MCPToolsResponse]:
  """List MCP Tools

   Get available Model Context Protocol tools for graph analysis.

  This endpoint returns a comprehensive list of MCP tools optimized for AI agents:
  - Tool schemas with detailed parameter documentation
  - Context-aware descriptions based on graph type
  - Capability indicators for streaming and progress

  The tool list is customized based on:
  - Graph type (shared repository vs user graph)
  - User permissions and subscription tier
  - Backend capabilities (LadybugDB, Neo4j, etc.)

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  The returned tool list is identical for parent graphs and subgraphs, as all
  MCP tools work uniformly across graph boundaries.

  **Note:**
  MCP tool listing is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | MCPToolsResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> ErrorResponse | HTTPValidationError | MCPToolsResponse | None:
  """List MCP Tools

   Get available Model Context Protocol tools for graph analysis.

  This endpoint returns a comprehensive list of MCP tools optimized for AI agents:
  - Tool schemas with detailed parameter documentation
  - Context-aware descriptions based on graph type
  - Capability indicators for streaming and progress

  The tool list is customized based on:
  - Graph type (shared repository vs user graph)
  - User permissions and subscription tier
  - Backend capabilities (LadybugDB, Neo4j, etc.)

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  The returned tool list is identical for parent graphs and subgraphs, as all
  MCP tools work uniformly across graph boundaries.

  **Note:**
  MCP tool listing is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | MCPToolsResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[ErrorResponse | HTTPValidationError | MCPToolsResponse]:
  """List MCP Tools

   Get available Model Context Protocol tools for graph analysis.

  This endpoint returns a comprehensive list of MCP tools optimized for AI agents:
  - Tool schemas with detailed parameter documentation
  - Context-aware descriptions based on graph type
  - Capability indicators for streaming and progress

  The tool list is customized based on:
  - Graph type (shared repository vs user graph)
  - User permissions and subscription tier
  - Backend capabilities (LadybugDB, Neo4j, etc.)

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  The returned tool list is identical for parent graphs and subgraphs, as all
  MCP tools work uniformly across graph boundaries.

  **Note:**
  MCP tool listing is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | MCPToolsResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> ErrorResponse | HTTPValidationError | MCPToolsResponse | None:
  """List MCP Tools

   Get available Model Context Protocol tools for graph analysis.

  This endpoint returns a comprehensive list of MCP tools optimized for AI agents:
  - Tool schemas with detailed parameter documentation
  - Context-aware descriptions based on graph type
  - Capability indicators for streaming and progress

  The tool list is customized based on:
  - Graph type (shared repository vs user graph)
  - User permissions and subscription tier
  - Backend capabilities (LadybugDB, Neo4j, etc.)

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  The returned tool list is identical for parent graphs and subgraphs, as all
  MCP tools work uniformly across graph boundaries.

  **Note:**
  MCP tool listing is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | MCPToolsResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
