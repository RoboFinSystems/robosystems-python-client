from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
  api_key_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "delete",
    "url": f"/v1/user/api-keys/{api_key_id}",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  if response.status_code == 200:
    response_200 = SuccessResponse.from_dict(response.json())

    return response_200

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  api_key_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  """Revoke API Key

   Revoke (deactivate) an API key.

  Args:
      api_key_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]
  """

  kwargs = _get_kwargs(
    api_key_id=api_key_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  api_key_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  """Revoke API Key

   Revoke (deactivate) an API key.

  Args:
      api_key_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, SuccessResponse]
  """

  return sync_detailed(
    api_key_id=api_key_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  api_key_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  """Revoke API Key

   Revoke (deactivate) an API key.

  Args:
      api_key_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]
  """

  kwargs = _get_kwargs(
    api_key_id=api_key_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  api_key_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, HTTPValidationError, SuccessResponse]]:
  """Revoke API Key

   Revoke (deactivate) an API key.

  Args:
      api_key_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, SuccessResponse]
  """

  return (
    await asyncio_detailed(
      api_key_id=api_key_id,
      client=client,
    )
  ).parsed
