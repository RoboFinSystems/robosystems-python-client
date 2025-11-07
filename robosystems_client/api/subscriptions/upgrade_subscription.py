from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.graph_subscription_response import GraphSubscriptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.upgrade_subscription_request import UpgradeSubscriptionRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: UpgradeSubscriptionRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "put",
    "url": f"/v1/graphs/{graph_id}/subscriptions/upgrade",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GraphSubscriptionResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = GraphSubscriptionResponse.from_dict(response.json())

    return response_200

  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GraphSubscriptionResponse, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: UpgradeSubscriptionRequest,
) -> Response[Union[Any, GraphSubscriptionResponse, HTTPValidationError]]:
  """Upgrade Subscription

   Upgrade a subscription to a different plan.

  Works for both user graphs and shared repositories.
  The subscription will be immediately updated to the new plan and pricing.

  Args:
      graph_id (str): Graph ID or repository name
      body (UpgradeSubscriptionRequest): Request to upgrade a subscription.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GraphSubscriptionResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: UpgradeSubscriptionRequest,
) -> Optional[Union[Any, GraphSubscriptionResponse, HTTPValidationError]]:
  """Upgrade Subscription

   Upgrade a subscription to a different plan.

  Works for both user graphs and shared repositories.
  The subscription will be immediately updated to the new plan and pricing.

  Args:
      graph_id (str): Graph ID or repository name
      body (UpgradeSubscriptionRequest): Request to upgrade a subscription.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GraphSubscriptionResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: UpgradeSubscriptionRequest,
) -> Response[Union[Any, GraphSubscriptionResponse, HTTPValidationError]]:
  """Upgrade Subscription

   Upgrade a subscription to a different plan.

  Works for both user graphs and shared repositories.
  The subscription will be immediately updated to the new plan and pricing.

  Args:
      graph_id (str): Graph ID or repository name
      body (UpgradeSubscriptionRequest): Request to upgrade a subscription.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GraphSubscriptionResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: UpgradeSubscriptionRequest,
) -> Optional[Union[Any, GraphSubscriptionResponse, HTTPValidationError]]:
  """Upgrade Subscription

   Upgrade a subscription to a different plan.

  Works for both user graphs and shared repositories.
  The subscription will be immediately updated to the new plan and pricing.

  Args:
      graph_id (str): Graph ID or repository name
      body (UpgradeSubscriptionRequest): Request to upgrade a subscription.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GraphSubscriptionResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
