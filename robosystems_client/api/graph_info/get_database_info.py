from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.database_info_response import DatabaseInfoResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/info",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DatabaseInfoResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = DatabaseInfoResponse.from_dict(response.json())

    return response_200
  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403
  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404
  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DatabaseInfoResponse, HTTPValidationError]]:
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
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, DatabaseInfoResponse, HTTPValidationError]]:
  """Database Information

   Get comprehensive database information and statistics.

  Returns detailed database metrics including:
  - **Database Metadata**: Name, path, size, and timestamps
  - **Schema Information**: Node labels, relationship types, and counts
  - **Storage Statistics**: Database size and usage metrics
  - **Data Composition**: Node and relationship counts
  - **Backup Information**: Available backups and last backup date
  - **Configuration**: Read-only status and schema version

  Database statistics:
  - **Size**: Storage usage in bytes and MB
  - **Content**: Node and relationship counts
  - **Schema**: Available labels and relationship types
  - **Backup Status**: Backup availability and recency
  - **Timestamps**: Creation and modification dates

  This endpoint provides essential database information for capacity planning and monitoring.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, DatabaseInfoResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, DatabaseInfoResponse, HTTPValidationError]]:
  """Database Information

   Get comprehensive database information and statistics.

  Returns detailed database metrics including:
  - **Database Metadata**: Name, path, size, and timestamps
  - **Schema Information**: Node labels, relationship types, and counts
  - **Storage Statistics**: Database size and usage metrics
  - **Data Composition**: Node and relationship counts
  - **Backup Information**: Available backups and last backup date
  - **Configuration**: Read-only status and schema version

  Database statistics:
  - **Size**: Storage usage in bytes and MB
  - **Content**: Node and relationship counts
  - **Schema**: Available labels and relationship types
  - **Backup Status**: Backup availability and recency
  - **Timestamps**: Creation and modification dates

  This endpoint provides essential database information for capacity planning and monitoring.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, DatabaseInfoResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, DatabaseInfoResponse, HTTPValidationError]]:
  """Database Information

   Get comprehensive database information and statistics.

  Returns detailed database metrics including:
  - **Database Metadata**: Name, path, size, and timestamps
  - **Schema Information**: Node labels, relationship types, and counts
  - **Storage Statistics**: Database size and usage metrics
  - **Data Composition**: Node and relationship counts
  - **Backup Information**: Available backups and last backup date
  - **Configuration**: Read-only status and schema version

  Database statistics:
  - **Size**: Storage usage in bytes and MB
  - **Content**: Node and relationship counts
  - **Schema**: Available labels and relationship types
  - **Backup Status**: Backup availability and recency
  - **Timestamps**: Creation and modification dates

  This endpoint provides essential database information for capacity planning and monitoring.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, DatabaseInfoResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, DatabaseInfoResponse, HTTPValidationError]]:
  """Database Information

   Get comprehensive database information and statistics.

  Returns detailed database metrics including:
  - **Database Metadata**: Name, path, size, and timestamps
  - **Schema Information**: Node labels, relationship types, and counts
  - **Storage Statistics**: Database size and usage metrics
  - **Data Composition**: Node and relationship counts
  - **Backup Information**: Available backups and last backup date
  - **Configuration**: Read-only status and schema version

  Database statistics:
  - **Size**: Storage usage in bytes and MB
  - **Content**: Node and relationship counts
  - **Schema**: Available labels and relationship types
  - **Backup Status**: Backup availability and recency
  - **Timestamps**: Creation and modification dates

  This endpoint provides essential database information for capacity planning and monitoring.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, DatabaseInfoResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      token=token,
      authorization=authorization,
    )
  ).parsed
