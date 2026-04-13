from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.truncate_schedule_request import TruncateScheduleRequest
from ...models.truncate_schedule_response import TruncateScheduleResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  structure_id: str,
  *,
  body: TruncateScheduleRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "patch",
    "url": "/v1/ledger/{graph_id}/schedules/{structure_id}/truncate".format(
      graph_id=quote(str(graph_id), safe=""),
      structure_id=quote(str(structure_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TruncateScheduleResponse | None:
  if response.status_code == 200:
    response_200 = TruncateScheduleResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TruncateScheduleResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  structure_id: str,
  *,
  client: AuthenticatedClient,
  body: TruncateScheduleRequest,
) -> Response[HTTPValidationError | TruncateScheduleResponse]:
  """Truncate Schedule (End Early)

   End a schedule early.

  Used for events that cut a schedule's lifespan short — an asset is sold,
  a prepaid is cancelled, a contract is terminated. Deletes all facts with
  `period_start > new_end_date` and any stale draft entries that were
  produced from them.

  Posted entries are preserved — if any period after `new_end_date` has a
  posted closing entry, the truncate fails with 422 and the caller must
  reopen that period first.

  The truncation is logged to the schedule's metadata for audit.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      body (TruncateScheduleRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | TruncateScheduleResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    structure_id=structure_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  structure_id: str,
  *,
  client: AuthenticatedClient,
  body: TruncateScheduleRequest,
) -> HTTPValidationError | TruncateScheduleResponse | None:
  """Truncate Schedule (End Early)

   End a schedule early.

  Used for events that cut a schedule's lifespan short — an asset is sold,
  a prepaid is cancelled, a contract is terminated. Deletes all facts with
  `period_start > new_end_date` and any stale draft entries that were
  produced from them.

  Posted entries are preserved — if any period after `new_end_date` has a
  posted closing entry, the truncate fails with 422 and the caller must
  reopen that period first.

  The truncation is logged to the schedule's metadata for audit.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      body (TruncateScheduleRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | TruncateScheduleResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    structure_id=structure_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  structure_id: str,
  *,
  client: AuthenticatedClient,
  body: TruncateScheduleRequest,
) -> Response[HTTPValidationError | TruncateScheduleResponse]:
  """Truncate Schedule (End Early)

   End a schedule early.

  Used for events that cut a schedule's lifespan short — an asset is sold,
  a prepaid is cancelled, a contract is terminated. Deletes all facts with
  `period_start > new_end_date` and any stale draft entries that were
  produced from them.

  Posted entries are preserved — if any period after `new_end_date` has a
  posted closing entry, the truncate fails with 422 and the caller must
  reopen that period first.

  The truncation is logged to the schedule's metadata for audit.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      body (TruncateScheduleRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | TruncateScheduleResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    structure_id=structure_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  structure_id: str,
  *,
  client: AuthenticatedClient,
  body: TruncateScheduleRequest,
) -> HTTPValidationError | TruncateScheduleResponse | None:
  """Truncate Schedule (End Early)

   End a schedule early.

  Used for events that cut a schedule's lifespan short — an asset is sold,
  a prepaid is cancelled, a contract is terminated. Deletes all facts with
  `period_start > new_end_date` and any stale draft entries that were
  produced from them.

  Posted entries are preserved — if any period after `new_end_date` has a
  posted closing entry, the truncate fails with 422 and the caller must
  reopen that period first.

  The truncation is logged to the schedule's metadata for audit.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      body (TruncateScheduleRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | TruncateScheduleResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      structure_id=structure_id,
      client=client,
      body=body,
    )
  ).parsed
