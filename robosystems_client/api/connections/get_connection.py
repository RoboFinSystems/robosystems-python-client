from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connection_response import ConnectionResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  connection_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/connections/{connection_id}",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = ConnectionResponse.from_dict(response.json())

    return response_200

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  """Get Connection

   Get detailed information about a specific connection.

  Returns comprehensive connection details including:
  - Current status and health indicators
  - Authentication state
  - Sync history and statistics
  - Error details if any
  - Provider-specific metadata

  No credits are consumed for viewing connection details.

  Args:
      graph_id (str):
      connection_id (str): Unique connection identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  """Get Connection

   Get detailed information about a specific connection.

  Returns comprehensive connection details including:
  - Current status and health indicators
  - Authentication state
  - Sync history and statistics
  - Error details if any
  - Provider-specific metadata

  No credits are consumed for viewing connection details.

  Args:
      graph_id (str):
      connection_id (str): Unique connection identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ConnectionResponse, ErrorResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    connection_id=connection_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  """Get Connection

   Get detailed information about a specific connection.

  Returns comprehensive connection details including:
  - Current status and health indicators
  - Authentication state
  - Sync history and statistics
  - Error details if any
  - Provider-specific metadata

  No credits are consumed for viewing connection details.

  Args:
      graph_id (str):
      connection_id (str): Unique connection identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[ConnectionResponse, ErrorResponse, HTTPValidationError]]:
  """Get Connection

   Get detailed information about a specific connection.

  Returns comprehensive connection details including:
  - Current status and health indicators
  - Authentication state
  - Sync history and statistics
  - Error details if any
  - Provider-specific metadata

  No credits are consumed for viewing connection details.

  Args:
      graph_id (str):
      connection_id (str): Unique connection identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ConnectionResponse, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      connection_id=connection_id,
      client=client,
    )
  ).parsed
