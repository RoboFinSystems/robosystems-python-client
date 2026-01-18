from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.save_view_request import SaveViewRequest
from ...models.save_view_response import SaveViewResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: SaveViewRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/views/save".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SaveViewResponse | None:
  if response.status_code == 200:
    response_200 = SaveViewResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SaveViewResponse]:
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
  body: SaveViewRequest,
) -> Response[HTTPValidationError | SaveViewResponse]:
  """Save View

   Save or update view as materialized report in the graph.

  Converts computed view results into persistent Report, Fact, and Structure nodes.
  This establishes what data exists in the subgraph, which then defines what
  needs to be exported for publishing to the parent graph.

  **Create Mode** (no report_id provided):
  - Generates new report_id from entity + period + report type
  - Creates new Report, Facts, and Structures

  **Update Mode** (report_id provided):
  - Deletes all existing Facts and Structures for the report
  - Updates Report metadata
  - Creates fresh Facts and Structures from current view
  - Useful for refreshing reports with updated data or view configurations

  **This is NOT publishing** - it only creates nodes in the subgraph workspace.
  Publishing (export → parquet → parent ingest) happens separately.

  Creates/Updates:
  - Report node with metadata
  - Fact nodes with all aspects (period, entity, element, unit)
  - PresentationStructure nodes (how facts are displayed)
  - CalculationStructure nodes (how facts roll up)

  Returns:
  - report_id: Unique identifier used as parquet export prefix
  - parquet_export_prefix: Filename prefix for future exports
  - All created facts and structures

  Args:
      graph_id (str):
      body (SaveViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | SaveViewResponse]
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
  body: SaveViewRequest,
) -> HTTPValidationError | SaveViewResponse | None:
  """Save View

   Save or update view as materialized report in the graph.

  Converts computed view results into persistent Report, Fact, and Structure nodes.
  This establishes what data exists in the subgraph, which then defines what
  needs to be exported for publishing to the parent graph.

  **Create Mode** (no report_id provided):
  - Generates new report_id from entity + period + report type
  - Creates new Report, Facts, and Structures

  **Update Mode** (report_id provided):
  - Deletes all existing Facts and Structures for the report
  - Updates Report metadata
  - Creates fresh Facts and Structures from current view
  - Useful for refreshing reports with updated data or view configurations

  **This is NOT publishing** - it only creates nodes in the subgraph workspace.
  Publishing (export → parquet → parent ingest) happens separately.

  Creates/Updates:
  - Report node with metadata
  - Fact nodes with all aspects (period, entity, element, unit)
  - PresentationStructure nodes (how facts are displayed)
  - CalculationStructure nodes (how facts roll up)

  Returns:
  - report_id: Unique identifier used as parquet export prefix
  - parquet_export_prefix: Filename prefix for future exports
  - All created facts and structures

  Args:
      graph_id (str):
      body (SaveViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | SaveViewResponse
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
  body: SaveViewRequest,
) -> Response[HTTPValidationError | SaveViewResponse]:
  """Save View

   Save or update view as materialized report in the graph.

  Converts computed view results into persistent Report, Fact, and Structure nodes.
  This establishes what data exists in the subgraph, which then defines what
  needs to be exported for publishing to the parent graph.

  **Create Mode** (no report_id provided):
  - Generates new report_id from entity + period + report type
  - Creates new Report, Facts, and Structures

  **Update Mode** (report_id provided):
  - Deletes all existing Facts and Structures for the report
  - Updates Report metadata
  - Creates fresh Facts and Structures from current view
  - Useful for refreshing reports with updated data or view configurations

  **This is NOT publishing** - it only creates nodes in the subgraph workspace.
  Publishing (export → parquet → parent ingest) happens separately.

  Creates/Updates:
  - Report node with metadata
  - Fact nodes with all aspects (period, entity, element, unit)
  - PresentationStructure nodes (how facts are displayed)
  - CalculationStructure nodes (how facts roll up)

  Returns:
  - report_id: Unique identifier used as parquet export prefix
  - parquet_export_prefix: Filename prefix for future exports
  - All created facts and structures

  Args:
      graph_id (str):
      body (SaveViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | SaveViewResponse]
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
  body: SaveViewRequest,
) -> HTTPValidationError | SaveViewResponse | None:
  """Save View

   Save or update view as materialized report in the graph.

  Converts computed view results into persistent Report, Fact, and Structure nodes.
  This establishes what data exists in the subgraph, which then defines what
  needs to be exported for publishing to the parent graph.

  **Create Mode** (no report_id provided):
  - Generates new report_id from entity + period + report type
  - Creates new Report, Facts, and Structures

  **Update Mode** (report_id provided):
  - Deletes all existing Facts and Structures for the report
  - Updates Report metadata
  - Creates fresh Facts and Structures from current view
  - Useful for refreshing reports with updated data or view configurations

  **This is NOT publishing** - it only creates nodes in the subgraph workspace.
  Publishing (export → parquet → parent ingest) happens separately.

  Creates/Updates:
  - Report node with metadata
  - Fact nodes with all aspects (period, entity, element, unit)
  - PresentationStructure nodes (how facts are displayed)
  - CalculationStructure nodes (how facts roll up)

  Returns:
  - report_id: Unique identifier used as parquet export prefix
  - parquet_export_prefix: Filename prefix for future exports
  - All created facts and structures

  Args:
      graph_id (str):
      body (SaveViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | SaveViewResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
