from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.storage_limit_response import StorageLimitResponse
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
    "url": f"/v1/graphs/{graph_id}/credits/storage/limits",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]]:
  if response.status_code == 200:
    response_200 = StorageLimitResponse.from_dict(response.json())

    return response_200
  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403
  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404
  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]]:
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
) -> Response[Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]]:
  """Check Storage Limits

   Check storage limits and usage for a graph.

  Returns comprehensive storage limit information including:
  - Current storage usage
  - Effective limit (override or default)
  - Usage percentage and warnings
  - Recommendations for limit management

  This endpoint helps users monitor storage usage and plan for potential
  limit increases. No credits are consumed for checking storage limits.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]]
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
) -> Optional[Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]]:
  """Check Storage Limits

   Check storage limits and usage for a graph.

  Returns comprehensive storage limit information including:
  - Current storage usage
  - Effective limit (override or default)
  - Usage percentage and warnings
  - Recommendations for limit management

  This endpoint helps users monitor storage usage and plan for potential
  limit increases. No credits are consumed for checking storage limits.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]
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
) -> Response[Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]]:
  """Check Storage Limits

   Check storage limits and usage for a graph.

  Returns comprehensive storage limit information including:
  - Current storage usage
  - Effective limit (override or default)
  - Usage percentage and warnings
  - Recommendations for limit management

  This endpoint helps users monitor storage usage and plan for potential
  limit increases. No credits are consumed for checking storage limits.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]]
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
) -> Optional[Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]]:
  """Check Storage Limits

   Check storage limits and usage for a graph.

  Returns comprehensive storage limit information including:
  - Current storage usage
  - Effective limit (override or default)
  - Usage percentage and warnings
  - Recommendations for limit management

  This endpoint helps users monitor storage usage and plan for potential
  limit increases. No credits are consumed for checking storage limits.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, HTTPValidationError, StorageLimitResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      token=token,
      authorization=authorization,
    )
  ).parsed
