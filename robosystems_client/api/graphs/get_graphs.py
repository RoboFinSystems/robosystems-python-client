from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_graphs_response import UserGraphsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UserGraphsResponse]]:
  if response.status_code == 200:
    response_200 = UserGraphsResponse.from_dict(response.json())

    return response_200

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, UserGraphsResponse]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[Union[Any, UserGraphsResponse]]:
  r"""Get User Graphs

   List all graph databases accessible to the current user with roles and selection status.

  Returns a comprehensive list of all graphs the user can access, including their
  role in each graph (admin or member) and which graph is currently selected as
  the active workspace.

  **Returned Information:**
  - Graph ID and display name for each accessible graph
  - User's role (admin/member) indicating permission level
  - Selection status (one graph can be marked as \"selected\")
  - Creation timestamp for each graph

  **Graph Roles:**
  - `admin`: Full access - can manage graph settings, invite users, delete graph
  - `member`: Read/write access - can query and modify data, cannot manage settings

  **Selected Graph Concept:**
  The \"selected\" graph is the user's currently active workspace. Many API operations
  default to the selected graph if no graph_id is provided. Users can change their
  selected graph via the `POST /v1/graphs/{graph_id}/select` endpoint.

  **Use Cases:**
  - Display graph selector in UI
  - Show user's accessible workspaces
  - Identify which graph is currently active
  - Filter graphs by role for permission-based features

  **Empty Response:**
  New users or users without graph access will receive an empty list with
  `selectedGraphId: null`. Users should create a new graph or request access
  to an existing graph.

  **Note:**
  Graph listing is included - no credit consumption required.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, UserGraphsResponse]]
  """

  kwargs = _get_kwargs()

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
) -> Optional[Union[Any, UserGraphsResponse]]:
  r"""Get User Graphs

   List all graph databases accessible to the current user with roles and selection status.

  Returns a comprehensive list of all graphs the user can access, including their
  role in each graph (admin or member) and which graph is currently selected as
  the active workspace.

  **Returned Information:**
  - Graph ID and display name for each accessible graph
  - User's role (admin/member) indicating permission level
  - Selection status (one graph can be marked as \"selected\")
  - Creation timestamp for each graph

  **Graph Roles:**
  - `admin`: Full access - can manage graph settings, invite users, delete graph
  - `member`: Read/write access - can query and modify data, cannot manage settings

  **Selected Graph Concept:**
  The \"selected\" graph is the user's currently active workspace. Many API operations
  default to the selected graph if no graph_id is provided. Users can change their
  selected graph via the `POST /v1/graphs/{graph_id}/select` endpoint.

  **Use Cases:**
  - Display graph selector in UI
  - Show user's accessible workspaces
  - Identify which graph is currently active
  - Filter graphs by role for permission-based features

  **Empty Response:**
  New users or users without graph access will receive an empty list with
  `selectedGraphId: null`. Users should create a new graph or request access
  to an existing graph.

  **Note:**
  Graph listing is included - no credit consumption required.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, UserGraphsResponse]
  """

  return sync_detailed(
    client=client,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[Union[Any, UserGraphsResponse]]:
  r"""Get User Graphs

   List all graph databases accessible to the current user with roles and selection status.

  Returns a comprehensive list of all graphs the user can access, including their
  role in each graph (admin or member) and which graph is currently selected as
  the active workspace.

  **Returned Information:**
  - Graph ID and display name for each accessible graph
  - User's role (admin/member) indicating permission level
  - Selection status (one graph can be marked as \"selected\")
  - Creation timestamp for each graph

  **Graph Roles:**
  - `admin`: Full access - can manage graph settings, invite users, delete graph
  - `member`: Read/write access - can query and modify data, cannot manage settings

  **Selected Graph Concept:**
  The \"selected\" graph is the user's currently active workspace. Many API operations
  default to the selected graph if no graph_id is provided. Users can change their
  selected graph via the `POST /v1/graphs/{graph_id}/select` endpoint.

  **Use Cases:**
  - Display graph selector in UI
  - Show user's accessible workspaces
  - Identify which graph is currently active
  - Filter graphs by role for permission-based features

  **Empty Response:**
  New users or users without graph access will receive an empty list with
  `selectedGraphId: null`. Users should create a new graph or request access
  to an existing graph.

  **Note:**
  Graph listing is included - no credit consumption required.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, UserGraphsResponse]]
  """

  kwargs = _get_kwargs()

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
) -> Optional[Union[Any, UserGraphsResponse]]:
  r"""Get User Graphs

   List all graph databases accessible to the current user with roles and selection status.

  Returns a comprehensive list of all graphs the user can access, including their
  role in each graph (admin or member) and which graph is currently selected as
  the active workspace.

  **Returned Information:**
  - Graph ID and display name for each accessible graph
  - User's role (admin/member) indicating permission level
  - Selection status (one graph can be marked as \"selected\")
  - Creation timestamp for each graph

  **Graph Roles:**
  - `admin`: Full access - can manage graph settings, invite users, delete graph
  - `member`: Read/write access - can query and modify data, cannot manage settings

  **Selected Graph Concept:**
  The \"selected\" graph is the user's currently active workspace. Many API operations
  default to the selected graph if no graph_id is provided. Users can change their
  selected graph via the `POST /v1/graphs/{graph_id}/select` endpoint.

  **Use Cases:**
  - Display graph selector in UI
  - Show user's accessible workspaces
  - Identify which graph is currently active
  - Filter graphs by role for permission-based features

  **Empty Response:**
  New users or users without graph access will receive an empty list with
  `selectedGraphId: null`. Users should create a new graph or request access
  to an existing graph.

  **Note:**
  Graph listing is included - no credit consumption required.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, UserGraphsResponse]
  """

  return (
    await asyncio_detailed(
      client=client,
    )
  ).parsed
