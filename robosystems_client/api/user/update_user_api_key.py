from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_info import APIKeyInfo
from ...models.http_validation_error import HTTPValidationError
from ...models.update_api_key_request import UpdateAPIKeyRequest
from ...types import Response


def _get_kwargs(
  api_key_id: str,
  *,
  body: UpdateAPIKeyRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "put",
    "url": f"/v1/user/api-keys/{api_key_id}",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[APIKeyInfo, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = APIKeyInfo.from_dict(response.json())

    return response_200

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[APIKeyInfo, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  api_key_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateAPIKeyRequest,
) -> Response[Union[APIKeyInfo, HTTPValidationError]]:
  """Update API Key

   Update an API key's name or description.

  Args:
      api_key_id (str):
      body (UpdateAPIKeyRequest): Request model for updating an API key.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[APIKeyInfo, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    api_key_id=api_key_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  api_key_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateAPIKeyRequest,
) -> Optional[Union[APIKeyInfo, HTTPValidationError]]:
  """Update API Key

   Update an API key's name or description.

  Args:
      api_key_id (str):
      body (UpdateAPIKeyRequest): Request model for updating an API key.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[APIKeyInfo, HTTPValidationError]
  """

  return sync_detailed(
    api_key_id=api_key_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  api_key_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateAPIKeyRequest,
) -> Response[Union[APIKeyInfo, HTTPValidationError]]:
  """Update API Key

   Update an API key's name or description.

  Args:
      api_key_id (str):
      body (UpdateAPIKeyRequest): Request model for updating an API key.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[APIKeyInfo, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    api_key_id=api_key_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  api_key_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateAPIKeyRequest,
) -> Optional[Union[APIKeyInfo, HTTPValidationError]]:
  """Update API Key

   Update an API key's name or description.

  Args:
      api_key_id (str):
      body (UpdateAPIKeyRequest): Request model for updating an API key.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[APIKeyInfo, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      api_key_id=api_key_id,
      client=client,
      body=body,
    )
  ).parsed
