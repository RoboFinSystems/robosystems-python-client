from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fiscal_calendar_response import FiscalCalendarResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.set_close_target_request import SetCloseTargetRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: SetCloseTargetRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/ledger/{graph_id}/fiscal-calendar/close-target".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FiscalCalendarResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = FiscalCalendarResponse.from_dict(response.json())

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
) -> Response[FiscalCalendarResponse | HTTPValidationError]:
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
  body: SetCloseTargetRequest,
) -> Response[FiscalCalendarResponse | HTTPValidationError]:
  """Set Close Target

   Set the close target for a graph.

  Validates that the target is a real YYYY-MM period, is not in the future,
  and is not before the current `closed_through`. Emits a `target_changed`
  audit event. Returns the updated calendar state.

  Args:
      graph_id (str):
      body (SetCloseTargetRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[FiscalCalendarResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: SetCloseTargetRequest,
) -> FiscalCalendarResponse | HTTPValidationError | None:
  """Set Close Target

   Set the close target for a graph.

  Validates that the target is a real YYYY-MM period, is not in the future,
  and is not before the current `closed_through`. Emits a `target_changed`
  audit event. Returns the updated calendar state.

  Args:
      graph_id (str):
      body (SetCloseTargetRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      FiscalCalendarResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: SetCloseTargetRequest,
) -> Response[FiscalCalendarResponse | HTTPValidationError]:
  """Set Close Target

   Set the close target for a graph.

  Validates that the target is a real YYYY-MM period, is not in the future,
  and is not before the current `closed_through`. Emits a `target_changed`
  audit event. Returns the updated calendar state.

  Args:
      graph_id (str):
      body (SetCloseTargetRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[FiscalCalendarResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: SetCloseTargetRequest,
) -> FiscalCalendarResponse | HTTPValidationError | None:
  """Set Close Target

   Set the close target for a graph.

  Validates that the target is a real YYYY-MM period, is not in the future,
  and is not before the current `closed_through`. Emits a `target_changed`
  audit event. Returns the updated calendar state.

  Args:
      graph_id (str):
      body (SetCloseTargetRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      FiscalCalendarResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
