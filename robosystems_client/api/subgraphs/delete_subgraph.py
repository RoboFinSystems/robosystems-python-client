from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_subgraph_request import DeleteSubgraphRequest
from ...models.delete_subgraph_response import DeleteSubgraphResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  subgraph_id: str,
  *,
  body: DeleteSubgraphRequest,
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
    "method": "delete",
    "url": f"/v1/graphs/{graph_id}/subgraphs/{subgraph_id}",
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeleteSubgraphResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = DeleteSubgraphResponse.from_dict(response.json())

    return response_200
  if response.status_code == 401:
    response_401 = cast(Any, None)
    return response_401
  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403
  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404
  if response.status_code == 400:
    response_400 = cast(Any, None)
    return response_400
  if response.status_code == 409:
    response_409 = cast(Any, None)
    return response_409
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
) -> Response[Union[Any, DeleteSubgraphResponse, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  subgraph_id: str,
  *,
  client: AuthenticatedClient,
  body: DeleteSubgraphRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, DeleteSubgraphResponse, HTTPValidationError]]:
  """Delete Subgraph

   Delete a subgraph database.

  **Requirements:**
  - Must be a valid subgraph (not parent graph)
  - User must have admin access to parent graph
  - Optional backup before deletion

  **Deletion Options:**
  - `force`: Delete even if contains data
  - `backup_first`: Create backup before deletion

  **Warning:**
  Deletion is permanent unless backup is created.
  All data in the subgraph will be lost.

  **Backup Location:**
  If backup requested, stored in S3 at:
  `s3://robosystems-backups/{instance_id}/{database_name}_{timestamp}.backup`

  Args:
      graph_id (str): Parent graph identifier
      subgraph_id (str): Subgraph identifier to delete
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (DeleteSubgraphRequest): Request model for deleting a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, DeleteSubgraphResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    subgraph_id=subgraph_id,
    body=body,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  subgraph_id: str,
  *,
  client: AuthenticatedClient,
  body: DeleteSubgraphRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, DeleteSubgraphResponse, HTTPValidationError]]:
  """Delete Subgraph

   Delete a subgraph database.

  **Requirements:**
  - Must be a valid subgraph (not parent graph)
  - User must have admin access to parent graph
  - Optional backup before deletion

  **Deletion Options:**
  - `force`: Delete even if contains data
  - `backup_first`: Create backup before deletion

  **Warning:**
  Deletion is permanent unless backup is created.
  All data in the subgraph will be lost.

  **Backup Location:**
  If backup requested, stored in S3 at:
  `s3://robosystems-backups/{instance_id}/{database_name}_{timestamp}.backup`

  Args:
      graph_id (str): Parent graph identifier
      subgraph_id (str): Subgraph identifier to delete
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (DeleteSubgraphRequest): Request model for deleting a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, DeleteSubgraphResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    subgraph_id=subgraph_id,
    client=client,
    body=body,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  subgraph_id: str,
  *,
  client: AuthenticatedClient,
  body: DeleteSubgraphRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, DeleteSubgraphResponse, HTTPValidationError]]:
  """Delete Subgraph

   Delete a subgraph database.

  **Requirements:**
  - Must be a valid subgraph (not parent graph)
  - User must have admin access to parent graph
  - Optional backup before deletion

  **Deletion Options:**
  - `force`: Delete even if contains data
  - `backup_first`: Create backup before deletion

  **Warning:**
  Deletion is permanent unless backup is created.
  All data in the subgraph will be lost.

  **Backup Location:**
  If backup requested, stored in S3 at:
  `s3://robosystems-backups/{instance_id}/{database_name}_{timestamp}.backup`

  Args:
      graph_id (str): Parent graph identifier
      subgraph_id (str): Subgraph identifier to delete
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (DeleteSubgraphRequest): Request model for deleting a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, DeleteSubgraphResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    subgraph_id=subgraph_id,
    body=body,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  subgraph_id: str,
  *,
  client: AuthenticatedClient,
  body: DeleteSubgraphRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, DeleteSubgraphResponse, HTTPValidationError]]:
  """Delete Subgraph

   Delete a subgraph database.

  **Requirements:**
  - Must be a valid subgraph (not parent graph)
  - User must have admin access to parent graph
  - Optional backup before deletion

  **Deletion Options:**
  - `force`: Delete even if contains data
  - `backup_first`: Create backup before deletion

  **Warning:**
  Deletion is permanent unless backup is created.
  All data in the subgraph will be lost.

  **Backup Location:**
  If backup requested, stored in S3 at:
  `s3://robosystems-backups/{instance_id}/{database_name}_{timestamp}.backup`

  Args:
      graph_id (str): Parent graph identifier
      subgraph_id (str): Subgraph identifier to delete
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (DeleteSubgraphRequest): Request model for deleting a subgraph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, DeleteSubgraphResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      subgraph_id=subgraph_id,
      client=client,
      body=body,
      token=token,
      authorization=authorization,
    )
  ).parsed
