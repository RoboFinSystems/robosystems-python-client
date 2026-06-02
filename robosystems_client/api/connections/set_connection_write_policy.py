from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connection_response import ConnectionResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.set_write_policy_request import SetWritePolicyRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  connection_id: str,
  *,
  body: SetWritePolicyRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "put",
    "url": "/v1/graphs/{graph_id}/connections/{connection_id}/write-policy".format(
      graph_id=quote(str(graph_id), safe=""),
      connection_id=quote(str(connection_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectionResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = ConnectionResponse.from_dict(response.json())

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
) -> Response[ConnectionResponse | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SetWritePolicyRequest,
) -> Response[ConnectionResponse | ErrorResponse | HTTPValidationError]:
  """Set Connection Write Policy

   Opt a connection into or out of outbound write-back. 'qb_authoritative' makes QuickBooks the source
  of truth — RoboSystems-originated entries (manual JEs, schedule drafts) publish to QuickBooks when
  executed or at close. 'native' keeps RoboSystems authoritative with no write-back. This is the
  explicit operator opt-in for writing to your books of record.

  Args:
      graph_id (str):
      connection_id (str): Unique connection identifier
      body (SetWritePolicyRequest): Request to set a connection's source-of-truth write policy.

          The explicit operator opt-in for outbound write-back. `hybrid` is omitted
          until its code path ships.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ConnectionResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SetWritePolicyRequest,
) -> ConnectionResponse | ErrorResponse | HTTPValidationError | None:
  """Set Connection Write Policy

   Opt a connection into or out of outbound write-back. 'qb_authoritative' makes QuickBooks the source
  of truth — RoboSystems-originated entries (manual JEs, schedule drafts) publish to QuickBooks when
  executed or at close. 'native' keeps RoboSystems authoritative with no write-back. This is the
  explicit operator opt-in for writing to your books of record.

  Args:
      graph_id (str):
      connection_id (str): Unique connection identifier
      body (SetWritePolicyRequest): Request to set a connection's source-of-truth write policy.

          The explicit operator opt-in for outbound write-back. `hybrid` is omitted
          until its code path ships.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ConnectionResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    connection_id=connection_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SetWritePolicyRequest,
) -> Response[ConnectionResponse | ErrorResponse | HTTPValidationError]:
  """Set Connection Write Policy

   Opt a connection into or out of outbound write-back. 'qb_authoritative' makes QuickBooks the source
  of truth — RoboSystems-originated entries (manual JEs, schedule drafts) publish to QuickBooks when
  executed or at close. 'native' keeps RoboSystems authoritative with no write-back. This is the
  explicit operator opt-in for writing to your books of record.

  Args:
      graph_id (str):
      connection_id (str): Unique connection identifier
      body (SetWritePolicyRequest): Request to set a connection's source-of-truth write policy.

          The explicit operator opt-in for outbound write-back. `hybrid` is omitted
          until its code path ships.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ConnectionResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  body: SetWritePolicyRequest,
) -> ConnectionResponse | ErrorResponse | HTTPValidationError | None:
  """Set Connection Write Policy

   Opt a connection into or out of outbound write-back. 'qb_authoritative' makes QuickBooks the source
  of truth — RoboSystems-originated entries (manual JEs, schedule drafts) publish to QuickBooks when
  executed or at close. 'native' keeps RoboSystems authoritative with no write-back. This is the
  explicit operator opt-in for writing to your books of record.

  Args:
      graph_id (str):
      connection_id (str): Unique connection identifier
      body (SetWritePolicyRequest): Request to set a connection's source-of-truth write policy.

          The explicit operator opt-in for outbound write-back. `hybrid` is omitted
          until its code path ships.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ConnectionResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      connection_id=connection_id,
      client=client,
      body=body,
    )
  ).parsed
