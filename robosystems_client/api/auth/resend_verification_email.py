from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.resend_verification_email_response_resendverificationemail import (
  ResendVerificationEmailResponseResendverificationemail,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/auth/email/resend",
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ResendVerificationEmailResponseResendverificationemail | None:
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

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ResendVerificationEmailResponseResendverificationemail]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | ResendVerificationEmailResponseResendverificationemail]:
  """Resend Email Verification

   Resend verification email to the authenticated user. Rate limited to 3 per hour.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | ResendVerificationEmailResponseResendverificationemail]
  """

  kwargs = _get_kwargs()

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient | Client,
) -> ErrorResponse | ResendVerificationEmailResponseResendverificationemail | None:
  """Resend Email Verification

   Resend verification email to the authenticated user. Rate limited to 3 per hour.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | ResendVerificationEmailResponseResendverificationemail
  """

  return sync_detailed(
    client=client,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | ResendVerificationEmailResponseResendverificationemail]:
  """Resend Email Verification

   Resend verification email to the authenticated user. Rate limited to 3 per hour.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | ResendVerificationEmailResponseResendverificationemail]
  """

  kwargs = _get_kwargs()

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient | Client,
) -> ErrorResponse | ResendVerificationEmailResponseResendverificationemail | None:
  """Resend Email Verification

   Resend verification email to the authenticated user. Rate limited to 3 per hour.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | ResendVerificationEmailResponseResendverificationemail
  """

  return (
    await asyncio_detailed(
      client=client,
    )
  ).parsed
