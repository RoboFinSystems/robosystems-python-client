from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.graph_subscription_response import GraphSubscriptionResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/billing/subscriptions",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["GraphSubscriptionResponse"]]:
  if response.status_code == 200:
    response_200 = []
    _response_200 = response.json()
    for response_200_item_data in _response_200:
      response_200_item = GraphSubscriptionResponse.from_dict(response_200_item_data)

      response_200.append(response_200_item)

    return response_200

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["GraphSubscriptionResponse"]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[list["GraphSubscriptionResponse"]]:
  """List All Subscriptions

   List all active and past subscriptions for the user.

  Includes both graph and repository subscriptions with their status, pricing, and billing
  information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[list['GraphSubscriptionResponse']]
  """

  kwargs = _get_kwargs()

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
) -> Optional[list["GraphSubscriptionResponse"]]:
  """List All Subscriptions

   List all active and past subscriptions for the user.

  Includes both graph and repository subscriptions with their status, pricing, and billing
  information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      list['GraphSubscriptionResponse']
  """

  return sync_detailed(
    client=client,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[list["GraphSubscriptionResponse"]]:
  """List All Subscriptions

   List all active and past subscriptions for the user.

  Includes both graph and repository subscriptions with their status, pricing, and billing
  information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[list['GraphSubscriptionResponse']]
  """

  kwargs = _get_kwargs()

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
) -> Optional[list["GraphSubscriptionResponse"]]:
  """List All Subscriptions

   List all active and past subscriptions for the user.

  Includes both graph and repository subscriptions with their status, pricing, and billing
  information.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      list['GraphSubscriptionResponse']
  """

  return (
    await asyncio_detailed(
      client=client,
    )
  ).parsed
