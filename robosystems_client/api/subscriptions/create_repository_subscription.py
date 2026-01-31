from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_repository_subscription_request import (
  CreateRepositorySubscriptionRequest,
)
from ...models.graph_subscription_response import GraphSubscriptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: CreateRepositorySubscriptionRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
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
  if response.status_code == 201:
    response_201 = GraphSubscriptionResponse.from_dict(response.json())

    return response_201

  if response.status_code == 400:
    response_400 = cast(Any, None)
    return response_400

  if response.status_code == 409:
    response_409 = cast(Any, None)
    return response_409

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
  body: CreateRepositorySubscriptionRequest,
) -> Response[Any | GraphSubscriptionResponse | HTTPValidationError]:
  """Create Repository Subscription

   Create a new subscription to a shared repository.

  This endpoint is ONLY for shared repositories (sec, industry, economic).
  User graph subscriptions are created automatically when the graph is provisioned.

  The subscription will be created in ACTIVE status immediately and credits will be allocated.

  Args:
      graph_id (str): Repository name (e.g., 'sec', 'industry')
      body (CreateRepositorySubscriptionRequest): Request to create a repository subscription.

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
  body: CreateRepositorySubscriptionRequest,
) -> Any | GraphSubscriptionResponse | HTTPValidationError | None:
  """Create Repository Subscription

   Create a new subscription to a shared repository.

  This endpoint is ONLY for shared repositories (sec, industry, economic).
  User graph subscriptions are created automatically when the graph is provisioned.

  The subscription will be created in ACTIVE status immediately and credits will be allocated.

  Args:
      graph_id (str): Repository name (e.g., 'sec', 'industry')
      body (CreateRepositorySubscriptionRequest): Request to create a repository subscription.

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
  body: CreateRepositorySubscriptionRequest,
) -> Response[Any | GraphSubscriptionResponse | HTTPValidationError]:
  """Create Repository Subscription

   Create a new subscription to a shared repository.

  This endpoint is ONLY for shared repositories (sec, industry, economic).
  User graph subscriptions are created automatically when the graph is provisioned.

  The subscription will be created in ACTIVE status immediately and credits will be allocated.

  Args:
      graph_id (str): Repository name (e.g., 'sec', 'industry')
      body (CreateRepositorySubscriptionRequest): Request to create a repository subscription.

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
  body: CreateRepositorySubscriptionRequest,
) -> Any | GraphSubscriptionResponse | HTTPValidationError | None:
  """Create Repository Subscription

   Create a new subscription to a shared repository.

  This endpoint is ONLY for shared repositories (sec, industry, economic).
  User graph subscriptions are created automatically when the graph is provisioned.

  The subscription will be created in ACTIVE status immediately and credits will be allocated.

  Args:
      graph_id (str): Repository name (e.g., 'sec', 'industry')
      body (CreateRepositorySubscriptionRequest): Request to create a repository subscription.

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
