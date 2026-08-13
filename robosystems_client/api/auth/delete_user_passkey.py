from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.passkey_delete_request import PasskeyDeleteRequest
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
  passkey_id: str,
  *,
  body: PasskeyDeleteRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "delete",
    "url": "/v1/auth/passkeys/{passkey_id}".format(
      passkey_id=quote(str(passkey_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
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

  if response.status_code == 409:
    response_409 = ErrorResponse.from_dict(response.json())

    return response_409

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
  passkey_id: str,
  *,
  client: AuthenticatedClient,
  body: PasskeyDeleteRequest,
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  """Remove Passkey

   Remove one passkey after re-authentication (password or fresh assertion). The last passkey of an
  MFA-required role cannot be removed while enforcement is active.

  Args:
      passkey_id (str):
      body (PasskeyDeleteRequest): Re-authentication proof for removing a passkey.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SuccessResponse]
  """

  kwargs = _get_kwargs(
    passkey_id=passkey_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  passkey_id: str,
  *,
  client: AuthenticatedClient,
  body: PasskeyDeleteRequest,
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  """Remove Passkey

   Remove one passkey after re-authentication (password or fresh assertion). The last passkey of an
  MFA-required role cannot be removed while enforcement is active.

  Args:
      passkey_id (str):
      body (PasskeyDeleteRequest): Re-authentication proof for removing a passkey.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SuccessResponse
  """

  return sync_detailed(
    passkey_id=passkey_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  passkey_id: str,
  *,
  client: AuthenticatedClient,
  body: PasskeyDeleteRequest,
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  """Remove Passkey

   Remove one passkey after re-authentication (password or fresh assertion). The last passkey of an
  MFA-required role cannot be removed while enforcement is active.

  Args:
      passkey_id (str):
      body (PasskeyDeleteRequest): Re-authentication proof for removing a passkey.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SuccessResponse]
  """

  kwargs = _get_kwargs(
    passkey_id=passkey_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  passkey_id: str,
  *,
  client: AuthenticatedClient,
  body: PasskeyDeleteRequest,
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  """Remove Passkey

   Remove one passkey after re-authentication (password or fresh assertion). The last passkey of an
  MFA-required role cannot be removed while enforcement is active.

  Args:
      passkey_id (str):
      body (PasskeyDeleteRequest): Re-authentication proof for removing a passkey.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SuccessResponse
  """

  return (
    await asyncio_detailed(
      passkey_id=passkey_id,
      client=client,
      body=body,
    )
  ).parsed
