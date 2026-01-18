from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.org_usage_response import OrgUsageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  org_id: str,
  *,
  days: int | Unset = 30,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  params["days"] = days

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/orgs/{org_id}/usage".format(
      org_id=quote(str(org_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | OrgUsageResponse | None:
  if response.status_code == 200:
    response_200 = OrgUsageResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | OrgUsageResponse]:
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
  days: int | Unset = 30,
) -> Response[HTTPValidationError | OrgUsageResponse]:
  """Get Organization Usage

   Get detailed usage statistics for an organization aggregated across all graphs.

  Args:
      org_id (str):
      days (int | Unset):  Default: 30.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | OrgUsageResponse]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
    days=days,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  org_id: str,
  *,
  client: AuthenticatedClient,
  days: int | Unset = 30,
) -> HTTPValidationError | OrgUsageResponse | None:
  """Get Organization Usage

   Get detailed usage statistics for an organization aggregated across all graphs.

  Args:
      org_id (str):
      days (int | Unset):  Default: 30.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | OrgUsageResponse
  """

  return sync_detailed(
    org_id=org_id,
    client=client,
    days=days,
  ).parsed


async def asyncio_detailed(
  org_id: str,
  *,
  client: AuthenticatedClient,
  days: int | Unset = 30,
) -> Response[HTTPValidationError | OrgUsageResponse]:
  """Get Organization Usage

   Get detailed usage statistics for an organization aggregated across all graphs.

  Args:
      org_id (str):
      days (int | Unset):  Default: 30.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | OrgUsageResponse]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
    days=days,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  org_id: str,
  *,
  client: AuthenticatedClient,
  days: int | Unset = 30,
) -> HTTPValidationError | OrgUsageResponse | None:
  """Get Organization Usage

   Get detailed usage statistics for an organization aggregated across all graphs.

  Args:
      org_id (str):
      days (int | Unset):  Default: 30.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | OrgUsageResponse
  """

  return (
    await asyncio_detailed(
      org_id=org_id,
      client=client,
      days=days,
    )
  ).parsed
