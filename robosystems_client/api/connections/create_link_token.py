from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.link_token_request import LinkTokenRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: LinkTokenRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/connections/link/token",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = response.json()
    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
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
  body: LinkTokenRequest,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Create Link Token

   Create a link token for embedded authentication providers.

  This endpoint generates a temporary token used to initialize embedded authentication UI.

  Currently supported providers:
  - **Plaid**: Bank account connections with real-time transaction access

  The link token:
  - Expires after 4 hours
  - Is single-use only
  - Must be used with the matching frontend SDK
  - Includes user and entity context

  No credits are consumed for creating link tokens.

  Args:
      graph_id (str):
      body (LinkTokenRequest): Request to create a link token for embedded authentication.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError]]
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
  body: LinkTokenRequest,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Create Link Token

   Create a link token for embedded authentication providers.

  This endpoint generates a temporary token used to initialize embedded authentication UI.

  Currently supported providers:
  - **Plaid**: Bank account connections with real-time transaction access

  The link token:
  - Expires after 4 hours
  - Is single-use only
  - Must be used with the matching frontend SDK
  - Includes user and entity context

  No credits are consumed for creating link tokens.

  Args:
      graph_id (str):
      body (LinkTokenRequest): Request to create a link token for embedded authentication.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError]
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
  body: LinkTokenRequest,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Create Link Token

   Create a link token for embedded authentication providers.

  This endpoint generates a temporary token used to initialize embedded authentication UI.

  Currently supported providers:
  - **Plaid**: Bank account connections with real-time transaction access

  The link token:
  - Expires after 4 hours
  - Is single-use only
  - Must be used with the matching frontend SDK
  - Includes user and entity context

  No credits are consumed for creating link tokens.

  Args:
      graph_id (str):
      body (LinkTokenRequest): Request to create a link token for embedded authentication.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, ErrorResponse, HTTPValidationError]]
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
  body: LinkTokenRequest,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Create Link Token

   Create a link token for embedded authentication providers.

  This endpoint generates a temporary token used to initialize embedded authentication UI.

  Currently supported providers:
  - **Plaid**: Bank account connections with real-time transaction access

  The link token:
  - Expires after 4 hours
  - Is single-use only
  - Must be used with the matching frontend SDK
  - Includes user and entity context

  No credits are consumed for creating link tokens.

  Args:
      graph_id (str):
      body (LinkTokenRequest): Request to create a link token for embedded authentication.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
