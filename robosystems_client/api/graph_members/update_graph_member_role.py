from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.graph_member_response import GraphMemberResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.update_graph_member_role_request import UpdateGraphMemberRoleRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  user_id: str,
  *,
  body: UpdateGraphMemberRoleRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "put",
    "url": "/v1/graphs/{graph_id}/members/{user_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      user_id=quote(str(user_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GraphMemberResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = GraphMemberResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GraphMemberResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateGraphMemberRoleRequest,
) -> Response[ErrorResponse | GraphMemberResponse | HTTPValidationError]:
  """Update Graph Member Role

   Change an explicit member's graph role. Requires graph admin. Implicit org owner/admin access is
  managed through org roles.

  Args:
      graph_id (str): Graph identifier
      user_id (str):
      body (UpdateGraphMemberRoleRequest): Request to change a graph member's role.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GraphMemberResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    user_id=user_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateGraphMemberRoleRequest,
) -> ErrorResponse | GraphMemberResponse | HTTPValidationError | None:
  """Update Graph Member Role

   Change an explicit member's graph role. Requires graph admin. Implicit org owner/admin access is
  managed through org roles.

  Args:
      graph_id (str): Graph identifier
      user_id (str):
      body (UpdateGraphMemberRoleRequest): Request to change a graph member's role.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | GraphMemberResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    user_id=user_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateGraphMemberRoleRequest,
) -> Response[ErrorResponse | GraphMemberResponse | HTTPValidationError]:
  """Update Graph Member Role

   Change an explicit member's graph role. Requires graph admin. Implicit org owner/admin access is
  managed through org roles.

  Args:
      graph_id (str): Graph identifier
      user_id (str):
      body (UpdateGraphMemberRoleRequest): Request to change a graph member's role.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GraphMemberResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    user_id=user_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateGraphMemberRoleRequest,
) -> ErrorResponse | GraphMemberResponse | HTTPValidationError | None:
  """Update Graph Member Role

   Change an explicit member's graph role. Requires graph admin. Implicit org owner/admin access is
  managed through org roles.

  Args:
      graph_id (str): Graph identifier
      user_id (str):
      body (UpdateGraphMemberRoleRequest): Request to change a graph member's role.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | GraphMemberResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      user_id=user_id,
      client=client,
      body=body,
    )
  ).parsed
