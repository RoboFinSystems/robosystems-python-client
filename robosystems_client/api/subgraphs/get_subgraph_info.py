from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.subgraph_response import SubgraphResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  subgraph_name: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/subgraphs/{subgraph_name}/info".format(
      graph_id=quote(str(graph_id), safe=""),
      subgraph_name=quote(str(subgraph_name), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | SubgraphResponse | None:
  if response.status_code == 200:
    response_200 = SubgraphResponse.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = cast(Any, None)
    return response_400

  if response.status_code == 401:
    response_401 = cast(Any, None)
    return response_401

  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403

  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | SubgraphResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  subgraph_name: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError | SubgraphResponse]:
  """Get Subgraph Details

   Get detailed information about a specific subgraph.

  **Requirements:**
  - User must have read access to parent graph
  - Subgraph name must be alphanumeric (1-20 characters)

  **Response includes:**
  - Full subgraph metadata
  - Database statistics (nodes, edges)
  - Size information
  - Schema configuration
  - Creation/modification timestamps
  - Last access time (when available)

  **Statistics:**
  Real-time statistics queried from LadybugDB:
  - Node count
  - Edge count
  - Database size on disk
  - Schema information

  **Note:**
  Use the subgraph name (e.g., 'dev', 'staging') not the full subgraph ID.
  The full ID is returned in the response (e.g., 'kg0123456789abcdef_dev').

  Args:
      graph_id (str):
      subgraph_name (str): Subgraph name (e.g., 'dev', 'staging')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError | SubgraphResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    subgraph_name=subgraph_name,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  subgraph_name: str,
  *,
  client: AuthenticatedClient,
) -> Any | HTTPValidationError | SubgraphResponse | None:
  """Get Subgraph Details

   Get detailed information about a specific subgraph.

  **Requirements:**
  - User must have read access to parent graph
  - Subgraph name must be alphanumeric (1-20 characters)

  **Response includes:**
  - Full subgraph metadata
  - Database statistics (nodes, edges)
  - Size information
  - Schema configuration
  - Creation/modification timestamps
  - Last access time (when available)

  **Statistics:**
  Real-time statistics queried from LadybugDB:
  - Node count
  - Edge count
  - Database size on disk
  - Schema information

  **Note:**
  Use the subgraph name (e.g., 'dev', 'staging') not the full subgraph ID.
  The full ID is returned in the response (e.g., 'kg0123456789abcdef_dev').

  Args:
      graph_id (str):
      subgraph_name (str): Subgraph name (e.g., 'dev', 'staging')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError | SubgraphResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    subgraph_name=subgraph_name,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  subgraph_name: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError | SubgraphResponse]:
  """Get Subgraph Details

   Get detailed information about a specific subgraph.

  **Requirements:**
  - User must have read access to parent graph
  - Subgraph name must be alphanumeric (1-20 characters)

  **Response includes:**
  - Full subgraph metadata
  - Database statistics (nodes, edges)
  - Size information
  - Schema configuration
  - Creation/modification timestamps
  - Last access time (when available)

  **Statistics:**
  Real-time statistics queried from LadybugDB:
  - Node count
  - Edge count
  - Database size on disk
  - Schema information

  **Note:**
  Use the subgraph name (e.g., 'dev', 'staging') not the full subgraph ID.
  The full ID is returned in the response (e.g., 'kg0123456789abcdef_dev').

  Args:
      graph_id (str):
      subgraph_name (str): Subgraph name (e.g., 'dev', 'staging')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError | SubgraphResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    subgraph_name=subgraph_name,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  subgraph_name: str,
  *,
  client: AuthenticatedClient,
) -> Any | HTTPValidationError | SubgraphResponse | None:
  """Get Subgraph Details

   Get detailed information about a specific subgraph.

  **Requirements:**
  - User must have read access to parent graph
  - Subgraph name must be alphanumeric (1-20 characters)

  **Response includes:**
  - Full subgraph metadata
  - Database statistics (nodes, edges)
  - Size information
  - Schema configuration
  - Creation/modification timestamps
  - Last access time (when available)

  **Statistics:**
  Real-time statistics queried from LadybugDB:
  - Node count
  - Edge count
  - Database size on disk
  - Schema information

  **Note:**
  Use the subgraph name (e.g., 'dev', 'staging') not the full subgraph ID.
  The full ID is returned in the response (e.g., 'kg0123456789abcdef_dev').

  Args:
      graph_id (str):
      subgraph_name (str): Subgraph name (e.g., 'dev', 'staging')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError | SubgraphResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      subgraph_name=subgraph_name,
      client=client,
    )
  ).parsed
