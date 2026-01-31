from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.subgraph_quota_response import SubgraphQuotaResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/{graph_id}/subgraphs/quota".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | SubgraphQuotaResponse | None:
  if response.status_code == 200:
    response_200 = SubgraphQuotaResponse.from_dict(response.json())

    return response_200

  if response.status_code == 401:
    response_401 = cast(Any, None)
    return response_401

  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403

  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | SubgraphQuotaResponse]:
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
) -> Response[Any | HTTPValidationError | SubgraphQuotaResponse]:
  """Get Subgraph Quota

   Get subgraph quota and usage information for a parent graph.

  **Shows:**
  - Current subgraph count
  - Maximum allowed subgraphs per tier
  - Remaining capacity
  - Total size usage across all subgraphs

  **Tier Limits:**
  - Standard: 0 subgraphs (not supported)
  - Enterprise: Configurable limit (default: 10 subgraphs)
  - Premium: Unlimited subgraphs
  - Limits are defined in deployment configuration

  **Size Tracking:**
  Provides aggregate size metrics when available.
  Individual subgraph sizes shown in list endpoint.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError | SubgraphQuotaResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Any | HTTPValidationError | SubgraphQuotaResponse | None:
  """Get Subgraph Quota

   Get subgraph quota and usage information for a parent graph.

  **Shows:**
  - Current subgraph count
  - Maximum allowed subgraphs per tier
  - Remaining capacity
  - Total size usage across all subgraphs

  **Tier Limits:**
  - Standard: 0 subgraphs (not supported)
  - Enterprise: Configurable limit (default: 10 subgraphs)
  - Premium: Unlimited subgraphs
  - Limits are defined in deployment configuration

  **Size Tracking:**
  Provides aggregate size metrics when available.
  Individual subgraph sizes shown in list endpoint.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError | SubgraphQuotaResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError | SubgraphQuotaResponse]:
  """Get Subgraph Quota

   Get subgraph quota and usage information for a parent graph.

  **Shows:**
  - Current subgraph count
  - Maximum allowed subgraphs per tier
  - Remaining capacity
  - Total size usage across all subgraphs

  **Tier Limits:**
  - Standard: 0 subgraphs (not supported)
  - Enterprise: Configurable limit (default: 10 subgraphs)
  - Premium: Unlimited subgraphs
  - Limits are defined in deployment configuration

  **Size Tracking:**
  Provides aggregate size metrics when available.
  Individual subgraph sizes shown in list endpoint.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError | SubgraphQuotaResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
) -> Any | HTTPValidationError | SubgraphQuotaResponse | None:
  """Get Subgraph Quota

   Get subgraph quota and usage information for a parent graph.

  **Shows:**
  - Current subgraph count
  - Maximum allowed subgraphs per tier
  - Remaining capacity
  - Total size usage across all subgraphs

  **Tier Limits:**
  - Standard: 0 subgraphs (not supported)
  - Enterprise: Configurable limit (default: 10 subgraphs)
  - Premium: Unlimited subgraphs
  - Limits are defined in deployment configuration

  **Size Tracking:**
  Provides aggregate size metrics when available.
  Individual subgraph sizes shown in list endpoint.

  Args:
      graph_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError | SubgraphQuotaResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
    )
  ).parsed
