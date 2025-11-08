from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_role import OrgRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="InviteMemberRequest")


@_attrs_define
class InviteMemberRequest:
  """Request to invite a member to an organization.

  Attributes:
      email (str):
      role (Union[None, OrgRole, Unset]):  Default: OrgRole.MEMBER.
  """

  email: str
  role: Union[None, OrgRole, Unset] = OrgRole.MEMBER
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    email = self.email

    role: Union[None, Unset, str]
    if isinstance(self.role, Unset):
      role = UNSET
    elif isinstance(self.role, OrgRole):
      role = self.role.value
    else:
      role = self.role

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "email": email,
      }
    )
    if role is not UNSET:
      field_dict["role"] = role

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    email = d.pop("email")

    def _parse_role(data: object) -> Union[None, OrgRole, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        role_type_0 = OrgRole(data)

        return role_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, OrgRole, Unset], data)

    role = _parse_role(d.pop("role", UNSET))

    invite_member_request = cls(
      email=email,
      role=role,
    )

    invite_member_request.additional_properties = d
    return invite_member_request

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
