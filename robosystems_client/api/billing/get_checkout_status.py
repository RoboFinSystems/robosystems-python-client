from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checkout_status_response import CheckoutStatusResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  session_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/billing/checkout/{session_id}/status",
  }

  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CheckoutStatusResponse, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = CheckoutStatusResponse.from_dict(response.json())

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
) -> Response[Union[CheckoutStatusResponse, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  session_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[CheckoutStatusResponse, HTTPValidationError]]:
  """Get Checkout Session Status

   Poll the status of a checkout session.

  Frontend should poll this endpoint after user returns from Stripe Checkout
  to determine when the resource is ready.

  **Status Values:**
  - `pending_payment`: Waiting for payment to complete
  - `provisioning`: Payment confirmed, resource being created
  - `completed`: Resource is ready (resource_id will be set)
  - `failed`: Something went wrong (error field will be set)

  **When status is 'completed':**
  - For graphs: `resource_id` will be the graph_id, and `operation_id` can be used to monitor SSE
  progress
  - For repositories: `resource_id` will be the repository name and access is immediately available

  Args:
      session_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[CheckoutStatusResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    session_id=session_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  session_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[CheckoutStatusResponse, HTTPValidationError]]:
  """Get Checkout Session Status

   Poll the status of a checkout session.

  Frontend should poll this endpoint after user returns from Stripe Checkout
  to determine when the resource is ready.

  **Status Values:**
  - `pending_payment`: Waiting for payment to complete
  - `provisioning`: Payment confirmed, resource being created
  - `completed`: Resource is ready (resource_id will be set)
  - `failed`: Something went wrong (error field will be set)

  **When status is 'completed':**
  - For graphs: `resource_id` will be the graph_id, and `operation_id` can be used to monitor SSE
  progress
  - For repositories: `resource_id` will be the repository name and access is immediately available

  Args:
      session_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[CheckoutStatusResponse, HTTPValidationError]
  """

  return sync_detailed(
    session_id=session_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  session_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Union[CheckoutStatusResponse, HTTPValidationError]]:
  """Get Checkout Session Status

   Poll the status of a checkout session.

  Frontend should poll this endpoint after user returns from Stripe Checkout
  to determine when the resource is ready.

  **Status Values:**
  - `pending_payment`: Waiting for payment to complete
  - `provisioning`: Payment confirmed, resource being created
  - `completed`: Resource is ready (resource_id will be set)
  - `failed`: Something went wrong (error field will be set)

  **When status is 'completed':**
  - For graphs: `resource_id` will be the graph_id, and `operation_id` can be used to monitor SSE
  progress
  - For repositories: `resource_id` will be the repository name and access is immediately available

  Args:
      session_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[CheckoutStatusResponse, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    session_id=session_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  session_id: str,
  *,
  client: AuthenticatedClient,
) -> Optional[Union[CheckoutStatusResponse, HTTPValidationError]]:
  """Get Checkout Session Status

   Poll the status of a checkout session.

  Frontend should poll this endpoint after user returns from Stripe Checkout
  to determine when the resource is ready.

  **Status Values:**
  - `pending_payment`: Waiting for payment to complete
  - `provisioning`: Payment confirmed, resource being created
  - `completed`: Resource is ready (resource_id will be set)
  - `failed`: Something went wrong (error field will be set)

  **When status is 'completed':**
  - For graphs: `resource_id` will be the graph_id, and `operation_id` can be used to monitor SSE
  progress
  - For repositories: `resource_id` will be the repository name and access is immediately available

  Args:
      session_id (str):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[CheckoutStatusResponse, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      session_id=session_id,
      client=client,
    )
  ).parsed
