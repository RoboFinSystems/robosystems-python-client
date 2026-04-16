from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

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
  format_: None | str | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  params: dict[str, Any] = {}

  json_format_: None | str | Unset
  if isinstance(format_, Unset):
    json_format_ = UNSET
  else:
    json_format_ = format_
  params["format"] = json_format_

  params["test_mode"] = test_mode

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/mcp/call-tool".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = response.json()
    return response_200

  if response.status_code == 202:
    response_202 = cast(Any, None)
    return response_202

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 408:
    response_408 = cast(Any, None)
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
    response_503 = cast(Any, None)
    return response_503

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | HTTPValidationError]:
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
  format_: None | str | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  """Execute MCP Tool

   Strategy auto-selected by tool type and load: JSON for fast tools, SSE for long queries, NDJSON for
  large results. Database operations (Cypher, schema, info) consume no credits — only AI LLM calls
  cost credits.

  Args:
      graph_id (str):
      format_ (None | str | Unset): Response format override (json, sse, ndjson)
      test_mode (bool | Unset): Enable test mode for debugging Default: False.
      body (MCPToolCall): Request model for MCP tool execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError]
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
  format_: None | str | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> Any | ErrorResponse | HTTPValidationError | None:
  """Execute MCP Tool

   Strategy auto-selected by tool type and load: JSON for fast tools, SSE for long queries, NDJSON for
  large results. Database operations (Cypher, schema, info) consume no credits — only AI LLM calls
  cost credits.

  Args:
      graph_id (str):
      format_ (None | str | Unset): Response format override (json, sse, ndjson)
      test_mode (bool | Unset): Enable test mode for debugging Default: False.
      body (MCPToolCall): Request model for MCP tool execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError
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
  format_: None | str | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  """Execute MCP Tool

   Strategy auto-selected by tool type and load: JSON for fast tools, SSE for long queries, NDJSON for
  large results. Database operations (Cypher, schema, info) consume no credits — only AI LLM calls
  cost credits.

  Args:
      graph_id (str):
      format_ (None | str | Unset): Response format override (json, sse, ndjson)
      test_mode (bool | Unset): Enable test mode for debugging Default: False.
      body (MCPToolCall): Request model for MCP tool execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError]
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
  format_: None | str | Unset = UNSET,
  test_mode: bool | Unset = False,
) -> Any | ErrorResponse | HTTPValidationError | None:
  """Execute MCP Tool

   Strategy auto-selected by tool type and load: JSON for fast tools, SSE for long queries, NDJSON for
  large results. Database operations (Cypher, schema, info) consume no credits — only AI LLM calls
  cost credits.

  Args:
      graph_id (str):
      format_ (None | str | Unset): Response format override (json, sse, ndjson)
      test_mode (bool | Unset): Enable test mode for debugging Default: False.
      body (MCPToolCall): Request model for MCP tool execution.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError
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
