from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_customer import BillingCustomer
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/billing/customer",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BillingCustomer]:
  if response.status_code == 200:
    response_200 = BillingCustomer.from_dict(response.json())

    return response_200

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BillingCustomer]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[BillingCustomer]:
  """Get Customer Info

   Get billing customer information including payment methods on file.

  Returns customer details, payment methods, and whether invoice billing is enabled.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[BillingCustomer]
  """

  kwargs = _get_kwargs()

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
) -> Optional[BillingCustomer]:
  """Get Customer Info

   Get billing customer information including payment methods on file.

  Returns customer details, payment methods, and whether invoice billing is enabled.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      BillingCustomer
  """

  return sync_detailed(
    client=client,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[BillingCustomer]:
  """Get Customer Info

   Get billing customer information including payment methods on file.

  Returns customer details, payment methods, and whether invoice billing is enabled.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[BillingCustomer]
  """

  kwargs = _get_kwargs()

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
) -> Optional[BillingCustomer]:
  """Get Customer Info

   Get billing customer information including payment methods on file.

  Returns customer details, payment methods, and whether invoice billing is enabled.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      BillingCustomer
  """

  return (
    await asyncio_detailed(
      client=client,
    )
  ).parsed
