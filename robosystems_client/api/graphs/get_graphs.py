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
  r"""Get User Graphs and Repositories

   List all graph databases and shared repositories accessible to the current user.

  Returns a unified list of both user-created graphs and shared repositories (like SEC data)
  that the user has access to, including their role/access level and selection status.

  **Returned Information:**
  - Graph/Repository ID and display name
  - User's role/access level (admin/member for graphs, read/write/admin for repositories)
  - Selection status (only user graphs can be selected)
  - Creation timestamp
  - Repository type indicator (isRepository: true for shared repositories)

  **User Graphs (isRepository: false):**
  - Collaborative workspaces that can be shared with other users
  - Roles: `admin` (full access, can invite users) or `member` (read/write access)
  - Can be selected as active workspace
  - Graphs you create or have been invited to

  **Shared Repositories (isRepository: true):**
  - Read-only data repositories like SEC filings, industry benchmarks
  - Access levels: `read`, `write` (for data contributions), `admin`
  - Cannot be selected (each has separate subscription)
  - Require separate subscriptions (personal, cannot be shared)

  **Selected Graph Concept:**
  The \"selected\" graph is the user's currently active workspace (user graphs only).
  Many API operations default to the selected graph if no graph_id is provided.
  Users can change their selected graph via `POST /v1/graphs/{graph_id}/select`.

  **Use Cases:**
  - Display unified graph/repository selector in UI
  - Show all accessible data sources (both owned graphs and subscribed repositories)
  - Identify currently active workspace
  - Filter by type (user graphs vs repositories)

  **Empty Response:**
  New users receive an empty list with `selectedGraphId: null`. Users should create
  a graph or subscribe to a repository.

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
  r"""Get User Graphs and Repositories

   List all graph databases and shared repositories accessible to the current user.

  Returns a unified list of both user-created graphs and shared repositories (like SEC data)
  that the user has access to, including their role/access level and selection status.

  **Returned Information:**
  - Graph/Repository ID and display name
  - User's role/access level (admin/member for graphs, read/write/admin for repositories)
  - Selection status (only user graphs can be selected)
  - Creation timestamp
  - Repository type indicator (isRepository: true for shared repositories)

  **User Graphs (isRepository: false):**
  - Collaborative workspaces that can be shared with other users
  - Roles: `admin` (full access, can invite users) or `member` (read/write access)
  - Can be selected as active workspace
  - Graphs you create or have been invited to

  **Shared Repositories (isRepository: true):**
  - Read-only data repositories like SEC filings, industry benchmarks
  - Access levels: `read`, `write` (for data contributions), `admin`
  - Cannot be selected (each has separate subscription)
  - Require separate subscriptions (personal, cannot be shared)

  **Selected Graph Concept:**
  The \"selected\" graph is the user's currently active workspace (user graphs only).
  Many API operations default to the selected graph if no graph_id is provided.
  Users can change their selected graph via `POST /v1/graphs/{graph_id}/select`.

  **Use Cases:**
  - Display unified graph/repository selector in UI
  - Show all accessible data sources (both owned graphs and subscribed repositories)
  - Identify currently active workspace
  - Filter by type (user graphs vs repositories)

  **Empty Response:**
  New users receive an empty list with `selectedGraphId: null`. Users should create
  a graph or subscribe to a repository.

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
  r"""Get User Graphs and Repositories

   List all graph databases and shared repositories accessible to the current user.

  Returns a unified list of both user-created graphs and shared repositories (like SEC data)
  that the user has access to, including their role/access level and selection status.

  **Returned Information:**
  - Graph/Repository ID and display name
  - User's role/access level (admin/member for graphs, read/write/admin for repositories)
  - Selection status (only user graphs can be selected)
  - Creation timestamp
  - Repository type indicator (isRepository: true for shared repositories)

  **User Graphs (isRepository: false):**
  - Collaborative workspaces that can be shared with other users
  - Roles: `admin` (full access, can invite users) or `member` (read/write access)
  - Can be selected as active workspace
  - Graphs you create or have been invited to

  **Shared Repositories (isRepository: true):**
  - Read-only data repositories like SEC filings, industry benchmarks
  - Access levels: `read`, `write` (for data contributions), `admin`
  - Cannot be selected (each has separate subscription)
  - Require separate subscriptions (personal, cannot be shared)

  **Selected Graph Concept:**
  The \"selected\" graph is the user's currently active workspace (user graphs only).
  Many API operations default to the selected graph if no graph_id is provided.
  Users can change their selected graph via `POST /v1/graphs/{graph_id}/select`.

  **Use Cases:**
  - Display unified graph/repository selector in UI
  - Show all accessible data sources (both owned graphs and subscribed repositories)
  - Identify currently active workspace
  - Filter by type (user graphs vs repositories)

  **Empty Response:**
  New users receive an empty list with `selectedGraphId: null`. Users should create
  a graph or subscribe to a repository.

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
  r"""Get User Graphs and Repositories

   List all graph databases and shared repositories accessible to the current user.

  Returns a unified list of both user-created graphs and shared repositories (like SEC data)
  that the user has access to, including their role/access level and selection status.

  **Returned Information:**
  - Graph/Repository ID and display name
  - User's role/access level (admin/member for graphs, read/write/admin for repositories)
  - Selection status (only user graphs can be selected)
  - Creation timestamp
  - Repository type indicator (isRepository: true for shared repositories)

  **User Graphs (isRepository: false):**
  - Collaborative workspaces that can be shared with other users
  - Roles: `admin` (full access, can invite users) or `member` (read/write access)
  - Can be selected as active workspace
  - Graphs you create or have been invited to

  **Shared Repositories (isRepository: true):**
  - Read-only data repositories like SEC filings, industry benchmarks
  - Access levels: `read`, `write` (for data contributions), `admin`
  - Cannot be selected (each has separate subscription)
  - Require separate subscriptions (personal, cannot be shared)

  **Selected Graph Concept:**
  The \"selected\" graph is the user's currently active workspace (user graphs only).
  Many API operations default to the selected graph if no graph_id is provided.
  Users can change their selected graph via `POST /v1/graphs/{graph_id}/select`.

  **Use Cases:**
  - Display unified graph/repository selector in UI
  - Show all accessible data sources (both owned graphs and subscribed repositories)
  - Identify currently active workspace
  - Filter by type (user graphs vs repositories)

  **Empty Response:**
  New users receive an empty list with `selectedGraphId: null`. Users should create
  a graph or subscribe to a repository.

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
