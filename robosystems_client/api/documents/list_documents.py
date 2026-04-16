from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_list_response import DocumentListResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  source_type: None | str | Unset = UNSET,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  json_source_type: None | str | Unset
  if isinstance(source_type, Unset):
    json_source_type = UNSET
  else:
    json_source_type = source_type
  params["source_type"] = json_source_type

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/documents".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DocumentListResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = DocumentListResponse.from_dict(response.json())

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
) -> Response[DocumentListResponse | ErrorResponse | HTTPValidationError]:
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
  source_type: None | str | Unset = UNSET,
) -> Response[DocumentListResponse | ErrorResponse | HTTPValidationError]:
  """List Documents

  Args:
      graph_id (str):
      source_type (None | str | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[DocumentListResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    source_type=source_type,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  source_type: None | str | Unset = UNSET,
) -> DocumentListResponse | ErrorResponse | HTTPValidationError | None:
  """List Documents

  Args:
      graph_id (str):
      source_type (None | str | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      DocumentListResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    source_type=source_type,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  source_type: None | str | Unset = UNSET,
) -> Response[DocumentListResponse | ErrorResponse | HTTPValidationError]:
  """List Documents

  Args:
      graph_id (str):
      source_type (None | str | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[DocumentListResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    source_type=source_type,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  source_type: None | str | Unset = UNSET,
) -> DocumentListResponse | ErrorResponse | HTTPValidationError | None:
  """List Documents

  Args:
      graph_id (str):
      source_type (None | str | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      DocumentListResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      source_type=source_type,
    )
  ).parsed
