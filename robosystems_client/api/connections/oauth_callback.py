from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.o_auth_callback_request import OAuthCallbackRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  provider: str,
  *,
  body: OAuthCallbackRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/connections/oauth/callback/{provider}".format(
      graph_id=quote(str(graph_id), safe=""),
      provider=quote(str(provider), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 200:
    response_200 = response.json()
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
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  provider: str,
  *,
  client: AuthenticatedClient,
  body: OAuthCallbackRequest,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  """OAuth Callback

   Completes the OAuth authorization flow after provider redirect. Exchanges the authorization code for
  tokens, stores them, and triggers an initial sync. This is a redirect target — not typically called
  directly.

  Args:
      graph_id (str):
      provider (str): OAuth provider name
      body (OAuthCallbackRequest): OAuth callback parameters.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    provider=provider,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  provider: str,
  *,
  client: AuthenticatedClient,
  body: OAuthCallbackRequest,
) -> Any | ErrorResponse | HTTPValidationError | None:
  """OAuth Callback

   Completes the OAuth authorization flow after provider redirect. Exchanges the authorization code for
  tokens, stores them, and triggers an initial sync. This is a redirect target — not typically called
  directly.

  Args:
      graph_id (str):
      provider (str): OAuth provider name
      body (OAuthCallbackRequest): OAuth callback parameters.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    provider=provider,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  provider: str,
  *,
  client: AuthenticatedClient,
  body: OAuthCallbackRequest,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  """OAuth Callback

   Completes the OAuth authorization flow after provider redirect. Exchanges the authorization code for
  tokens, stores them, and triggers an initial sync. This is a redirect target — not typically called
  directly.

  Args:
      graph_id (str):
      provider (str): OAuth provider name
      body (OAuthCallbackRequest): OAuth callback parameters.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    provider=provider,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  provider: str,
  *,
  client: AuthenticatedClient,
  body: OAuthCallbackRequest,
) -> Any | ErrorResponse | HTTPValidationError | None:
  """OAuth Callback

   Completes the OAuth authorization flow after provider redirect. Exchanges the authorization code for
  tokens, stores them, and triggers an initial sync. This is a redirect target — not typically called
  directly.

  Args:
      graph_id (str):
      provider (str): OAuth provider name
      body (OAuthCallbackRequest): OAuth callback parameters.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      provider=provider,
      client=client,
      body=body,
    )
  ).parsed
