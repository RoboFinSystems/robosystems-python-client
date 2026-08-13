from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_role import OrgRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgInvitationResponse")


@_attrs_define
class OrgInvitationResponse:
  """Organization invitation response.

  Attributes:
      id (str):
      org_id (str):
      email (str):
      role (OrgRole):
      status (str):
      invited_by_user_id (str):
      invited_by_name (None | str):
      created_at (datetime.datetime):
      expires_at (datetime.datetime):
      is_expired (bool):
      token (None | str | Unset): Test-support only: the raw invite token. Populated ONLY when
          AUTH_INVITE_TOKEN_IN_RESPONSE is enabled in a non-production environment; always null in production. Lets
          automated authorization tests complete the invite -> register flow without email interception.
  """

  id: str
  org_id: str
  email: str
  role: OrgRole
  status: str
  invited_by_user_id: str
  invited_by_name: None | str
  created_at: datetime.datetime
  expires_at: datetime.datetime
  is_expired: bool
  token: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    org_id = self.org_id

    email = self.email

    role = self.role.value

    status = self.status

    invited_by_user_id = self.invited_by_user_id

    invited_by_name: None | str
    invited_by_name = self.invited_by_name

    created_at = self.created_at.isoformat()

    expires_at = self.expires_at.isoformat()

    is_expired = self.is_expired

    token: None | str | Unset
    if isinstance(self.token, Unset):
      token = UNSET
    else:
      token = self.token

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "org_id": org_id,
        "email": email,
        "role": role,
        "status": status,
        "invited_by_user_id": invited_by_user_id,
        "invited_by_name": invited_by_name,
        "created_at": created_at,
        "expires_at": expires_at,
        "is_expired": is_expired,
      }
    )
    if token is not UNSET:
      field_dict["token"] = token

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    org_id = d.pop("org_id")

    email = d.pop("email")

    role = OrgRole(d.pop("role"))

    status = d.pop("status")

    invited_by_user_id = d.pop("invited_by_user_id")

    def _parse_invited_by_name(data: object) -> None | str:
      if data is None:
        return data
      return cast(None | str, data)

    invited_by_name = _parse_invited_by_name(d.pop("invited_by_name"))

    created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

    expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

    is_expired = d.pop("is_expired")

    def _parse_token(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    token = _parse_token(d.pop("token", UNSET))

    org_invitation_response = cls(
      id=id,
      org_id=org_id,
      email=email,
      role=role,
      status=status,
      invited_by_user_id=invited_by_user_id,
      invited_by_name=invited_by_name,
      created_at=created_at,
      expires_at=expires_at,
      is_expired=is_expired,
      token=token,
    )

    org_invitation_response.additional_properties = d
    return org_invitation_response

  @property
  def additional_keys(self) -> list[str]:
    return list(self.additional_properties.keys())

  def __getitem__(self, key: str) -> Any:
    return self.additional_properties[key]

  def __setitem__(self, key: str, value: Any) -> None:
    self.additional_properties[key] = value

  def __delitem__(self, key: str) -> None:
    del self.additional_properties[key]

  def __contains__(self, key: str) -> bool:
    return key in self.additional_properties
