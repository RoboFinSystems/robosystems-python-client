from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.subgraph_response import SubgraphResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  subgraph_name: str,
) -> dict[str, Any]:

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/subgraphs/{subgraph_name}".format(
      graph_id=quote(str(graph_id), safe=""),
      subgraph_name=quote(str(subgraph_name), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SubgraphResponse | None:
  if response.status_code == 200:
    response_200 = SubgraphResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | SubgraphResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  subgraph_name: str,
  *,
  client: AuthenticatedClient,
) -> Response[ErrorResponse | HTTPValidationError | SubgraphResponse]:
  """Get Subgraph Details

   Pass the subgraph name (e.g., `dev`) not the full subgraph ID (e.g., `kg0123_dev`).

  Args:
      graph_id (str):
      subgraph_name (str): Subgraph name (e.g., 'dev', 'staging')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SubgraphResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    subgraph_name=subgraph_name,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  subgraph_name: str,
  *,
  client: AuthenticatedClient,
) -> ErrorResponse | HTTPValidationError | SubgraphResponse | None:
  """Get Subgraph Details

   Pass the subgraph name (e.g., `dev`) not the full subgraph ID (e.g., `kg0123_dev`).

  Args:
      graph_id (str):
      subgraph_name (str): Subgraph name (e.g., 'dev', 'staging')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SubgraphResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    subgraph_name=subgraph_name,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  subgraph_name: str,
  *,
  client: AuthenticatedClient,
) -> Response[ErrorResponse | HTTPValidationError | SubgraphResponse]:
  """Get Subgraph Details

   Pass the subgraph name (e.g., `dev`) not the full subgraph ID (e.g., `kg0123_dev`).

  Args:
      graph_id (str):
      subgraph_name (str): Subgraph name (e.g., 'dev', 'staging')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SubgraphResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    subgraph_name=subgraph_name,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  subgraph_name: str,
  *,
  client: AuthenticatedClient,
) -> ErrorResponse | HTTPValidationError | SubgraphResponse | None:
  """Get Subgraph Details

   Pass the subgraph name (e.g., `dev`) not the full subgraph ID (e.g., `kg0123_dev`).

  Args:
      graph_id (str):
      subgraph_name (str): Subgraph name (e.g., 'dev', 'staging')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SubgraphResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      subgraph_name=subgraph_name,
      client=client,
    )
  ).parsed
