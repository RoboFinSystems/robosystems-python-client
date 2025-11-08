import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.org_role import OrgRole

T = TypeVar("T", bound="OrgMemberResponse")


@_attrs_define
class OrgMemberResponse:
  """Organization member response.

  Attributes:
      user_id (str):
      name (str):
      email (str):
      role (OrgRole):
      joined_at (datetime.datetime):
      is_active (bool):
  """

  user_id: str
  name: str
  email: str
  role: OrgRole
  joined_at: datetime.datetime
  is_active: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    user_id = self.user_id

    name = self.name

    email = self.email

    role = self.role.value

    joined_at = self.joined_at.isoformat()

    is_active = self.is_active

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "user_id": user_id,
        "name": name,
        "email": email,
        "role": role,
        "joined_at": joined_at,
        "is_active": is_active,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    user_id = d.pop("user_id")

    name = d.pop("name")

    email = d.pop("email")

    role = OrgRole(d.pop("role"))

    joined_at = isoparse(d.pop("joined_at"))

    is_active = d.pop("is_active")

    org_member_response = cls(
      user_id=user_id,
      name=name,
      email=email,
      role=role,
      joined_at=joined_at,
      is_active=is_active,
    )

    org_member_response.additional_properties = d
    return org_member_response

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
