from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_update_request import DocumentUpdateRequest
from ...models.document_upload_response import DocumentUploadResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  document_id: str,
  *,
  body: DocumentUpdateRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "put",
    "url": "/v1/graphs/{graph_id}/documents/{document_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      document_id=quote(str(document_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DocumentUploadResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = DocumentUploadResponse.from_dict(response.json())

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
) -> Response[DocumentUploadResponse | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  document_id: str,
  *,
  client: AuthenticatedClient,
  body: DocumentUpdateRequest,
) -> Response[DocumentUploadResponse | ErrorResponse | HTTPValidationError]:
  """Update Document

   Updates content and/or metadata. Re-syncs to OpenSearch.

  Args:
      graph_id (str):
      document_id (str):
      body (DocumentUpdateRequest): Update a document's metadata and/or content.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[DocumentUploadResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    document_id=document_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  document_id: str,
  *,
  client: AuthenticatedClient,
  body: DocumentUpdateRequest,
) -> DocumentUploadResponse | ErrorResponse | HTTPValidationError | None:
  """Update Document

   Updates content and/or metadata. Re-syncs to OpenSearch.

  Args:
      graph_id (str):
      document_id (str):
      body (DocumentUpdateRequest): Update a document's metadata and/or content.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      DocumentUploadResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    document_id=document_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  document_id: str,
  *,
  client: AuthenticatedClient,
  body: DocumentUpdateRequest,
) -> Response[DocumentUploadResponse | ErrorResponse | HTTPValidationError]:
  """Update Document

   Updates content and/or metadata. Re-syncs to OpenSearch.

  Args:
      graph_id (str):
      document_id (str):
      body (DocumentUpdateRequest): Update a document's metadata and/or content.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[DocumentUploadResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    document_id=document_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  document_id: str,
  *,
  client: AuthenticatedClient,
  body: DocumentUpdateRequest,
) -> DocumentUploadResponse | ErrorResponse | HTTPValidationError | None:
  """Update Document

   Updates content and/or metadata. Re-syncs to OpenSearch.

  Args:
      graph_id (str):
      document_id (str):
      body (DocumentUpdateRequest): Update a document's metadata and/or content.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      DocumentUploadResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      document_id=document_id,
      client=client,
      body=body,
    )
  ).parsed
