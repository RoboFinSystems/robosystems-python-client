from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.position_response import PositionResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  position_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/investor/{graph_id}/positions/{position_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      position_id=quote(str(position_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PositionResponse | None:
  if response.status_code == 200:
    response_200 = PositionResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PositionResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  position_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | PositionResponse]:
  """Get Position

  Args:
      graph_id (str):
      position_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PositionResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    position_id=position_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  position_id: str,
  *,
  client: AuthenticatedClient,
) -> HTTPValidationError | PositionResponse | None:
  """Get Position

  Args:
      graph_id (str):
      position_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PositionResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    position_id=position_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  position_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | PositionResponse]:
  """Get Position

  Args:
      graph_id (str):
      position_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PositionResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    position_id=position_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  position_id: str,
  *,
  client: AuthenticatedClient,
) -> HTTPValidationError | PositionResponse | None:
  """Get Position

  Args:
      graph_id (str):
      position_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PositionResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      position_id=position_id,
      client=client,
    )
  ).parsed
