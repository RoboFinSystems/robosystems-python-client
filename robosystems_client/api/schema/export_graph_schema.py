from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.schema_export_response import SchemaExportResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  format_: Union[Unset, str] = "json",
  include_data_stats: Union[Unset, bool] = False,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  params["format"] = format_

  params["include_data_stats"] = include_data_stats

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/schema/export",
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, SchemaExportResponse]]:
  if response.status_code == 200:
    response_200 = SchemaExportResponse.from_dict(response.json())

    return response_200

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
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, SchemaExportResponse]]:
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
  format_: Union[Unset, str] = "json",
  include_data_stats: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, SchemaExportResponse]]:
  """Export Declared Graph Schema

   Export the declared schema definition of an existing graph.

  ## What This Returns

  This endpoint returns the **original schema definition** that was used to create the graph:
  - The schema as it was **declared** during graph creation
  - Complete node and relationship definitions
  - Property types and constraints
  - Schema metadata (name, version, type)

  ## Runtime vs Declared Schema

  **Use this endpoint** (`/schema/export`) when you need:
  - The original schema definition used to create the graph
  - Schema in a specific format (JSON, YAML, Cypher DDL)
  - Schema for documentation or version control
  - Schema to replicate in another graph

  **Use `/schema` instead** when you need:
  - What data is ACTUALLY in the database right now
  - What properties exist on real nodes (discovered from data)
  - Current runtime database structure for querying

  ## Export Formats

  ### JSON Format (`format=json`)
  Returns structured JSON with nodes, relationships, and properties.
  Best for programmatic access and API integration.

  ### YAML Format (`format=yaml`)
  Returns human-readable YAML with comments.
  Best for documentation and configuration management.

  ### Cypher DDL Format (`format=cypher`)
  Returns Cypher CREATE statements for recreating the schema.
  Best for database migration and replication.

  ## Data Statistics

  Set `include_data_stats=true` to include:
  - Node counts by label
  - Relationship counts by type
  - Total nodes and relationships

  This combines declared schema with runtime statistics.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      format_ (Union[Unset, str]): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (Union[Unset, bool]): Include statistics about actual data in the graph
          (node counts, relationship counts) Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, SchemaExportResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    format_=format_,
    include_data_stats=include_data_stats,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  format_: Union[Unset, str] = "json",
  include_data_stats: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, SchemaExportResponse]]:
  """Export Declared Graph Schema

   Export the declared schema definition of an existing graph.

  ## What This Returns

  This endpoint returns the **original schema definition** that was used to create the graph:
  - The schema as it was **declared** during graph creation
  - Complete node and relationship definitions
  - Property types and constraints
  - Schema metadata (name, version, type)

  ## Runtime vs Declared Schema

  **Use this endpoint** (`/schema/export`) when you need:
  - The original schema definition used to create the graph
  - Schema in a specific format (JSON, YAML, Cypher DDL)
  - Schema for documentation or version control
  - Schema to replicate in another graph

  **Use `/schema` instead** when you need:
  - What data is ACTUALLY in the database right now
  - What properties exist on real nodes (discovered from data)
  - Current runtime database structure for querying

  ## Export Formats

  ### JSON Format (`format=json`)
  Returns structured JSON with nodes, relationships, and properties.
  Best for programmatic access and API integration.

  ### YAML Format (`format=yaml`)
  Returns human-readable YAML with comments.
  Best for documentation and configuration management.

  ### Cypher DDL Format (`format=cypher`)
  Returns Cypher CREATE statements for recreating the schema.
  Best for database migration and replication.

  ## Data Statistics

  Set `include_data_stats=true` to include:
  - Node counts by label
  - Relationship counts by type
  - Total nodes and relationships

  This combines declared schema with runtime statistics.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      format_ (Union[Unset, str]): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (Union[Unset, bool]): Include statistics about actual data in the graph
          (node counts, relationship counts) Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, SchemaExportResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    format_=format_,
    include_data_stats=include_data_stats,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  format_: Union[Unset, str] = "json",
  include_data_stats: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, SchemaExportResponse]]:
  """Export Declared Graph Schema

   Export the declared schema definition of an existing graph.

  ## What This Returns

  This endpoint returns the **original schema definition** that was used to create the graph:
  - The schema as it was **declared** during graph creation
  - Complete node and relationship definitions
  - Property types and constraints
  - Schema metadata (name, version, type)

  ## Runtime vs Declared Schema

  **Use this endpoint** (`/schema/export`) when you need:
  - The original schema definition used to create the graph
  - Schema in a specific format (JSON, YAML, Cypher DDL)
  - Schema for documentation or version control
  - Schema to replicate in another graph

  **Use `/schema` instead** when you need:
  - What data is ACTUALLY in the database right now
  - What properties exist on real nodes (discovered from data)
  - Current runtime database structure for querying

  ## Export Formats

  ### JSON Format (`format=json`)
  Returns structured JSON with nodes, relationships, and properties.
  Best for programmatic access and API integration.

  ### YAML Format (`format=yaml`)
  Returns human-readable YAML with comments.
  Best for documentation and configuration management.

  ### Cypher DDL Format (`format=cypher`)
  Returns Cypher CREATE statements for recreating the schema.
  Best for database migration and replication.

  ## Data Statistics

  Set `include_data_stats=true` to include:
  - Node counts by label
  - Relationship counts by type
  - Total nodes and relationships

  This combines declared schema with runtime statistics.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      format_ (Union[Unset, str]): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (Union[Unset, bool]): Include statistics about actual data in the graph
          (node counts, relationship counts) Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, SchemaExportResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    format_=format_,
    include_data_stats=include_data_stats,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  format_: Union[Unset, str] = "json",
  include_data_stats: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, SchemaExportResponse]]:
  """Export Declared Graph Schema

   Export the declared schema definition of an existing graph.

  ## What This Returns

  This endpoint returns the **original schema definition** that was used to create the graph:
  - The schema as it was **declared** during graph creation
  - Complete node and relationship definitions
  - Property types and constraints
  - Schema metadata (name, version, type)

  ## Runtime vs Declared Schema

  **Use this endpoint** (`/schema/export`) when you need:
  - The original schema definition used to create the graph
  - Schema in a specific format (JSON, YAML, Cypher DDL)
  - Schema for documentation or version control
  - Schema to replicate in another graph

  **Use `/schema` instead** when you need:
  - What data is ACTUALLY in the database right now
  - What properties exist on real nodes (discovered from data)
  - Current runtime database structure for querying

  ## Export Formats

  ### JSON Format (`format=json`)
  Returns structured JSON with nodes, relationships, and properties.
  Best for programmatic access and API integration.

  ### YAML Format (`format=yaml`)
  Returns human-readable YAML with comments.
  Best for documentation and configuration management.

  ### Cypher DDL Format (`format=cypher`)
  Returns Cypher CREATE statements for recreating the schema.
  Best for database migration and replication.

  ## Data Statistics

  Set `include_data_stats=true` to include:
  - Node counts by label
  - Relationship counts by type
  - Total nodes and relationships

  This combines declared schema with runtime statistics.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      format_ (Union[Unset, str]): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (Union[Unset, bool]): Include statistics about actual data in the graph
          (node counts, relationship counts) Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, SchemaExportResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      format_=format_,
      include_data_stats=include_data_stats,
    )
  ).parsed
