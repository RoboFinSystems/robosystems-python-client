from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.unmapped_element_response import UnmappedElementResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  mapping_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_mapping_id: None | str | Unset
  if isinstance(mapping_id, Unset):
    json_mapping_id = UNSET
  else:
    json_mapping_id = mapping_id
  params["mapping_id"] = json_mapping_id

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/elements/unmapped".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[UnmappedElementResponse] | None:
  if response.status_code == 200:
    response_200 = []
    _response_200 = response.json()
    for response_200_item_data in _response_200:
      response_200_item = UnmappedElementResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[UnmappedElementResponse]]:
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
  mapping_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[UnmappedElementResponse]]:
  """List Unmapped Elements

   List CoA elements that are not yet mapped to the reporting taxonomy.

  Args:
      graph_id (str):
      mapping_id (None | str | Unset): Mapping structure to check against

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | list[UnmappedElementResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    mapping_id=mapping_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  mapping_id: None | str | Unset = UNSET,
) -> HTTPValidationError | list[UnmappedElementResponse] | None:
  """List Unmapped Elements

   List CoA elements that are not yet mapped to the reporting taxonomy.

  Args:
      graph_id (str):
      mapping_id (None | str | Unset): Mapping structure to check against

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | list[UnmappedElementResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    mapping_id=mapping_id,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  mapping_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[UnmappedElementResponse]]:
  """List Unmapped Elements

   List CoA elements that are not yet mapped to the reporting taxonomy.

  Args:
      graph_id (str):
      mapping_id (None | str | Unset): Mapping structure to check against

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | list[UnmappedElementResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    mapping_id=mapping_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  mapping_id: None | str | Unset = UNSET,
) -> HTTPValidationError | list[UnmappedElementResponse] | None:
  """List Unmapped Elements

   List CoA elements that are not yet mapped to the reporting taxonomy.

  Args:
      graph_id (str):
      mapping_id (None | str | Unset): Mapping structure to check against

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | list[UnmappedElementResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      mapping_id=mapping_id,
    )
  ).parsed
