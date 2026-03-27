from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ledger_entity_response import LedgerEntityResponse
from ...models.update_entity_request import UpdateEntityRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: UpdateEntityRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "put",
    "url": "/v1/ledger/{graph_id}/entity".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LedgerEntityResponse | None:
  if response.status_code == 200:
    response_200 = LedgerEntityResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | LedgerEntityResponse]:
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
  body: UpdateEntityRequest,
) -> Response[HTTPValidationError | LedgerEntityResponse]:
  """Update Entity

   Update entity details. Only provided (non-null) fields are updated.

  Args:
      graph_id (str):
      body (UpdateEntityRequest): Request to update entity details. Only provided fields are
          updated.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | LedgerEntityResponse]
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
  body: UpdateEntityRequest,
) -> HTTPValidationError | LedgerEntityResponse | None:
  """Update Entity

   Update entity details. Only provided (non-null) fields are updated.

  Args:
      graph_id (str):
      body (UpdateEntityRequest): Request to update entity details. Only provided fields are
          updated.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | LedgerEntityResponse
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
  body: UpdateEntityRequest,
) -> Response[HTTPValidationError | LedgerEntityResponse]:
  """Update Entity

   Update entity details. Only provided (non-null) fields are updated.

  Args:
      graph_id (str):
      body (UpdateEntityRequest): Request to update entity details. Only provided fields are
          updated.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | LedgerEntityResponse]
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
  body: UpdateEntityRequest,
) -> HTTPValidationError | LedgerEntityResponse | None:
  """Update Entity

   Update entity details. Only provided (non-null) fields are updated.

  Args:
      graph_id (str):
      body (UpdateEntityRequest): Request to update entity details. Only provided fields are
          updated.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | LedgerEntityResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
