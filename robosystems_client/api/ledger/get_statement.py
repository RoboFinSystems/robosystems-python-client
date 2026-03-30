from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.statement_response import StatementResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  report_id: str,
  structure_type: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/reports/{report_id}/statements/{structure_type}".format(
      graph_id=quote(str(graph_id), safe=""),
      report_id=quote(str(report_id), safe=""),
      structure_type=quote(str(structure_type), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | StatementResponse | None:
  if response.status_code == 200:
    response_200 = StatementResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | StatementResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  report_id: str,
  structure_type: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | StatementResponse]:
  """Get Statement

   Render a financial statement — facts viewed through a structure's hierarchy.

  Same report, different structure_type = different view (IS, BS, CF).

  Args:
      graph_id (str):
      report_id (str): Report definition ID
      structure_type (str): Structure type: income_statement, balance_sheet, cash_flow_statement

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | StatementResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    report_id=report_id,
    structure_type=structure_type,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  report_id: str,
  structure_type: str,
  *,
  client: AuthenticatedClient,
) -> HTTPValidationError | StatementResponse | None:
  """Get Statement

   Render a financial statement — facts viewed through a structure's hierarchy.

  Same report, different structure_type = different view (IS, BS, CF).

  Args:
      graph_id (str):
      report_id (str): Report definition ID
      structure_type (str): Structure type: income_statement, balance_sheet, cash_flow_statement

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | StatementResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    report_id=report_id,
    structure_type=structure_type,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  report_id: str,
  structure_type: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | StatementResponse]:
  """Get Statement

   Render a financial statement — facts viewed through a structure's hierarchy.

  Same report, different structure_type = different view (IS, BS, CF).

  Args:
      graph_id (str):
      report_id (str): Report definition ID
      structure_type (str): Structure type: income_statement, balance_sheet, cash_flow_statement

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | StatementResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    report_id=report_id,
    structure_type=structure_type,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  report_id: str,
  structure_type: str,
  *,
  client: AuthenticatedClient,
) -> HTTPValidationError | StatementResponse | None:
  """Get Statement

   Render a financial statement — facts viewed through a structure's hierarchy.

  Same report, different structure_type = different view (IS, BS, CF).

  Args:
      graph_id (str):
      report_id (str): Report definition ID
      structure_type (str): Structure type: income_statement, balance_sheet, cash_flow_statement

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | StatementResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      report_id=report_id,
      structure_type=structure_type,
      client=client,
    )
  ).parsed
