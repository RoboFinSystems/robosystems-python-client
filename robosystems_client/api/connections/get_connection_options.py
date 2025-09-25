from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connection_options_response import ConnectionOptionsResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/connections/options",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = ConnectionOptionsResponse.from_dict(response.json())

    return response_200
  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403
  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]]:
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
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]]:
  """List Connection Options

   Get metadata about all available data connection providers.

  This endpoint returns comprehensive information about each supported provider:

  **SEC EDGAR**: Public entity financial filings
  - No authentication required (public data)
  - 10-K, 10-Q, 8-K reports with XBRL data
  - Historical and real-time filing access

  **QuickBooks Online**: Full accounting system integration
  - OAuth 2.0 authentication
  - Chart of accounts, transactions, trial balance
  - Real-time sync capabilities

  **Plaid**: Bank account connections
  - Secure bank authentication via Plaid Link
  - Transaction history and balances
  - Multi-account support

  No credits are consumed for viewing connection options.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]]:
  """List Connection Options

   Get metadata about all available data connection providers.

  This endpoint returns comprehensive information about each supported provider:

  **SEC EDGAR**: Public entity financial filings
  - No authentication required (public data)
  - 10-K, 10-Q, 8-K reports with XBRL data
  - Historical and real-time filing access

  **QuickBooks Online**: Full accounting system integration
  - OAuth 2.0 authentication
  - Chart of accounts, transactions, trial balance
  - Real-time sync capabilities

  **Plaid**: Bank account connections
  - Secure bank authentication via Plaid Link
  - Transaction history and balances
  - Multi-account support

  No credits are consumed for viewing connection options.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]]:
  """List Connection Options

   Get metadata about all available data connection providers.

  This endpoint returns comprehensive information about each supported provider:

  **SEC EDGAR**: Public entity financial filings
  - No authentication required (public data)
  - 10-K, 10-Q, 8-K reports with XBRL data
  - Historical and real-time filing access

  **QuickBooks Online**: Full accounting system integration
  - OAuth 2.0 authentication
  - Chart of accounts, transactions, trial balance
  - Real-time sync capabilities

  **Plaid**: Bank account connections
  - Secure bank authentication via Plaid Link
  - Transaction history and balances
  - Multi-account support

  No credits are consumed for viewing connection options.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]]:
  """List Connection Options

   Get metadata about all available data connection providers.

  This endpoint returns comprehensive information about each supported provider:

  **SEC EDGAR**: Public entity financial filings
  - No authentication required (public data)
  - 10-K, 10-Q, 8-K reports with XBRL data
  - Historical and real-time filing access

  **QuickBooks Online**: Full accounting system integration
  - OAuth 2.0 authentication
  - Chart of accounts, transactions, trial balance
  - Real-time sync capabilities

  **Plaid**: Bank account connections
  - Secure bank authentication via Plaid Link
  - Transaction history and balances
  - Multi-account support

  No credits are consumed for viewing connection options.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ConnectionOptionsResponse, ErrorResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      token=token,
      authorization=authorization,
    )
  ).parsed
