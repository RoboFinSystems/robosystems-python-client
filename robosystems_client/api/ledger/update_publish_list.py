from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.publish_list_response import PublishListResponse
from ...models.update_publish_list_request import UpdatePublishListRequest
from ...types import Response


def _get_kwargs(
  graph_id: str,
  list_id: str,
  *,
  body: UpdatePublishListRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "patch",
    "url": "/v1/ledger/{graph_id}/publish-lists/{list_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      list_id=quote(str(list_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PublishListResponse | None:
  if response.status_code == 200:
    response_200 = PublishListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PublishListResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  list_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdatePublishListRequest,
) -> Response[HTTPValidationError | PublishListResponse]:
  """Update Publish List

  Args:
      graph_id (str):
      list_id (str):
      body (UpdatePublishListRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PublishListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    list_id=list_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  list_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdatePublishListRequest,
) -> HTTPValidationError | PublishListResponse | None:
  """Update Publish List

  Args:
      graph_id (str):
      list_id (str):
      body (UpdatePublishListRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PublishListResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    list_id=list_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  list_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdatePublishListRequest,
) -> Response[HTTPValidationError | PublishListResponse]:
  """Update Publish List

  Args:
      graph_id (str):
      list_id (str):
      body (UpdatePublishListRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | PublishListResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    list_id=list_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  list_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdatePublishListRequest,
) -> HTTPValidationError | PublishListResponse | None:
  """Update Publish List

  Args:
      graph_id (str):
      list_id (str):
      body (UpdatePublishListRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | PublishListResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      list_id=list_id,
      client=client,
      body=body,
    )
  ).parsed
