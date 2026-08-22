from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.sql_statement_request import SqlStatementRequest
from ...models.sql_statement_response import SqlStatementResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: SqlStatementRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/query/sql".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | SqlStatementResponse | None:
  if response.status_code == 200:
    response_200 = SqlStatementResponse.from_dict(response.json())

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

  if response.status_code == 408:
    response_408 = cast(Any, None)
    return response_408

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
) -> Response[Any | ErrorResponse | HTTPValidationError | SqlStatementResponse]:
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
  body: SqlStatementRequest,
) -> Response[Any | ErrorResponse | HTTPValidationError | SqlStatementResponse]:
  """Execute SQL Statement

   SQL over the graph's columnar tables (DuckDB) — a relational lens on the same graph-centric data,
  often ahead of the materialized graph. Use `?` placeholders with the `parameters` array to prevent
  injection. Read-only (SELECT only), 30s timeout, 10,000 row limit. Not available on shared
  repositories.

  Args:
      graph_id (str):
      body (SqlStatementRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | SqlStatementResponse]
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
  body: SqlStatementRequest,
) -> Any | ErrorResponse | HTTPValidationError | SqlStatementResponse | None:
  """Execute SQL Statement

   SQL over the graph's columnar tables (DuckDB) — a relational lens on the same graph-centric data,
  often ahead of the materialized graph. Use `?` placeholders with the `parameters` array to prevent
  injection. Read-only (SELECT only), 30s timeout, 10,000 row limit. Not available on shared
  repositories.

  Args:
      graph_id (str):
      body (SqlStatementRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | SqlStatementResponse
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
  body: SqlStatementRequest,
) -> Response[Any | ErrorResponse | HTTPValidationError | SqlStatementResponse]:
  """Execute SQL Statement

   SQL over the graph's columnar tables (DuckDB) — a relational lens on the same graph-centric data,
  often ahead of the materialized graph. Use `?` placeholders with the `parameters` array to prevent
  injection. Read-only (SELECT only), 30s timeout, 10,000 row limit. Not available on shared
  repositories.

  Args:
      graph_id (str):
      body (SqlStatementRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | SqlStatementResponse]
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
  body: SqlStatementRequest,
) -> Any | ErrorResponse | HTTPValidationError | SqlStatementResponse | None:
  """Execute SQL Statement

   SQL over the graph's columnar tables (DuckDB) — a relational lens on the same graph-centric data,
  often ahead of the materialized graph. Use `?` placeholders with the `parameters` array to prevent
  injection. Read-only (SELECT only), 30s timeout, 10,000 row limit. Not available on shared
  repositories.

  Args:
      graph_id (str):
      body (SqlStatementRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | SqlStatementResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
