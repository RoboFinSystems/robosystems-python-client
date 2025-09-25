from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_graph_schema_info_response_getgraphschemainfo import (
  GetGraphSchemaInfoResponseGetgraphschemainfo,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
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
    "url": f"/v1/graphs/{graph_id}/schema/info",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]
]:
  if response.status_code == 200:
    response_200 = GetGraphSchemaInfoResponseGetgraphschemainfo.from_dict(
      response.json()
    )

    return response_200
  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403
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
) -> Response[
  Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]
]:
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
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]
]:
  """Get Runtime Graph Schema Information

   Get runtime schema information for the specified graph database.

  This endpoint inspects the actual graph database structure and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties for each node type (limited to first 10 for performance)

  This is different from custom schema management - it shows what actually exists in the database,
  useful for understanding the current graph structure before writing queries.

  This operation is FREE - no credit consumption required.

  Args:
      graph_id (str): The graph database to get schema for
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]
]:
  """Get Runtime Graph Schema Information

   Get runtime schema information for the specified graph database.

  This endpoint inspects the actual graph database structure and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties for each node type (limited to first 10 for performance)

  This is different from custom schema management - it shows what actually exists in the database,
  useful for understanding the current graph structure before writing queries.

  This operation is FREE - no credit consumption required.

  Args:
      graph_id (str): The graph database to get schema for
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]
]:
  """Get Runtime Graph Schema Information

   Get runtime schema information for the specified graph database.

  This endpoint inspects the actual graph database structure and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties for each node type (limited to first 10 for performance)

  This is different from custom schema management - it shows what actually exists in the database,
  useful for understanding the current graph structure before writing queries.

  This operation is FREE - no credit consumption required.

  Args:
      graph_id (str): The graph database to get schema for
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]
]:
  """Get Runtime Graph Schema Information

   Get runtime schema information for the specified graph database.

  This endpoint inspects the actual graph database structure and returns:
  - **Node Labels**: All node types currently in the database
  - **Relationship Types**: All relationship types currently in the database
  - **Node Properties**: Properties for each node type (limited to first 10 for performance)

  This is different from custom schema management - it shows what actually exists in the database,
  useful for understanding the current graph structure before writing queries.

  This operation is FREE - no credit consumption required.

  Args:
      graph_id (str): The graph database to get schema for
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GetGraphSchemaInfoResponseGetgraphschemainfo, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      token=token,
      authorization=authorization,
    )
  ).parsed
