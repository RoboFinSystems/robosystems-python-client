from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.schema_export_response import SchemaExportResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  format_: str | Unset = "json",
  include_data_stats: bool | Unset = False,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  params["format"] = format_

  params["include_data_stats"] = include_data_stats

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/schema/export".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SchemaExportResponse | None:
  if response.status_code == 200:
    response_200 = SchemaExportResponse.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | SchemaExportResponse]:
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
  format_: str | Unset = "json",
  include_data_stats: bool | Unset = False,
) -> Response[ErrorResponse | HTTPValidationError | SchemaExportResponse]:
  """Export Declared Graph Schema

   Returns the original schema definition from graph creation, not the runtime state. Set
  `include_data_stats=true` to add live node/relationship counts. Use `/schema` to inspect what's
  actually in the database.

  Args:
      graph_id (str):
      format_ (str | Unset): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (bool | Unset): Include statistics about actual data in the graph (node
          counts, relationship counts) Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SchemaExportResponse]
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
  format_: str | Unset = "json",
  include_data_stats: bool | Unset = False,
) -> ErrorResponse | HTTPValidationError | SchemaExportResponse | None:
  """Export Declared Graph Schema

   Returns the original schema definition from graph creation, not the runtime state. Set
  `include_data_stats=true` to add live node/relationship counts. Use `/schema` to inspect what's
  actually in the database.

  Args:
      graph_id (str):
      format_ (str | Unset): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (bool | Unset): Include statistics about actual data in the graph (node
          counts, relationship counts) Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SchemaExportResponse
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
  format_: str | Unset = "json",
  include_data_stats: bool | Unset = False,
) -> Response[ErrorResponse | HTTPValidationError | SchemaExportResponse]:
  """Export Declared Graph Schema

   Returns the original schema definition from graph creation, not the runtime state. Set
  `include_data_stats=true` to add live node/relationship counts. Use `/schema` to inspect what's
  actually in the database.

  Args:
      graph_id (str):
      format_ (str | Unset): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (bool | Unset): Include statistics about actual data in the graph (node
          counts, relationship counts) Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SchemaExportResponse]
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
  format_: str | Unset = "json",
  include_data_stats: bool | Unset = False,
) -> ErrorResponse | HTTPValidationError | SchemaExportResponse | None:
  """Export Declared Graph Schema

   Returns the original schema definition from graph creation, not the runtime state. Set
  `include_data_stats=true` to add live node/relationship counts. Use `/schema` to inspect what's
  actually in the database.

  Args:
      graph_id (str):
      format_ (str | Unset): Export format: json, yaml, or cypher Default: 'json'.
      include_data_stats (bool | Unset): Include statistics about actual data in the graph (node
          counts, relationship counts) Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SchemaExportResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      format_=format_,
      include_data_stats=include_data_stats,
    )
  ).parsed
