from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.operation_resume_request import OperationResumeRequest
from ...models.resume_operation_response_resumeoperation import (
  ResumeOperationResponseResumeoperation,
)
from ...types import Response


def _get_kwargs(
  operation_id: str,
  *,
  body: OperationResumeRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/operations/{operation_id}/resume".format(
      operation_id=quote(str(operation_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
  Any
  | ErrorResponse
  | HTTPValidationError
  | ResumeOperationResponseResumeoperation
  | None
):
  if response.status_code == 202:
    response_202 = ResumeOperationResponseResumeoperation.from_dict(response.json())

    return response_202

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

  if response.status_code == 409:
    response_409 = cast(Any, None)
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
) -> Response[
  Any | ErrorResponse | HTTPValidationError | ResumeOperationResponseResumeoperation
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
  body: OperationResumeRequest,
) -> Response[
  Any | ErrorResponse | HTTPValidationError | ResumeOperationResponseResumeoperation
]:
  """Resume Operation

   Answers an operation that paused at a checkpoint (status `awaiting_input`) and puts it back on the
  worker queue with the answer. The operation keeps its id, so the stream, status and cancel links
  stay valid; reconnect to `/stream` to follow the resumed run. Consumes no credits.

  Args:
      operation_id (str): Operation identifier
      body (OperationResumeRequest): Answer for an operation paused at a checkpoint
          (`awaiting_input`).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | ResumeOperationResponseResumeoperation]
  """

  kwargs = _get_kwargs(
    operation_id=operation_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  operation_id: str,
  *,
  client: AuthenticatedClient,
  body: OperationResumeRequest,
) -> (
  Any
  | ErrorResponse
  | HTTPValidationError
  | ResumeOperationResponseResumeoperation
  | None
):
  """Resume Operation

   Answers an operation that paused at a checkpoint (status `awaiting_input`) and puts it back on the
  worker queue with the answer. The operation keeps its id, so the stream, status and cancel links
  stay valid; reconnect to `/stream` to follow the resumed run. Consumes no credits.

  Args:
      operation_id (str): Operation identifier
      body (OperationResumeRequest): Answer for an operation paused at a checkpoint
          (`awaiting_input`).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | ResumeOperationResponseResumeoperation
  """

  return sync_detailed(
    operation_id=operation_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  operation_id: str,
  *,
  client: AuthenticatedClient,
  body: OperationResumeRequest,
) -> Response[
  Any | ErrorResponse | HTTPValidationError | ResumeOperationResponseResumeoperation
]:
  """Resume Operation

   Answers an operation that paused at a checkpoint (status `awaiting_input`) and puts it back on the
  worker queue with the answer. The operation keeps its id, so the stream, status and cancel links
  stay valid; reconnect to `/stream` to follow the resumed run. Consumes no credits.

  Args:
      operation_id (str): Operation identifier
      body (OperationResumeRequest): Answer for an operation paused at a checkpoint
          (`awaiting_input`).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | ResumeOperationResponseResumeoperation]
  """

  kwargs = _get_kwargs(
    operation_id=operation_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  operation_id: str,
  *,
  client: AuthenticatedClient,
  body: OperationResumeRequest,
) -> (
  Any
  | ErrorResponse
  | HTTPValidationError
  | ResumeOperationResponseResumeoperation
  | None
):
  """Resume Operation

   Answers an operation that paused at a checkpoint (status `awaiting_input`) and puts it back on the
  worker queue with the answer. The operation keeps its id, so the stream, status and cancel links
  stay valid; reconnect to `/stream` to follow the resumed run. Consumes no credits.

  Args:
      operation_id (str): Operation identifier
      body (OperationResumeRequest): Answer for an operation paused at a checkpoint
          (`awaiting_input`).

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | ResumeOperationResponseResumeoperation
  """

  return (
    await asyncio_detailed(
      operation_id=operation_id,
      client=client,
      body=body,
    )
  ).parsed
