from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_connection_disposition import DeleteConnectionDisposition
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.success_response import SuccessResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  connection_id: str,
  *,
  disposition: DeleteConnectionDisposition
  | Unset = DeleteConnectionDisposition.DISCONNECT,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  json_disposition: str | Unset = UNSET
  if not isinstance(disposition, Unset):
    json_disposition = disposition.value

  params["disposition"] = json_disposition

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "delete",
    "url": "/v1/graphs/{graph_id}/connections/{connection_id}".format(
      graph_id=quote(str(graph_id), safe=""),
      connection_id=quote(str(connection_id), safe=""),
    ),
    "params": params,
  }

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
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  disposition: DeleteConnectionDisposition
  | Unset = DeleteConnectionDisposition.DISCONNECT,
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  """Delete Connection

   Removes the connection and revokes credentials. Imported data is preserved in the graph. Requires
  admin role. `disposition=sever` (QuickBooks only) is the cutover to native books: the chart
  QuickBooks created becomes the tenant's own and QuickBooks can never resume over it; the default
  `disconnect` keeps the connection reconnectable.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      disposition (DeleteConnectionDisposition | Unset): `disconnect` (default): soft-delete; a
          later re-OAuth to the same realm revives the connection. `sever`: the native-accounting
          cutover — QuickBooks only; the chart it created is stamped native-owned, write_policy
          drops to native, and the connection is never revived. Default:
          DeleteConnectionDisposition.DISCONNECT.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SuccessResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
    disposition=disposition,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  disposition: DeleteConnectionDisposition
  | Unset = DeleteConnectionDisposition.DISCONNECT,
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  """Delete Connection

   Removes the connection and revokes credentials. Imported data is preserved in the graph. Requires
  admin role. `disposition=sever` (QuickBooks only) is the cutover to native books: the chart
  QuickBooks created becomes the tenant's own and QuickBooks can never resume over it; the default
  `disconnect` keeps the connection reconnectable.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      disposition (DeleteConnectionDisposition | Unset): `disconnect` (default): soft-delete; a
          later re-OAuth to the same realm revives the connection. `sever`: the native-accounting
          cutover — QuickBooks only; the chart it created is stamped native-owned, write_policy
          drops to native, and the connection is never revived. Default:
          DeleteConnectionDisposition.DISCONNECT.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SuccessResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    connection_id=connection_id,
    client=client,
    disposition=disposition,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  disposition: DeleteConnectionDisposition
  | Unset = DeleteConnectionDisposition.DISCONNECT,
) -> Response[ErrorResponse | HTTPValidationError | SuccessResponse]:
  """Delete Connection

   Removes the connection and revokes credentials. Imported data is preserved in the graph. Requires
  admin role. `disposition=sever` (QuickBooks only) is the cutover to native books: the chart
  QuickBooks created becomes the tenant's own and QuickBooks can never resume over it; the default
  `disconnect` keeps the connection reconnectable.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      disposition (DeleteConnectionDisposition | Unset): `disconnect` (default): soft-delete; a
          later re-OAuth to the same realm revives the connection. `sever`: the native-accounting
          cutover — QuickBooks only; the chart it created is stamped native-owned, write_policy
          drops to native, and the connection is never revived. Default:
          DeleteConnectionDisposition.DISCONNECT.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | SuccessResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    connection_id=connection_id,
    disposition=disposition,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  connection_id: str,
  *,
  client: AuthenticatedClient,
  disposition: DeleteConnectionDisposition
  | Unset = DeleteConnectionDisposition.DISCONNECT,
) -> ErrorResponse | HTTPValidationError | SuccessResponse | None:
  """Delete Connection

   Removes the connection and revokes credentials. Imported data is preserved in the graph. Requires
  admin role. `disposition=sever` (QuickBooks only) is the cutover to native books: the chart
  QuickBooks created becomes the tenant's own and QuickBooks can never resume over it; the default
  `disconnect` keeps the connection reconnectable.

  Args:
      graph_id (str):
      connection_id (str): Connection identifier
      disposition (DeleteConnectionDisposition | Unset): `disconnect` (default): soft-delete; a
          later re-OAuth to the same realm revives the connection. `sever`: the native-accounting
          cutover — QuickBooks only; the chart it created is stamped native-owned, write_policy
          drops to native, and the connection is never revived. Default:
          DeleteConnectionDisposition.DISCONNECT.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | SuccessResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      connection_id=connection_id,
      client=client,
      disposition=disposition,
    )
  ).parsed
