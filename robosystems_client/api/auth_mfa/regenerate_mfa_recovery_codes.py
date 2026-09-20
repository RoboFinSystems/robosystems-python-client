from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.recovery_codes_request import RecoveryCodesRequest
from ...models.recovery_codes_response import RecoveryCodesResponse
from ...types import Response


def _get_kwargs(
  *,
  body: RecoveryCodesRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/auth/mfa/recovery-codes/regenerate",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | RecoveryCodesResponse | None:
  if response.status_code == 200:
    response_200 = RecoveryCodesResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | RecoveryCodesResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  body: RecoveryCodesRequest,
) -> Response[ErrorResponse | HTTPValidationError | RecoveryCodesResponse]:
  """Regenerate Recovery Codes

   Replace the recovery-code set after re-authentication; codes are shown once.

  Args:
      body (RecoveryCodesRequest): Re-authentication proof for regenerating recovery codes.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | RecoveryCodesResponse]
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
  client: AuthenticatedClient,
  body: RecoveryCodesRequest,
) -> ErrorResponse | HTTPValidationError | RecoveryCodesResponse | None:
  """Regenerate Recovery Codes

   Replace the recovery-code set after re-authentication; codes are shown once.

  Args:
      body (RecoveryCodesRequest): Re-authentication proof for regenerating recovery codes.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | RecoveryCodesResponse
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  body: RecoveryCodesRequest,
) -> Response[ErrorResponse | HTTPValidationError | RecoveryCodesResponse]:
  """Regenerate Recovery Codes

   Replace the recovery-code set after re-authentication; codes are shown once.

  Args:
      body (RecoveryCodesRequest): Re-authentication proof for regenerating recovery codes.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | RecoveryCodesResponse]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  body: RecoveryCodesRequest,
) -> ErrorResponse | HTTPValidationError | RecoveryCodesResponse | None:
  """Regenerate Recovery Codes

   Replace the recovery-code set after re-authentication; codes are shown once.

  Args:
      body (RecoveryCodesRequest): Re-authentication proof for regenerating recovery codes.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | RecoveryCodesResponse
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
