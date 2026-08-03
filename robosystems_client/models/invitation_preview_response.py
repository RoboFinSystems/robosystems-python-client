from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_role import OrgRole

T = TypeVar("T", bound="InvitationPreviewResponse")


@_attrs_define
class InvitationPreviewResponse:
  """Public preview of an invitation, looked up by its token.

  Attributes:
      org_name (str):
      email (str):
      role (OrgRole):
      expires_at (datetime.datetime):
  """

  org_name: str
  email: str
  role: OrgRole
  expires_at: datetime.datetime
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    org_name = self.org_name

    email = self.email

    role = self.role.value

    expires_at = self.expires_at.isoformat()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "org_name": org_name,
        "email": email,
        "role": role,
        "expires_at": expires_at,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    org_name = d.pop("org_name")

    email = d.pop("email")

    role = OrgRole(d.pop("role"))

    expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

    invitation_preview_response = cls(
      org_name=org_name,
      email=email,
      role=role,
      expires_at=expires_at,
    )

    invitation_preview_response.additional_properties = d
    return invitation_preview_response

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
