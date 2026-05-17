from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.operator_request import OperatorRequest
from ...models.operator_response import OperatorResponse
from ...models.response_mode import ResponseMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  operator_type: str,
  *,
  body: OperatorRequest,
  mode: None | ResponseMode | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  params: dict[str, Any] = {}

  json_mode: None | str | Unset
  if isinstance(mode, Unset):
    json_mode = UNSET
  elif isinstance(mode, ResponseMode):
    json_mode = mode.value
  else:
    json_mode = mode
  params["mode"] = json_mode

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/operator/{operator_type}".format(
      graph_id=quote(str(graph_id), safe=""),
      operator_type=quote(str(operator_type), safe=""),
    ),
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | OperatorResponse | None:
  if response.status_code == 200:
    response_200 = OperatorResponse.from_dict(response.json())

    return response_200

  if response.status_code == 202:
    response_202 = cast(Any, None)
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
) -> Response[Any | ErrorResponse | HTTPValidationError | OperatorResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  operator_type: str,
  *,
  client: AuthenticatedClient,
  body: OperatorRequest,
  mode: None | ResponseMode | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError | OperatorResponse]:
  """Execute Specific Operator

   Available: `financial` (SEC filings, accounting), `research` (deep analysis), `rag` (retrieval, no
  credits). Execution strategy auto-selected; override with `?mode=sync|async`.

  Args:
      graph_id (str):
      operator_type (str):
      mode (None | ResponseMode | Unset): Override execution mode: sync, async, stream, or auto
      body (OperatorRequest): Request model for operator interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | OperatorResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    operator_type=operator_type,
    body=body,
    mode=mode,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  operator_type: str,
  *,
  client: AuthenticatedClient,
  body: OperatorRequest,
  mode: None | ResponseMode | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | OperatorResponse | None:
  """Execute Specific Operator

   Available: `financial` (SEC filings, accounting), `research` (deep analysis), `rag` (retrieval, no
  credits). Execution strategy auto-selected; override with `?mode=sync|async`.

  Args:
      graph_id (str):
      operator_type (str):
      mode (None | ResponseMode | Unset): Override execution mode: sync, async, stream, or auto
      body (OperatorRequest): Request model for operator interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | OperatorResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    operator_type=operator_type,
    client=client,
    body=body,
    mode=mode,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  operator_type: str,
  *,
  client: AuthenticatedClient,
  body: OperatorRequest,
  mode: None | ResponseMode | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError | OperatorResponse]:
  """Execute Specific Operator

   Available: `financial` (SEC filings, accounting), `research` (deep analysis), `rag` (retrieval, no
  credits). Execution strategy auto-selected; override with `?mode=sync|async`.

  Args:
      graph_id (str):
      operator_type (str):
      mode (None | ResponseMode | Unset): Override execution mode: sync, async, stream, or auto
      body (OperatorRequest): Request model for operator interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError | OperatorResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    operator_type=operator_type,
    body=body,
    mode=mode,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  operator_type: str,
  *,
  client: AuthenticatedClient,
  body: OperatorRequest,
  mode: None | ResponseMode | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | OperatorResponse | None:
  """Execute Specific Operator

   Available: `financial` (SEC filings, accounting), `research` (deep analysis), `rag` (retrieval, no
  credits). Execution strategy auto-selected; override with `?mode=sync|async`.

  Args:
      graph_id (str):
      operator_type (str):
      mode (None | ResponseMode | Unset): Override execution mode: sync, async, stream, or auto
      body (OperatorRequest): Request model for operator interactions.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError | OperatorResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      operator_type=operator_type,
      client=client,
      body=body,
      mode=mode,
    )
  ).parsed
