import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.org_role import OrgRole
from ..models.org_type import OrgType

if TYPE_CHECKING:
  from ..models.org_detail_response_graphs_item import OrgDetailResponseGraphsItem
  from ..models.org_detail_response_limits_type_0 import OrgDetailResponseLimitsType0
  from ..models.org_detail_response_members_item import OrgDetailResponseMembersItem


T = TypeVar("T", bound="OrgDetailResponse")


@_attrs_define
class OrgDetailResponse:
  """Detailed organization response.

  Attributes:
      id (str):
      name (str):
      org_type (OrgType):
      user_role (OrgRole):
      members (list['OrgDetailResponseMembersItem']):
      graphs (list['OrgDetailResponseGraphsItem']):
      limits (Union['OrgDetailResponseLimitsType0', None]):
      created_at (datetime.datetime):
      updated_at (datetime.datetime):
  """

  id: str
  name: str
  org_type: OrgType
  user_role: OrgRole
  members: list["OrgDetailResponseMembersItem"]
  graphs: list["OrgDetailResponseGraphsItem"]
  limits: Union["OrgDetailResponseLimitsType0", None]
  created_at: datetime.datetime
  updated_at: datetime.datetime
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.org_detail_response_limits_type_0 import OrgDetailResponseLimitsType0

    id = self.id

    name = self.name

    org_type = self.org_type.value

    user_role = self.user_role.value

    members = []
    for members_item_data in self.members:
      members_item = members_item_data.to_dict()
      members.append(members_item)

    graphs = []
    for graphs_item_data in self.graphs:
      graphs_item = graphs_item_data.to_dict()
      graphs.append(graphs_item)

    limits: Union[None, dict[str, Any]]
    if isinstance(self.limits, OrgDetailResponseLimitsType0):
      limits = self.limits.to_dict()
    else:
      limits = self.limits

    created_at = self.created_at.isoformat()

    updated_at = self.updated_at.isoformat()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "org_type": org_type,
        "user_role": user_role,
        "members": members,
        "graphs": graphs,
        "limits": limits,
        "created_at": created_at,
        "updated_at": updated_at,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.org_detail_response_graphs_item import OrgDetailResponseGraphsItem
    from ..models.org_detail_response_limits_type_0 import OrgDetailResponseLimitsType0
    from ..models.org_detail_response_members_item import OrgDetailResponseMembersItem

    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    org_type = OrgType(d.pop("org_type"))

    user_role = OrgRole(d.pop("user_role"))

    members = []
    _members = d.pop("members")
    for members_item_data in _members:
      members_item = OrgDetailResponseMembersItem.from_dict(members_item_data)

      members.append(members_item)

    graphs = []
    _graphs = d.pop("graphs")
    for graphs_item_data in _graphs:
      graphs_item = OrgDetailResponseGraphsItem.from_dict(graphs_item_data)

      graphs.append(graphs_item)

    def _parse_limits(data: object) -> Union["OrgDetailResponseLimitsType0", None]:
      if data is None:
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        limits_type_0 = OrgDetailResponseLimitsType0.from_dict(data)

        return limits_type_0
      except:  # noqa: E722
        pass
      return cast(Union["OrgDetailResponseLimitsType0", None], data)

    limits = _parse_limits(d.pop("limits"))

    created_at = isoparse(d.pop("created_at"))

    updated_at = isoparse(d.pop("updated_at"))

    org_detail_response = cls(
      id=id,
      name=name,
      org_type=org_type,
      user_role=user_role,
      members=members,
      graphs=graphs,
      limits=limits,
      created_at=created_at,
      updated_at=updated_at,
    )

    org_detail_response.additional_properties = d
    return org_detail_response

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
