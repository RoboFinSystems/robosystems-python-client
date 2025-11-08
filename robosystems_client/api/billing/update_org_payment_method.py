from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.update_payment_method_request import UpdatePaymentMethodRequest
from ...models.update_payment_method_response import UpdatePaymentMethodResponse
from ...types import Response


def _get_kwargs(
  org_id: str,
  *,
  body: UpdatePaymentMethodRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/billing/customer/{org_id}/payment-method",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, UpdatePaymentMethodResponse]]:
  if response.status_code == 200:
    response_200 = UpdatePaymentMethodResponse.from_dict(response.json())

    return response_200

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, UpdatePaymentMethodResponse]]:
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
  body: UpdatePaymentMethodRequest,
) -> Response[Union[HTTPValidationError, UpdatePaymentMethodResponse]]:
  """Update Organization Default Payment Method

   Update the default payment method for the organization.

  This changes which payment method will be used for future subscription charges.

  **Requirements:**
  - User must be an OWNER of the organization

  Args:
      org_id (str):
      body (UpdatePaymentMethodRequest): Request to update default payment method.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, UpdatePaymentMethodResponse]]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
    body=body,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  org_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdatePaymentMethodRequest,
) -> Optional[Union[HTTPValidationError, UpdatePaymentMethodResponse]]:
  """Update Organization Default Payment Method

   Update the default payment method for the organization.

  This changes which payment method will be used for future subscription charges.

  **Requirements:**
  - User must be an OWNER of the organization

  Args:
      org_id (str):
      body (UpdatePaymentMethodRequest): Request to update default payment method.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, UpdatePaymentMethodResponse]
  """

  return sync_detailed(
    org_id=org_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  org_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdatePaymentMethodRequest,
) -> Response[Union[HTTPValidationError, UpdatePaymentMethodResponse]]:
  """Update Organization Default Payment Method

   Update the default payment method for the organization.

  This changes which payment method will be used for future subscription charges.

  **Requirements:**
  - User must be an OWNER of the organization

  Args:
      org_id (str):
      body (UpdatePaymentMethodRequest): Request to update default payment method.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, UpdatePaymentMethodResponse]]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  org_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdatePaymentMethodRequest,
) -> Optional[Union[HTTPValidationError, UpdatePaymentMethodResponse]]:
  """Update Organization Default Payment Method

   Update the default payment method for the organization.

  This changes which payment method will be used for future subscription charges.

  **Requirements:**
  - User must be an OWNER of the organization

  Args:
      org_id (str):
      body (UpdatePaymentMethodRequest): Request to update default payment method.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, UpdatePaymentMethodResponse]
  """

  return (
    await asyncio_detailed(
      org_id=org_id,
      client=client,
      body=body,
    )
  ).parsed
