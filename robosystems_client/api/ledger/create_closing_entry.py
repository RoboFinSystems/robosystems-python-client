from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.closing_entry_response import ClosingEntryResponse
from ...models.create_closing_entry_request import CreateClosingEntryRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  structure_id: str,
  *,
  body: CreateClosingEntryRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/ledger/{graph_id}/schedules/{structure_id}/closing-entry".format(
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
) -> ClosingEntryResponse | HTTPValidationError | None:
  if response.status_code == 201:
    response_201 = ClosingEntryResponse.from_dict(response.json())

    return response_201

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ClosingEntryResponse | HTTPValidationError]:
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
  body: CreateClosingEntryRequest,
) -> Response[ClosingEntryResponse | HTTPValidationError]:
  """Create Closing Entry

   Create a draft closing entry from a schedule's facts for a period.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      body (CreateClosingEntryRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ClosingEntryResponse | HTTPValidationError]
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
  body: CreateClosingEntryRequest,
) -> ClosingEntryResponse | HTTPValidationError | None:
  """Create Closing Entry

   Create a draft closing entry from a schedule's facts for a period.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      body (CreateClosingEntryRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ClosingEntryResponse | HTTPValidationError
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
  body: CreateClosingEntryRequest,
) -> Response[ClosingEntryResponse | HTTPValidationError]:
  """Create Closing Entry

   Create a draft closing entry from a schedule's facts for a period.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      body (CreateClosingEntryRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ClosingEntryResponse | HTTPValidationError]
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
  body: CreateClosingEntryRequest,
) -> ClosingEntryResponse | HTTPValidationError | None:
  """Create Closing Entry

   Create a draft closing entry from a schedule's facts for a period.

  Args:
      graph_id (str):
      structure_id (str): Schedule structure ID
      body (CreateClosingEntryRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ClosingEntryResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      structure_id=structure_id,
      client=client,
      body=body,
    )
  ).parsed
