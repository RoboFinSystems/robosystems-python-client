from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_list_response import AgentListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  capability: None | str | Unset = UNSET,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_capability: None | str | Unset
  if isinstance(capability, Unset):
    json_capability = UNSET
  else:
    json_capability = capability
  params["capability"] = json_capability

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/agent".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentListResponse | Any | HTTPValidationError | None:
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
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentListResponse | Any | HTTPValidationError]:
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
  capability: None | str | Unset = UNSET,
) -> Response[AgentListResponse | Any | HTTPValidationError]:
  """List available agents

   Get a comprehensive list of all available agents with their metadata.

  **Returns:**
  - Agent types and names
  - Capabilities and supported modes
  - Version information
  - Credit requirements

  Use the optional `capability` filter to find agents with specific capabilities.

  Args:
      graph_id (str):
      capability (None | str | Unset): Filter by capability (e.g., 'financial_analysis',
          'rag_search')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[AgentListResponse | Any | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    capability=capability,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  capability: None | str | Unset = UNSET,
) -> AgentListResponse | Any | HTTPValidationError | None:
  """List available agents

   Get a comprehensive list of all available agents with their metadata.

  **Returns:**
  - Agent types and names
  - Capabilities and supported modes
  - Version information
  - Credit requirements

  Use the optional `capability` filter to find agents with specific capabilities.

  Args:
      graph_id (str):
      capability (None | str | Unset): Filter by capability (e.g., 'financial_analysis',
          'rag_search')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      AgentListResponse | Any | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    capability=capability,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  capability: None | str | Unset = UNSET,
) -> Response[AgentListResponse | Any | HTTPValidationError]:
  """List available agents

   Get a comprehensive list of all available agents with their metadata.

  **Returns:**
  - Agent types and names
  - Capabilities and supported modes
  - Version information
  - Credit requirements

  Use the optional `capability` filter to find agents with specific capabilities.

  Args:
      graph_id (str):
      capability (None | str | Unset): Filter by capability (e.g., 'financial_analysis',
          'rag_search')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[AgentListResponse | Any | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    capability=capability,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  capability: None | str | Unset = UNSET,
) -> AgentListResponse | Any | HTTPValidationError | None:
  """List available agents

   Get a comprehensive list of all available agents with their metadata.

  **Returns:**
  - Agent types and names
  - Capabilities and supported modes
  - Version information
  - Credit requirements

  Use the optional `capability` filter to find agents with specific capabilities.

  Args:
      graph_id (str):
      capability (None | str | Unset): Filter by capability (e.g., 'financial_analysis',
          'rag_search')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      AgentListResponse | Any | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      capability=capability,
    )
  ).parsed
