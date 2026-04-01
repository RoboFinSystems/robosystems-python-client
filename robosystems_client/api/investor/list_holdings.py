from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.holdings_list_response import HoldingsListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  portfolio_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/investor/{graph_id}/portfolios/{portfolio_id}/holdings".format(
      graph_id=quote(str(graph_id), safe=""),
      portfolio_id=quote(str(portfolio_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | HoldingsListResponse | None:
  if response.status_code == 200:
    response_200 = HoldingsListResponse.from_dict(response.json())

    return response_200

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | HoldingsListResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  portfolio_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | HoldingsListResponse]:
  """List Holdings (grouped by entity)

  Args:
      graph_id (str):
      portfolio_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | HoldingsListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    portfolio_id=portfolio_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  portfolio_id: str,
  *,
  client: AuthenticatedClient,
) -> HTTPValidationError | HoldingsListResponse | None:
  """List Holdings (grouped by entity)

  Args:
      graph_id (str):
      portfolio_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | HoldingsListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    portfolio_id=portfolio_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  portfolio_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | HoldingsListResponse]:
  """List Holdings (grouped by entity)

  Args:
      graph_id (str):
      portfolio_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | HoldingsListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    portfolio_id=portfolio_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  portfolio_id: str,
  *,
  client: AuthenticatedClient,
) -> HTTPValidationError | HoldingsListResponse | None:
  """List Holdings (grouped by entity)

  Args:
      graph_id (str):
      portfolio_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | HoldingsListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      portfolio_id=portfolio_id,
      client=client,
    )
  ).parsed
