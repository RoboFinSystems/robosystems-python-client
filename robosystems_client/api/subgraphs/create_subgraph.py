from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_subgraph_request import CreateSubgraphRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.subgraph_response import SubgraphResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: CreateSubgraphRequest,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  cookies = {}
  if auth_token is not UNSET:
    cookies["auth-token"] = auth_token

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/{graph_id}/subgraphs",
    "cookies": cookies,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

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
  if response.status_code == 409:
    response_409 = cast(Any, None)
    return response_409
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
  *,
  client: AuthenticatedClient,
  body: CreateSubgraphRequest,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, SubgraphResponse]]:
  """Create New Subgraph

   Create a new subgraph database under an Enterprise or Premium parent graph.

  **Requirements:**
  - Parent graph must be Enterprise or Premium tier
  - User must have admin access to parent graph
  - Subgraph name must be unique within parent
  - Subgraph name must be alphanumeric (1-20 chars)

  **Subgraph Benefits:**
  - Shares parent's infrastructure (no additional cost)
  - Inherits parent's credit pool
  - Isolated database on same instance
  - Full Kuzu database capabilities

  **Use Cases:**
  - Separate environments (dev/staging/prod)
  - Department-specific data isolation
  - Multi-tenant applications
  - Testing and experimentation

  **Schema Inheritance:**
  - Subgraphs can use parent's schema or custom extensions
  - Extensions are additive only
  - Base schema always included

  **Limits:**
  - Enterprise: Maximum 10 subgraphs
  - Premium: Unlimited subgraphs
  - Standard: Not supported

  **Response includes:**
  - `graph_id`: Full subgraph identifier
  - `parent_graph_id`: Parent graph ID
  - `subgraph_name`: Short name within parent
  - `status`: Creation status

  Args:
      graph_id (str): Parent graph identifier
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):
      body (CreateSubgraphRequest): Request model for creating a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, SubgraphResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    authorization=authorization,
    auth_token=auth_token,
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
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, SubgraphResponse]]:
  """Create New Subgraph

   Create a new subgraph database under an Enterprise or Premium parent graph.

  **Requirements:**
  - Parent graph must be Enterprise or Premium tier
  - User must have admin access to parent graph
  - Subgraph name must be unique within parent
  - Subgraph name must be alphanumeric (1-20 chars)

  **Subgraph Benefits:**
  - Shares parent's infrastructure (no additional cost)
  - Inherits parent's credit pool
  - Isolated database on same instance
  - Full Kuzu database capabilities

  **Use Cases:**
  - Separate environments (dev/staging/prod)
  - Department-specific data isolation
  - Multi-tenant applications
  - Testing and experimentation

  **Schema Inheritance:**
  - Subgraphs can use parent's schema or custom extensions
  - Extensions are additive only
  - Base schema always included

  **Limits:**
  - Enterprise: Maximum 10 subgraphs
  - Premium: Unlimited subgraphs
  - Standard: Not supported

  **Response includes:**
  - `graph_id`: Full subgraph identifier
  - `parent_graph_id`: Parent graph ID
  - `subgraph_name`: Short name within parent
  - `status`: Creation status

  Args:
      graph_id (str): Parent graph identifier
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):
      body (CreateSubgraphRequest): Request model for creating a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, SubgraphResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
    authorization=authorization,
    auth_token=auth_token,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateSubgraphRequest,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, SubgraphResponse]]:
  """Create New Subgraph

   Create a new subgraph database under an Enterprise or Premium parent graph.

  **Requirements:**
  - Parent graph must be Enterprise or Premium tier
  - User must have admin access to parent graph
  - Subgraph name must be unique within parent
  - Subgraph name must be alphanumeric (1-20 chars)

  **Subgraph Benefits:**
  - Shares parent's infrastructure (no additional cost)
  - Inherits parent's credit pool
  - Isolated database on same instance
  - Full Kuzu database capabilities

  **Use Cases:**
  - Separate environments (dev/staging/prod)
  - Department-specific data isolation
  - Multi-tenant applications
  - Testing and experimentation

  **Schema Inheritance:**
  - Subgraphs can use parent's schema or custom extensions
  - Extensions are additive only
  - Base schema always included

  **Limits:**
  - Enterprise: Maximum 10 subgraphs
  - Premium: Unlimited subgraphs
  - Standard: Not supported

  **Response includes:**
  - `graph_id`: Full subgraph identifier
  - `parent_graph_id`: Parent graph ID
  - `subgraph_name`: Short name within parent
  - `status`: Creation status

  Args:
      graph_id (str): Parent graph identifier
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):
      body (CreateSubgraphRequest): Request model for creating a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, SubgraphResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    authorization=authorization,
    auth_token=auth_token,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateSubgraphRequest,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, SubgraphResponse]]:
  """Create New Subgraph

   Create a new subgraph database under an Enterprise or Premium parent graph.

  **Requirements:**
  - Parent graph must be Enterprise or Premium tier
  - User must have admin access to parent graph
  - Subgraph name must be unique within parent
  - Subgraph name must be alphanumeric (1-20 chars)

  **Subgraph Benefits:**
  - Shares parent's infrastructure (no additional cost)
  - Inherits parent's credit pool
  - Isolated database on same instance
  - Full Kuzu database capabilities

  **Use Cases:**
  - Separate environments (dev/staging/prod)
  - Department-specific data isolation
  - Multi-tenant applications
  - Testing and experimentation

  **Schema Inheritance:**
  - Subgraphs can use parent's schema or custom extensions
  - Extensions are additive only
  - Base schema always included

  **Limits:**
  - Enterprise: Maximum 10 subgraphs
  - Premium: Unlimited subgraphs
  - Standard: Not supported

  **Response includes:**
  - `graph_id`: Full subgraph identifier
  - `parent_graph_id`: Parent graph ID
  - `subgraph_name`: Short name within parent
  - `status`: Creation status

  Args:
      graph_id (str): Parent graph identifier
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):
      body (CreateSubgraphRequest): Request model for creating a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, SubgraphResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      authorization=authorization,
      auth_token=auth_token,
    )
  ).parsed
