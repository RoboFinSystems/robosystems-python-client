from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.operator_thread_list_response import OperatorThreadListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  user_id: None | str | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  json_user_id: None | str | Unset
  if isinstance(user_id, Unset):
    json_user_id = UNSET
  else:
    json_user_id = user_id
  params["user_id"] = json_user_id

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
    "url": "/v1/graphs/{graph_id}/audit/threads".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | OperatorThreadListResponse | None:
  if response.status_code == 200:
    response_200 = OperatorThreadListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | OperatorThreadListResponse]:
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
  user_id: None | str | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> Response[ErrorResponse | HTTPValidationError | OperatorThreadListResponse]:
  """List Operator Threads

   The conversations held with this graph's AI operators, most recently active first: every run made
  under a `thread_id` grouped by it, with the first question as the title. A graph admin sees every
  user's threads; any other member sees their own. Open a thread's runs at `/audit/runs`.

  Args:
      graph_id (str): Graph identifier
      user_id (None | str | Unset): Only this user's threads (admins; members see their own)
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Threads per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | OperatorThreadListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    user_id=user_id,
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
  user_id: None | str | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> ErrorResponse | HTTPValidationError | OperatorThreadListResponse | None:
  """List Operator Threads

   The conversations held with this graph's AI operators, most recently active first: every run made
  under a `thread_id` grouped by it, with the first question as the title. A graph admin sees every
  user's threads; any other member sees their own. Open a thread's runs at `/audit/runs`.

  Args:
      graph_id (str): Graph identifier
      user_id (None | str | Unset): Only this user's threads (admins; members see their own)
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Threads per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | OperatorThreadListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    user_id=user_id,
    cursor=cursor,
    limit=limit,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  user_id: None | str | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> Response[ErrorResponse | HTTPValidationError | OperatorThreadListResponse]:
  """List Operator Threads

   The conversations held with this graph's AI operators, most recently active first: every run made
  under a `thread_id` grouped by it, with the first question as the title. A graph admin sees every
  user's threads; any other member sees their own. Open a thread's runs at `/audit/runs`.

  Args:
      graph_id (str): Graph identifier
      user_id (None | str | Unset): Only this user's threads (admins; members see their own)
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Threads per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | OperatorThreadListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    user_id=user_id,
    cursor=cursor,
    limit=limit,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  user_id: None | str | Unset = UNSET,
  cursor: None | str | Unset = UNSET,
  limit: int | Unset = 50,
) -> ErrorResponse | HTTPValidationError | OperatorThreadListResponse | None:
  """List Operator Threads

   The conversations held with this graph's AI operators, most recently active first: every run made
  under a `thread_id` grouped by it, with the first question as the title. A graph admin sees every
  user's threads; any other member sees their own. Open a thread's runs at `/audit/runs`.

  Args:
      graph_id (str): Graph identifier
      user_id (None | str | Unset): Only this user's threads (admins; members see their own)
      cursor (None | str | Unset): The `next_cursor` of the previous page
      limit (int | Unset): Threads per page Default: 50.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | OperatorThreadListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      user_id=user_id,
      cursor=cursor,
      limit=limit,
    )
  ).parsed
