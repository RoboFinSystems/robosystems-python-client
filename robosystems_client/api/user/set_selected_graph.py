from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.set_selected_graph_request import SetSelectedGraphRequest
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
  *,
  body: SetSelectedGraphRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "put",
    "url": "/v1/user/selected-graph",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  if response.status_code == 200:
    response_200 = SuccessResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
  body: SetSelectedGraphRequest,
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  """Set Selected Graph

   Remembers the graph as the caller's current one: `GET /v1/graphs` then reports it as
  `selectedGraphId`, and the apps open on it. One graph per user, replacing the previous selection.
  Only a graph the caller belongs to can be selected; shared repositories cannot be.

  Args:
      body (SetSelectedGraphRequest): Request model for setting the user's selected graph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SuccessResponse]
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
  body: SetSelectedGraphRequest,
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  """Set Selected Graph

   Remembers the graph as the caller's current one: `GET /v1/graphs` then reports it as
  `selectedGraphId`, and the apps open on it. One graph per user, replacing the previous selection.
  Only a graph the caller belongs to can be selected; shared repositories cannot be.

  Args:
      body (SetSelectedGraphRequest): Request model for setting the user's selected graph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SuccessResponse
  """

  return sync_detailed(
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
  body: SetSelectedGraphRequest,
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  """Set Selected Graph

   Remembers the graph as the caller's current one: `GET /v1/graphs` then reports it as
  `selectedGraphId`, and the apps open on it. One graph per user, replacing the previous selection.
  Only a graph the caller belongs to can be selected; shared repositories cannot be.

  Args:
      body (SetSelectedGraphRequest): Request model for setting the user's selected graph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SuccessResponse]
  """

  kwargs = _get_kwargs(
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
  body: SetSelectedGraphRequest,
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  """Set Selected Graph

   Remembers the graph as the caller's current one: `GET /v1/graphs` then reports it as
  `selectedGraphId`, and the apps open on it. One graph per user, replacing the previous selection.
  Only a graph the caller belongs to can be selected; shared repositories cannot be.

  Args:
      body (SetSelectedGraphRequest): Request model for setting the user's selected graph.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SuccessResponse
  """

  return (
    await asyncio_detailed(
      client=client,
      body=body,
    )
  ).parsed
