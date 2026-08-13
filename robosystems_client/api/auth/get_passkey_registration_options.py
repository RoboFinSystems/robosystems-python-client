from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ceremony_options_response import CeremonyOptionsResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.passkey_register_options_request import PasskeyRegisterOptionsRequest
from ...types import Response


def _get_kwargs(
  *,
  body: PasskeyRegisterOptionsRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/auth/passkeys/register/options",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CeremonyOptionsResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = CeremonyOptionsResponse.from_dict(response.json())

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
) -> Response[CeremonyOptionsResponse | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient | Client,
  body: PasskeyRegisterOptionsRequest,
) -> Response[CeremonyOptionsResponse | ErrorResponse | HTTPValidationError]:
  """Passkey Registration Options

   Begin a passkey enrollment ceremony. The settings lane requires a fresh re-auth proof (password or
  assertion); the forced lane presents its enrollment token.

  Args:
      body (PasskeyRegisterOptionsRequest): Begin enrollment.

          Two disjoint lanes: ``mfa_token`` (forced enrollment — the token was minted
          seconds after a password verify, so it is its own freshness proof) or an
          authenticated settings-flow enrollment, which must carry a fresh re-auth
          proof — ``password``, or a ``reauth``-ceremony ``assertion`` when adding a
          passkey beside an existing one.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[CeremonyOptionsResponse | ErrorResponse | HTTPValidationError]
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
  client: AuthenticatedClient | Client,
  body: PasskeyRegisterOptionsRequest,
) -> CeremonyOptionsResponse | ErrorResponse | HTTPValidationError | None:
  """Passkey Registration Options

   Begin a passkey enrollment ceremony. The settings lane requires a fresh re-auth proof (password or
  assertion); the forced lane presents its enrollment token.

  Args:
      body (PasskeyRegisterOptionsRequest): Begin enrollment.

          Two disjoint lanes: ``mfa_token`` (forced enrollment — the token was minted
          seconds after a password verify, so it is its own freshness proof) or an
          authenticated settings-flow enrollment, which must carry a fresh re-auth
          proof — ``password``, or a ``reauth``-ceremony ``assertion`` when adding a
          passkey beside an existing one.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      CeremonyOptionsResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient | Client,
  body: PasskeyRegisterOptionsRequest,
) -> Response[CeremonyOptionsResponse | ErrorResponse | HTTPValidationError]:
  """Passkey Registration Options

   Begin a passkey enrollment ceremony. The settings lane requires a fresh re-auth proof (password or
  assertion); the forced lane presents its enrollment token.

  Args:
      body (PasskeyRegisterOptionsRequest): Begin enrollment.

          Two disjoint lanes: ``mfa_token`` (forced enrollment — the token was minted
          seconds after a password verify, so it is its own freshness proof) or an
          authenticated settings-flow enrollment, which must carry a fresh re-auth
          proof — ``password``, or a ``reauth``-ceremony ``assertion`` when adding a
          passkey beside an existing one.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[CeremonyOptionsResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient | Client,
  body: PasskeyRegisterOptionsRequest,
) -> CeremonyOptionsResponse | ErrorResponse | HTTPValidationError | None:
  """Passkey Registration Options

   Begin a passkey enrollment ceremony. The settings lane requires a fresh re-auth proof (password or
  assertion); the forced lane presents its enrollment token.

  Args:
      body (PasskeyRegisterOptionsRequest): Begin enrollment.

          Two disjoint lanes: ``mfa_token`` (forced enrollment — the token was minted
          seconds after a password verify, so it is its own freshness proof) or an
          authenticated settings-flow enrollment, which must carry a fresh re-auth
          proof — ``password``, or a ``reauth``-ceremony ``assertion`` when adding a
          passkey beside an existing one.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      CeremonyOptionsResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
