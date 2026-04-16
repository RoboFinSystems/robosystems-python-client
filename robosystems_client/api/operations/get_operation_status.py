from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_operation_status_response_getoperationstatus import (
  GetOperationStatusResponseGetoperationstatus,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  operation_id: str,
) -> dict[str, Any]:

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/operations/{operation_id}/status".format(
      operation_id=quote(str(operation_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
  ErrorResponse
  | GetOperationStatusResponseGetoperationstatus
  | HTTPValidationError
  | None
):
  if response.status_code == 200:
    response_200 = GetOperationStatusResponseGetoperationstatus.from_dict(
      response.json()
    )

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
) -> Response[
  ErrorResponse | GetOperationStatusResponseGetoperationstatus | HTTPValidationError
]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  operation_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[
  ErrorResponse | GetOperationStatusResponseGetoperationstatus | HTTPValidationError
]:
  """Get Operation Status

   Point-in-time status check. Use `/stream` for real-time updates. Consumes no credits.

  Args:
      operation_id (str): Operation identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GetOperationStatusResponseGetoperationstatus | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    operation_id=operation_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  operation_id: str,
  *,
  client: AuthenticatedClient,
) -> (
  ErrorResponse
  | GetOperationStatusResponseGetoperationstatus
  | HTTPValidationError
  | None
):
  """Get Operation Status

   Point-in-time status check. Use `/stream` for real-time updates. Consumes no credits.

  Args:
      operation_id (str): Operation identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | GetOperationStatusResponseGetoperationstatus | HTTPValidationError
  """

  return sync_detailed(
    operation_id=operation_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  operation_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[
  ErrorResponse | GetOperationStatusResponseGetoperationstatus | HTTPValidationError
]:
  """Get Operation Status

   Point-in-time status check. Use `/stream` for real-time updates. Consumes no credits.

  Args:
      operation_id (str): Operation identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | GetOperationStatusResponseGetoperationstatus | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    operation_id=operation_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  operation_id: str,
  *,
  client: AuthenticatedClient,
) -> (
  ErrorResponse
  | GetOperationStatusResponseGetoperationstatus
  | HTTPValidationError
  | None
):
  """Get Operation Status

   Point-in-time status check. Use `/stream` for real-time updates. Consumes no credits.

  Args:
      operation_id (str): Operation identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | GetOperationStatusResponseGetoperationstatus | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      operation_id=operation_id,
      client=client,
    )
  ).parsed
