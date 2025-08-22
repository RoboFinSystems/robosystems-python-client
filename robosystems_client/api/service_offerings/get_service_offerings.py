from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/offering",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse]]:
  if response.status_code == 200:
    response_200 = response.json()
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
) -> Response[Union[Any, ErrorResponse]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ErrorResponse]]:
  """Get Service Offerings

   Get comprehensive information about all subscription offerings.

  This endpoint provides complete information about both graph database subscriptions
  and shared repository subscriptions. This is the primary endpoint for frontend
  applications to display subscription options.

  Includes:
  - Graph subscription tiers (standard, enterprise, premium)
  - Shared repository subscriptions (SEC, industry, economic data)
  - Operation costs and credit information
  - Features and capabilities for each tier
  - Enabled/disabled status for repositories

  All data comes from the config-based systems to ensure accuracy with backend behavior.

  No authentication required - this is public service information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse]]
  """

  kwargs = _get_kwargs()

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ErrorResponse]]:
  """Get Service Offerings

   Get comprehensive information about all subscription offerings.

  This endpoint provides complete information about both graph database subscriptions
  and shared repository subscriptions. This is the primary endpoint for frontend
  applications to display subscription options.

  Includes:
  - Graph subscription tiers (standard, enterprise, premium)
  - Shared repository subscriptions (SEC, industry, economic data)
  - Operation costs and credit information
  - Features and capabilities for each tier
  - Enabled/disabled status for repositories

  All data comes from the config-based systems to ensure accuracy with backend behavior.

  No authentication required - this is public service information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse]
  """

  return sync_detailed(
    client=client,
  ).parsed


async def asyncio_detailed(
  *,
  client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ErrorResponse]]:
  """Get Service Offerings

   Get comprehensive information about all subscription offerings.

  This endpoint provides complete information about both graph database subscriptions
  and shared repository subscriptions. This is the primary endpoint for frontend
  applications to display subscription options.

  Includes:
  - Graph subscription tiers (standard, enterprise, premium)
  - Shared repository subscriptions (SEC, industry, economic data)
  - Operation costs and credit information
  - Features and capabilities for each tier
  - Enabled/disabled status for repositories

  All data comes from the config-based systems to ensure accuracy with backend behavior.

  No authentication required - this is public service information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse]]
  """

  kwargs = _get_kwargs()

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ErrorResponse]]:
  """Get Service Offerings

   Get comprehensive information about all subscription offerings.

  This endpoint provides complete information about both graph database subscriptions
  and shared repository subscriptions. This is the primary endpoint for frontend
  applications to display subscription options.

  Includes:
  - Graph subscription tiers (standard, enterprise, premium)
  - Shared repository subscriptions (SEC, industry, economic data)
  - Operation costs and credit information
  - Features and capabilities for each tier
  - Enabled/disabled status for repositories

  All data comes from the config-based systems to ensure accuracy with backend behavior.

  No authentication required - this is public service information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse]
  """

  return (
    await asyncio_detailed(
      client=client,
    )
  ).parsed
