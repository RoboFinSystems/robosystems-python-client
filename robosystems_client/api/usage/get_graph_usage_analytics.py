from http import HTTPStatus
from typing import Any
from urllib.parse import quote

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
  time_range: str | Unset = "30d",
  include_storage: bool | Unset = True,
  include_credits: bool | Unset = True,
  include_performance: bool | Unset = False,
  include_events: bool | Unset = False,
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
    "url": "/v1/graphs/{graph_id}/analytics/usage".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GraphUsageResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = GraphUsageResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GraphUsageResponse | HTTPValidationError]:
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
  time_range: str | Unset = "30d",
  include_storage: bool | Unset = True,
  include_credits: bool | Unset = True,
  include_performance: bool | Unset = False,
  include_events: bool | Unset = False,
) -> Response[ErrorResponse | GraphUsageResponse | HTTPValidationError]:
  """Get Graph Usage Analytics

   Time ranges: 24h, 7d, 30d, current_month, last_month. Toggle storage, credits, performance, and
  events sections via query params.

  Args:
      graph_id (str):
      time_range (str | Unset): Time range: 24h, 7d, 30d, current_month, last_month Default:
          '30d'.
      include_storage (bool | Unset): Include storage usage summary Default: True.
      include_credits (bool | Unset): Include credit consumption summary Default: True.
      include_performance (bool | Unset): Include performance insights (may be slower) Default:
          False.
      include_events (bool | Unset): Include recent usage events Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GraphUsageResponse | HTTPValidationError]
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
  time_range: str | Unset = "30d",
  include_storage: bool | Unset = True,
  include_credits: bool | Unset = True,
  include_performance: bool | Unset = False,
  include_events: bool | Unset = False,
) -> ErrorResponse | GraphUsageResponse | HTTPValidationError | None:
  """Get Graph Usage Analytics

   Time ranges: 24h, 7d, 30d, current_month, last_month. Toggle storage, credits, performance, and
  events sections via query params.

  Args:
      graph_id (str):
      time_range (str | Unset): Time range: 24h, 7d, 30d, current_month, last_month Default:
          '30d'.
      include_storage (bool | Unset): Include storage usage summary Default: True.
      include_credits (bool | Unset): Include credit consumption summary Default: True.
      include_performance (bool | Unset): Include performance insights (may be slower) Default:
          False.
      include_events (bool | Unset): Include recent usage events Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | GraphUsageResponse | HTTPValidationError
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
  time_range: str | Unset = "30d",
  include_storage: bool | Unset = True,
  include_credits: bool | Unset = True,
  include_performance: bool | Unset = False,
  include_events: bool | Unset = False,
) -> Response[ErrorResponse | GraphUsageResponse | HTTPValidationError]:
  """Get Graph Usage Analytics

   Time ranges: 24h, 7d, 30d, current_month, last_month. Toggle storage, credits, performance, and
  events sections via query params.

  Args:
      graph_id (str):
      time_range (str | Unset): Time range: 24h, 7d, 30d, current_month, last_month Default:
          '30d'.
      include_storage (bool | Unset): Include storage usage summary Default: True.
      include_credits (bool | Unset): Include credit consumption summary Default: True.
      include_performance (bool | Unset): Include performance insights (may be slower) Default:
          False.
      include_events (bool | Unset): Include recent usage events Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GraphUsageResponse | HTTPValidationError]
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
  time_range: str | Unset = "30d",
  include_storage: bool | Unset = True,
  include_credits: bool | Unset = True,
  include_performance: bool | Unset = False,
  include_events: bool | Unset = False,
) -> ErrorResponse | GraphUsageResponse | HTTPValidationError | None:
  """Get Graph Usage Analytics

   Time ranges: 24h, 7d, 30d, current_month, last_month. Toggle storage, credits, performance, and
  events sections via query params.

  Args:
      graph_id (str):
      time_range (str | Unset): Time range: 24h, 7d, 30d, current_month, last_month Default:
          '30d'.
      include_storage (bool | Unset): Include storage usage summary Default: True.
      include_credits (bool | Unset): Include credit consumption summary Default: True.
      include_performance (bool | Unset): Include performance insights (may be slower) Default:
          False.
      include_events (bool | Unset): Include recent usage events Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | GraphUsageResponse | HTTPValidationError
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
