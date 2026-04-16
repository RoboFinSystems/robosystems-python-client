from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_graph_request import CreateGraphRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.operation_envelope import OperationEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
  *,
  body: CreateGraphRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | OperationEnvelope | None:
  if response.status_code == 202:
    response_202 = OperationEnvelope.from_dict(response.json())

    return response_202

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401

  if response.status_code == 402:
    response_402 = cast(Any, None)
    return response_402

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 409:
    response_409 = ErrorResponse.from_dict(response.json())

    return response_409

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
) -> Response[Any | ErrorResponse | HTTPValidationError | OperationEnvelope]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError | OperationEnvelope]:
  """Create New Graph Database

   Creates a graph asynchronously. Returns an `OperationEnvelope` with `operation_id` for SSE progress
  at `/v1/operations/{operation_id}/stream`. Entity graphs require `initial_entity`. Supports
  `Idempotency-Key` header.

  Args:
      idempotency_key (None | str | Unset):
      body (CreateGraphRequest): Request model for creating a new graph.

          Use this to create either:
          - **Entity graphs**: Standard graphs with entity schema. Requires `initial_entity`.
          - **Custom graphs**: Generic graphs with a fully custom schema. Requires `custom_schema`;
          `initial_entity` is not used.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | OperationEnvelope]
  """

  kwargs = _get_kwargs(
    body=body,
    idempotency_key=idempotency_key,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | OperationEnvelope | None:
  """Create New Graph Database

   Creates a graph asynchronously. Returns an `OperationEnvelope` with `operation_id` for SSE progress
  at `/v1/operations/{operation_id}/stream`. Entity graphs require `initial_entity`. Supports
  `Idempotency-Key` header.

  Args:
      idempotency_key (None | str | Unset):
      body (CreateGraphRequest): Request model for creating a new graph.

          Use this to create either:
          - **Entity graphs**: Standard graphs with entity schema. Requires `initial_entity`.
          - **Custom graphs**: Generic graphs with a fully custom schema. Requires `custom_schema`;
          `initial_entity` is not used.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | OperationEnvelope
  """

  return sync_detailed(
    client=client,
    body=body,
    idempotency_key=idempotency_key,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError | OperationEnvelope]:
  """Create New Graph Database

   Creates a graph asynchronously. Returns an `OperationEnvelope` with `operation_id` for SSE progress
  at `/v1/operations/{operation_id}/stream`. Entity graphs require `initial_entity`. Supports
  `Idempotency-Key` header.

  Args:
      idempotency_key (None | str | Unset):
      body (CreateGraphRequest): Request model for creating a new graph.

          Use this to create either:
          - **Entity graphs**: Standard graphs with entity schema. Requires `initial_entity`.
          - **Custom graphs**: Generic graphs with a fully custom schema. Requires `custom_schema`;
          `initial_entity` is not used.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | OperationEnvelope]
  """

  kwargs = _get_kwargs(
    body=body,
    idempotency_key=idempotency_key,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  body: CreateGraphRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | OperationEnvelope | None:
  """Create New Graph Database

   Creates a graph asynchronously. Returns an `OperationEnvelope` with `operation_id` for SSE progress
  at `/v1/operations/{operation_id}/stream`. Entity graphs require `initial_entity`. Supports
  `Idempotency-Key` header.

  Args:
      idempotency_key (None | str | Unset):
      body (CreateGraphRequest): Request model for creating a new graph.

          Use this to create either:
          - **Entity graphs**: Standard graphs with entity schema. Requires `initial_entity`.
          - **Custom graphs**: Generic graphs with a fully custom schema. Requires `custom_schema`;
          `initial_entity` is not used.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | OperationEnvelope
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
