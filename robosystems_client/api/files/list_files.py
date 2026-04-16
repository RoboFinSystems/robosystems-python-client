from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_table_files_response import ListTableFilesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  json_table_name: None | str | Unset
  if isinstance(table_name, Unset):
    json_table_name = UNSET
  else:
    json_table_name = table_name
  params["table_name"] = json_table_name

  json_status: None | str | Unset
  if isinstance(status, Unset):
    json_status = UNSET
  else:
    json_status = status
  params["status"] = json_status

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/files".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | ListTableFilesResponse | None:
  if response.status_code == 200:
    response_200 = ListTableFilesResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ListTableFilesResponse]:
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
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListTableFilesResponse]:
  """List Files in Graph

   Filter by `table_name` or upload `status`. Files are graph-scoped resources with S3 → DuckDB → Graph
  lifecycle tracking.

  Args:
      graph_id (str):
      table_name (None | str | Unset): Filter by table name (optional)
      status (None | str | Unset): Filter by upload status (optional)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | ListTableFilesResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    table_name=table_name,
    status=status,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListTableFilesResponse | None:
  """List Files in Graph

   Filter by `table_name` or upload `status`. Files are graph-scoped resources with S3 → DuckDB → Graph
  lifecycle tracking.

  Args:
      graph_id (str):
      table_name (None | str | Unset): Filter by table name (optional)
      status (None | str | Unset): Filter by upload status (optional)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | ListTableFilesResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    table_name=table_name,
    status=status,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListTableFilesResponse]:
  """List Files in Graph

   Filter by `table_name` or upload `status`. Files are graph-scoped resources with S3 → DuckDB → Graph
  lifecycle tracking.

  Args:
      graph_id (str):
      table_name (None | str | Unset): Filter by table name (optional)
      status (None | str | Unset): Filter by upload status (optional)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | ListTableFilesResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    table_name=table_name,
    status=status,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  table_name: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListTableFilesResponse | None:
  """List Files in Graph

   Filter by `table_name` or upload `status`. Files are graph-scoped resources with S3 → DuckDB → Graph
  lifecycle tracking.

  Args:
      graph_id (str):
      table_name (None | str | Unset): Filter by table name (optional)
      status (None | str | Unset): Filter by upload status (optional)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | ListTableFilesResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      table_name=table_name,
      status=status,
    )
  ).parsed
