from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.portal_session_response import PortalSessionResponse
from ...types import Response


def _get_kwargs(
  org_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/billing/customer/{org_id}/portal",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, PortalSessionResponse]]:
  if response.status_code == 200:
    response_200 = PortalSessionResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, PortalSessionResponse]]:
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
) -> Response[Union[HTTPValidationError, PortalSessionResponse]]:
  """Create Customer Portal Session

   Create a Stripe Customer Portal session for managing payment methods.

  The portal allows users to:
  - Add new payment methods
  - Remove existing payment methods
  - Update default payment method
  - View billing history

  The user will be redirected to Stripe's hosted portal page and returned to the billing page when
  done.

  **Requirements:**
  - User must be an OWNER of the organization
  - Organization must have a Stripe customer ID (i.e., has gone through checkout at least once)

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, PortalSessionResponse]]
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
) -> Optional[Union[HTTPValidationError, PortalSessionResponse]]:
  """Create Customer Portal Session

   Create a Stripe Customer Portal session for managing payment methods.

  The portal allows users to:
  - Add new payment methods
  - Remove existing payment methods
  - Update default payment method
  - View billing history

  The user will be redirected to Stripe's hosted portal page and returned to the billing page when
  done.

  **Requirements:**
  - User must be an OWNER of the organization
  - Organization must have a Stripe customer ID (i.e., has gone through checkout at least once)

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, PortalSessionResponse]
  """

  return sync_detailed(
    org_id=org_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  org_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, PortalSessionResponse]]:
  """Create Customer Portal Session

   Create a Stripe Customer Portal session for managing payment methods.

  The portal allows users to:
  - Add new payment methods
  - Remove existing payment methods
  - Update default payment method
  - View billing history

  The user will be redirected to Stripe's hosted portal page and returned to the billing page when
  done.

  **Requirements:**
  - User must be an OWNER of the organization
  - Organization must have a Stripe customer ID (i.e., has gone through checkout at least once)

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, PortalSessionResponse]]
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
) -> Optional[Union[HTTPValidationError, PortalSessionResponse]]:
  """Create Customer Portal Session

   Create a Stripe Customer Portal session for managing payment methods.

  The portal allows users to:
  - Add new payment methods
  - Remove existing payment methods
  - Update default payment method
  - View billing history

  The user will be redirected to Stripe's hosted portal page and returned to the billing page when
  done.

  **Requirements:**
  - User must be an OWNER of the organization
  - Organization must have a Stripe customer ID (i.e., has gone through checkout at least once)

  Args:
      org_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, PortalSessionResponse]
  """

  return (
    await asyncio_detailed(
      org_id=org_id,
      client=client,
    )
  ).parsed
