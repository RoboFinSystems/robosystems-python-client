from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_current_auth_user_response_getcurrentauthuser import (
  GetCurrentAuthUserResponseGetcurrentauthuser,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  *,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/auth/me",
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[
    ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError
  ]
]:
  if response.status_code == 200:
    response_200 = GetCurrentAuthUserResponseGetcurrentauthuser.from_dict(
      response.json()
    )

    return response_200
  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401
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
    ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError
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
    ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError
  ]
]:
  """Get Current User

   Get the currently authenticated user.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError]]
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
    ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError
  ]
]:
  """Get Current User

   Get the currently authenticated user.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError]
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
    ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError
  ]
]:
  """Get Current User

   Get the currently authenticated user.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError]]
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
    ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError
  ]
]:
  """Get Current User

   Get the currently authenticated user.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, GetCurrentAuthUserResponseGetcurrentauthuser, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      client=client,
      authorization=authorization,
    )
  ).parsed
