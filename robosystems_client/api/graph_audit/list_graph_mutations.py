import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_graph_mutations_surface_type_0 import ListGraphMutationsSurfaceType0
from ...models.mutation_audit_list_response import MutationAuditListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  surface: ListGraphMutationsSurfaceType0 | None | Unset = UNSET,
  operation_name: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operation_id: None | str | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  json_surface: None | str | Unset
  if isinstance(surface, Unset):
    json_surface = UNSET
  elif isinstance(surface, ListGraphMutationsSurfaceType0):
    json_surface = surface.value
  else:
    json_surface = surface
  params["surface"] = json_surface

  json_operation_name: None | str | Unset
  if isinstance(operation_name, Unset):
    json_operation_name = UNSET
  else:
    json_operation_name = operation_name
  params["operation_name"] = json_operation_name

  json_user_id: None | str | Unset
  if isinstance(user_id, Unset):
    json_user_id = UNSET
  else:
    json_user_id = user_id
  params["user_id"] = json_user_id

  json_operation_id: None | str | Unset
  if isinstance(operation_id, Unset):
    json_operation_id = UNSET
  else:
    json_operation_id = operation_id
  params["operation_id"] = json_operation_id

  json_since: None | str | Unset
  if isinstance(since, Unset):
    json_since = UNSET
  elif isinstance(since, datetime.datetime):
    json_since = since.isoformat()
  else:
    json_since = since
  params["since"] = json_since

  json_until: None | str | Unset
  if isinstance(until, Unset):
    json_until = UNSET
  elif isinstance(until, datetime.datetime):
    json_until = until.isoformat()
  else:
    json_until = until
  params["until"] = json_until

  json_cursor: None | str | Unset
  if isinstance(cursor, Unset):
    json_cursor = UNSET
  else:
    json_cursor = cursor
  params["cursor"] = json_cursor

  params["limit"] = limit

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/audit/mutations".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | MutationAuditListResponse | None:
  if response.status_code == 200:
    response_200 = MutationAuditListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | MutationAuditListResponse]:
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
  surface: ListGraphMutationsSurfaceType0 | None | Unset = UNSET,
  operation_name: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operation_id: None | str | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> Response[ErrorResponse | HTTPValidationError | MutationAuditListResponse]:
  """List Graph Mutations

   Every call that changed this graph, newest first: REST operations, external MCP clients, and in-app
  AI operator runs. Each entry names the operation, the outcome, who made it and with which
  credential, and the objects it touched. Arguments are not stored, only their SHA-256 fingerprint.
  Requires graph admin.

  Args:
      graph_id (str): Graph identifier
      surface (ListGraphMutationsSurfaceType0 | None | Unset): Only calls from this surface
      operation_name (None | str | Unset): Only this operation or MCP tool
      user_id (None | str | Unset): Only calls made as this user
      operation_id (None | str | Unset): Only calls from this REST operation or operator run
      since (datetime.datetime | None | Unset): Only calls at or after this time
      until (datetime.datetime | None | Unset): Only calls before this time
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Entries per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | MutationAuditListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    surface=surface,
    operation_name=operation_name,
    user_id=user_id,
    operation_id=operation_id,
    since=since,
    until=until,
    cursor=cursor,
    limit=limit,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  surface: ListGraphMutationsSurfaceType0 | None | Unset = UNSET,
  operation_name: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operation_id: None | str | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> ErrorResponse | HTTPValidationError | MutationAuditListResponse | None:
  """List Graph Mutations

   Every call that changed this graph, newest first: REST operations, external MCP clients, and in-app
  AI operator runs. Each entry names the operation, the outcome, who made it and with which
  credential, and the objects it touched. Arguments are not stored, only their SHA-256 fingerprint.
  Requires graph admin.

  Args:
      graph_id (str): Graph identifier
      surface (ListGraphMutationsSurfaceType0 | None | Unset): Only calls from this surface
      operation_name (None | str | Unset): Only this operation or MCP tool
      user_id (None | str | Unset): Only calls made as this user
      operation_id (None | str | Unset): Only calls from this REST operation or operator run
      since (datetime.datetime | None | Unset): Only calls at or after this time
      until (datetime.datetime | None | Unset): Only calls before this time
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Entries per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | MutationAuditListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    surface=surface,
    operation_name=operation_name,
    user_id=user_id,
    operation_id=operation_id,
    since=since,
    until=until,
    cursor=cursor,
    limit=limit,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  surface: ListGraphMutationsSurfaceType0 | None | Unset = UNSET,
  operation_name: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operation_id: None | str | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> Response[ErrorResponse | HTTPValidationError | MutationAuditListResponse]:
  """List Graph Mutations

   Every call that changed this graph, newest first: REST operations, external MCP clients, and in-app
  AI operator runs. Each entry names the operation, the outcome, who made it and with which
  credential, and the objects it touched. Arguments are not stored, only their SHA-256 fingerprint.
  Requires graph admin.

  Args:
      graph_id (str): Graph identifier
      surface (ListGraphMutationsSurfaceType0 | None | Unset): Only calls from this surface
      operation_name (None | str | Unset): Only this operation or MCP tool
      user_id (None | str | Unset): Only calls made as this user
      operation_id (None | str | Unset): Only calls from this REST operation or operator run
      since (datetime.datetime | None | Unset): Only calls at or after this time
      until (datetime.datetime | None | Unset): Only calls before this time
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Entries per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | MutationAuditListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    surface=surface,
    operation_name=operation_name,
    user_id=user_id,
    operation_id=operation_id,
    since=since,
    until=until,
    cursor=cursor,
    limit=limit,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  surface: ListGraphMutationsSurfaceType0 | None | Unset = UNSET,
  operation_name: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operation_id: None | str | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> ErrorResponse | HTTPValidationError | MutationAuditListResponse | None:
  """List Graph Mutations

   Every call that changed this graph, newest first: REST operations, external MCP clients, and in-app
  AI operator runs. Each entry names the operation, the outcome, who made it and with which
  credential, and the objects it touched. Arguments are not stored, only their SHA-256 fingerprint.
  Requires graph admin.

  Args:
      graph_id (str): Graph identifier
      surface (ListGraphMutationsSurfaceType0 | None | Unset): Only calls from this surface
      operation_name (None | str | Unset): Only this operation or MCP tool
      user_id (None | str | Unset): Only calls made as this user
      operation_id (None | str | Unset): Only calls from this REST operation or operator run
      since (datetime.datetime | None | Unset): Only calls at or after this time
      until (datetime.datetime | None | Unset): Only calls before this time
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Entries per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | MutationAuditListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      surface=surface,
      operation_name=operation_name,
      user_id=user_id,
      operation_id=operation_id,
      since=since,
      until=until,
      cursor=cursor,
      limit=limit,
    )
  ).parsed
