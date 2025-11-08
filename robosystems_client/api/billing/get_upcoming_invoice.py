from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upcoming_invoice import UpcomingInvoice
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/billing/invoices/upcoming",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["UpcomingInvoice", None]]:
  if response.status_code == 200:

    def _parse_response_200(data: object) -> Union["UpcomingInvoice", None]:
      if data is None:
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        response_200_type_0 = UpcomingInvoice.from_dict(data)

        return response_200_type_0
      except:  # noqa: E722
        pass
      return cast(Union["UpcomingInvoice", None], data)

    response_200 = _parse_response_200(response.json())

    return response_200

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["UpcomingInvoice", None]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[Union["UpcomingInvoice", None]]:
  """Get Upcoming Invoice

   Get preview of the next invoice.

  Returns estimated charges for the next billing period.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union['UpcomingInvoice', None]]
  """

  kwargs = _get_kwargs()

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  *,
  client: AuthenticatedClient,
) -> Optional[Union["UpcomingInvoice", None]]:
  """Get Upcoming Invoice

   Get preview of the next invoice.

  Returns estimated charges for the next billing period.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union['UpcomingInvoice', None]
  """

  return sync_detailed(
    client=client,
  ).parsed


async def asyncio_detailed(
  *,
  client: AuthenticatedClient,
) -> Response[Union["UpcomingInvoice", None]]:
  """Get Upcoming Invoice

   Get preview of the next invoice.

  Returns estimated charges for the next billing period.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union['UpcomingInvoice', None]]
  """

  kwargs = _get_kwargs()

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  *,
  client: AuthenticatedClient,
) -> Optional[Union["UpcomingInvoice", None]]:
  """Get Upcoming Invoice

   Get preview of the next invoice.

  Returns estimated charges for the next billing period.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union['UpcomingInvoice', None]
  """

  return (
    await asyncio_detailed(
      client=client,
    )
  ).parsed
