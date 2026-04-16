from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  org_id: str,
  user_id: str,
) -> dict[str, Any]:

  _kwargs: dict[str, Any] = {
    "method": "delete",
    "url": "/v1/orgs/{org_id}/members/{user_id}".format(
      org_id=quote(str(org_id), safe=""),
      user_id=quote(str(user_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | None:
  if response.status_code == 204:
    response_204 = cast(Any, None)
    return response_204

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
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  org_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  """Remove Member

   Requires admin or owner role. Members may remove themselves.

  Args:
      org_id (str):
      user_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
    user_id=user_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  org_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
) -> Any | ErrorResponse | HTTPValidationError | None:
  """Remove Member

   Requires admin or owner role. Members may remove themselves.

  Args:
      org_id (str):
      user_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError
  """

  return sync_detailed(
    org_id=org_id,
    user_id=user_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  org_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
  """Remove Member

   Requires admin or owner role. Members may remove themselves.

  Args:
      org_id (str):
      user_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | ErrorResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
    user_id=user_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  org_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
) -> Any | ErrorResponse | HTTPValidationError | None:
  """Remove Member

   Requires admin or owner role. Members may remove themselves.

  Args:
      org_id (str):
      user_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | ErrorResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      org_id=org_id,
      user_id=user_id,
      client=client,
    )
  ).parsed
