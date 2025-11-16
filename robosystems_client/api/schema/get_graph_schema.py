from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.schema_info_response import SchemaInfoResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/schema",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, SchemaInfoResponse]]:
  if response.status_code == 200:
    response_200 = SchemaInfoResponse.from_dict(response.json())

    return response_200

  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if response.status_code == 504:
    response_504 = cast(Any, None)
    return response_504

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, SchemaInfoResponse]]:
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
) -> Response[Union[Any, HTTPValidationError, SchemaInfoResponse]]:
  """Get Runtime Graph Schema

   Get runtime schema information for the specified graph database.

  ## What This Returns

  This endpoint inspects the **actual current state** of the graph database and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties discovered from actual data (up to 10 properties per node type)

  ## Runtime vs Declared Schema

  **Use this endpoint** (`/schema`) when you need to know:
  - What data is ACTUALLY in the database right now
  - What properties exist on real nodes
  - What relationships have been created
  - Current database structure for querying

  **Use `/schema/export` instead** when you need:
  - The original schema definition used to create the graph
  - Schema in a specific format (JSON, YAML, Cypher DDL)
  - Schema for documentation or version control
  - Schema to replicate in another graph

  ## Example Use Cases

  - **Building queries**: See what node labels and properties exist to write accurate Cypher
  - **Data exploration**: Discover what's in an unfamiliar graph
  - **Schema drift detection**: Compare runtime vs declared schema
  - **API integration**: Dynamically adapt to current graph structure

  ## Performance Note

  Property discovery is limited to 10 properties per node type for performance.
  For complete schema definitions, use `/schema/export`.

  ## Subgraph Support

  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has independent schema and data. The returned schema reflects
  only the specified graph/subgraph's actual structure.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, SchemaInfoResponse]]
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
) -> Optional[Union[Any, HTTPValidationError, SchemaInfoResponse]]:
  """Get Runtime Graph Schema

   Get runtime schema information for the specified graph database.

  ## What This Returns

  This endpoint inspects the **actual current state** of the graph database and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties discovered from actual data (up to 10 properties per node type)

  ## Runtime vs Declared Schema

  **Use this endpoint** (`/schema`) when you need to know:
  - What data is ACTUALLY in the database right now
  - What properties exist on real nodes
  - What relationships have been created
  - Current database structure for querying

  **Use `/schema/export` instead** when you need:
  - The original schema definition used to create the graph
  - Schema in a specific format (JSON, YAML, Cypher DDL)
  - Schema for documentation or version control
  - Schema to replicate in another graph

  ## Example Use Cases

  - **Building queries**: See what node labels and properties exist to write accurate Cypher
  - **Data exploration**: Discover what's in an unfamiliar graph
  - **Schema drift detection**: Compare runtime vs declared schema
  - **API integration**: Dynamically adapt to current graph structure

  ## Performance Note

  Property discovery is limited to 10 properties per node type for performance.
  For complete schema definitions, use `/schema/export`.

  ## Subgraph Support

  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has independent schema and data. The returned schema reflects
  only the specified graph/subgraph's actual structure.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, SchemaInfoResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError, SchemaInfoResponse]]:
  """Get Runtime Graph Schema

   Get runtime schema information for the specified graph database.

  ## What This Returns

  This endpoint inspects the **actual current state** of the graph database and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties discovered from actual data (up to 10 properties per node type)

  ## Runtime vs Declared Schema

  **Use this endpoint** (`/schema`) when you need to know:
  - What data is ACTUALLY in the database right now
  - What properties exist on real nodes
  - What relationships have been created
  - Current database structure for querying

  **Use `/schema/export` instead** when you need:
  - The original schema definition used to create the graph
  - Schema in a specific format (JSON, YAML, Cypher DDL)
  - Schema for documentation or version control
  - Schema to replicate in another graph

  ## Example Use Cases

  - **Building queries**: See what node labels and properties exist to write accurate Cypher
  - **Data exploration**: Discover what's in an unfamiliar graph
  - **Schema drift detection**: Compare runtime vs declared schema
  - **API integration**: Dynamically adapt to current graph structure

  ## Performance Note

  Property discovery is limited to 10 properties per node type for performance.
  For complete schema definitions, use `/schema/export`.

  ## Subgraph Support

  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has independent schema and data. The returned schema reflects
  only the specified graph/subgraph's actual structure.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, SchemaInfoResponse]]
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
) -> Optional[Union[Any, HTTPValidationError, SchemaInfoResponse]]:
  """Get Runtime Graph Schema

   Get runtime schema information for the specified graph database.

  ## What This Returns

  This endpoint inspects the **actual current state** of the graph database and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties discovered from actual data (up to 10 properties per node type)

  ## Runtime vs Declared Schema

  **Use this endpoint** (`/schema`) when you need to know:
  - What data is ACTUALLY in the database right now
  - What properties exist on real nodes
  - What relationships have been created
  - Current database structure for querying

  **Use `/schema/export` instead** when you need:
  - The original schema definition used to create the graph
  - Schema in a specific format (JSON, YAML, Cypher DDL)
  - Schema for documentation or version control
  - Schema to replicate in another graph

  ## Example Use Cases

  - **Building queries**: See what node labels and properties exist to write accurate Cypher
  - **Data exploration**: Discover what's in an unfamiliar graph
  - **Schema drift detection**: Compare runtime vs declared schema
  - **API integration**: Dynamically adapt to current graph structure

  ## Performance Note

  Property discovery is limited to 10 properties per node type for performance.
  For complete schema definitions, use `/schema/export`.

  ## Subgraph Support

  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Each subgraph has independent schema and data. The returned schema reflects
  only the specified graph/subgraph's actual structure.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, SchemaInfoResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
