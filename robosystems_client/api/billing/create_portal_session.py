from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.portal_session_response import PortalSessionResponse
from ...types import Response


def _get_kwargs(
  org_id: str,
) -> dict[str, Any]:

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/billing/customer/{org_id}/portal".format(
      org_id=quote(str(org_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | PortalSessionResponse | None:
  if response.status_code == 200:
    response_200 = PortalSessionResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | PortalSessionResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  org_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[ErrorResponse | HTTPValidationError | PortalSessionResponse]:
  """Create Customer Portal Session

   Returns a Stripe Customer Portal URL for managing payment methods and billing history. Requires org
  owner role.

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | PortalSessionResponse]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  org_id: str,
  *,
  client: AuthenticatedClient,
) -> ErrorResponse | HTTPValidationError | PortalSessionResponse | None:
  """Create Customer Portal Session

   Returns a Stripe Customer Portal URL for managing payment methods and billing history. Requires org
  owner role.

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | PortalSessionResponse
  """

  return sync_detailed(
    org_id=org_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  org_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[ErrorResponse | HTTPValidationError | PortalSessionResponse]:
  """Create Customer Portal Session

   Returns a Stripe Customer Portal URL for managing payment methods and billing history. Requires org
  owner role.

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | PortalSessionResponse]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  org_id: str,
  *,
  client: AuthenticatedClient,
) -> ErrorResponse | HTTPValidationError | PortalSessionResponse | None:
  """Create Customer Portal Session

   Returns a Stripe Customer Portal URL for managing payment methods and billing history. Requires org
  owner role.

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | PortalSessionResponse
  """

  return (
    await asyncio_detailed(
      org_id=org_id,
      client=client,
    )
  ).parsed
