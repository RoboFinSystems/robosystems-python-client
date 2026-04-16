from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_graph_tiers_response import AvailableGraphTiersResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  *,
  include_disabled: bool | Unset = False,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  params["include_disabled"] = include_disabled

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/tiers",
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = AvailableGraphTiersResponse.from_dict(response.json())

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
) -> Response[AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  include_disabled: bool | Unset = False,
) -> Response[AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError]:
  """Get Available Graph Tiers

  Args:
      include_disabled (bool | Unset):  Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    include_disabled=include_disabled,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
  include_disabled: bool | Unset = False,
) -> AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError | None:
  """Get Available Graph Tiers

  Args:
      include_disabled (bool | Unset):  Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    client=client,
    include_disabled=include_disabled,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  include_disabled: bool | Unset = False,
) -> Response[AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError]:
  """Get Available Graph Tiers

  Args:
      include_disabled (bool | Unset):  Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    include_disabled=include_disabled,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  include_disabled: bool | Unset = False,
) -> AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError | None:
  """Get Available Graph Tiers

  Args:
      include_disabled (bool | Unset):  Default: False.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      AvailableGraphTiersResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      client=client,
      include_disabled=include_disabled,
    )
  ).parsed
