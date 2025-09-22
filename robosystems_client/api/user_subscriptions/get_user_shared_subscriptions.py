from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_subscriptions_response import UserSubscriptionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  *,
  active_only: Union[Unset, bool] = True,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  params["active_only"] = active_only

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/user/subscriptions/shared-repositories",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, UserSubscriptionsResponse]]:
  if response.status_code == 200:
    response_200 = UserSubscriptionsResponse.from_dict(response.json())

    return response_200
  if response.status_code == 401:
    response_401 = cast(Any, None)
    return response_401
  if response.status_code == 500:
    response_500 = cast(Any, None)
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
) -> Response[Union[Any, HTTPValidationError, UserSubscriptionsResponse]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  active_only: Union[Unset, bool] = True,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, UserSubscriptionsResponse]]:
  """Get User Subscriptions

   Retrieve user's current shared repository subscriptions with detailed information

  Args:
      active_only (Union[Unset, bool]): Only return active subscriptions Default: True.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, UserSubscriptionsResponse]]
  """

  kwargs = _get_kwargs(
    active_only=active_only,
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
  active_only: Union[Unset, bool] = True,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, UserSubscriptionsResponse]]:
  """Get User Subscriptions

   Retrieve user's current shared repository subscriptions with detailed information

  Args:
      active_only (Union[Unset, bool]): Only return active subscriptions Default: True.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, UserSubscriptionsResponse]
  """

  return sync_detailed(
    client=client,
    active_only=active_only,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  active_only: Union[Unset, bool] = True,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, UserSubscriptionsResponse]]:
  """Get User Subscriptions

   Retrieve user's current shared repository subscriptions with detailed information

  Args:
      active_only (Union[Unset, bool]): Only return active subscriptions Default: True.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, UserSubscriptionsResponse]]
  """

  kwargs = _get_kwargs(
    active_only=active_only,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  active_only: Union[Unset, bool] = True,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, UserSubscriptionsResponse]]:
  """Get User Subscriptions

   Retrieve user's current shared repository subscriptions with detailed information

  Args:
      active_only (Union[Unset, bool]): Only return active subscriptions Default: True.
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, UserSubscriptionsResponse]
  """

  return (
    await asyncio_detailed(
      client=client,
      active_only=active_only,
      token=token,
      authorization=authorization,
    )
  ).parsed
