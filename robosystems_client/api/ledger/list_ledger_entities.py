from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ledger_entity_response import LedgerEntityResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  source: None | str | Unset = UNSET,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_source: None | str | Unset
  if isinstance(source, Unset):
    json_source = UNSET
  else:
    json_source = source
  params["source"] = json_source

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/entities".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[LedgerEntityResponse] | None:
  if response.status_code == 200:
    response_200 = []
    _response_200 = response.json()
    for response_200_item_data in _response_200:
      response_200_item = LedgerEntityResponse.from_dict(response_200_item_data)

      response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[LedgerEntityResponse]]:
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
  source: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[LedgerEntityResponse]]:
  """List Entities

   List entities for this graph, optionally filtered by source.

  Args:
      graph_id (str):
      source (None | str | Unset): Filter by source (e.g., 'linked')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | list[LedgerEntityResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    source=source,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  source: None | str | Unset = UNSET,
) -> HTTPValidationError | list[LedgerEntityResponse] | None:
  """List Entities

   List entities for this graph, optionally filtered by source.

  Args:
      graph_id (str):
      source (None | str | Unset): Filter by source (e.g., 'linked')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | list[LedgerEntityResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    source=source,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  source: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[LedgerEntityResponse]]:
  """List Entities

   List entities for this graph, optionally filtered by source.

  Args:
      graph_id (str):
      source (None | str | Unset): Filter by source (e.g., 'linked')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | list[LedgerEntityResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    source=source,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  source: None | str | Unset = UNSET,
) -> HTTPValidationError | list[LedgerEntityResponse] | None:
  """List Entities

   List entities for this graph, optionally filtered by source.

  Args:
      graph_id (str):
      source (None | str | Unset): Filter by source (e.g., 'linked')

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | list[LedgerEntityResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      source=source,
    )
  ).parsed
