from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_subgraph_request import CreateSubgraphRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.subgraph_response import SubgraphResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: CreateSubgraphRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/subgraphs",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, SubgraphResponse]]:
  if response.status_code == 201:
    response_201 = SubgraphResponse.from_dict(response.json())

    return response_201

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, SubgraphResponse]]:
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
  body: CreateSubgraphRequest,
) -> Response[Union[HTTPValidationError, SubgraphResponse]]:
  """Create Subgraph

   Create a new subgraph within a parent graph.

  **Requirements:**
  - Valid authentication
  - Parent graph must exist and be accessible to the user
  - User must have 'admin' permission on the parent graph
  - Parent graph tier must support subgraphs (Kuzu Large/XLarge or Neo4j Enterprise XLarge)
  - Must be within subgraph quota limits
  - Subgraph name must be unique within the parent graph

  **Returns:**
  - Created subgraph details including its unique ID
  - Subgraph ID format: `{parent_id}_{subgraph_name}` (e.g., kg1234567890abcdef_dev)

  **Usage:**
  - Subgraphs share parent's credit pool
  - Subgraph ID can be used in all standard `/v1/graphs/{graph_id}/*` endpoints
  - Permissions inherited from parent graph

  Args:
      graph_id (str):
      body (CreateSubgraphRequest): Request model for creating a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, SubgraphResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateSubgraphRequest,
) -> Optional[Union[HTTPValidationError, SubgraphResponse]]:
  """Create Subgraph

   Create a new subgraph within a parent graph.

  **Requirements:**
  - Valid authentication
  - Parent graph must exist and be accessible to the user
  - User must have 'admin' permission on the parent graph
  - Parent graph tier must support subgraphs (Kuzu Large/XLarge or Neo4j Enterprise XLarge)
  - Must be within subgraph quota limits
  - Subgraph name must be unique within the parent graph

  **Returns:**
  - Created subgraph details including its unique ID
  - Subgraph ID format: `{parent_id}_{subgraph_name}` (e.g., kg1234567890abcdef_dev)

  **Usage:**
  - Subgraphs share parent's credit pool
  - Subgraph ID can be used in all standard `/v1/graphs/{graph_id}/*` endpoints
  - Permissions inherited from parent graph

  Args:
      graph_id (str):
      body (CreateSubgraphRequest): Request model for creating a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, SubgraphResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateSubgraphRequest,
) -> Response[Union[HTTPValidationError, SubgraphResponse]]:
  """Create Subgraph

   Create a new subgraph within a parent graph.

  **Requirements:**
  - Valid authentication
  - Parent graph must exist and be accessible to the user
  - User must have 'admin' permission on the parent graph
  - Parent graph tier must support subgraphs (Kuzu Large/XLarge or Neo4j Enterprise XLarge)
  - Must be within subgraph quota limits
  - Subgraph name must be unique within the parent graph

  **Returns:**
  - Created subgraph details including its unique ID
  - Subgraph ID format: `{parent_id}_{subgraph_name}` (e.g., kg1234567890abcdef_dev)

  **Usage:**
  - Subgraphs share parent's credit pool
  - Subgraph ID can be used in all standard `/v1/graphs/{graph_id}/*` endpoints
  - Permissions inherited from parent graph

  Args:
      graph_id (str):
      body (CreateSubgraphRequest): Request model for creating a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, SubgraphResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateSubgraphRequest,
) -> Optional[Union[HTTPValidationError, SubgraphResponse]]:
  """Create Subgraph

   Create a new subgraph within a parent graph.

  **Requirements:**
  - Valid authentication
  - Parent graph must exist and be accessible to the user
  - User must have 'admin' permission on the parent graph
  - Parent graph tier must support subgraphs (Kuzu Large/XLarge or Neo4j Enterprise XLarge)
  - Must be within subgraph quota limits
  - Subgraph name must be unique within the parent graph

  **Returns:**
  - Created subgraph details including its unique ID
  - Subgraph ID format: `{parent_id}_{subgraph_name}` (e.g., kg1234567890abcdef_dev)

  **Usage:**
  - Subgraphs share parent's credit pool
  - Subgraph ID can be used in all standard `/v1/graphs/{graph_id}/*` endpoints
  - Permissions inherited from parent graph

  Args:
      graph_id (str):
      body (CreateSubgraphRequest): Request model for creating a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, SubgraphResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
