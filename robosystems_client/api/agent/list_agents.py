from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_list_response import AgentListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  capability: Union[None, Unset, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_capability: Union[None, Unset, str]
  if isinstance(capability, Unset):
    json_capability = UNSET
  else:
    json_capability = capability
  params["capability"] = json_capability

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/agent/list",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AgentListResponse, Any, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = AgentListResponse.from_dict(response.json())

    return response_200
  if response.status_code == 401:
    response_401 = cast(Any, None)
    return response_401
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AgentListResponse, Any, HTTPValidationError]]:
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
  capability: Union[None, Unset, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[AgentListResponse, Any, HTTPValidationError]]:
  """List available agents

   Get a comprehensive list of all available agents with their metadata.

  **Returns:**
  - Agent types and names
  - Capabilities and supported modes
  - Version information
  - Credit requirements

  Use the optional `capability` filter to find agents with specific capabilities.

  Args:
      graph_id (str): Graph database identifier
      capability (Union[None, Unset, str]): Filter by capability (e.g., 'financial_analysis',
          'rag_search')
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentListResponse, Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    capability=capability,
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
  capability: Union[None, Unset, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[AgentListResponse, Any, HTTPValidationError]]:
  """List available agents

   Get a comprehensive list of all available agents with their metadata.

  **Returns:**
  - Agent types and names
  - Capabilities and supported modes
  - Version information
  - Credit requirements

  Use the optional `capability` filter to find agents with specific capabilities.

  Args:
      graph_id (str): Graph database identifier
      capability (Union[None, Unset, str]): Filter by capability (e.g., 'financial_analysis',
          'rag_search')
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentListResponse, Any, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    capability=capability,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  capability: Union[None, Unset, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[AgentListResponse, Any, HTTPValidationError]]:
  """List available agents

   Get a comprehensive list of all available agents with their metadata.

  **Returns:**
  - Agent types and names
  - Capabilities and supported modes
  - Version information
  - Credit requirements

  Use the optional `capability` filter to find agents with specific capabilities.

  Args:
      graph_id (str): Graph database identifier
      capability (Union[None, Unset, str]): Filter by capability (e.g., 'financial_analysis',
          'rag_search')
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentListResponse, Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    capability=capability,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  capability: Union[None, Unset, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[AgentListResponse, Any, HTTPValidationError]]:
  """List available agents

   Get a comprehensive list of all available agents with their metadata.

  **Returns:**
  - Agent types and names
  - Capabilities and supported modes
  - Version information
  - Credit requirements

  Use the optional `capability` filter to find agents with specific capabilities.

  Args:
      graph_id (str): Graph database identifier
      capability (Union[None, Unset, str]): Filter by capability (e.g., 'financial_analysis',
          'rag_search')
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentListResponse, Any, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      capability=capability,
      token=token,
      authorization=authorization,
    )
  ).parsed
