from http import HTTPStatus
from typing import Any
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
) -> ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile | None:
  if response.status_code == 200:
    response_200 = UpdateFileResponseUpdatefile.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

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

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]:
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
) -> Response[ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]:
  """Update File Status

   Setting `status=uploaded` validates the file in S3, calculates row count, and triggers DuckDB
  staging. Small files use direct staging; large files use a background Dagster job with an
  `operation_id` for SSE monitoring. Set `ingest_to_graph=true` to auto-chain graph materialization.

  Args:
      graph_id (str):
      file_id (str): File ID
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]
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
) -> ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile | None:
  """Update File Status

   Setting `status=uploaded` validates the file in S3, calculates row count, and triggers DuckDB
  staging. Small files use direct staging; large files use a background Dagster job with an
  `operation_id` for SSE monitoring. Set `ingest_to_graph=true` to auto-chain graph materialization.

  Args:
      graph_id (str):
      file_id (str): File ID
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile
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
) -> Response[ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]:
  """Update File Status

   Setting `status=uploaded` validates the file in S3, calculates row count, and triggers DuckDB
  staging. Small files use direct staging; large files use a background Dagster job with an
  `operation_id` for SSE monitoring. Set `ingest_to_graph=true` to auto-chain graph materialization.

  Args:
      graph_id (str):
      file_id (str): File ID
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile]
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
) -> ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile | None:
  """Update File Status

   Setting `status=uploaded` validates the file in S3, calculates row count, and triggers DuckDB
  staging. Small files use direct staging; large files use a background Dagster job with an
  `operation_id` for SSE monitoring. Set `ingest_to_graph=true` to auto-chain graph materialization.

  Args:
      graph_id (str):
      file_id (str): File ID
      body (FileStatusUpdate):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | UpdateFileResponseUpdatefile
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      file_id=file_id,
      client=client,
      body=body,
    )
  ).parsed
