from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_all_credit_summaries_response_getallcreditsummaries import (
  GetAllCreditSummariesResponseGetallcreditsummaries,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  *,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/user/credits",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[
    ErrorResponse,
    GetAllCreditSummariesResponseGetallcreditsummaries,
    HTTPValidationError,
  ]
]:
  if response.status_code == 200:
    response_200 = GetAllCreditSummariesResponseGetallcreditsummaries.from_dict(
      response.json()
    )

    return response_200
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
    GetAllCreditSummariesResponseGetallcreditsummaries,
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
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    ErrorResponse,
    GetAllCreditSummariesResponseGetallcreditsummaries,
    HTTPValidationError,
  ]
]:
  """Get All Credit Summaries

   Get credit summaries for all graphs owned by the user.

  This endpoint provides a consolidated view of credit usage across
  all graphs where the user has access, helping to monitor overall
  credit consumption and plan usage.

  No credits are consumed for viewing summaries.

  Args:
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetAllCreditSummariesResponseGetallcreditsummaries, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    ErrorResponse,
    GetAllCreditSummariesResponseGetallcreditsummaries,
    HTTPValidationError,
  ]
]:
  """Get All Credit Summaries

   Get credit summaries for all graphs owned by the user.

  This endpoint provides a consolidated view of credit usage across
  all graphs where the user has access, helping to monitor overall
  credit consumption and plan usage.

  No credits are consumed for viewing summaries.

  Args:
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetAllCreditSummariesResponseGetallcreditsummaries, HTTPValidationError]
  """

  return sync_detailed(
    client=client,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    ErrorResponse,
    GetAllCreditSummariesResponseGetallcreditsummaries,
    HTTPValidationError,
  ]
]:
  """Get All Credit Summaries

   Get credit summaries for all graphs owned by the user.

  This endpoint provides a consolidated view of credit usage across
  all graphs where the user has access, helping to monitor overall
  credit consumption and plan usage.

  No credits are consumed for viewing summaries.

  Args:
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetAllCreditSummariesResponseGetallcreditsummaries, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    ErrorResponse,
    GetAllCreditSummariesResponseGetallcreditsummaries,
    HTTPValidationError,
  ]
]:
  """Get All Credit Summaries

   Get credit summaries for all graphs owned by the user.

  This endpoint provides a consolidated view of credit usage across
  all graphs where the user has access, helping to monitor overall
  credit consumption and plan usage.

  No credits are consumed for viewing summaries.

  Args:
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetAllCreditSummariesResponseGetallcreditsummaries, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      client=client,
      token=token,
      authorization=authorization,
    )
  ).parsed
