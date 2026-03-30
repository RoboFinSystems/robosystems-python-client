from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.report_response import ReportResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  report_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/reports/{report_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      report_id=quote(str(report_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ReportResponse | None:
  if response.status_code == 200:
    response_200 = ReportResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ReportResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | ReportResponse]:
  """Get Report

   Get a report definition with its available structures.

  Args:
      graph_id (str):
      report_id (str): Report definition ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | ReportResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    report_id=report_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
) -> HTTPValidationError | ReportResponse | None:
  """Get Report

   Get a report definition with its available structures.

  Args:
      graph_id (str):
      report_id (str): Report definition ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | ReportResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    report_id=report_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | ReportResponse]:
  """Get Report

   Get a report definition with its available structures.

  Args:
      graph_id (str):
      report_id (str): Report definition ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | ReportResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    report_id=report_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
) -> HTTPValidationError | ReportResponse | None:
  """Get Report

   Get a report definition with its available structures.

  Args:
      graph_id (str):
      report_id (str): Report definition ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | ReportResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      report_id=report_id,
      client=client,
    )
  ).parsed
