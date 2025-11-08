import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.org_role import OrgRole
from ..models.org_type import OrgType

T = TypeVar("T", bound="OrgResponse")


@_attrs_define
class OrgResponse:
  """Organization summary response.

  Attributes:
      id (str):
      name (str):
      org_type (OrgType):
      role (OrgRole):
      member_count (int):
      graph_count (int):
      created_at (datetime.datetime):
      joined_at (datetime.datetime):
  """

  id: str
  name: str
  org_type: OrgType
  role: OrgRole
  member_count: int
  graph_count: int
  created_at: datetime.datetime
  joined_at: datetime.datetime
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    org_type = self.org_type.value

    role = self.role.value

    member_count = self.member_count

    graph_count = self.graph_count

    created_at = self.created_at.isoformat()

    joined_at = self.joined_at.isoformat()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "org_type": org_type,
        "role": role,
        "member_count": member_count,
        "graph_count": graph_count,
        "created_at": created_at,
        "joined_at": joined_at,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    org_type = OrgType(d.pop("org_type"))

    role = OrgRole(d.pop("role"))

    member_count = d.pop("member_count")

    graph_count = d.pop("graph_count")

    created_at = isoparse(d.pop("created_at"))

    joined_at = isoparse(d.pop("joined_at"))

    org_response = cls(
      id=id,
      name=name,
      org_type=org_type,
      role=role,
      member_count=member_count,
      graph_count=graph_count,
      created_at=created_at,
      joined_at=joined_at,
    )

    org_response.additional_properties = d
    return org_response

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
