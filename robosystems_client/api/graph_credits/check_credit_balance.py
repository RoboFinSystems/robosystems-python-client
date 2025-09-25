from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_credit_balance_response_checkcreditbalance import (
  CheckCreditBalanceResponseCheckcreditbalance,
)
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  operation_type: str,
  base_cost: Union[None, Unset, float, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  params["operation_type"] = operation_type

  json_base_cost: Union[None, Unset, float, str]
  if isinstance(base_cost, Unset):
    json_base_cost = UNSET
  else:
    json_base_cost = base_cost
  params["base_cost"] = json_base_cost

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/credits/balance/check",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[
    CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError
  ]
]:
  if response.status_code == 200:
    response_200 = CheckCreditBalanceResponseCheckcreditbalance.from_dict(
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
    CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError
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
  operation_type: str,
  base_cost: Union[None, Unset, float, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError
  ]
]:
  """Check Credit Balance

   Check if the graph has sufficient credits for a planned operation.

  This endpoint allows you to verify credit availability before performing
  an operation, helping prevent failed operations due to insufficient credits.

  The check considers:
  - Base operation cost
  - Graph tier multiplier
  - Current credit balance

  No credits are consumed for checking availability.

  Args:
      graph_id (str): Graph database identifier
      operation_type (str): Type of operation to check
      base_cost (Union[None, Unset, float, str]): Custom base cost (uses default if not
          provided)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    operation_type=operation_type,
    base_cost=base_cost,
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
  operation_type: str,
  base_cost: Union[None, Unset, float, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError
  ]
]:
  """Check Credit Balance

   Check if the graph has sufficient credits for a planned operation.

  This endpoint allows you to verify credit availability before performing
  an operation, helping prevent failed operations due to insufficient credits.

  The check considers:
  - Base operation cost
  - Graph tier multiplier
  - Current credit balance

  No credits are consumed for checking availability.

  Args:
      graph_id (str): Graph database identifier
      operation_type (str): Type of operation to check
      base_cost (Union[None, Unset, float, str]): Custom base cost (uses default if not
          provided)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    operation_type=operation_type,
    base_cost=base_cost,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  operation_type: str,
  base_cost: Union[None, Unset, float, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError
  ]
]:
  """Check Credit Balance

   Check if the graph has sufficient credits for a planned operation.

  This endpoint allows you to verify credit availability before performing
  an operation, helping prevent failed operations due to insufficient credits.

  The check considers:
  - Base operation cost
  - Graph tier multiplier
  - Current credit balance

  No credits are consumed for checking availability.

  Args:
      graph_id (str): Graph database identifier
      operation_type (str): Type of operation to check
      base_cost (Union[None, Unset, float, str]): Custom base cost (uses default if not
          provided)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    operation_type=operation_type,
    base_cost=base_cost,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  operation_type: str,
  base_cost: Union[None, Unset, float, str] = UNSET,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError
  ]
]:
  """Check Credit Balance

   Check if the graph has sufficient credits for a planned operation.

  This endpoint allows you to verify credit availability before performing
  an operation, helping prevent failed operations due to insufficient credits.

  The check considers:
  - Base operation cost
  - Graph tier multiplier
  - Current credit balance

  No credits are consumed for checking availability.

  Args:
      graph_id (str): Graph database identifier
      operation_type (str): Type of operation to check
      base_cost (Union[None, Unset, float, str]): Custom base cost (uses default if not
          provided)
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[CheckCreditBalanceResponseCheckcreditbalance, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      operation_type=operation_type,
      base_cost=base_cost,
      token=token,
      authorization=authorization,
    )
  ).parsed
