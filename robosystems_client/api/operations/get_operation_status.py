from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
    "url": f"/v1/operations/{operation_id}/status",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
  Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]
]:
  if response.status_code == 200:
    response_200 = GetOperationStatusResponseGetoperationstatus.from_dict(
      response.json()
    )

    return response_200

  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403

  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
  Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]
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
  Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]
]:
  """Get Operation Status

   Get current status and metadata for an operation.

  Returns detailed information including:
  - Current status (pending, running, completed, failed, cancelled)
  - Creation and update timestamps
  - Operation type and associated graph
  - Result data (for completed operations)
  - Error details (for failed operations)

  This endpoint provides a point-in-time status check, while the `/stream` endpoint
  provides real-time updates. Use this for polling or initial status checks.

  **No credits are consumed for status checks.**

  Args:
      operation_id (str): Operation identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]]
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
) -> Optional[
  Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]
]:
  """Get Operation Status

   Get current status and metadata for an operation.

  Returns detailed information including:
  - Current status (pending, running, completed, failed, cancelled)
  - Creation and update timestamps
  - Operation type and associated graph
  - Result data (for completed operations)
  - Error details (for failed operations)

  This endpoint provides a point-in-time status check, while the `/stream` endpoint
  provides real-time updates. Use this for polling or initial status checks.

  **No credits are consumed for status checks.**

  Args:
      operation_id (str): Operation identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]
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
  Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]
]:
  """Get Operation Status

   Get current status and metadata for an operation.

  Returns detailed information including:
  - Current status (pending, running, completed, failed, cancelled)
  - Creation and update timestamps
  - Operation type and associated graph
  - Result data (for completed operations)
  - Error details (for failed operations)

  This endpoint provides a point-in-time status check, while the `/stream` endpoint
  provides real-time updates. Use this for polling or initial status checks.

  **No credits are consumed for status checks.**

  Args:
      operation_id (str): Operation identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]]
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
) -> Optional[
  Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]
]:
  """Get Operation Status

   Get current status and metadata for an operation.

  Returns detailed information including:
  - Current status (pending, running, completed, failed, cancelled)
  - Creation and update timestamps
  - Operation type and associated graph
  - Result data (for completed operations)
  - Error details (for failed operations)

  This endpoint provides a point-in-time status check, while the `/stream` endpoint
  provides real-time updates. Use this for polling or initial status checks.

  **No credits are consumed for status checks.**

  Args:
      operation_id (str): Operation identifier

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[Any, GetOperationStatusResponseGetoperationstatus, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      operation_id=operation_id,
      client=client,
    )
  ).parsed
