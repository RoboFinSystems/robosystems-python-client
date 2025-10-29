from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/select",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  if response.status_code == 200:
    response_200 = SuccessResponse.from_dict(response.json())

    return response_200

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

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
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
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
) -> Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  """Select Graph

   Select a specific graph as the active workspace for the user.

  The selected graph becomes the default context for operations in client applications
  and can be used to maintain user workspace preferences across sessions.

  **Functionality:**
  - Sets the specified graph as the user's currently selected graph
  - Deselects any previously selected graph (only one can be selected at a time)
  - Persists selection across sessions until changed
  - Returns confirmation with the selected graph ID

  **Requirements:**
  - User must have access to the graph (as admin or member)
  - Graph must exist and not be deleted
  - User can only select graphs they have permission to access

  **Use Cases:**
  - Switch between multiple graphs in a multi-graph environment
  - Set default workspace after creating a new graph
  - Restore user's preferred workspace on login
  - Support graph context switching in client applications

  **Client Integration:**
  Many client operations can default to the selected graph, simplifying API calls
  by eliminating the need to specify graph_id repeatedly. Check the selected
  graph with `GET /v1/graphs` which returns `selectedGraphId`.

  **Note:**
  Graph selection is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]
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
) -> Optional[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  """Select Graph

   Select a specific graph as the active workspace for the user.

  The selected graph becomes the default context for operations in client applications
  and can be used to maintain user workspace preferences across sessions.

  **Functionality:**
  - Sets the specified graph as the user's currently selected graph
  - Deselects any previously selected graph (only one can be selected at a time)
  - Persists selection across sessions until changed
  - Returns confirmation with the selected graph ID

  **Requirements:**
  - User must have access to the graph (as admin or member)
  - Graph must exist and not be deleted
  - User can only select graphs they have permission to access

  **Use Cases:**
  - Switch between multiple graphs in a multi-graph environment
  - Set default workspace after creating a new graph
  - Restore user's preferred workspace on login
  - Support graph context switching in client applications

  **Client Integration:**
  Many client operations can default to the selected graph, simplifying API calls
  by eliminating the need to specify graph_id repeatedly. Check the selected
  graph with `GET /v1/graphs` which returns `selectedGraphId`.

  **Note:**
  Graph selection is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, SuccessResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  """Select Graph

   Select a specific graph as the active workspace for the user.

  The selected graph becomes the default context for operations in client applications
  and can be used to maintain user workspace preferences across sessions.

  **Functionality:**
  - Sets the specified graph as the user's currently selected graph
  - Deselects any previously selected graph (only one can be selected at a time)
  - Persists selection across sessions until changed
  - Returns confirmation with the selected graph ID

  **Requirements:**
  - User must have access to the graph (as admin or member)
  - Graph must exist and not be deleted
  - User can only select graphs they have permission to access

  **Use Cases:**
  - Switch between multiple graphs in a multi-graph environment
  - Set default workspace after creating a new graph
  - Restore user's preferred workspace on login
  - Support graph context switching in client applications

  **Client Integration:**
  Many client operations can default to the selected graph, simplifying API calls
  by eliminating the need to specify graph_id repeatedly. Check the selected
  graph with `GET /v1/graphs` which returns `selectedGraphId`.

  **Note:**
  Graph selection is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]
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
) -> Optional[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  """Select Graph

   Select a specific graph as the active workspace for the user.

  The selected graph becomes the default context for operations in client applications
  and can be used to maintain user workspace preferences across sessions.

  **Functionality:**
  - Sets the specified graph as the user's currently selected graph
  - Deselects any previously selected graph (only one can be selected at a time)
  - Persists selection across sessions until changed
  - Returns confirmation with the selected graph ID

  **Requirements:**
  - User must have access to the graph (as admin or member)
  - Graph must exist and not be deleted
  - User can only select graphs they have permission to access

  **Use Cases:**
  - Switch between multiple graphs in a multi-graph environment
  - Set default workspace after creating a new graph
  - Restore user's preferred workspace on login
  - Support graph context switching in client applications

  **Client Integration:**
  Many client operations can default to the selected graph, simplifying API calls
  by eliminating the need to specify graph_id repeatedly. Check the selected
  graph with `GET /v1/graphs` which returns `selectedGraphId`.

  **Note:**
  Graph selection is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, SuccessResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
