from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.graph_capacity_response import GraphCapacityResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/graphs/capacity",
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GraphCapacityResponse | None:
  if response.status_code == 200:
    response_200 = GraphCapacityResponse.from_dict(response.json())

    return response_200

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GraphCapacityResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[Any | GraphCapacityResponse]:
  """Get Graph Tier Capacity

   Check current infrastructure capacity for each graph database tier.

  Returns a status per tier indicating whether instances are immediately available,
  can be provisioned on demand, or are at capacity.

  **Status Values:**
  - `ready` — An instance slot is available; graph creation will succeed immediately
  - `scalable` — No slots right now, but a new instance can be provisioned (3-5 min)
  - `at_capacity` — Tier is full and cannot auto-scale; contact support

  **Use Cases:**
  - Pre-flight check before entering the graph creation wizard
  - Show availability badges on tier selection cards
  - Gate tier selection and show contact form for at-capacity tiers

  **Caching:**
  Results are cached for 60 seconds to avoid excessive infrastructure queries.

  **Note:**
  No credit consumption required. Does not expose instance counts or IPs.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | GraphCapacityResponse]
  """

  kwargs = _get_kwargs()

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
) -> Any | GraphCapacityResponse | None:
  """Get Graph Tier Capacity

   Check current infrastructure capacity for each graph database tier.

  Returns a status per tier indicating whether instances are immediately available,
  can be provisioned on demand, or are at capacity.

  **Status Values:**
  - `ready` — An instance slot is available; graph creation will succeed immediately
  - `scalable` — No slots right now, but a new instance can be provisioned (3-5 min)
  - `at_capacity` — Tier is full and cannot auto-scale; contact support

  **Use Cases:**
  - Pre-flight check before entering the graph creation wizard
  - Show availability badges on tier selection cards
  - Gate tier selection and show contact form for at-capacity tiers

  **Caching:**
  Results are cached for 60 seconds to avoid excessive infrastructure queries.

  **Note:**
  No credit consumption required. Does not expose instance counts or IPs.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | GraphCapacityResponse
  """

  return sync_detailed(
    client=client,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[Any | GraphCapacityResponse]:
  """Get Graph Tier Capacity

   Check current infrastructure capacity for each graph database tier.

  Returns a status per tier indicating whether instances are immediately available,
  can be provisioned on demand, or are at capacity.

  **Status Values:**
  - `ready` — An instance slot is available; graph creation will succeed immediately
  - `scalable` — No slots right now, but a new instance can be provisioned (3-5 min)
  - `at_capacity` — Tier is full and cannot auto-scale; contact support

  **Use Cases:**
  - Pre-flight check before entering the graph creation wizard
  - Show availability badges on tier selection cards
  - Gate tier selection and show contact form for at-capacity tiers

  **Caching:**
  Results are cached for 60 seconds to avoid excessive infrastructure queries.

  **Note:**
  No credit consumption required. Does not expose instance counts or IPs.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | GraphCapacityResponse]
  """

  kwargs = _get_kwargs()

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
) -> Any | GraphCapacityResponse | None:
  """Get Graph Tier Capacity

   Check current infrastructure capacity for each graph database tier.

  Returns a status per tier indicating whether instances are immediately available,
  can be provisioned on demand, or are at capacity.

  **Status Values:**
  - `ready` — An instance slot is available; graph creation will succeed immediately
  - `scalable` — No slots right now, but a new instance can be provisioned (3-5 min)
  - `at_capacity` — Tier is full and cannot auto-scale; contact support

  **Use Cases:**
  - Pre-flight check before entering the graph creation wizard
  - Show availability badges on tier selection cards
  - Gate tier selection and show contact form for at-capacity tiers

  **Caching:**
  Results are cached for 60 seconds to avoid excessive infrastructure queries.

  **Note:**
  No credit consumption required. Does not expose instance counts or IPs.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | GraphCapacityResponse
  """

  return (
    await asyncio_detailed(
      client=client,
    )
  ).parsed
