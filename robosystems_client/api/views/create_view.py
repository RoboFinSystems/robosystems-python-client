from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_view_request import CreateViewRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: CreateViewRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/views".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
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
  body: CreateViewRequest,
) -> Response[Any | HTTPValidationError]:
  """Create View

   Generate financial report view from data source (dual-mode support).

  **Mode 1: Transaction Aggregation (generate_from_transactions)**
  - Aggregates raw transaction data to trial balance
  - Creates facts on-demand
  - Shows real-time reporting from source of truth

  **Mode 2: Existing Facts (pivot_existing_facts)**
  - Queries existing Fact nodes
  - Supports multi-dimensional analysis
  - Works with SEC filings and pre-computed facts

  Both modes:
  - Build FactGrid from data
  - Generate pivot table presentation
  - Return consistent response format

  Args:
      graph_id (str):
      body (CreateViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError]
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
  body: CreateViewRequest,
) -> Any | HTTPValidationError | None:
  """Create View

   Generate financial report view from data source (dual-mode support).

  **Mode 1: Transaction Aggregation (generate_from_transactions)**
  - Aggregates raw transaction data to trial balance
  - Creates facts on-demand
  - Shows real-time reporting from source of truth

  **Mode 2: Existing Facts (pivot_existing_facts)**
  - Queries existing Fact nodes
  - Supports multi-dimensional analysis
  - Works with SEC filings and pre-computed facts

  Both modes:
  - Build FactGrid from data
  - Generate pivot table presentation
  - Return consistent response format

  Args:
      graph_id (str):
      body (CreateViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError
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
  body: CreateViewRequest,
) -> Response[Any | HTTPValidationError]:
  """Create View

   Generate financial report view from data source (dual-mode support).

  **Mode 1: Transaction Aggregation (generate_from_transactions)**
  - Aggregates raw transaction data to trial balance
  - Creates facts on-demand
  - Shows real-time reporting from source of truth

  **Mode 2: Existing Facts (pivot_existing_facts)**
  - Queries existing Fact nodes
  - Supports multi-dimensional analysis
  - Works with SEC filings and pre-computed facts

  Both modes:
  - Build FactGrid from data
  - Generate pivot table presentation
  - Return consistent response format

  Args:
      graph_id (str):
      body (CreateViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError]
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
  body: CreateViewRequest,
) -> Any | HTTPValidationError | None:
  """Create View

   Generate financial report view from data source (dual-mode support).

  **Mode 1: Transaction Aggregation (generate_from_transactions)**
  - Aggregates raw transaction data to trial balance
  - Creates facts on-demand
  - Shows real-time reporting from source of truth

  **Mode 2: Existing Facts (pivot_existing_facts)**
  - Queries existing Fact nodes
  - Supports multi-dimensional analysis
  - Works with SEC filings and pre-computed facts

  Both modes:
  - Build FactGrid from data
  - Generate pivot table presentation
  - Return consistent response format

  Args:
      graph_id (str):
      body (CreateViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
