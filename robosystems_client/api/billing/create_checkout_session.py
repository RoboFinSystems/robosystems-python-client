from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checkout_response import CheckoutResponse
from ...models.create_checkout_request import CreateCheckoutRequest
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
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CheckoutResponse, HTTPValidationError]]:
  if response.status_code == 201:
    response_201 = CheckoutResponse.from_dict(response.json())

    return response_201

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CheckoutResponse, HTTPValidationError]]:
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
) -> Response[Union[CheckoutResponse, HTTPValidationError]]:
  """Create Payment Checkout Session

   Create a Stripe checkout session for collecting payment method.

  This endpoint is used when an organization owner needs to add a payment method before
  provisioning resources. It creates a pending subscription and redirects
  to Stripe Checkout to collect payment details.

  **Flow:**
  1. Owner tries to create a graph but org has no payment method
  2. Frontend calls this endpoint with graph configuration
  3. Backend creates a subscription in PENDING_PAYMENT status for the user's org
  4. Returns Stripe Checkout URL
  5. User completes payment on Stripe
  6. Webhook activates subscription and provisions resource

  **Requirements:**
  - User must be an OWNER of their organization
  - Enterprise customers (with invoice_billing_enabled) should not call this endpoint.

  Args:
      body (CreateCheckoutRequest): Request to create a checkout session for payment collection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[CheckoutResponse, HTTPValidationError]]
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
) -> Optional[Union[CheckoutResponse, HTTPValidationError]]:
  """Create Payment Checkout Session

   Create a Stripe checkout session for collecting payment method.

  This endpoint is used when an organization owner needs to add a payment method before
  provisioning resources. It creates a pending subscription and redirects
  to Stripe Checkout to collect payment details.

  **Flow:**
  1. Owner tries to create a graph but org has no payment method
  2. Frontend calls this endpoint with graph configuration
  3. Backend creates a subscription in PENDING_PAYMENT status for the user's org
  4. Returns Stripe Checkout URL
  5. User completes payment on Stripe
  6. Webhook activates subscription and provisions resource

  **Requirements:**
  - User must be an OWNER of their organization
  - Enterprise customers (with invoice_billing_enabled) should not call this endpoint.

  Args:
      body (CreateCheckoutRequest): Request to create a checkout session for payment collection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[CheckoutResponse, HTTPValidationError]
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  body: CreateCheckoutRequest,
) -> Response[Union[CheckoutResponse, HTTPValidationError]]:
  """Create Payment Checkout Session

   Create a Stripe checkout session for collecting payment method.

  This endpoint is used when an organization owner needs to add a payment method before
  provisioning resources. It creates a pending subscription and redirects
  to Stripe Checkout to collect payment details.

  **Flow:**
  1. Owner tries to create a graph but org has no payment method
  2. Frontend calls this endpoint with graph configuration
  3. Backend creates a subscription in PENDING_PAYMENT status for the user's org
  4. Returns Stripe Checkout URL
  5. User completes payment on Stripe
  6. Webhook activates subscription and provisions resource

  **Requirements:**
  - User must be an OWNER of their organization
  - Enterprise customers (with invoice_billing_enabled) should not call this endpoint.

  Args:
      body (CreateCheckoutRequest): Request to create a checkout session for payment collection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[CheckoutResponse, HTTPValidationError]]
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
) -> Optional[Union[CheckoutResponse, HTTPValidationError]]:
  """Create Payment Checkout Session

   Create a Stripe checkout session for collecting payment method.

  This endpoint is used when an organization owner needs to add a payment method before
  provisioning resources. It creates a pending subscription and redirects
  to Stripe Checkout to collect payment details.

  **Flow:**
  1. Owner tries to create a graph but org has no payment method
  2. Frontend calls this endpoint with graph configuration
  3. Backend creates a subscription in PENDING_PAYMENT status for the user's org
  4. Returns Stripe Checkout URL
  5. User completes payment on Stripe
  6. Webhook activates subscription and provisions resource

  **Requirements:**
  - User must be an OWNER of their organization
  - Enterprise customers (with invoice_billing_enabled) should not call this endpoint.

  Args:
      body (CreateCheckoutRequest): Request to create a checkout session for payment collection.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[CheckoutResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
