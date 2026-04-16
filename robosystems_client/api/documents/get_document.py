from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_detail_response import DocumentDetailResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  document_id: str,
) -> dict[str, Any]:

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/documents/{document_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      document_id=quote(str(document_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DocumentDetailResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = DocumentDetailResponse.from_dict(response.json())

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
) -> Response[DocumentDetailResponse | HTTPValidationError]:
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
) -> Response[DocumentDetailResponse | HTTPValidationError]:
  """Get Document

   Get a document with full content from PostgreSQL.

  Args:
      graph_id (str):
      document_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[DocumentDetailResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    document_id=document_id,
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
) -> DocumentDetailResponse | HTTPValidationError | None:
  """Get Document

   Get a document with full content from PostgreSQL.

  Args:
      graph_id (str):
      document_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      DocumentDetailResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    document_id=document_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  document_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[DocumentDetailResponse | HTTPValidationError]:
  """Get Document

   Get a document with full content from PostgreSQL.

  Args:
      graph_id (str):
      document_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[DocumentDetailResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    document_id=document_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  document_id: str,
  *,
  client: AuthenticatedClient,
) -> DocumentDetailResponse | HTTPValidationError | None:
  """Get Document

   Get a document with full content from PostgreSQL.

  Args:
      graph_id (str):
      document_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      DocumentDetailResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      document_id=document_id,
      client=client,
    )
  ).parsed
