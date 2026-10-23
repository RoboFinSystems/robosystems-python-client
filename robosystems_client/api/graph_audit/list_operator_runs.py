import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_operator_runs_status_type_0 import ListOperatorRunsStatusType0
from ...models.operator_run_list_response import OperatorRunListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  thread_id: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operator_type: None | str | Unset = UNSET,
  status: ListOperatorRunsStatusType0 | None | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  json_thread_id: None | str | Unset
  if isinstance(thread_id, Unset):
    json_thread_id = UNSET
  else:
    json_thread_id = thread_id
  params["thread_id"] = json_thread_id

  json_user_id: None | str | Unset
  if isinstance(user_id, Unset):
    json_user_id = UNSET
  else:
    json_user_id = user_id
  params["user_id"] = json_user_id

  json_operator_type: None | str | Unset
  if isinstance(operator_type, Unset):
    json_operator_type = UNSET
  else:
    json_operator_type = operator_type
  params["operator_type"] = json_operator_type

  json_status: None | str | Unset
  if isinstance(status, Unset):
    json_status = UNSET
  elif isinstance(status, ListOperatorRunsStatusType0):
    json_status = status.value
  else:
    json_status = status
  params["status"] = json_status

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
    "url": "/v1/graphs/{graph_id}/audit/runs".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | OperatorRunListResponse | None:
  if response.status_code == 200:
    response_200 = OperatorRunListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | OperatorRunListResponse]:
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
  thread_id: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operator_type: None | str | Unset = UNSET,
  status: ListOperatorRunsStatusType0 | None | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> Response[ErrorResponse | HTTPValidationError | OperatorRunListResponse]:
  """List Operator Runs

   The in-app AI operator runs made on this graph, newest first: each run's question, answer, outcome,
  cost and the tools it called. This is the record behind a mutation audit entry's `operation_id`,
  kept after the operation itself has expired. A graph admin sees every user's runs; any other member
  sees their own. Filter by `thread_id` for one conversation.

  Args:
      graph_id (str): Graph identifier
      thread_id (None | str | Unset): Only the runs of this thread
      user_id (None | str | Unset): Only runs made as this user (admins; members see their own)
      operator_type (None | str | Unset): Only runs of this operator
      status (ListOperatorRunsStatusType0 | None | Unset): Only runs that ended this way
      since (datetime.datetime | None | Unset): Only runs started at or after this time
      until (datetime.datetime | None | Unset): Only runs started before this time
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Runs per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | OperatorRunListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    thread_id=thread_id,
    user_id=user_id,
    operator_type=operator_type,
    status=status,
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
  thread_id: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operator_type: None | str | Unset = UNSET,
  status: ListOperatorRunsStatusType0 | None | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> ErrorResponse | HTTPValidationError | OperatorRunListResponse | None:
  """List Operator Runs

   The in-app AI operator runs made on this graph, newest first: each run's question, answer, outcome,
  cost and the tools it called. This is the record behind a mutation audit entry's `operation_id`,
  kept after the operation itself has expired. A graph admin sees every user's runs; any other member
  sees their own. Filter by `thread_id` for one conversation.

  Args:
      graph_id (str): Graph identifier
      thread_id (None | str | Unset): Only the runs of this thread
      user_id (None | str | Unset): Only runs made as this user (admins; members see their own)
      operator_type (None | str | Unset): Only runs of this operator
      status (ListOperatorRunsStatusType0 | None | Unset): Only runs that ended this way
      since (datetime.datetime | None | Unset): Only runs started at or after this time
      until (datetime.datetime | None | Unset): Only runs started before this time
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Runs per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | OperatorRunListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    thread_id=thread_id,
    user_id=user_id,
    operator_type=operator_type,
    status=status,
    since=since,
    until=until,
    cursor=cursor,
    limit=limit,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  thread_id: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operator_type: None | str | Unset = UNSET,
  status: ListOperatorRunsStatusType0 | None | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> Response[ErrorResponse | HTTPValidationError | OperatorRunListResponse]:
  """List Operator Runs

   The in-app AI operator runs made on this graph, newest first: each run's question, answer, outcome,
  cost and the tools it called. This is the record behind a mutation audit entry's `operation_id`,
  kept after the operation itself has expired. A graph admin sees every user's runs; any other member
  sees their own. Filter by `thread_id` for one conversation.

  Args:
      graph_id (str): Graph identifier
      thread_id (None | str | Unset): Only the runs of this thread
      user_id (None | str | Unset): Only runs made as this user (admins; members see their own)
      operator_type (None | str | Unset): Only runs of this operator
      status (ListOperatorRunsStatusType0 | None | Unset): Only runs that ended this way
      since (datetime.datetime | None | Unset): Only runs started at or after this time
      until (datetime.datetime | None | Unset): Only runs started before this time
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Runs per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | OperatorRunListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    thread_id=thread_id,
    user_id=user_id,
    operator_type=operator_type,
    status=status,
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
  thread_id: None | str | Unset = UNSET,
  user_id: None | str | Unset = UNSET,
  operator_type: None | str | Unset = UNSET,
  status: ListOperatorRunsStatusType0 | None | Unset = UNSET,
  since: datetime.datetime | None | Unset = UNSET,
  until: datetime.datetime | None | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> ErrorResponse | HTTPValidationError | OperatorRunListResponse | None:
  """List Operator Runs

   The in-app AI operator runs made on this graph, newest first: each run's question, answer, outcome,
  cost and the tools it called. This is the record behind a mutation audit entry's `operation_id`,
  kept after the operation itself has expired. A graph admin sees every user's runs; any other member
  sees their own. Filter by `thread_id` for one conversation.

  Args:
      graph_id (str): Graph identifier
      thread_id (None | str | Unset): Only the runs of this thread
      user_id (None | str | Unset): Only runs made as this user (admins; members see their own)
      operator_type (None | str | Unset): Only runs of this operator
      status (ListOperatorRunsStatusType0 | None | Unset): Only runs that ended this way
      since (datetime.datetime | None | Unset): Only runs started at or after this time
      until (datetime.datetime | None | Unset): Only runs started before this time
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Runs per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | OperatorRunListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      thread_id=thread_id,
      user_id=user_id,
      operator_type=operator_type,
      status=status,
      since=since,
      until=until,
      cursor=cursor,
      limit=limit,
    )
  ).parsed
