from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.exchange_token_request import ExchangeTokenRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: ExchangeTokenRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/connections/link/exchange",
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
  body: ExchangeTokenRequest,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Exchange Link Token

   Exchange a public token for permanent access credentials.

  This completes the embedded authentication flow after user authorization.

  The exchange process:
  1. Validates the temporary public token
  2. Exchanges it for permanent access credentials
  3. Updates the connection with account information
  4. Optionally triggers initial data sync

  Supported providers:
  - **Plaid**: Exchanges Plaid Link public token for access token

  Security:
  - Public tokens expire after 30 minutes
  - Each token can only be exchanged once
  - Full audit trail is maintained

  No credits are consumed for token exchange.

  Args:
      graph_id (str):
      body (ExchangeTokenRequest): Exchange temporary token for permanent credentials.

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
  body: ExchangeTokenRequest,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Exchange Link Token

   Exchange a public token for permanent access credentials.

  This completes the embedded authentication flow after user authorization.

  The exchange process:
  1. Validates the temporary public token
  2. Exchanges it for permanent access credentials
  3. Updates the connection with account information
  4. Optionally triggers initial data sync

  Supported providers:
  - **Plaid**: Exchanges Plaid Link public token for access token

  Security:
  - Public tokens expire after 30 minutes
  - Each token can only be exchanged once
  - Full audit trail is maintained

  No credits are consumed for token exchange.

  Args:
      graph_id (str):
      body (ExchangeTokenRequest): Exchange temporary token for permanent credentials.

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
  body: ExchangeTokenRequest,
) -> Response[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Exchange Link Token

   Exchange a public token for permanent access credentials.

  This completes the embedded authentication flow after user authorization.

  The exchange process:
  1. Validates the temporary public token
  2. Exchanges it for permanent access credentials
  3. Updates the connection with account information
  4. Optionally triggers initial data sync

  Supported providers:
  - **Plaid**: Exchanges Plaid Link public token for access token

  Security:
  - Public tokens expire after 30 minutes
  - Each token can only be exchanged once
  - Full audit trail is maintained

  No credits are consumed for token exchange.

  Args:
      graph_id (str):
      body (ExchangeTokenRequest): Exchange temporary token for permanent credentials.

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
  body: ExchangeTokenRequest,
) -> Optional[Union[Any, ErrorResponse, HTTPValidationError]]:
  """Exchange Link Token

   Exchange a public token for permanent access credentials.

  This completes the embedded authentication flow after user authorization.

  The exchange process:
  1. Validates the temporary public token
  2. Exchanges it for permanent access credentials
  3. Updates the connection with account information
  4. Optionally triggers initial data sync

  Supported providers:
  - **Plaid**: Exchanges Plaid Link public token for access token

  Security:
  - Public tokens expire after 30 minutes
  - Each token can only be exchanged once
  - Full audit trail is maintained

  No credits are consumed for token exchange.

  Args:
      graph_id (str):
      body (ExchangeTokenRequest): Exchange temporary token for permanent credentials.

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
