from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checkout_status_response import CheckoutStatusResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  session_id: str,
) -> dict[str, Any]:

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/billing/checkout/{session_id}/status".format(
      session_id=quote(str(session_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CheckoutStatusResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = CheckoutStatusResponse.from_dict(response.json())

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
) -> Response[CheckoutStatusResponse | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  session_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[CheckoutStatusResponse | ErrorResponse | HTTPValidationError]:
  """Get Checkout Session Status

   Poll after returning from Stripe Checkout. Status progresses: pending_payment → provisioning →
  active. When active, resource_id is populated; for graphs, operation_id tracks SSE provisioning
  progress.

  Args:
      session_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[CheckoutStatusResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    session_id=session_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  session_id: str,
  *,
  client: AuthenticatedClient,
) -> CheckoutStatusResponse | ErrorResponse | HTTPValidationError | None:
  """Get Checkout Session Status

   Poll after returning from Stripe Checkout. Status progresses: pending_payment → provisioning →
  active. When active, resource_id is populated; for graphs, operation_id tracks SSE provisioning
  progress.

  Args:
      session_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      CheckoutStatusResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    session_id=session_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  session_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[CheckoutStatusResponse | ErrorResponse | HTTPValidationError]:
  """Get Checkout Session Status

   Poll after returning from Stripe Checkout. Status progresses: pending_payment → provisioning →
  active. When active, resource_id is populated; for graphs, operation_id tracks SSE provisioning
  progress.

  Args:
      session_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[CheckoutStatusResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    session_id=session_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  session_id: str,
  *,
  client: AuthenticatedClient,
) -> CheckoutStatusResponse | ErrorResponse | HTTPValidationError | None:
  """Get Checkout Session Status

   Poll after returning from Stripe Checkout. Status progresses: pending_payment → provisioning →
  active. When active, resource_id is populated; for graphs, operation_id tracks SSE provisioning
  progress.

  Args:
      session_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      CheckoutStatusResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      session_id=session_id,
      client=client,
    )
  ).parsed
