from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checkout_response import CheckoutResponse
from ...models.create_checkout_request import CreateCheckoutRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  *,
  body: CreateCheckoutRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/billing/checkout",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CheckoutResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 201:
    response_201 = CheckoutResponse.from_dict(response.json())

    return response_201

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401

  if response.status_code == 402:
    response_402 = cast(Any, None)
    return response_402

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

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
) -> Response[Any | CheckoutResponse | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  body: CreateCheckoutRequest,
) -> Response[Any | CheckoutResponse | ErrorResponse | HTTPValidationError]:
  """Create Payment Checkout Session

   Initiates a Stripe checkout session for payment collection. Creates a pending subscription; the
  webhook activates it and provisions the resource after payment completes. Returns
  billing_disabled=true with no URL when billing is off. Requires org owner role.

  Args:
      body (CreateCheckoutRequest): Request to create a checkout session for payment collection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | CheckoutResponse | ErrorResponse | HTTPValidationError]
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
  body: CreateCheckoutRequest,
) -> Any | CheckoutResponse | ErrorResponse | HTTPValidationError | None:
  """Create Payment Checkout Session

   Initiates a Stripe checkout session for payment collection. Creates a pending subscription; the
  webhook activates it and provisions the resource after payment completes. Returns
  billing_disabled=true with no URL when billing is off. Requires org owner role.

  Args:
      body (CreateCheckoutRequest): Request to create a checkout session for payment collection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | CheckoutResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  body: CreateCheckoutRequest,
) -> Response[Any | CheckoutResponse | ErrorResponse | HTTPValidationError]:
  """Create Payment Checkout Session

   Initiates a Stripe checkout session for payment collection. Creates a pending subscription; the
  webhook activates it and provisions the resource after payment completes. Returns
  billing_disabled=true with no URL when billing is off. Requires org owner role.

  Args:
      body (CreateCheckoutRequest): Request to create a checkout session for payment collection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | CheckoutResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  body: CreateCheckoutRequest,
) -> Any | CheckoutResponse | ErrorResponse | HTTPValidationError | None:
  """Create Payment Checkout Session

   Initiates a Stripe checkout session for payment collection. Creates a pending subscription; the
  webhook activates it and provisions the resource after payment completes. Returns
  billing_disabled=true with no URL when billing is off. Requires org owner role.

  Args:
      body (CreateCheckoutRequest): Request to create a checkout session for payment collection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | CheckoutResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
