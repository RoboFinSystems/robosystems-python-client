from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_graph_schema_response_getgraphschema import (
  GetGraphSchemaResponseGetgraphschema,
)
from ...models.http_validation_error import HTTPValidationError
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
) -> Optional[Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = GetGraphSchemaResponseGetgraphschema.from_dict(response.json())

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

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]]:
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
) -> Response[Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]]:
  """Get Runtime Graph Schema

   Get runtime schema information for the specified graph database.

  This endpoint inspects the actual graph database structure and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties for each node type (limited to first 10 for performance)

  This shows what actually exists in the database right now - the runtime state.
  For the declared schema definition, use GET /schema/export instead.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]]
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
) -> Optional[Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]]:
  """Get Runtime Graph Schema

   Get runtime schema information for the specified graph database.

  This endpoint inspects the actual graph database structure and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties for each node type (limited to first 10 for performance)

  This shows what actually exists in the database right now - the runtime state.
  For the declared schema definition, use GET /schema/export instead.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]]:
  """Get Runtime Graph Schema

   Get runtime schema information for the specified graph database.

  This endpoint inspects the actual graph database structure and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties for each node type (limited to first 10 for performance)

  This shows what actually exists in the database right now - the runtime state.
  For the declared schema definition, use GET /schema/export instead.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]]
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
) -> Optional[Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]]:
  """Get Runtime Graph Schema

   Get runtime schema information for the specified graph database.

  This endpoint inspects the actual graph database structure and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties for each node type (limited to first 10 for performance)

  This shows what actually exists in the database right now - the runtime state.
  For the declared schema definition, use GET /schema/export instead.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GetGraphSchemaResponseGetgraphschema, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
