from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_association_request import CreateAssociationRequest
from ...models.element_association_response import ElementAssociationResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  mapping_id: str,
  *,
  body: CreateAssociationRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/ledger/{graph_id}/mappings/{mapping_id}/associations".format(
      graph_id=quote(str(graph_id), safe=""),
      mapping_id=quote(str(mapping_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ElementAssociationResponse | HTTPValidationError | None:
  if response.status_code == 201:
    response_201 = ElementAssociationResponse.from_dict(response.json())

    return response_201

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ElementAssociationResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  mapping_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateAssociationRequest,
) -> Response[ElementAssociationResponse | HTTPValidationError]:
  """Create Mapping Association

   Add a mapping association (CoA element → reporting concept).

  Args:
      graph_id (str):
      mapping_id (str):
      body (CreateAssociationRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ElementAssociationResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    mapping_id=mapping_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  mapping_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateAssociationRequest,
) -> ElementAssociationResponse | HTTPValidationError | None:
  """Create Mapping Association

   Add a mapping association (CoA element → reporting concept).

  Args:
      graph_id (str):
      mapping_id (str):
      body (CreateAssociationRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ElementAssociationResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    mapping_id=mapping_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  mapping_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateAssociationRequest,
) -> Response[ElementAssociationResponse | HTTPValidationError]:
  """Create Mapping Association

   Add a mapping association (CoA element → reporting concept).

  Args:
      graph_id (str):
      mapping_id (str):
      body (CreateAssociationRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ElementAssociationResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    mapping_id=mapping_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  mapping_id: str,
  *,
  client: AuthenticatedClient,
  body: CreateAssociationRequest,
) -> ElementAssociationResponse | HTTPValidationError | None:
  """Create Mapping Association

   Add a mapping association (CoA element → reporting concept).

  Args:
      graph_id (str):
      mapping_id (str):
      body (CreateAssociationRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ElementAssociationResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      mapping_id=mapping_id,
      client=client,
      body=body,
    )
  ).parsed
