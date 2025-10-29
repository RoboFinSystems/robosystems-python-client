from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_storage_usage_response_getstorageusage import (
  GetStorageUsageResponseGetstorageusage,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  days: Union[Unset, int] = 30,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  params["days"] = days

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/credits/storage/usage",
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]
]:
  if response.status_code == 200:
    response_200 = GetStorageUsageResponseGetstorageusage.from_dict(response.json())

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
) -> Response[
  Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]
]:
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
  days: Union[Unset, int] = 30,
) -> Response[
  Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]
]:
  """Get Storage Usage

   Get storage usage history for a graph.

  Returns detailed storage usage information including:
  - Daily average storage consumption
  - Storage trends over time
  - Credit costs for storage
  - Current storage billing information

  This endpoint helps users understand their storage patterns
  and associated credit costs.

  Args:
      graph_id (str): Graph database identifier
      days (Union[Unset, int]): Number of days of history to return Default: 30.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    days=days,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  days: Union[Unset, int] = 30,
) -> Optional[
  Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]
]:
  """Get Storage Usage

   Get storage usage history for a graph.

  Returns detailed storage usage information including:
  - Daily average storage consumption
  - Storage trends over time
  - Credit costs for storage
  - Current storage billing information

  This endpoint helps users understand their storage patterns
  and associated credit costs.

  Args:
      graph_id (str): Graph database identifier
      days (Union[Unset, int]): Number of days of history to return Default: 30.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    days=days,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  days: Union[Unset, int] = 30,
) -> Response[
  Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]
]:
  """Get Storage Usage

   Get storage usage history for a graph.

  Returns detailed storage usage information including:
  - Daily average storage consumption
  - Storage trends over time
  - Credit costs for storage
  - Current storage billing information

  This endpoint helps users understand their storage patterns
  and associated credit costs.

  Args:
      graph_id (str): Graph database identifier
      days (Union[Unset, int]): Number of days of history to return Default: 30.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    days=days,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  days: Union[Unset, int] = 30,
) -> Optional[
  Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]
]:
  """Get Storage Usage

   Get storage usage history for a graph.

  Returns detailed storage usage information including:
  - Daily average storage consumption
  - Storage trends over time
  - Credit costs for storage
  - Current storage billing information

  This endpoint helps users understand their storage patterns
  and associated credit costs.

  Args:
      graph_id (str): Graph database identifier
      days (Union[Unset, int]): Number of days of history to return Default: 30.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetStorageUsageResponseGetstorageusage, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      days=days,
    )
  ).parsed
