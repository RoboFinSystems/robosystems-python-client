from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.invite_member_request import InviteMemberRequest
from ...models.org_member_response import OrgMemberResponse
from ...types import Response


def _get_kwargs(
  org_id: str,
  *,
  body: InviteMemberRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/orgs/{org_id}/members",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, OrgMemberResponse]]:
  if response.status_code == 201:
    response_201 = OrgMemberResponse.from_dict(response.json())

    return response_201

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
  *,
  client: AuthenticatedClient,
  body: InviteMemberRequest,
) -> Response[Union[HTTPValidationError, OrgMemberResponse]]:
  """Invite Member

   Invite a user to join the organization. Requires admin or owner role.

    **⚠️ FEATURE NOT READY**: This endpoint is disabled by default
  (ORG_MEMBER_INVITATIONS_ENABLED=false).
    Returns 501 NOT IMPLEMENTED when disabled. See endpoint implementation for TODO list before
  enabling.

  Args:
      org_id (str):
      body (InviteMemberRequest): Request to invite a member to an organization.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, OrgMemberResponse]]
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
  body: InviteMemberRequest,
) -> Optional[Union[HTTPValidationError, OrgMemberResponse]]:
  """Invite Member

   Invite a user to join the organization. Requires admin or owner role.

    **⚠️ FEATURE NOT READY**: This endpoint is disabled by default
  (ORG_MEMBER_INVITATIONS_ENABLED=false).
    Returns 501 NOT IMPLEMENTED when disabled. See endpoint implementation for TODO list before
  enabling.

  Args:
      org_id (str):
      body (InviteMemberRequest): Request to invite a member to an organization.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, OrgMemberResponse]
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
  body: InviteMemberRequest,
) -> Response[Union[HTTPValidationError, OrgMemberResponse]]:
  """Invite Member

   Invite a user to join the organization. Requires admin or owner role.

    **⚠️ FEATURE NOT READY**: This endpoint is disabled by default
  (ORG_MEMBER_INVITATIONS_ENABLED=false).
    Returns 501 NOT IMPLEMENTED when disabled. See endpoint implementation for TODO list before
  enabling.

  Args:
      org_id (str):
      body (InviteMemberRequest): Request to invite a member to an organization.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[HTTPValidationError, OrgMemberResponse]]
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
  body: InviteMemberRequest,
) -> Optional[Union[HTTPValidationError, OrgMemberResponse]]:
  """Invite Member

   Invite a user to join the organization. Requires admin or owner role.

    **⚠️ FEATURE NOT READY**: This endpoint is disabled by default
  (ORG_MEMBER_INVITATIONS_ENABLED=false).
    Returns 501 NOT IMPLEMENTED when disabled. See endpoint implementation for TODO list before
  enabling.

  Args:
      org_id (str):
      body (InviteMemberRequest): Request to invite a member to an organization.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[HTTPValidationError, OrgMemberResponse]
  """

  return (
    await asyncio_detailed(
      org_id=org_id,
      client=client,
      body=body,
    )
  ).parsed
