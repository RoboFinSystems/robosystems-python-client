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
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  cookies = {}
  if auth_token is not UNSET:
    cookies["auth-token"] = auth_token

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/user/credits/summary",
    "cookies": cookies,
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
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
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
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetAllCreditSummariesResponseGetallcreditsummaries, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    authorization=authorization,
    auth_token=auth_token,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
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
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetAllCreditSummariesResponseGetallcreditsummaries, HTTPValidationError]
  """

  return sync_detailed(
    client=client,
    authorization=authorization,
    auth_token=auth_token,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
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
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetAllCreditSummariesResponseGetallcreditsummaries, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    authorization=authorization,
    auth_token=auth_token,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  authorization: Union[None, Unset, str] = UNSET,
  auth_token: Union[None, Unset, str] = UNSET,
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
      authorization (Union[None, Unset, str]):
      auth_token (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetAllCreditSummariesResponseGetallcreditsummaries, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      client=client,
      authorization=authorization,
      auth_token=auth_token,
    )
  ).parsed
