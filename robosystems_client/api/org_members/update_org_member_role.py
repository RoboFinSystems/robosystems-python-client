from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.org_member_response import OrgMemberResponse
from ...models.update_member_role_request import UpdateMemberRoleRequest
from ...types import Response


def _get_kwargs(
  org_id: str,
  user_id: str,
  *,
  body: UpdateMemberRoleRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "put",
    "url": f"/v1/orgs/{org_id}/members/{user_id}",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, OrgMemberResponse]]:
  if response.status_code == 200:
    response_200 = OrgMemberResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, OrgMemberResponse]]:
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
  body: UpdateMemberRoleRequest,
) -> Response[Union[HTTPValidationError, OrgMemberResponse]]:
  """Update Member Role

   Update a member's role in the organization. Requires admin or owner role.

  Args:
      org_id (str):
      user_id (str):
      body (UpdateMemberRoleRequest): Request to update a member's role.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, OrgMemberResponse]]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
    user_id=user_id,
    body=body,
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
  body: UpdateMemberRoleRequest,
) -> Optional[Union[HTTPValidationError, OrgMemberResponse]]:
  """Update Member Role

   Update a member's role in the organization. Requires admin or owner role.

  Args:
      org_id (str):
      user_id (str):
      body (UpdateMemberRoleRequest): Request to update a member's role.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, OrgMemberResponse]
  """

  return sync_detailed(
    org_id=org_id,
    user_id=user_id,
    client=client,
    body=body,
  ).parsed


async def asyncio_detailed(
  org_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateMemberRoleRequest,
) -> Response[Union[HTTPValidationError, OrgMemberResponse]]:
  """Update Member Role

   Update a member's role in the organization. Requires admin or owner role.

  Args:
      org_id (str):
      user_id (str):
      body (UpdateMemberRoleRequest): Request to update a member's role.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, OrgMemberResponse]]
  """

  kwargs = _get_kwargs(
    org_id=org_id,
    user_id=user_id,
    body=body,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  org_id: str,
  user_id: str,
  *,
  client: AuthenticatedClient,
  body: UpdateMemberRoleRequest,
) -> Optional[Union[HTTPValidationError, OrgMemberResponse]]:
  """Update Member Role

   Update a member's role in the organization. Requires admin or owner role.

  Args:
      org_id (str):
      user_id (str):
      body (UpdateMemberRoleRequest): Request to update a member's role.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, OrgMemberResponse]
  """

  return (
    await asyncio_detailed(
      org_id=org_id,
      user_id=user_id,
      client=client,
      body=body,
    )
  ).parsed
