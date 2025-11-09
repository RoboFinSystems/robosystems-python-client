from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.org_member_response import OrgMemberResponse


T = TypeVar("T", bound="OrgMemberListResponse")


@_attrs_define
class OrgMemberListResponse:
  """List of organization members response.

  Attributes:
      members (list['OrgMemberResponse']):
      total (int):
      org_id (str):
  """

  members: list["OrgMemberResponse"]
  total: int
  org_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    members = []
    for members_item_data in self.members:
      members_item = members_item_data.to_dict()
      members.append(members_item)

    total = self.total

    org_id = self.org_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "members": members,
        "total": total,
        "org_id": org_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.org_member_response import OrgMemberResponse

    d = dict(src_dict)
    members = []
    _members = d.pop("members")
    for members_item_data in _members:
      members_item = OrgMemberResponse.from_dict(members_item_data)

      members.append(members_item)

    total = d.pop("total")

    org_id = d.pop("org_id")

    org_member_list_response = cls(
      members=members,
      total=total,
      org_id=org_id,
    )

    org_member_list_response.additional_properties = d
    return org_member_list_response

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
