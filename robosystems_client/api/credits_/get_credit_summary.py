from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credit_summary_response import CreditSummaryResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/credits/summary".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreditSummaryResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = CreditSummaryResponse.from_dict(response.json())

    return response_200

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreditSummaryResponse | ErrorResponse | HTTPValidationError]:
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
) -> Response[CreditSummaryResponse | ErrorResponse | HTTPValidationError]:
  """Get Credit Summary

   Retrieve comprehensive credit usage summary for the specified graph.

  This endpoint provides:
  - Current credit balance and monthly allocation
  - Credit consumption metrics for the current month
  - Graph tier and credit multiplier information
  - Usage percentage to help monitor credit consumption

  No credits are consumed for checking credit status.

  Args:
      graph_id (str): Graph database identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[CreditSummaryResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> CreditSummaryResponse | ErrorResponse | HTTPValidationError | None:
  """Get Credit Summary

   Retrieve comprehensive credit usage summary for the specified graph.

  This endpoint provides:
  - Current credit balance and monthly allocation
  - Credit consumption metrics for the current month
  - Graph tier and credit multiplier information
  - Usage percentage to help monitor credit consumption

  No credits are consumed for checking credit status.

  Args:
      graph_id (str): Graph database identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      CreditSummaryResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[CreditSummaryResponse | ErrorResponse | HTTPValidationError]:
  """Get Credit Summary

   Retrieve comprehensive credit usage summary for the specified graph.

  This endpoint provides:
  - Current credit balance and monthly allocation
  - Credit consumption metrics for the current month
  - Graph tier and credit multiplier information
  - Usage percentage to help monitor credit consumption

  No credits are consumed for checking credit status.

  Args:
      graph_id (str): Graph database identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[CreditSummaryResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> CreditSummaryResponse | ErrorResponse | HTTPValidationError | None:
  """Get Credit Summary

   Retrieve comprehensive credit usage summary for the specified graph.

  This endpoint provides:
  - Current credit balance and monthly allocation
  - Credit consumption metrics for the current month
  - Graph tier and credit multiplier information
  - Usage percentage to help monitor credit consumption

  No credits are consumed for checking credit status.

  Args:
      graph_id (str): Graph database identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      CreditSummaryResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
