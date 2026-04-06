from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

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
    "method": "patch",
    "url": "/v1/graphs/{graph_id}/subscriptions".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GraphSubscriptionResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = GraphSubscriptionResponse.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = cast(Any, None)
    return response_400

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
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GraphSubscriptionResponse | HTTPValidationError]:
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
) -> Response[Any | GraphSubscriptionResponse | HTTPValidationError]:
  """Change Subscription Plan

   Change the plan on an existing subscription.

  **For shared repositories** (sec, industry, etc.): Changes access tier (e.g., starter -> advanced).
  Synchronous — takes effect immediately.

  **For user graphs** (kg*): Changes infrastructure tier (e.g., ladybug-standard -> ladybug-large).
  Asynchronous — returns an `operation_id` for tracking the EBS volume migration via SSE.

  Stripe handles proration automatically for both types.

  **Requirements:**
  - User must be an OWNER of their organization
  - Subscription must be active
  - New plan must be valid for the resource type

  **Downgrade restrictions (graphs only):**
  - Subgraph count must fit the target tier's limit
  - Storage usage must fit the target tier's limit

  Args:
      graph_id (str): Graph ID or repository name
      body (UpgradeSubscriptionRequest): Request to upgrade a subscription.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | GraphSubscriptionResponse | HTTPValidationError]
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
) -> Any | GraphSubscriptionResponse | HTTPValidationError | None:
  """Change Subscription Plan

   Change the plan on an existing subscription.

  **For shared repositories** (sec, industry, etc.): Changes access tier (e.g., starter -> advanced).
  Synchronous — takes effect immediately.

  **For user graphs** (kg*): Changes infrastructure tier (e.g., ladybug-standard -> ladybug-large).
  Asynchronous — returns an `operation_id` for tracking the EBS volume migration via SSE.

  Stripe handles proration automatically for both types.

  **Requirements:**
  - User must be an OWNER of their organization
  - Subscription must be active
  - New plan must be valid for the resource type

  **Downgrade restrictions (graphs only):**
  - Subgraph count must fit the target tier's limit
  - Storage usage must fit the target tier's limit

  Args:
      graph_id (str): Graph ID or repository name
      body (UpgradeSubscriptionRequest): Request to upgrade a subscription.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | GraphSubscriptionResponse | HTTPValidationError
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
) -> Response[Any | GraphSubscriptionResponse | HTTPValidationError]:
  """Change Subscription Plan

   Change the plan on an existing subscription.

  **For shared repositories** (sec, industry, etc.): Changes access tier (e.g., starter -> advanced).
  Synchronous — takes effect immediately.

  **For user graphs** (kg*): Changes infrastructure tier (e.g., ladybug-standard -> ladybug-large).
  Asynchronous — returns an `operation_id` for tracking the EBS volume migration via SSE.

  Stripe handles proration automatically for both types.

  **Requirements:**
  - User must be an OWNER of their organization
  - Subscription must be active
  - New plan must be valid for the resource type

  **Downgrade restrictions (graphs only):**
  - Subgraph count must fit the target tier's limit
  - Storage usage must fit the target tier's limit

  Args:
      graph_id (str): Graph ID or repository name
      body (UpgradeSubscriptionRequest): Request to upgrade a subscription.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | GraphSubscriptionResponse | HTTPValidationError]
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
) -> Any | GraphSubscriptionResponse | HTTPValidationError | None:
  """Change Subscription Plan

   Change the plan on an existing subscription.

  **For shared repositories** (sec, industry, etc.): Changes access tier (e.g., starter -> advanced).
  Synchronous — takes effect immediately.

  **For user graphs** (kg*): Changes infrastructure tier (e.g., ladybug-standard -> ladybug-large).
  Asynchronous — returns an `operation_id` for tracking the EBS volume migration via SSE.

  Stripe handles proration automatically for both types.

  **Requirements:**
  - User must be an OWNER of their organization
  - Subscription must be active
  - New plan must be valid for the resource type

  **Downgrade restrictions (graphs only):**
  - Subgraph count must fit the target tier's limit
  - Storage usage must fit the target tier's limit

  Args:
      graph_id (str): Graph ID or repository name
      body (UpgradeSubscriptionRequest): Request to upgrade a subscription.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | GraphSubscriptionResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
