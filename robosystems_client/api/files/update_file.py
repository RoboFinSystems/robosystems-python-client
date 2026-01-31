from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.file_status_update import FileStatusUpdate
from ...models.http_validation_error import HTTPValidationError
from ...models.update_file_response_updatefile import UpdateFileResponseUpdatefile
from ...types import Response


def _get_kwargs(
  graph_id: str,
  file_id: str,
  *,
  body: FileStatusUpdate,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "patch",
    "url": "/v1/graphs/{graph_id}/files/{file_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      file_id=quote(str(file_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile | None:
  if response.status_code == 200:
    response_200 = UpdateFileResponseUpdatefile.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = cast(Any, None)
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

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileStatusUpdate,
) -> Response[Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]:
  """Update File Status

   Update file status and trigger processing.

  Update file status after upload completion. Setting status='uploaded' triggers
  immediate DuckDB staging and optional graph ingestion.

  **Request Body:**
  - `status`: New status (uploaded, disabled, failed)
  - `ingest_to_graph` (optional): If true, auto-ingest to graph after DuckDB staging

  **What Happens (status='uploaded'):**
  1. File validated in S3
  2. Row count calculated
  3. DuckDB staging triggered immediately (background task)
  4. If ingest_to_graph=true, graph ingestion queued
  5. File queryable in DuckDB within seconds

  **Use Cases:**
  - Signal upload completion
  - Trigger immediate DuckDB staging
  - Enable/disable files
  - Mark failed uploads

  **Important:**
  - Files must exist in S3 before marking uploaded
  - DuckDB staging happens asynchronously
  - Graph ingestion is optional (ingest_to_graph flag)

  Args:
      graph_id (str):
      file_id (str): File ID
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileStatusUpdate,
) -> Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile | None:
  """Update File Status

   Update file status and trigger processing.

  Update file status after upload completion. Setting status='uploaded' triggers
  immediate DuckDB staging and optional graph ingestion.

  **Request Body:**
  - `status`: New status (uploaded, disabled, failed)
  - `ingest_to_graph` (optional): If true, auto-ingest to graph after DuckDB staging

  **What Happens (status='uploaded'):**
  1. File validated in S3
  2. Row count calculated
  3. DuckDB staging triggered immediately (background task)
  4. If ingest_to_graph=true, graph ingestion queued
  5. File queryable in DuckDB within seconds

  **Use Cases:**
  - Signal upload completion
  - Trigger immediate DuckDB staging
  - Enable/disable files
  - Mark failed uploads

  **Important:**
  - Files must exist in S3 before marking uploaded
  - DuckDB staging happens asynchronously
  - Graph ingestion is optional (ingest_to_graph flag)

  Args:
      graph_id (str):
      file_id (str): File ID
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile
  """

  return sync_detailed(
    graph_id=graph_id,
    file_id=file_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileStatusUpdate,
) -> Response[Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]:
  """Update File Status

   Update file status and trigger processing.

  Update file status after upload completion. Setting status='uploaded' triggers
  immediate DuckDB staging and optional graph ingestion.

  **Request Body:**
  - `status`: New status (uploaded, disabled, failed)
  - `ingest_to_graph` (optional): If true, auto-ingest to graph after DuckDB staging

  **What Happens (status='uploaded'):**
  1. File validated in S3
  2. Row count calculated
  3. DuckDB staging triggered immediately (background task)
  4. If ingest_to_graph=true, graph ingestion queued
  5. File queryable in DuckDB within seconds

  **Use Cases:**
  - Signal upload completion
  - Trigger immediate DuckDB staging
  - Enable/disable files
  - Mark failed uploads

  **Important:**
  - Files must exist in S3 before marking uploaded
  - DuckDB staging happens asynchronously
  - Graph ingestion is optional (ingest_to_graph flag)

  Args:
      graph_id (str):
      file_id (str): File ID
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    file_id=file_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  file_id: str,
  *,
  client: AuthenticatedClient,
  body: FileStatusUpdate,
) -> Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile | None:
  """Update File Status

   Update file status and trigger processing.

  Update file status after upload completion. Setting status='uploaded' triggers
  immediate DuckDB staging and optional graph ingestion.

  **Request Body:**
  - `status`: New status (uploaded, disabled, failed)
  - `ingest_to_graph` (optional): If true, auto-ingest to graph after DuckDB staging

  **What Happens (status='uploaded'):**
  1. File validated in S3
  2. Row count calculated
  3. DuckDB staging triggered immediately (background task)
  4. If ingest_to_graph=true, graph ingestion queued
  5. File queryable in DuckDB within seconds

  **Use Cases:**
  - Signal upload completion
  - Trigger immediate DuckDB staging
  - Enable/disable files
  - Mark failed uploads

  **Important:**
  - Files must exist in S3 before marking uploaded
  - DuckDB staging happens asynchronously
  - Graph ingestion is optional (ingest_to_graph flag)

  Args:
      graph_id (str):
      file_id (str): File ID
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      file_id=file_id,
      client=client,
      body=body,
    )
  ).parsed
