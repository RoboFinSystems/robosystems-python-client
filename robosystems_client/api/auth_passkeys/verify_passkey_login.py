from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_response import AuthResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.passkey_login_verify_request import PasskeyLoginVerifyRequest
from ...types import Response


def _get_kwargs(
  *,
  body: PasskeyLoginVerifyRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/auth/passkeys/login/verify",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuthResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = AuthResponse.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuthResponse | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient | Client,
  body: PasskeyLoginVerifyRequest,
) -> Response[AuthResponse | ErrorResponse | HTTPValidationError]:
  """Passwordless Login Verify

   Complete a passwordless login. A user-verified passkey assertion is two factors in one gesture.

  Args:
      body (PasskeyLoginVerifyRequest): Complete a passwordless login with a discoverable-
          credential assertion.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[AuthResponse | ErrorResponse | HTTPValidationError]
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
  client: AuthenticatedClient | Client,
  body: PasskeyLoginVerifyRequest,
) -> AuthResponse | ErrorResponse | HTTPValidationError | None:
  """Passwordless Login Verify

   Complete a passwordless login. A user-verified passkey assertion is two factors in one gesture.

  Args:
      body (PasskeyLoginVerifyRequest): Complete a passwordless login with a discoverable-
          credential assertion.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      AuthResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient | Client,
  body: PasskeyLoginVerifyRequest,
) -> Response[AuthResponse | ErrorResponse | HTTPValidationError]:
  """Passwordless Login Verify

   Complete a passwordless login. A user-verified passkey assertion is two factors in one gesture.

  Args:
      body (PasskeyLoginVerifyRequest): Complete a passwordless login with a discoverable-
          credential assertion.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[AuthResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient | Client,
  body: PasskeyLoginVerifyRequest,
) -> AuthResponse | ErrorResponse | HTTPValidationError | None:
  """Passwordless Login Verify

   Complete a passwordless login. A user-verified passkey assertion is two factors in one gesture.

  Args:
      body (PasskeyLoginVerifyRequest): Complete a passwordless login with a discoverable-
          credential assertion.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      AuthResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
