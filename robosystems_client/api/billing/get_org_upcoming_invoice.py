from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.upcoming_invoice import UpcomingInvoice
from ...types import Response


def _get_kwargs(
  org_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/billing/invoices/{org_id}/upcoming".format(
      org_id=quote(str(org_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | None | UpcomingInvoice | None:
  if response.status_code == 200:

    def _parse_response_200(data: object) -> None | UpcomingInvoice:
      if data is None:
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        response_200_type_0 = UpcomingInvoice.from_dict(data)

        return response_200_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | UpcomingInvoice, data)

    response_200 = _parse_response_200(response.json())

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
) -> Response[HTTPValidationError | None | UpcomingInvoice]:
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
) -> Response[HTTPValidationError | None | UpcomingInvoice]:
  """Get Organization Upcoming Invoice

   Get preview of the next invoice for an organization.

  Returns estimated charges for the next billing period.

  **Requirements:**
  - User must be a member of the organization
  - Full invoice details are only visible to owners and admins

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | None | UpcomingInvoice]
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
) -> HTTPValidationError | None | UpcomingInvoice | None:
  """Get Organization Upcoming Invoice

   Get preview of the next invoice for an organization.

  Returns estimated charges for the next billing period.

  **Requirements:**
  - User must be a member of the organization
  - Full invoice details are only visible to owners and admins

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | None | UpcomingInvoice
  """

  return sync_detailed(
    org_id=org_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  org_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[HTTPValidationError | None | UpcomingInvoice]:
  """Get Organization Upcoming Invoice

   Get preview of the next invoice for an organization.

  Returns estimated charges for the next billing period.

  **Requirements:**
  - User must be a member of the organization
  - Full invoice details are only visible to owners and admins

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | None | UpcomingInvoice]
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
) -> HTTPValidationError | None | UpcomingInvoice | None:
  """Get Organization Upcoming Invoice

   Get preview of the next invoice for an organization.

  Returns estimated charges for the next billing period.

  **Requirements:**
  - User must be a member of the organization
  - Full invoice details are only visible to owners and admins

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | None | UpcomingInvoice
  """

  return (
    await asyncio_detailed(
      org_id=org_id,
      client=client,
    )
  ).parsed
