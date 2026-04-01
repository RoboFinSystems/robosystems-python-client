from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.security_response import SecurityResponse
from ...models.update_security_request import UpdateSecurityRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  security_id: str,
  *,
  body: UpdateSecurityRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "patch",
    "url": "/v1/investor/{graph_id}/securities/{security_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      security_id=quote(str(security_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SecurityResponse | None:
  if response.status_code == 200:
    response_200 = SecurityResponse.from_dict(response.json())

    return response_200

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | SecurityResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  security_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateSecurityRequest,
) -> Response[HTTPValidationError | SecurityResponse]:
  """Update Security

  Args:
      graph_id (str):
      security_id (str):
      body (UpdateSecurityRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | SecurityResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    security_id=security_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  security_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateSecurityRequest,
) -> HTTPValidationError | SecurityResponse | None:
  """Update Security

  Args:
      graph_id (str):
      security_id (str):
      body (UpdateSecurityRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | SecurityResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    security_id=security_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  security_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateSecurityRequest,
) -> Response[HTTPValidationError | SecurityResponse]:
  """Update Security

  Args:
      graph_id (str):
      security_id (str):
      body (UpdateSecurityRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | SecurityResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    security_id=security_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  security_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateSecurityRequest,
) -> HTTPValidationError | SecurityResponse | None:
  """Update Security

  Args:
      graph_id (str):
      security_id (str):
      body (UpdateSecurityRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | SecurityResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      security_id=security_id,
      client=client,
      body=body,
    )
  ).parsed
