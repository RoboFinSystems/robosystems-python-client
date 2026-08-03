from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_invitation_request import CreateInvitationRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.org_invitation_response import OrgInvitationResponse
from ...types import Response


def _get_kwargs(
  org_id: str,
  *,
  body: CreateInvitationRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/orgs/{org_id}/invitations".format(
      org_id=quote(str(org_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | OrgInvitationResponse | None:
  if response.status_code == 201:
    response_201 = OrgInvitationResponse.from_dict(response.json())

    return response_201

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

  if response.status_code == 409:
    response_409 = ErrorResponse.from_dict(response.json())

    return response_409

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if response.status_code == 501:
    response_501 = ErrorResponse.from_dict(response.json())

    return response_501

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | OrgInvitationResponse]:
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
  body: CreateInvitationRequest,
) -> Response[ErrorResponse | HTTPValidationError | OrgInvitationResponse]:
  """Invite Member

   Invite a new user to the organization by email. Disabled by default
  (ORG_MEMBER_INVITATIONS_ENABLED=false); returns 501 when disabled. Requires admin or owner role.
  Only emails without an existing account can be invited.

  Args:
      org_id (str):
      body (CreateInvitationRequest): Request to invite a new user to an organization by email.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | OrgInvitationResponse]
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
  body: CreateInvitationRequest,
) -> ErrorResponse | HTTPValidationError | OrgInvitationResponse | None:
  """Invite Member

   Invite a new user to the organization by email. Disabled by default
  (ORG_MEMBER_INVITATIONS_ENABLED=false); returns 501 when disabled. Requires admin or owner role.
  Only emails without an existing account can be invited.

  Args:
      org_id (str):
      body (CreateInvitationRequest): Request to invite a new user to an organization by email.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | OrgInvitationResponse
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
  body: CreateInvitationRequest,
) -> Response[ErrorResponse | HTTPValidationError | OrgInvitationResponse]:
  """Invite Member

   Invite a new user to the organization by email. Disabled by default
  (ORG_MEMBER_INVITATIONS_ENABLED=false); returns 501 when disabled. Requires admin or owner role.
  Only emails without an existing account can be invited.

  Args:
      org_id (str):
      body (CreateInvitationRequest): Request to invite a new user to an organization by email.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | HTTPValidationError | OrgInvitationResponse]
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
  body: CreateInvitationRequest,
) -> ErrorResponse | HTTPValidationError | OrgInvitationResponse | None:
  """Invite Member

   Invite a new user to the organization by email. Disabled by default
  (ORG_MEMBER_INVITATIONS_ENABLED=false); returns 501 when disabled. Requires admin or owner role.
  Only emails without an existing account can be invited.

  Args:
      org_id (str):
      body (CreateInvitationRequest): Request to invite a new user to an organization by email.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | HTTPValidationError | OrgInvitationResponse
  """

  return (
    await asyncio_detailed(
      org_id=org_id,
      client=client,
      body=body,
    )
  ).parsed
