from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.reset_password_validate_response import ResetPasswordValidateResponse
from ...types import UNSET, Response


def _get_kwargs(
  *,
  token: str,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  params["token"] = token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/auth/password/reset/validate",
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ResetPasswordValidateResponse | None:
  if response.status_code == 200:
    response_200 = ResetPasswordValidateResponse.from_dict(response.json())

    return response_200

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | ResetPasswordValidateResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient | Client,
  token: str,
) -> Response[HTTPValidationError | ResetPasswordValidateResponse]:
  """Validate Reset Token

   Check if a password reset token is valid without consuming it.

  Args:
      token (str): Password reset token

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | ResetPasswordValidateResponse]
  """

  kwargs = _get_kwargs(
    token=token,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient | Client,
  token: str,
) -> HTTPValidationError | ResetPasswordValidateResponse | None:
  """Validate Reset Token

   Check if a password reset token is valid without consuming it.

  Args:
      token (str): Password reset token

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | ResetPasswordValidateResponse
  """

  return sync_detailed(
    client=client,
    token=token,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient | Client,
  token: str,
) -> Response[HTTPValidationError | ResetPasswordValidateResponse]:
  """Validate Reset Token

   Check if a password reset token is valid without consuming it.

  Args:
      token (str): Password reset token

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | ResetPasswordValidateResponse]
  """

  kwargs = _get_kwargs(
    token=token,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient | Client,
  token: str,
) -> HTTPValidationError | ResetPasswordValidateResponse | None:
  """Validate Reset Token

   Check if a password reset token is valid without consuming it.

  Args:
      token (str): Password reset token

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | ResetPasswordValidateResponse
  """

  return (
    await asyncio_detailed(
      client=client,
      token=token,
    )
  ).parsed
