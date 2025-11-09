from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.service_offerings_response import ServiceOfferingsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/offering",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ServiceOfferingsResponse]]:
  if response.status_code == 200:
    response_200 = ServiceOfferingsResponse.from_dict(response.json())

    return response_200

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, ServiceOfferingsResponse]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, ServiceOfferingsResponse]]:
  """Get Service Offerings

   Get comprehensive information about all subscription offerings.

  This endpoint provides complete information about both graph database subscriptions
  and shared repository subscriptions. This is the primary endpoint for frontend
  applications to display subscription options.

  **Pricing Model:**
  - Graph subscriptions are **per-graph** with infrastructure-based pricing
  - Each graph you create has its own monthly subscription
  - Organizations can have multiple graphs with different infrastructure tiers
  - Credits are allocated per-graph, not shared across organization

  Includes:
  - Graph infrastructure tiers (kuzu-standard, kuzu-large, kuzu-xlarge) - per-graph pricing
  - Shared repository subscriptions (SEC, industry, economic data) - org-level
  - Operation costs and credit information
  - Features and capabilities for each tier
  - Enabled/disabled status for repositories

  All data comes from the config-based systems to ensure accuracy with backend behavior.

  No authentication required - this is public service information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, ServiceOfferingsResponse]]
  """

  kwargs = _get_kwargs()

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, ServiceOfferingsResponse]]:
  """Get Service Offerings

   Get comprehensive information about all subscription offerings.

  This endpoint provides complete information about both graph database subscriptions
  and shared repository subscriptions. This is the primary endpoint for frontend
  applications to display subscription options.

  **Pricing Model:**
  - Graph subscriptions are **per-graph** with infrastructure-based pricing
  - Each graph you create has its own monthly subscription
  - Organizations can have multiple graphs with different infrastructure tiers
  - Credits are allocated per-graph, not shared across organization

  Includes:
  - Graph infrastructure tiers (kuzu-standard, kuzu-large, kuzu-xlarge) - per-graph pricing
  - Shared repository subscriptions (SEC, industry, economic data) - org-level
  - Operation costs and credit information
  - Features and capabilities for each tier
  - Enabled/disabled status for repositories

  All data comes from the config-based systems to ensure accuracy with backend behavior.

  No authentication required - this is public service information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, ServiceOfferingsResponse]
  """

  return sync_detailed(
    client=client,
  ).parsed


async def asyncio_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, ServiceOfferingsResponse]]:
  """Get Service Offerings

   Get comprehensive information about all subscription offerings.

  This endpoint provides complete information about both graph database subscriptions
  and shared repository subscriptions. This is the primary endpoint for frontend
  applications to display subscription options.

  **Pricing Model:**
  - Graph subscriptions are **per-graph** with infrastructure-based pricing
  - Each graph you create has its own monthly subscription
  - Organizations can have multiple graphs with different infrastructure tiers
  - Credits are allocated per-graph, not shared across organization

  Includes:
  - Graph infrastructure tiers (kuzu-standard, kuzu-large, kuzu-xlarge) - per-graph pricing
  - Shared repository subscriptions (SEC, industry, economic data) - org-level
  - Operation costs and credit information
  - Features and capabilities for each tier
  - Enabled/disabled status for repositories

  All data comes from the config-based systems to ensure accuracy with backend behavior.

  No authentication required - this is public service information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, ServiceOfferingsResponse]]
  """

  kwargs = _get_kwargs()

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, ServiceOfferingsResponse]]:
  """Get Service Offerings

   Get comprehensive information about all subscription offerings.

  This endpoint provides complete information about both graph database subscriptions
  and shared repository subscriptions. This is the primary endpoint for frontend
  applications to display subscription options.

  **Pricing Model:**
  - Graph subscriptions are **per-graph** with infrastructure-based pricing
  - Each graph you create has its own monthly subscription
  - Organizations can have multiple graphs with different infrastructure tiers
  - Credits are allocated per-graph, not shared across organization

  Includes:
  - Graph infrastructure tiers (kuzu-standard, kuzu-large, kuzu-xlarge) - per-graph pricing
  - Shared repository subscriptions (SEC, industry, economic data) - org-level
  - Operation costs and credit information
  - Features and capabilities for each tier
  - Enabled/disabled status for repositories

  All data comes from the config-based systems to ensure accuracy with backend behavior.

  No authentication required - this is public service information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, ServiceOfferingsResponse]
  """

  return (
    await asyncio_detailed(
      client=client,
    )
  ).parsed
