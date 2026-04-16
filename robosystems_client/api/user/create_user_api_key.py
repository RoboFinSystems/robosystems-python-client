from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_api_key_request import CreateAPIKeyRequest
from ...models.create_api_key_response import CreateAPIKeyResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  *,
  body: CreateAPIKeyRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/user/api-keys",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAPIKeyResponse | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 201:
    response_201 = CreateAPIKeyResponse.from_dict(response.json())

    return response_201

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
) -> Response[CreateAPIKeyResponse | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  body: CreateAPIKeyRequest,
) -> Response[CreateAPIKeyResponse | ErrorResponse | HTTPValidationError]:
  """Create API Key

   The raw key value is only returned once at creation time and cannot be retrieved again.

  Args:
      body (CreateAPIKeyRequest): Request model for creating a new API key.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[CreateAPIKeyResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
  body: CreateAPIKeyRequest,
) -> CreateAPIKeyResponse | ErrorResponse | HTTPValidationError | None:
  """Create API Key

   The raw key value is only returned once at creation time and cannot be retrieved again.

  Args:
      body (CreateAPIKeyRequest): Request model for creating a new API key.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      CreateAPIKeyResponse | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  body: CreateAPIKeyRequest,
) -> Response[CreateAPIKeyResponse | ErrorResponse | HTTPValidationError]:
  """Create API Key

   The raw key value is only returned once at creation time and cannot be retrieved again.

  Args:
      body (CreateAPIKeyRequest): Request model for creating a new API key.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[CreateAPIKeyResponse | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  body: CreateAPIKeyRequest,
) -> CreateAPIKeyResponse | ErrorResponse | HTTPValidationError | None:
  """Create API Key

   The raw key value is only returned once at creation time and cannot be retrieved again.

  Args:
      body (CreateAPIKeyRequest): Request model for creating a new API key.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      CreateAPIKeyResponse | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
