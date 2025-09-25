from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_graph_usage_details_response_getgraphusagedetails import (
  GetGraphUsageDetailsResponseGetgraphusagedetails,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  year: Union[None, Unset, int] = UNSET,
  month: Union[None, Unset, int] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_year: Union[None, Unset, int]
  if isinstance(year, Unset):
    json_year = UNSET
  else:
    json_year = year
  params["year"] = json_year

  json_month: Union[None, Unset, int]
  if isinstance(month, Unset):
    json_month = UNSET
  else:
    json_month = month
  params["month"] = json_month

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/billing/usage",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[
    ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError
  ]
]:
  if response.status_code == 200:
    response_200 = GetGraphUsageDetailsResponseGetgraphusagedetails.from_dict(
      response.json()
    )

    return response_200
  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400
  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403
  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404
  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
  Union[
    ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError
  ]
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
  year: Union[None, Unset, int] = UNSET,
  month: Union[None, Unset, int] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError
  ]
]:
  """Get Usage Details

   Get detailed usage metrics for the graph.

  Provides granular usage information including:
  - **Daily Credit Consumption**: Track credit usage patterns
  - **Storage Growth**: Monitor database size over time
  - **Operation Breakdown**: Credits by operation type
  - **Peak Usage Times**: Identify high-activity periods
  - **API Call Volumes**: Request counts and patterns

  Useful for:
  - Optimizing credit consumption
  - Capacity planning
  - Usage trend analysis
  - Cost optimization

  ℹ️ No credits are consumed for viewing usage details.

  Args:
      graph_id (str): Graph database identifier
      year (Union[None, Unset, int]): Year (defaults to current)
      month (Union[None, Unset, int]): Month (defaults to current)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    year=year,
    month=month,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  year: Union[None, Unset, int] = UNSET,
  month: Union[None, Unset, int] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError
  ]
]:
  """Get Usage Details

   Get detailed usage metrics for the graph.

  Provides granular usage information including:
  - **Daily Credit Consumption**: Track credit usage patterns
  - **Storage Growth**: Monitor database size over time
  - **Operation Breakdown**: Credits by operation type
  - **Peak Usage Times**: Identify high-activity periods
  - **API Call Volumes**: Request counts and patterns

  Useful for:
  - Optimizing credit consumption
  - Capacity planning
  - Usage trend analysis
  - Cost optimization

  ℹ️ No credits are consumed for viewing usage details.

  Args:
      graph_id (str): Graph database identifier
      year (Union[None, Unset, int]): Year (defaults to current)
      month (Union[None, Unset, int]): Month (defaults to current)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    year=year,
    month=month,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  year: Union[None, Unset, int] = UNSET,
  month: Union[None, Unset, int] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError
  ]
]:
  """Get Usage Details

   Get detailed usage metrics for the graph.

  Provides granular usage information including:
  - **Daily Credit Consumption**: Track credit usage patterns
  - **Storage Growth**: Monitor database size over time
  - **Operation Breakdown**: Credits by operation type
  - **Peak Usage Times**: Identify high-activity periods
  - **API Call Volumes**: Request counts and patterns

  Useful for:
  - Optimizing credit consumption
  - Capacity planning
  - Usage trend analysis
  - Cost optimization

  ℹ️ No credits are consumed for viewing usage details.

  Args:
      graph_id (str): Graph database identifier
      year (Union[None, Unset, int]): Year (defaults to current)
      month (Union[None, Unset, int]): Month (defaults to current)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    year=year,
    month=month,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  year: Union[None, Unset, int] = UNSET,
  month: Union[None, Unset, int] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError
  ]
]:
  """Get Usage Details

   Get detailed usage metrics for the graph.

  Provides granular usage information including:
  - **Daily Credit Consumption**: Track credit usage patterns
  - **Storage Growth**: Monitor database size over time
  - **Operation Breakdown**: Credits by operation type
  - **Peak Usage Times**: Identify high-activity periods
  - **API Call Volumes**: Request counts and patterns

  Useful for:
  - Optimizing credit consumption
  - Capacity planning
  - Usage trend analysis
  - Cost optimization

  ℹ️ No credits are consumed for viewing usage details.

  Args:
      graph_id (str): Graph database identifier
      year (Union[None, Unset, int]): Year (defaults to current)
      month (Union[None, Unset, int]): Month (defaults to current)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetGraphUsageDetailsResponseGetgraphusagedetails, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      year=year,
      month=month,
      token=token,
      authorization=authorization,
    )
  ).parsed
