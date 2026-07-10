from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schema_validation_request import SchemaValidationRequest
from ...models.schema_validation_response import SchemaValidationResponse
from ...types import Response


def _get_kwargs(
  *,
  body: SchemaValidationRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/schema/validate",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | SchemaValidationResponse | None:
  if response.status_code == 200:
    response_200 = SchemaValidationResponse.from_dict(response.json())

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
    response_422 = cast(Any, None)
    return response_422

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if response.status_code == 504:
    response_504 = cast(Any, None)
    return response_504

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | SchemaValidationResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  body: SchemaValidationRequest,
) -> Response[Any | ErrorResponse | SchemaValidationResponse]:
  """Validate Schema

   Validates a custom schema definition before deployment — checks structure, types, constraints, and
  relationship references. Returns errors and warnings without applying changes. Supports JSON, YAML,
  and dict formats.

  Args:
      body (SchemaValidationRequest): Request model for schema validation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | SchemaValidationResponse]
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
  body: SchemaValidationRequest,
) -> Any | ErrorResponse | SchemaValidationResponse | None:
  """Validate Schema

   Validates a custom schema definition before deployment — checks structure, types, constraints, and
  relationship references. Returns errors and warnings without applying changes. Supports JSON, YAML,
  and dict formats.

  Args:
      body (SchemaValidationRequest): Request model for schema validation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | SchemaValidationResponse
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  body: SchemaValidationRequest,
) -> Response[Any | ErrorResponse | SchemaValidationResponse]:
  """Validate Schema

   Validates a custom schema definition before deployment — checks structure, types, constraints, and
  relationship references. Returns errors and warnings without applying changes. Supports JSON, YAML,
  and dict formats.

  Args:
      body (SchemaValidationRequest): Request model for schema validation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | SchemaValidationResponse]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  body: SchemaValidationRequest,
) -> Any | ErrorResponse | SchemaValidationResponse | None:
  """Validate Schema

   Validates a custom schema definition before deployment — checks structure, types, constraints, and
  relationship references. Returns errors and warnings without applying changes. Supports JSON, YAML,
  and dict formats.

  Args:
      body (SchemaValidationRequest): Request model for schema validation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | SchemaValidationResponse
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
