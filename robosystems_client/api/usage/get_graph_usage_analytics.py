from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.graph_usage_response import GraphUsageResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  time_range: Union[Unset, str] = "30d",
  include_storage: Union[Unset, bool] = True,
  include_credits: Union[Unset, bool] = True,
  include_performance: Union[Unset, bool] = False,
  include_events: Union[Unset, bool] = False,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  params["time_range"] = time_range

  params["include_storage"] = include_storage

  params["include_credits"] = include_credits

  params["include_performance"] = include_performance

  params["include_events"] = include_events

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/analytics/usage",
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = GraphUsageResponse.from_dict(response.json())

    return response_200

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

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
) -> Response[Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]]:
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
  time_range: Union[Unset, str] = "30d",
  include_storage: Union[Unset, bool] = True,
  include_credits: Union[Unset, bool] = True,
  include_performance: Union[Unset, bool] = False,
  include_events: Union[Unset, bool] = False,
) -> Response[Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]]:
  """Get Graph Usage Analytics

   Get comprehensive usage analytics tracked by the GraphUsage model.

  Provides temporal usage patterns including:
  - **Storage Analytics**: GB-hours for billing, breakdown by type (files, tables, graphs, subgraphs)
  - **Credit Analytics**: Consumption patterns, operation breakdown, cached vs billable
  - **Performance Insights**: Operation stats, slow queries, performance scoring
  - **Recent Events**: Latest usage events with full details

  Time ranges available:
  - `24h` - Last 24 hours (hourly breakdown)
  - `7d` - Last 7 days (daily breakdown)
  - `30d` - Last 30 days (daily breakdown)
  - `current_month` - Current billing month
  - `last_month` - Previous billing month

  Include options:
  - `storage` - Storage usage summary (GB-hours, averages, peaks)
  - `credits` - Credit consumption analytics
  - `performance` - Performance insights and optimization opportunities
  - `events` - Recent usage events (last 50)

  Useful for:
  - Billing and cost analysis
  - Capacity planning
  - Performance optimization
  - Usage trend analysis

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      time_range (Union[Unset, str]): Time range: 24h, 7d, 30d, current_month, last_month
          Default: '30d'.
      include_storage (Union[Unset, bool]): Include storage usage summary Default: True.
      include_credits (Union[Unset, bool]): Include credit consumption summary Default: True.
      include_performance (Union[Unset, bool]): Include performance insights (may be slower)
          Default: False.
      include_events (Union[Unset, bool]): Include recent usage events Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    time_range=time_range,
    include_storage=include_storage,
    include_credits=include_credits,
    include_performance=include_performance,
    include_events=include_events,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  time_range: Union[Unset, str] = "30d",
  include_storage: Union[Unset, bool] = True,
  include_credits: Union[Unset, bool] = True,
  include_performance: Union[Unset, bool] = False,
  include_events: Union[Unset, bool] = False,
) -> Optional[Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]]:
  """Get Graph Usage Analytics

   Get comprehensive usage analytics tracked by the GraphUsage model.

  Provides temporal usage patterns including:
  - **Storage Analytics**: GB-hours for billing, breakdown by type (files, tables, graphs, subgraphs)
  - **Credit Analytics**: Consumption patterns, operation breakdown, cached vs billable
  - **Performance Insights**: Operation stats, slow queries, performance scoring
  - **Recent Events**: Latest usage events with full details

  Time ranges available:
  - `24h` - Last 24 hours (hourly breakdown)
  - `7d` - Last 7 days (daily breakdown)
  - `30d` - Last 30 days (daily breakdown)
  - `current_month` - Current billing month
  - `last_month` - Previous billing month

  Include options:
  - `storage` - Storage usage summary (GB-hours, averages, peaks)
  - `credits` - Credit consumption analytics
  - `performance` - Performance insights and optimization opportunities
  - `events` - Recent usage events (last 50)

  Useful for:
  - Billing and cost analysis
  - Capacity planning
  - Performance optimization
  - Usage trend analysis

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      time_range (Union[Unset, str]): Time range: 24h, 7d, 30d, current_month, last_month
          Default: '30d'.
      include_storage (Union[Unset, bool]): Include storage usage summary Default: True.
      include_credits (Union[Unset, bool]): Include credit consumption summary Default: True.
      include_performance (Union[Unset, bool]): Include performance insights (may be slower)
          Default: False.
      include_events (Union[Unset, bool]): Include recent usage events Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    time_range=time_range,
    include_storage=include_storage,
    include_credits=include_credits,
    include_performance=include_performance,
    include_events=include_events,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  time_range: Union[Unset, str] = "30d",
  include_storage: Union[Unset, bool] = True,
  include_credits: Union[Unset, bool] = True,
  include_performance: Union[Unset, bool] = False,
  include_events: Union[Unset, bool] = False,
) -> Response[Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]]:
  """Get Graph Usage Analytics

   Get comprehensive usage analytics tracked by the GraphUsage model.

  Provides temporal usage patterns including:
  - **Storage Analytics**: GB-hours for billing, breakdown by type (files, tables, graphs, subgraphs)
  - **Credit Analytics**: Consumption patterns, operation breakdown, cached vs billable
  - **Performance Insights**: Operation stats, slow queries, performance scoring
  - **Recent Events**: Latest usage events with full details

  Time ranges available:
  - `24h` - Last 24 hours (hourly breakdown)
  - `7d` - Last 7 days (daily breakdown)
  - `30d` - Last 30 days (daily breakdown)
  - `current_month` - Current billing month
  - `last_month` - Previous billing month

  Include options:
  - `storage` - Storage usage summary (GB-hours, averages, peaks)
  - `credits` - Credit consumption analytics
  - `performance` - Performance insights and optimization opportunities
  - `events` - Recent usage events (last 50)

  Useful for:
  - Billing and cost analysis
  - Capacity planning
  - Performance optimization
  - Usage trend analysis

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      time_range (Union[Unset, str]): Time range: 24h, 7d, 30d, current_month, last_month
          Default: '30d'.
      include_storage (Union[Unset, bool]): Include storage usage summary Default: True.
      include_credits (Union[Unset, bool]): Include credit consumption summary Default: True.
      include_performance (Union[Unset, bool]): Include performance insights (may be slower)
          Default: False.
      include_events (Union[Unset, bool]): Include recent usage events Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    time_range=time_range,
    include_storage=include_storage,
    include_credits=include_credits,
    include_performance=include_performance,
    include_events=include_events,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  time_range: Union[Unset, str] = "30d",
  include_storage: Union[Unset, bool] = True,
  include_credits: Union[Unset, bool] = True,
  include_performance: Union[Unset, bool] = False,
  include_events: Union[Unset, bool] = False,
) -> Optional[Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]]:
  """Get Graph Usage Analytics

   Get comprehensive usage analytics tracked by the GraphUsage model.

  Provides temporal usage patterns including:
  - **Storage Analytics**: GB-hours for billing, breakdown by type (files, tables, graphs, subgraphs)
  - **Credit Analytics**: Consumption patterns, operation breakdown, cached vs billable
  - **Performance Insights**: Operation stats, slow queries, performance scoring
  - **Recent Events**: Latest usage events with full details

  Time ranges available:
  - `24h` - Last 24 hours (hourly breakdown)
  - `7d` - Last 7 days (daily breakdown)
  - `30d` - Last 30 days (daily breakdown)
  - `current_month` - Current billing month
  - `last_month` - Previous billing month

  Include options:
  - `storage` - Storage usage summary (GB-hours, averages, peaks)
  - `credits` - Credit consumption analytics
  - `performance` - Performance insights and optimization opportunities
  - `events` - Recent usage events (last 50)

  Useful for:
  - Billing and cost analysis
  - Capacity planning
  - Performance optimization
  - Usage trend analysis

  Note:
  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
      time_range (Union[Unset, str]): Time range: 24h, 7d, 30d, current_month, last_month
          Default: '30d'.
      include_storage (Union[Unset, bool]): Include storage usage summary Default: True.
      include_credits (Union[Unset, bool]): Include credit consumption summary Default: True.
      include_performance (Union[Unset, bool]): Include performance insights (may be slower)
          Default: False.
      include_events (Union[Unset, bool]): Include recent usage events Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GraphUsageResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      time_range=time_range,
      include_storage=include_storage,
      include_credits=include_credits,
      include_performance=include_performance,
      include_events=include_events,
    )
  ).parsed
