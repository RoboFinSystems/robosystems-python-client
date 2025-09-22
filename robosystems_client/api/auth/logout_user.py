from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.logout_user_response_logoutuser import LogoutUserResponseLogoutuser
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
    "url": "/v1/auth/logout",
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, LogoutUserResponseLogoutuser]]:
  if response.status_code == 200:
    response_200 = LogoutUserResponseLogoutuser.from_dict(response.json())

    return response_200
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, LogoutUserResponseLogoutuser]]:
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
) -> Response[Union[HTTPValidationError, LogoutUserResponseLogoutuser]]:
  """User Logout

   Logout user and invalidate session.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, LogoutUserResponseLogoutuser]]
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
) -> Optional[Union[HTTPValidationError, LogoutUserResponseLogoutuser]]:
  """User Logout

   Logout user and invalidate session.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, LogoutUserResponseLogoutuser]
  """

  return sync_detailed(
    client=client,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, LogoutUserResponseLogoutuser]]:
  """User Logout

   Logout user and invalidate session.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, LogoutUserResponseLogoutuser]]
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
) -> Optional[Union[HTTPValidationError, LogoutUserResponseLogoutuser]]:
  """User Logout

   Logout user and invalidate session.

  Args:
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, LogoutUserResponseLogoutuser]
  """

  return (
    await asyncio_detailed(
      client=client,
      authorization=authorization,
    )
  ).parsed
