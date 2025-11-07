from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancellation_response import CancellationResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "delete",
    "url": f"/v1/graphs/{graph_id}/subscriptions",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CancellationResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = CancellationResponse.from_dict(response.json())

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
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CancellationResponse, HTTPValidationError]]:
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
) -> Response[Union[Any, CancellationResponse, HTTPValidationError]]:
  """Cancel Subscription

   Cancel a subscription.

  For shared repositories: Cancels the user's personal subscription
  For user graphs: Not allowed - delete the graph instead

  The subscription will be marked as canceled and will end at the current period end date.

  Args:
      graph_id (str): Graph ID or repository name

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, CancellationResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[Any, CancellationResponse, HTTPValidationError]]:
  """Cancel Subscription

   Cancel a subscription.

  For shared repositories: Cancels the user's personal subscription
  For user graphs: Not allowed - delete the graph instead

  The subscription will be marked as canceled and will end at the current period end date.

  Args:
      graph_id (str): Graph ID or repository name

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, CancellationResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[Any, CancellationResponse, HTTPValidationError]]:
  """Cancel Subscription

   Cancel a subscription.

  For shared repositories: Cancels the user's personal subscription
  For user graphs: Not allowed - delete the graph instead

  The subscription will be marked as canceled and will end at the current period end date.

  Args:
      graph_id (str): Graph ID or repository name

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, CancellationResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[Any, CancellationResponse, HTTPValidationError]]:
  """Cancel Subscription

   Cancel a subscription.

  For shared repositories: Cancels the user's personal subscription
  For user graphs: Not allowed - delete the graph instead

  The subscription will be marked as canceled and will end at the current period end date.

  Args:
      graph_id (str): Graph ID or repository name

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, CancellationResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
