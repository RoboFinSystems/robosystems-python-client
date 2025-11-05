from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_graph_tiers_response import AvailableGraphTiersResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  *,
  include_disabled: Union[Unset, bool] = False,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  params["include_disabled"] = include_disabled

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/tiers",
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AvailableGraphTiersResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = AvailableGraphTiersResponse.from_dict(response.json())

    return response_200

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
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, AvailableGraphTiersResponse, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  include_disabled: Union[Unset, bool] = False,
) -> Response[Union[Any, AvailableGraphTiersResponse, HTTPValidationError]]:
  """Get Available Graph Tiers

   List all available graph database tier configurations.

  This endpoint provides comprehensive technical specifications for each available
  graph database tier, including instance types, resource limits, and features.

  **Tier Information:**
  Each tier includes:
  - Technical specifications (instance type, memory, storage)
  - Resource limits (subgraphs, credits, rate limits)
  - Feature list with capabilities
  - Availability status

  **Available Tiers:**
  - **kuzu-standard**: Multi-tenant entry-level tier
  - **kuzu-large**: Dedicated professional tier with subgraph support
  - **kuzu-xlarge**: Enterprise tier with maximum resources
  - **neo4j-community-large**: Neo4j Community Edition (optional, if enabled)
  - **neo4j-enterprise-xlarge**: Neo4j Enterprise Edition (optional, if enabled)

  **Use Cases:**
  - Display tier options in graph creation UI
  - Show technical specifications for tier selection
  - Validate tier availability before graph creation
  - Display feature comparisons

  **Note:**
  Tier listing is included - no credit consumption required.

  Args:
      include_disabled (Union[Unset, bool]):  Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, AvailableGraphTiersResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    include_disabled=include_disabled,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
  include_disabled: Union[Unset, bool] = False,
) -> Optional[Union[Any, AvailableGraphTiersResponse, HTTPValidationError]]:
  """Get Available Graph Tiers

   List all available graph database tier configurations.

  This endpoint provides comprehensive technical specifications for each available
  graph database tier, including instance types, resource limits, and features.

  **Tier Information:**
  Each tier includes:
  - Technical specifications (instance type, memory, storage)
  - Resource limits (subgraphs, credits, rate limits)
  - Feature list with capabilities
  - Availability status

  **Available Tiers:**
  - **kuzu-standard**: Multi-tenant entry-level tier
  - **kuzu-large**: Dedicated professional tier with subgraph support
  - **kuzu-xlarge**: Enterprise tier with maximum resources
  - **neo4j-community-large**: Neo4j Community Edition (optional, if enabled)
  - **neo4j-enterprise-xlarge**: Neo4j Enterprise Edition (optional, if enabled)

  **Use Cases:**
  - Display tier options in graph creation UI
  - Show technical specifications for tier selection
  - Validate tier availability before graph creation
  - Display feature comparisons

  **Note:**
  Tier listing is included - no credit consumption required.

  Args:
      include_disabled (Union[Unset, bool]):  Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, AvailableGraphTiersResponse, HTTPValidationError]
  """

  return sync_detailed(
    client=client,
    include_disabled=include_disabled,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  include_disabled: Union[Unset, bool] = False,
) -> Response[Union[Any, AvailableGraphTiersResponse, HTTPValidationError]]:
  """Get Available Graph Tiers

   List all available graph database tier configurations.

  This endpoint provides comprehensive technical specifications for each available
  graph database tier, including instance types, resource limits, and features.

  **Tier Information:**
  Each tier includes:
  - Technical specifications (instance type, memory, storage)
  - Resource limits (subgraphs, credits, rate limits)
  - Feature list with capabilities
  - Availability status

  **Available Tiers:**
  - **kuzu-standard**: Multi-tenant entry-level tier
  - **kuzu-large**: Dedicated professional tier with subgraph support
  - **kuzu-xlarge**: Enterprise tier with maximum resources
  - **neo4j-community-large**: Neo4j Community Edition (optional, if enabled)
  - **neo4j-enterprise-xlarge**: Neo4j Enterprise Edition (optional, if enabled)

  **Use Cases:**
  - Display tier options in graph creation UI
  - Show technical specifications for tier selection
  - Validate tier availability before graph creation
  - Display feature comparisons

  **Note:**
  Tier listing is included - no credit consumption required.

  Args:
      include_disabled (Union[Unset, bool]):  Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, AvailableGraphTiersResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    include_disabled=include_disabled,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  include_disabled: Union[Unset, bool] = False,
) -> Optional[Union[Any, AvailableGraphTiersResponse, HTTPValidationError]]:
  """Get Available Graph Tiers

   List all available graph database tier configurations.

  This endpoint provides comprehensive technical specifications for each available
  graph database tier, including instance types, resource limits, and features.

  **Tier Information:**
  Each tier includes:
  - Technical specifications (instance type, memory, storage)
  - Resource limits (subgraphs, credits, rate limits)
  - Feature list with capabilities
  - Availability status

  **Available Tiers:**
  - **kuzu-standard**: Multi-tenant entry-level tier
  - **kuzu-large**: Dedicated professional tier with subgraph support
  - **kuzu-xlarge**: Enterprise tier with maximum resources
  - **neo4j-community-large**: Neo4j Community Edition (optional, if enabled)
  - **neo4j-enterprise-xlarge**: Neo4j Enterprise Edition (optional, if enabled)

  **Use Cases:**
  - Display tier options in graph creation UI
  - Show technical specifications for tier selection
  - Validate tier availability before graph creation
  - Display feature comparisons

  **Note:**
  Tier listing is included - no credit consumption required.

  Args:
      include_disabled (Union[Unset, bool]):  Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, AvailableGraphTiersResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      client=client,
      include_disabled=include_disabled,
    )
  ).parsed
