from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.repository_credits_response import RepositoryCreditsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  repository: str,
  *,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/user/subscriptions/shared-repositories/credits/{repository}",
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, RepositoryCreditsResponse]]:
  if response.status_code == 200:
    response_200 = RepositoryCreditsResponse.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, RepositoryCreditsResponse]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  repository: str,
  *,
  client: AuthenticatedClient,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, RepositoryCreditsResponse]]:
  """Get Repository Credits

   Get credit balance for a specific shared repository

  Args:
      repository (str):
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, RepositoryCreditsResponse]]
  """

  kwargs = _get_kwargs(
    repository=repository,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  repository: str,
  *,
  client: AuthenticatedClient,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, RepositoryCreditsResponse]]:
  """Get Repository Credits

   Get credit balance for a specific shared repository

  Args:
      repository (str):
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, RepositoryCreditsResponse]
  """

  return sync_detailed(
    repository=repository,
    client=client,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  repository: str,
  *,
  client: AuthenticatedClient,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, RepositoryCreditsResponse]]:
  """Get Repository Credits

   Get credit balance for a specific shared repository

  Args:
      repository (str):
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, HTTPValidationError, RepositoryCreditsResponse]]
  """

  kwargs = _get_kwargs(
    repository=repository,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  repository: str,
  *,
  client: AuthenticatedClient,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, RepositoryCreditsResponse]]:
  """Get Repository Credits

   Get credit balance for a specific shared repository

  Args:
      repository (str):
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, HTTPValidationError, RepositoryCreditsResponse]
  """

  return (
    await asyncio_detailed(
      repository=repository,
      client=client,
      authorization=authorization,
    )
  ).parsed
