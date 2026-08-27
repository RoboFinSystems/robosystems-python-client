from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
  grant_id: str,
) -> dict[str, Any]:

  _kwargs: dict[str, Any] = {
    "method": "delete",
    "url": "/v1/user/oauth/grants/{grant_id}".format(
      grant_id=quote(str(grant_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  if response.status_code == 200:
    response_200 = SuccessResponse.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

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
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  grant_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  """Revoke Connected App

   Revokes the grant and every access and refresh token minted from it. The client's next request fails
  with 401 and it must ask the user to authorize again. Revoking an already revoked grant succeeds and
  changes nothing.

  Args:
      grant_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SuccessResponse]
  """

  kwargs = _get_kwargs(
    grant_id=grant_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  grant_id: str,
  *,
  client: AuthenticatedClient,
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  """Revoke Connected App

   Revokes the grant and every access and refresh token minted from it. The client's next request fails
  with 401 and it must ask the user to authorize again. Revoking an already revoked grant succeeds and
  changes nothing.

  Args:
      grant_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SuccessResponse
  """

  return sync_detailed(
    grant_id=grant_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  grant_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  """Revoke Connected App

   Revokes the grant and every access and refresh token minted from it. The client's next request fails
  with 401 and it must ask the user to authorize again. Revoking an already revoked grant succeeds and
  changes nothing.

  Args:
      grant_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SuccessResponse]
  """

  kwargs = _get_kwargs(
    grant_id=grant_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  grant_id: str,
  *,
  client: AuthenticatedClient,
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  """Revoke Connected App

   Revokes the grant and every access and refresh token minted from it. The client's next request fails
  with 401 and it must ask the user to authorize again. Revoking an already revoked grant succeeds and
  changes nothing.

  Args:
      grant_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SuccessResponse
  """

  return (
    await asyncio_detailed(
      grant_id=grant_id,
      client=client,
    )
  ).parsed
