from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_analytics_response import UserAnalyticsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  *,
  include_api_stats: Union[Unset, bool] = True,
  include_recent_activity: Union[Unset, bool] = True,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  params["include_api_stats"] = include_api_stats

  params["include_recent_activity"] = include_recent_activity

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/user/analytics/detailed",
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, UserAnalyticsResponse]]:
  if response.status_code == 200:
    response_200 = UserAnalyticsResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, UserAnalyticsResponse]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  include_api_stats: Union[Unset, bool] = True,
  include_recent_activity: Union[Unset, bool] = True,
) -> Response[Union[HTTPValidationError, UserAnalyticsResponse]]:
  """Get Detailed User Analytics

   Get comprehensive analytics for the current user including API usage and recent activity.

  Args:
      include_api_stats (Union[Unset, bool]): Include API usage statistics Default: True.
      include_recent_activity (Union[Unset, bool]): Include recent activity Default: True.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, UserAnalyticsResponse]]
  """

  kwargs = _get_kwargs(
    include_api_stats=include_api_stats,
    include_recent_activity=include_recent_activity,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
  include_api_stats: Union[Unset, bool] = True,
  include_recent_activity: Union[Unset, bool] = True,
) -> Optional[Union[HTTPValidationError, UserAnalyticsResponse]]:
  """Get Detailed User Analytics

   Get comprehensive analytics for the current user including API usage and recent activity.

  Args:
      include_api_stats (Union[Unset, bool]): Include API usage statistics Default: True.
      include_recent_activity (Union[Unset, bool]): Include recent activity Default: True.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, UserAnalyticsResponse]
  """

  return sync_detailed(
    client=client,
    include_api_stats=include_api_stats,
    include_recent_activity=include_recent_activity,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  include_api_stats: Union[Unset, bool] = True,
  include_recent_activity: Union[Unset, bool] = True,
) -> Response[Union[HTTPValidationError, UserAnalyticsResponse]]:
  """Get Detailed User Analytics

   Get comprehensive analytics for the current user including API usage and recent activity.

  Args:
      include_api_stats (Union[Unset, bool]): Include API usage statistics Default: True.
      include_recent_activity (Union[Unset, bool]): Include recent activity Default: True.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, UserAnalyticsResponse]]
  """

  kwargs = _get_kwargs(
    include_api_stats=include_api_stats,
    include_recent_activity=include_recent_activity,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  include_api_stats: Union[Unset, bool] = True,
  include_recent_activity: Union[Unset, bool] = True,
) -> Optional[Union[HTTPValidationError, UserAnalyticsResponse]]:
  """Get Detailed User Analytics

   Get comprehensive analytics for the current user including API usage and recent activity.

  Args:
      include_api_stats (Union[Unset, bool]): Include API usage statistics Default: True.
      include_recent_activity (Union[Unset, bool]): Include recent activity Default: True.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, UserAnalyticsResponse]
  """

  return (
    await asyncio_detailed(
      client=client,
      include_api_stats=include_api_stats,
      include_recent_activity=include_recent_activity,
    )
  ).parsed
