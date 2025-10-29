from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_graph_monthly_bill_response_getgraphmonthlybill import (
  GetGraphMonthlyBillResponseGetgraphmonthlybill,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  year: int,
  month: int,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/billing/history/{year}/{month}",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[
    ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError
  ]
]:
  if response.status_code == 200:
    response_200 = GetGraphMonthlyBillResponseGetgraphmonthlybill.from_dict(
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
  Union[
    ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError
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
  year: int,
  month: int,
  *,
  client: AuthenticatedClient,
) -> Response[
  Union[
    ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError
  ]
]:
  """Get Monthly Bill

   Get billing details for a specific month.

  Retrieve historical billing information for any previous month.
  Useful for:
  - Reconciling past charges
  - Tracking usage trends
  - Expense reporting
  - Budget analysis

  Returns the same detailed breakdown as the current bill endpoint.

  ℹ️ No credits are consumed for viewing billing history.

  Args:
      graph_id (str):
      year (int): Year (2024-2030)
      month (int): Month (1-12)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    year=year,
    month=month,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  year: int,
  month: int,
  *,
  client: AuthenticatedClient,
) -> Optional[
  Union[
    ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError
  ]
]:
  """Get Monthly Bill

   Get billing details for a specific month.

  Retrieve historical billing information for any previous month.
  Useful for:
  - Reconciling past charges
  - Tracking usage trends
  - Expense reporting
  - Budget analysis

  Returns the same detailed breakdown as the current bill endpoint.

  ℹ️ No credits are consumed for viewing billing history.

  Args:
      graph_id (str):
      year (int): Year (2024-2030)
      month (int): Month (1-12)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    year=year,
    month=month,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  year: int,
  month: int,
  *,
  client: AuthenticatedClient,
) -> Response[
  Union[
    ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError
  ]
]:
  """Get Monthly Bill

   Get billing details for a specific month.

  Retrieve historical billing information for any previous month.
  Useful for:
  - Reconciling past charges
  - Tracking usage trends
  - Expense reporting
  - Budget analysis

  Returns the same detailed breakdown as the current bill endpoint.

  ℹ️ No credits are consumed for viewing billing history.

  Args:
      graph_id (str):
      year (int): Year (2024-2030)
      month (int): Month (1-12)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    year=year,
    month=month,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  year: int,
  month: int,
  *,
  client: AuthenticatedClient,
) -> Optional[
  Union[
    ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError
  ]
]:
  """Get Monthly Bill

   Get billing details for a specific month.

  Retrieve historical billing information for any previous month.
  Useful for:
  - Reconciling past charges
  - Tracking usage trends
  - Expense reporting
  - Budget analysis

  Returns the same detailed breakdown as the current bill endpoint.

  ℹ️ No credits are consumed for viewing billing history.

  Args:
      graph_id (str):
      year (int): Year (2024-2030)
      month (int): Month (1-12)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetGraphMonthlyBillResponseGetgraphmonthlybill, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      year=year,
      month=month,
      client=client,
    )
  ).parsed
