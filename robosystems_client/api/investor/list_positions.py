from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.position_list_response import PositionListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  portfolio_id: None | str | Unset = UNSET,
  security_id: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_portfolio_id: None | str | Unset
  if isinstance(portfolio_id, Unset):
    json_portfolio_id = UNSET
  else:
    json_portfolio_id = portfolio_id
  params["portfolio_id"] = json_portfolio_id

  json_security_id: None | str | Unset
  if isinstance(security_id, Unset):
    json_security_id = UNSET
  else:
    json_security_id = security_id
  params["security_id"] = json_security_id

  json_status: None | str | Unset
  if isinstance(status, Unset):
    json_status = UNSET
  else:
    json_status = status
  params["status"] = json_status

  params["limit"] = limit

  params["offset"] = offset

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/investor/{graph_id}/positions".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PositionListResponse | None:
  if response.status_code == 200:
    response_200 = PositionListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PositionListResponse]:
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
  portfolio_id: None | str | Unset = UNSET,
  security_id: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[HTTPValidationError | PositionListResponse]:
  """List Positions

  Args:
      graph_id (str):
      portfolio_id (None | str | Unset): Filter by portfolio
      security_id (None | str | Unset): Filter by security
      status (None | str | Unset): Filter by status
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PositionListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    portfolio_id=portfolio_id,
    security_id=security_id,
    status=status,
    limit=limit,
    offset=offset,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  portfolio_id: None | str | Unset = UNSET,
  security_id: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> HTTPValidationError | PositionListResponse | None:
  """List Positions

  Args:
      graph_id (str):
      portfolio_id (None | str | Unset): Filter by portfolio
      security_id (None | str | Unset): Filter by security
      status (None | str | Unset): Filter by status
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PositionListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    portfolio_id=portfolio_id,
    security_id=security_id,
    status=status,
    limit=limit,
    offset=offset,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  portfolio_id: None | str | Unset = UNSET,
  security_id: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> Response[HTTPValidationError | PositionListResponse]:
  """List Positions

  Args:
      graph_id (str):
      portfolio_id (None | str | Unset): Filter by portfolio
      security_id (None | str | Unset): Filter by security
      status (None | str | Unset): Filter by status
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PositionListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    portfolio_id=portfolio_id,
    security_id=security_id,
    status=status,
    limit=limit,
    offset=offset,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  portfolio_id: None | str | Unset = UNSET,
  security_id: None | str | Unset = UNSET,
  status: None | str | Unset = UNSET,
  limit: int | Unset = 100,
  offset: int | Unset = 0,
) -> HTTPValidationError | PositionListResponse | None:
  """List Positions

  Args:
      graph_id (str):
      portfolio_id (None | str | Unset): Filter by portfolio
      security_id (None | str | Unset): Filter by security
      status (None | str | Unset): Filter by status
      limit (int | Unset):  Default: 100.
      offset (int | Unset):  Default: 0.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PositionListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      portfolio_id=portfolio_id,
      security_id=security_id,
      status=status,
      limit=limit,
      offset=offset,
    )
  ).parsed
