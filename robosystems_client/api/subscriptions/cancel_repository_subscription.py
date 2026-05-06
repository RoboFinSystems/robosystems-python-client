from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_subscription_request import CancelSubscriptionRequest
from ...models.error_response import ErrorResponse
from ...models.graph_subscription_response import GraphSubscriptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: CancelSubscriptionRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/subscriptions/cancel".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GraphSubscriptionResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = GraphSubscriptionResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GraphSubscriptionResponse | HTTPValidationError]:
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
  body: CancelSubscriptionRequest,
) -> Response[ErrorResponse | GraphSubscriptionResponse | HTTPValidationError]:
  """Cancel Repository Subscription

   Cancel a shared repository subscription. Two modes via the `immediate` flag: omit it (default
  `false`) to cancel at period end (access stays until the period closes); pass `true` with
  `confirm=<repo_id>` to stop access right away. For user graphs, use `POST
  /v1/graphs/{graph_id}/operations/delete-graph` — this endpoint rejects user graphs. Requires org
  owner role.

  Args:
      graph_id (str): Repository name (e.g., 'sec', 'industry')
      body (CancelSubscriptionRequest): Request to cancel a subscription.

          Default behavior cancels at period end (soft cancel). Pass `immediate=True`
          to terminate the subscription right away — this requires `confirm` to equal
          the subscription's `resource_id` (e.g. the graph_id) as a guard against
          accidental destructive calls.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GraphSubscriptionResponse | HTTPValidationError]
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
  body: CancelSubscriptionRequest,
) -> ErrorResponse | GraphSubscriptionResponse | HTTPValidationError | None:
  """Cancel Repository Subscription

   Cancel a shared repository subscription. Two modes via the `immediate` flag: omit it (default
  `false`) to cancel at period end (access stays until the period closes); pass `true` with
  `confirm=<repo_id>` to stop access right away. For user graphs, use `POST
  /v1/graphs/{graph_id}/operations/delete-graph` — this endpoint rejects user graphs. Requires org
  owner role.

  Args:
      graph_id (str): Repository name (e.g., 'sec', 'industry')
      body (CancelSubscriptionRequest): Request to cancel a subscription.

          Default behavior cancels at period end (soft cancel). Pass `immediate=True`
          to terminate the subscription right away — this requires `confirm` to equal
          the subscription's `resource_id` (e.g. the graph_id) as a guard against
          accidental destructive calls.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | GraphSubscriptionResponse | HTTPValidationError
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
  body: CancelSubscriptionRequest,
) -> Response[ErrorResponse | GraphSubscriptionResponse | HTTPValidationError]:
  """Cancel Repository Subscription

   Cancel a shared repository subscription. Two modes via the `immediate` flag: omit it (default
  `false`) to cancel at period end (access stays until the period closes); pass `true` with
  `confirm=<repo_id>` to stop access right away. For user graphs, use `POST
  /v1/graphs/{graph_id}/operations/delete-graph` — this endpoint rejects user graphs. Requires org
  owner role.

  Args:
      graph_id (str): Repository name (e.g., 'sec', 'industry')
      body (CancelSubscriptionRequest): Request to cancel a subscription.

          Default behavior cancels at period end (soft cancel). Pass `immediate=True`
          to terminate the subscription right away — this requires `confirm` to equal
          the subscription's `resource_id` (e.g. the graph_id) as a guard against
          accidental destructive calls.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GraphSubscriptionResponse | HTTPValidationError]
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
  body: CancelSubscriptionRequest,
) -> ErrorResponse | GraphSubscriptionResponse | HTTPValidationError | None:
  """Cancel Repository Subscription

   Cancel a shared repository subscription. Two modes via the `immediate` flag: omit it (default
  `false`) to cancel at period end (access stays until the period closes); pass `true` with
  `confirm=<repo_id>` to stop access right away. For user graphs, use `POST
  /v1/graphs/{graph_id}/operations/delete-graph` — this endpoint rejects user graphs. Requires org
  owner role.

  Args:
      graph_id (str): Repository name (e.g., 'sec', 'industry')
      body (CancelSubscriptionRequest): Request to cancel a subscription.

          Default behavior cancels at period end (soft cancel). Pass `immediate=True`
          to terminate the subscription right away — this requires `confirm` to equal
          the subscription's `resource_id` (e.g. the graph_id) as a guard against
          accidental destructive calls.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | GraphSubscriptionResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
