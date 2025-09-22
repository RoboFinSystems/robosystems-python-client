from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.resend_verification_email_response_resendverificationemail import (
  ResendVerificationEmailResponseResendverificationemail,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  *,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/auth/email/resend",
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[
    ErrorResponse,
    HTTPValidationError,
    ResendVerificationEmailResponseResendverificationemail,
  ]
]:
  if response.status_code == 200:
    response_200 = ResendVerificationEmailResponseResendverificationemail.from_dict(
      response.json()
    )

    return response_200
  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400
  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429
  if response.status_code == 503:
    response_503 = ErrorResponse.from_dict(response.json())

    return response_503
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
    HTTPValidationError,
    ResendVerificationEmailResponseResendverificationemail,
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
  client: Union[AuthenticatedClient, Client],
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    ErrorResponse,
    HTTPValidationError,
    ResendVerificationEmailResponseResendverificationemail,
  ]
]:
  """Resend Email Verification

   Resend verification email to the authenticated user. Rate limited to 3 per hour.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, ResendVerificationEmailResponseResendverificationemail]]
  """

  kwargs = _get_kwargs(
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: Union[AuthenticatedClient, Client],
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    ErrorResponse,
    HTTPValidationError,
    ResendVerificationEmailResponseResendverificationemail,
  ]
]:
  """Resend Email Verification

   Resend verification email to the authenticated user. Rate limited to 3 per hour.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, ResendVerificationEmailResponseResendverificationemail]
  """

  return sync_detailed(
    client=client,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[
  Union[
    ErrorResponse,
    HTTPValidationError,
    ResendVerificationEmailResponseResendverificationemail,
  ]
]:
  """Resend Email Verification

   Resend verification email to the authenticated user. Rate limited to 3 per hour.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, ResendVerificationEmailResponseResendverificationemail]]
  """

  kwargs = _get_kwargs(
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: Union[AuthenticatedClient, Client],
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[
  Union[
    ErrorResponse,
    HTTPValidationError,
    ResendVerificationEmailResponseResendverificationemail,
  ]
]:
  """Resend Email Verification

   Resend verification email to the authenticated user. Rate limited to 3 per hour.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, ResendVerificationEmailResponseResendverificationemail]
  """

  return (
    await asyncio_detailed(
      client=client,
      authorization=authorization,
    )
  ).parsed
