from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.database_health_response import DatabaseHealthResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/health",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DatabaseHealthResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = DatabaseHealthResponse.from_dict(response.json())

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
) -> Response[Union[Any, DatabaseHealthResponse, HTTPValidationError]]:
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
) -> Response[Union[Any, DatabaseHealthResponse, HTTPValidationError]]:
  """Database Health Check

   Get comprehensive health information for the graph database.

  Returns detailed health metrics including:
  - **Connection Status**: Database connectivity and responsiveness
  - **Performance Metrics**: Query execution times and throughput
  - **Resource Usage**: Memory and storage utilization
  - **Error Monitoring**: Recent error rates and patterns
  - **Uptime Statistics**: Service availability metrics

  Health indicators:
  - **Status**: healthy, degraded, or unhealthy
  - **Query Performance**: Average execution times
  - **Error Rates**: Recent failure percentages
  - **Resource Usage**: Memory and storage consumption
  - **Alerts**: Active warnings or issues

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Health metrics are specific to the requested graph/subgraph. Subgraphs share the
  same physical instance as their parent but have independent health indicators.

  This endpoint provides essential monitoring data for operational visibility.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, DatabaseHealthResponse, HTTPValidationError]]
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
) -> Optional[Union[Any, DatabaseHealthResponse, HTTPValidationError]]:
  """Database Health Check

   Get comprehensive health information for the graph database.

  Returns detailed health metrics including:
  - **Connection Status**: Database connectivity and responsiveness
  - **Performance Metrics**: Query execution times and throughput
  - **Resource Usage**: Memory and storage utilization
  - **Error Monitoring**: Recent error rates and patterns
  - **Uptime Statistics**: Service availability metrics

  Health indicators:
  - **Status**: healthy, degraded, or unhealthy
  - **Query Performance**: Average execution times
  - **Error Rates**: Recent failure percentages
  - **Resource Usage**: Memory and storage consumption
  - **Alerts**: Active warnings or issues

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Health metrics are specific to the requested graph/subgraph. Subgraphs share the
  same physical instance as their parent but have independent health indicators.

  This endpoint provides essential monitoring data for operational visibility.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, DatabaseHealthResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[Any, DatabaseHealthResponse, HTTPValidationError]]:
  """Database Health Check

   Get comprehensive health information for the graph database.

  Returns detailed health metrics including:
  - **Connection Status**: Database connectivity and responsiveness
  - **Performance Metrics**: Query execution times and throughput
  - **Resource Usage**: Memory and storage utilization
  - **Error Monitoring**: Recent error rates and patterns
  - **Uptime Statistics**: Service availability metrics

  Health indicators:
  - **Status**: healthy, degraded, or unhealthy
  - **Query Performance**: Average execution times
  - **Error Rates**: Recent failure percentages
  - **Resource Usage**: Memory and storage consumption
  - **Alerts**: Active warnings or issues

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Health metrics are specific to the requested graph/subgraph. Subgraphs share the
  same physical instance as their parent but have independent health indicators.

  This endpoint provides essential monitoring data for operational visibility.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, DatabaseHealthResponse, HTTPValidationError]]
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
) -> Optional[Union[Any, DatabaseHealthResponse, HTTPValidationError]]:
  """Database Health Check

   Get comprehensive health information for the graph database.

  Returns detailed health metrics including:
  - **Connection Status**: Database connectivity and responsiveness
  - **Performance Metrics**: Query execution times and throughput
  - **Resource Usage**: Memory and storage utilization
  - **Error Monitoring**: Recent error rates and patterns
  - **Uptime Statistics**: Service availability metrics

  Health indicators:
  - **Status**: healthy, degraded, or unhealthy
  - **Query Performance**: Average execution times
  - **Error Rates**: Recent failure percentages
  - **Resource Usage**: Memory and storage consumption
  - **Alerts**: Active warnings or issues

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Health metrics are specific to the requested graph/subgraph. Subgraphs share the
  same physical instance as their parent but have independent health indicators.

  This endpoint provides essential monitoring data for operational visibility.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, DatabaseHealthResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
