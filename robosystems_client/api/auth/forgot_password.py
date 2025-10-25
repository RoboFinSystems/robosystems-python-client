from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.forgot_password_request import ForgotPasswordRequest
from ...models.forgot_password_response_forgotpassword import (
  ForgotPasswordResponseForgotpassword,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  *,
  body: ForgotPasswordRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/auth/password/forgot",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]
]:
  if response.status_code == 200:
    response_200 = ForgotPasswordResponseForgotpassword.from_dict(response.json())

    return response_200

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
  Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]
]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
  body: ForgotPasswordRequest,
) -> Response[
  Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]
]:
  """Forgot Password

   Request password reset email. Always returns success to prevent email enumeration.

  Args:
      body (ForgotPasswordRequest): Forgot password request model.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: Union[AuthenticatedClient, Client],
  body: ForgotPasswordRequest,
) -> Optional[
  Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]
]:
  """Forgot Password

   Request password reset email. Always returns success to prevent email enumeration.

  Args:
      body (ForgotPasswordRequest): Forgot password request model.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
  body: ForgotPasswordRequest,
) -> Response[
  Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]
]:
  """Forgot Password

   Request password reset email. Always returns success to prevent email enumeration.

  Args:
      body (ForgotPasswordRequest): Forgot password request model.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: Union[AuthenticatedClient, Client],
  body: ForgotPasswordRequest,
) -> Optional[
  Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]
]:
  """Forgot Password

   Request password reset email. Always returns success to prevent email enumeration.

  Args:
      body (ForgotPasswordRequest): Forgot password request model.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, ForgotPasswordResponseForgotpassword, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
