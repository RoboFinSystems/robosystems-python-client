from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.graph_metrics_response import GraphMetricsResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/analytics",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = GraphMetricsResponse.from_dict(response.json())

    return response_200

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]]:
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
) -> Response[Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]]:
  """Get Graph Metrics

   Get comprehensive metrics for the graph database.

  Provides detailed analytics including:
  - **Node Statistics**: Counts by type (Entity, Report, Account, Transaction)
  - **Relationship Metrics**: Connection counts and patterns
  - **Data Quality**: Completeness scores and validation results
  - **Performance Metrics**: Query response times and database health
  - **Storage Analytics**: Database size and growth trends

  This data helps with:
  - Monitoring data completeness
  - Identifying data quality issues
  - Capacity planning
  - Performance optimization

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]]
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
) -> Optional[Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]]:
  """Get Graph Metrics

   Get comprehensive metrics for the graph database.

  Provides detailed analytics including:
  - **Node Statistics**: Counts by type (Entity, Report, Account, Transaction)
  - **Relationship Metrics**: Connection counts and patterns
  - **Data Quality**: Completeness scores and validation results
  - **Performance Metrics**: Query response times and database health
  - **Storage Analytics**: Database size and growth trends

  This data helps with:
  - Monitoring data completeness
  - Identifying data quality issues
  - Capacity planning
  - Performance optimization

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]]:
  """Get Graph Metrics

   Get comprehensive metrics for the graph database.

  Provides detailed analytics including:
  - **Node Statistics**: Counts by type (Entity, Report, Account, Transaction)
  - **Relationship Metrics**: Connection counts and patterns
  - **Data Quality**: Completeness scores and validation results
  - **Performance Metrics**: Query response times and database health
  - **Storage Analytics**: Database size and growth trends

  This data helps with:
  - Monitoring data completeness
  - Identifying data quality issues
  - Capacity planning
  - Performance optimization

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]]
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
) -> Optional[Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]]:
  """Get Graph Metrics

   Get comprehensive metrics for the graph database.

  Provides detailed analytics including:
  - **Node Statistics**: Counts by type (Entity, Report, Account, Transaction)
  - **Relationship Metrics**: Connection counts and patterns
  - **Data Quality**: Completeness scores and validation results
  - **Performance Metrics**: Query response times and database health
  - **Storage Analytics**: Database size and growth trends

  This data helps with:
  - Monitoring data completeness
  - Identifying data quality issues
  - Capacity planning
  - Performance optimization

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GraphMetricsResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
