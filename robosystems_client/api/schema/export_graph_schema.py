from http import HTTPStatus
from typing import Any, Optional, Union

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
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  params["format"] = format_

  params["include_data_stats"] = include_data_stats

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/schema/export",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, SchemaExportResponse]]:
  if response.status_code == 200:
    response_200 = SchemaExportResponse.from_dict(response.json())

    return response_200
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, SchemaExportResponse]]:
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
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, SchemaExportResponse]]:
  """Export Graph Schema

   Export the schema of an existing graph in JSON, YAML, or Cypher format

  Args:
      graph_id (str): The graph ID to export schema from
      format_ (Union[Unset, str]): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (Union[Unset, bool]): Include statistics about actual data in the graph
          Default: False.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, SchemaExportResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    format_=format_,
    include_data_stats=include_data_stats,
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
  format_: Union[Unset, str] = "json",
  include_data_stats: Union[Unset, bool] = False,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, SchemaExportResponse]]:
  """Export Graph Schema

   Export the schema of an existing graph in JSON, YAML, or Cypher format

  Args:
      graph_id (str): The graph ID to export schema from
      format_ (Union[Unset, str]): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (Union[Unset, bool]): Include statistics about actual data in the graph
          Default: False.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, SchemaExportResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    format_=format_,
    include_data_stats=include_data_stats,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  format_: Union[Unset, str] = "json",
  include_data_stats: Union[Unset, bool] = False,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, SchemaExportResponse]]:
  """Export Graph Schema

   Export the schema of an existing graph in JSON, YAML, or Cypher format

  Args:
      graph_id (str): The graph ID to export schema from
      format_ (Union[Unset, str]): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (Union[Unset, bool]): Include statistics about actual data in the graph
          Default: False.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, SchemaExportResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    format_=format_,
    include_data_stats=include_data_stats,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  format_: Union[Unset, str] = "json",
  include_data_stats: Union[Unset, bool] = False,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, SchemaExportResponse]]:
  """Export Graph Schema

   Export the schema of an existing graph in JSON, YAML, or Cypher format

  Args:
      graph_id (str): The graph ID to export schema from
      format_ (Union[Unset, str]): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (Union[Unset, bool]): Include statistics about actual data in the graph
          Default: False.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, SchemaExportResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      format_=format_,
      include_data_stats=include_data_stats,
      token=token,
      authorization=authorization,
    )
  ).parsed
