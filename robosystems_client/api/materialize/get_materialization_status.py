from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.materialize_status_response import MaterializeStatusResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/materialize/status".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse | None:
  if response.status_code == 200:
    response_200 = MaterializeStatusResponse.from_dict(response.json())

    return response_200

  if response.status_code == 401:
    response_401 = cast(Any, None)
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

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse]:
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
) -> Response[Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse]:
  """Get Materialization Status

   Get current materialization status for the graph.

  Shows whether the graph is stale (DuckDB has changes not yet in graph database),
  when it was last materialized, and how long since last materialization.

  **Status Information:**
  - Whether graph is currently stale
  - Reason for staleness if applicable
  - When graph became stale
  - When graph was last materialized
  - Total materialization count
  - Hours since last materialization

  **Use Cases:**
  - Decide if materialization is needed
  - Monitor graph freshness
  - Track materialization history
  - Understand data pipeline state

  **Important Notes:**
  - Stale graph means DuckDB has changes not in graph
  - Graph becomes stale after file deletions
  - Materialization clears staleness
  - Status retrieval is included - no credit consumption

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse]
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
) -> Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse | None:
  """Get Materialization Status

   Get current materialization status for the graph.

  Shows whether the graph is stale (DuckDB has changes not yet in graph database),
  when it was last materialized, and how long since last materialization.

  **Status Information:**
  - Whether graph is currently stale
  - Reason for staleness if applicable
  - When graph became stale
  - When graph was last materialized
  - Total materialization count
  - Hours since last materialization

  **Use Cases:**
  - Decide if materialization is needed
  - Monitor graph freshness
  - Track materialization history
  - Understand data pipeline state

  **Important Notes:**
  - Stale graph means DuckDB has changes not in graph
  - Graph becomes stale after file deletions
  - Materialization clears staleness
  - Status retrieval is included - no credit consumption

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse]:
  """Get Materialization Status

   Get current materialization status for the graph.

  Shows whether the graph is stale (DuckDB has changes not yet in graph database),
  when it was last materialized, and how long since last materialization.

  **Status Information:**
  - Whether graph is currently stale
  - Reason for staleness if applicable
  - When graph became stale
  - When graph was last materialized
  - Total materialization count
  - Hours since last materialization

  **Use Cases:**
  - Decide if materialization is needed
  - Monitor graph freshness
  - Track materialization history
  - Understand data pipeline state

  **Important Notes:**
  - Stale graph means DuckDB has changes not in graph
  - Graph becomes stale after file deletions
  - Materialization clears staleness
  - Status retrieval is included - no credit consumption

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse]
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
) -> Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse | None:
  """Get Materialization Status

   Get current materialization status for the graph.

  Shows whether the graph is stale (DuckDB has changes not yet in graph database),
  when it was last materialized, and how long since last materialization.

  **Status Information:**
  - Whether graph is currently stale
  - Reason for staleness if applicable
  - When graph became stale
  - When graph was last materialized
  - Total materialization count
  - Hours since last materialization

  **Use Cases:**
  - Decide if materialization is needed
  - Monitor graph freshness
  - Track materialization history
  - Understand data pipeline state

  **Important Notes:**
  - Stale graph means DuckDB has changes not in graph
  - Graph becomes stale after file deletions
  - Materialization clears staleness
  - Status retrieval is included - no credit consumption

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | MaterializeStatusResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
