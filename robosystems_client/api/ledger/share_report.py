from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.share_report_request import ShareReportRequest
from ...models.share_report_response import ShareReportResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  report_id: str,
  *,
  body: ShareReportRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/ledger/{graph_id}/reports/{report_id}/share".format(
      graph_id=quote(str(graph_id), safe=""),
      report_id=quote(str(report_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ShareReportResponse | None:
  if response.status_code == 200:
    response_200 = ShareReportResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ShareReportResponse]:
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
  body: ShareReportRequest,
) -> Response[HTTPValidationError | ShareReportResponse]:
  """Share Report

   Share a published report to other graphs.

  Copies the report definition and its generated facts to each target graph's
  tenant schema. The target graph must have 'roboledger' in its schema_extensions.
  This is a snapshot — the target gets an immutable copy of the facts at this
  point in time.

  Args:
      graph_id (str):
      report_id (str): Report definition ID
      body (ShareReportRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | ShareReportResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    report_id=report_id,
    body=body,
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
  body: ShareReportRequest,
) -> HTTPValidationError | ShareReportResponse | None:
  """Share Report

   Share a published report to other graphs.

  Copies the report definition and its generated facts to each target graph's
  tenant schema. The target graph must have 'roboledger' in its schema_extensions.
  This is a snapshot — the target gets an immutable copy of the facts at this
  point in time.

  Args:
      graph_id (str):
      report_id (str): Report definition ID
      body (ShareReportRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | ShareReportResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    report_id=report_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
  body: ShareReportRequest,
) -> Response[HTTPValidationError | ShareReportResponse]:
  """Share Report

   Share a published report to other graphs.

  Copies the report definition and its generated facts to each target graph's
  tenant schema. The target graph must have 'roboledger' in its schema_extensions.
  This is a snapshot — the target gets an immutable copy of the facts at this
  point in time.

  Args:
      graph_id (str):
      report_id (str): Report definition ID
      body (ShareReportRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | ShareReportResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    report_id=report_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
  body: ShareReportRequest,
) -> HTTPValidationError | ShareReportResponse | None:
  """Share Report

   Share a published report to other graphs.

  Copies the report definition and its generated facts to each target graph's
  tenant schema. The target graph must have 'roboledger' in its schema_extensions.
  This is a snapshot — the target gets an immutable copy of the facts at this
  point in time.

  Args:
      graph_id (str):
      report_id (str): Report definition ID
      body (ShareReportRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | ShareReportResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      report_id=report_id,
      client=client,
      body=body,
    )
  ).parsed
