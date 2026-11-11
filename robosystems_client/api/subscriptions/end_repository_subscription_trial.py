from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.graph_subscription_response import GraphSubscriptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/subscriptions/end-trial".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

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
) -> Response[ErrorResponse | GraphSubscriptionResponse | HTTPValidationError]:
  """End Repository Trial

   End your free trial of a shared repository now and start the paid plan. The first period is charged
  to the payment method on file; raw queries, the AI analyst and the plan's credits open once the
  payment clears, usually within a minute. Returns 400 when the subscription is not on a trial.

  Args:
      graph_id (str): Repository name (e.g., 'sec')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GraphSubscriptionResponse | HTTPValidationError]
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
) -> ErrorResponse | GraphSubscriptionResponse | HTTPValidationError | None:
  """End Repository Trial

   End your free trial of a shared repository now and start the paid plan. The first period is charged
  to the payment method on file; raw queries, the AI analyst and the plan's credits open once the
  payment clears, usually within a minute. Returns 400 when the subscription is not on a trial.

  Args:
      graph_id (str): Repository name (e.g., 'sec')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | GraphSubscriptionResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[ErrorResponse | GraphSubscriptionResponse | HTTPValidationError]:
  """End Repository Trial

   End your free trial of a shared repository now and start the paid plan. The first period is charged
  to the payment method on file; raw queries, the AI analyst and the plan's credits open once the
  payment clears, usually within a minute. Returns 400 when the subscription is not on a trial.

  Args:
      graph_id (str): Repository name (e.g., 'sec')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GraphSubscriptionResponse | HTTPValidationError]
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
) -> ErrorResponse | GraphSubscriptionResponse | HTTPValidationError | None:
  """End Repository Trial

   End your free trial of a shared repository now and start the paid plan. The first period is charged
  to the payment method on file; raw queries, the AI analyst and the plan's credits open once the
  payment clears, usually within a minute. Returns 400 when the subscription is not on a trial.

  Args:
      graph_id (str): Repository name (e.g., 'sec')

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
    )
  ).parsed
