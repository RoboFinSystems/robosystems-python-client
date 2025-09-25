from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.subgraph_response import SubgraphResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  subgraph_id: str,
  *,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/subgraphs/{subgraph_id}/info",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, SubgraphResponse]]:
  if response.status_code == 200:
    response_200 = SubgraphResponse.from_dict(response.json())

    return response_200
  if response.status_code == 401:
    response_401 = cast(Any, None)
    return response_401
  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403
  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404
  if response.status_code == 400:
    response_400 = cast(Any, None)
    return response_400
  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, SubgraphResponse]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  subgraph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, SubgraphResponse]]:
  """Get Subgraph Details

   Get detailed information about a specific subgraph.

  **Requirements:**
  - User must have read access to parent graph

  **Response includes:**
  - Full subgraph metadata
  - Database statistics (nodes, edges)
  - Size information
  - Schema configuration
  - Creation/modification timestamps
  - Last access time (when available)

  **Statistics:**
  Real-time statistics queried from Kuzu:
  - Node count
  - Edge count
  - Database size on disk
  - Schema information

  Args:
      graph_id (str): Parent graph identifier
      subgraph_id (str): Subgraph identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, SubgraphResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    subgraph_id=subgraph_id,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  subgraph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, SubgraphResponse]]:
  """Get Subgraph Details

   Get detailed information about a specific subgraph.

  **Requirements:**
  - User must have read access to parent graph

  **Response includes:**
  - Full subgraph metadata
  - Database statistics (nodes, edges)
  - Size information
  - Schema configuration
  - Creation/modification timestamps
  - Last access time (when available)

  **Statistics:**
  Real-time statistics queried from Kuzu:
  - Node count
  - Edge count
  - Database size on disk
  - Schema information

  Args:
      graph_id (str): Parent graph identifier
      subgraph_id (str): Subgraph identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, SubgraphResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    subgraph_id=subgraph_id,
    client=client,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  subgraph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, SubgraphResponse]]:
  """Get Subgraph Details

   Get detailed information about a specific subgraph.

  **Requirements:**
  - User must have read access to parent graph

  **Response includes:**
  - Full subgraph metadata
  - Database statistics (nodes, edges)
  - Size information
  - Schema configuration
  - Creation/modification timestamps
  - Last access time (when available)

  **Statistics:**
  Real-time statistics queried from Kuzu:
  - Node count
  - Edge count
  - Database size on disk
  - Schema information

  Args:
      graph_id (str): Parent graph identifier
      subgraph_id (str): Subgraph identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, SubgraphResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    subgraph_id=subgraph_id,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  subgraph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, SubgraphResponse]]:
  """Get Subgraph Details

   Get detailed information about a specific subgraph.

  **Requirements:**
  - User must have read access to parent graph

  **Response includes:**
  - Full subgraph metadata
  - Database statistics (nodes, edges)
  - Size information
  - Schema configuration
  - Creation/modification timestamps
  - Last access time (when available)

  **Statistics:**
  Real-time statistics queried from Kuzu:
  - Node count
  - Edge count
  - Database size on disk
  - Schema information

  Args:
      graph_id (str): Parent graph identifier
      subgraph_id (str): Subgraph identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, SubgraphResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      subgraph_id=subgraph_id,
      client=client,
      token=token,
      authorization=authorization,
    )
  ).parsed
