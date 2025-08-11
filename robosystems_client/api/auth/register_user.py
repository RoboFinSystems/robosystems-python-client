from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_response import AuthResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.register_request import RegisterRequest
from ...types import Response


def _get_kwargs(
  *,
  body: RegisterRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/auth/register",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AuthResponse, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 201:
    response_201 = AuthResponse.from_dict(response.json())

    return response_201
  if response.status_code == 409:
    response_409 = ErrorResponse.from_dict(response.json())

    return response_409
  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400
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
) -> Response[Union[AuthResponse, ErrorResponse, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
  body: RegisterRequest,
) -> Response[Union[AuthResponse, ErrorResponse, HTTPValidationError]]:
  """Register New User

   Register a new user account with email and password. Security controls vary by environment: CAPTCHA
  and email verification are disabled in development for API testing, but required in production.

  Args:
      body (RegisterRequest): Registration request model.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AuthResponse, ErrorResponse, HTTPValidationError]]
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
  body: RegisterRequest,
) -> Optional[Union[AuthResponse, ErrorResponse, HTTPValidationError]]:
  """Register New User

   Register a new user account with email and password. Security controls vary by environment: CAPTCHA
  and email verification are disabled in development for API testing, but required in production.

  Args:
      body (RegisterRequest): Registration request model.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AuthResponse, ErrorResponse, HTTPValidationError]
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
  body: RegisterRequest,
) -> Response[Union[AuthResponse, ErrorResponse, HTTPValidationError]]:
  """Register New User

   Register a new user account with email and password. Security controls vary by environment: CAPTCHA
  and email verification are disabled in development for API testing, but required in production.

  Args:
      body (RegisterRequest): Registration request model.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AuthResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: Union[AuthenticatedClient, Client],
  body: RegisterRequest,
) -> Optional[Union[AuthResponse, ErrorResponse, HTTPValidationError]]:
  """Register New User

   Register a new user account with email and password. Security controls vary by environment: CAPTCHA
  and email verification are disabled in development for API testing, but required in production.

  Args:
      body (RegisterRequest): Registration request model.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AuthResponse, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
