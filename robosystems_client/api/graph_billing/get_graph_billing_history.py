from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_graph_billing_history_response_getgraphbillinghistory import (
  GetGraphBillingHistoryResponseGetgraphbillinghistory,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  months: Union[Unset, int] = 6,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  params["months"] = months

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/billing/history",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[
    ErrorResponse,
    GetGraphBillingHistoryResponseGetgraphbillinghistory,
    HTTPValidationError,
  ]
]:
  if response.status_code == 200:
    response_200 = GetGraphBillingHistoryResponseGetgraphbillinghistory.from_dict(
      response.json()
    )

    return response_200
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
    ErrorResponse,
    GetGraphBillingHistoryResponseGetgraphbillinghistory,
    HTTPValidationError,
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
  months: Union[Unset, int] = 6,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    ErrorResponse,
    GetGraphBillingHistoryResponseGetgraphbillinghistory,
    HTTPValidationError,
  ]
]:
  """Get Billing History

   Get billing history for the graph.

  Returns a chronological list of monthly bills, perfect for:
  - Tracking spending trends over time
  - Identifying usage patterns
  - Budget forecasting
  - Financial reporting

  Each month includes:
  - Credit usage and overages
  - Storage charges
  - Total charges
  - Usage metrics

  ℹ️ No credits are consumed for viewing billing history.

  Args:
      graph_id (str): Graph database identifier
      months (Union[Unset, int]): Number of months to retrieve (1-24) Default: 6.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetGraphBillingHistoryResponseGetgraphbillinghistory, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    months=months,
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
  months: Union[Unset, int] = 6,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    ErrorResponse,
    GetGraphBillingHistoryResponseGetgraphbillinghistory,
    HTTPValidationError,
  ]
]:
  """Get Billing History

   Get billing history for the graph.

  Returns a chronological list of monthly bills, perfect for:
  - Tracking spending trends over time
  - Identifying usage patterns
  - Budget forecasting
  - Financial reporting

  Each month includes:
  - Credit usage and overages
  - Storage charges
  - Total charges
  - Usage metrics

  ℹ️ No credits are consumed for viewing billing history.

  Args:
      graph_id (str): Graph database identifier
      months (Union[Unset, int]): Number of months to retrieve (1-24) Default: 6.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetGraphBillingHistoryResponseGetgraphbillinghistory, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    months=months,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  months: Union[Unset, int] = 6,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    ErrorResponse,
    GetGraphBillingHistoryResponseGetgraphbillinghistory,
    HTTPValidationError,
  ]
]:
  """Get Billing History

   Get billing history for the graph.

  Returns a chronological list of monthly bills, perfect for:
  - Tracking spending trends over time
  - Identifying usage patterns
  - Budget forecasting
  - Financial reporting

  Each month includes:
  - Credit usage and overages
  - Storage charges
  - Total charges
  - Usage metrics

  ℹ️ No credits are consumed for viewing billing history.

  Args:
      graph_id (str): Graph database identifier
      months (Union[Unset, int]): Number of months to retrieve (1-24) Default: 6.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetGraphBillingHistoryResponseGetgraphbillinghistory, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    months=months,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  months: Union[Unset, int] = 6,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    ErrorResponse,
    GetGraphBillingHistoryResponseGetgraphbillinghistory,
    HTTPValidationError,
  ]
]:
  """Get Billing History

   Get billing history for the graph.

  Returns a chronological list of monthly bills, perfect for:
  - Tracking spending trends over time
  - Identifying usage patterns
  - Budget forecasting
  - Financial reporting

  Each month includes:
  - Credit usage and overages
  - Storage charges
  - Total charges
  - Usage metrics

  ℹ️ No credits are consumed for viewing billing history.

  Args:
      graph_id (str): Graph database identifier
      months (Union[Unset, int]): Number of months to retrieve (1-24) Default: 6.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetGraphBillingHistoryResponseGetgraphbillinghistory, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      months=months,
      token=token,
      authorization=authorization,
    )
  ).parsed
