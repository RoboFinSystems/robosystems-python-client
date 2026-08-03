from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.graph_member_response import GraphMemberResponse


T = TypeVar("T", bound="GraphMemberListResponse")


@_attrs_define
class GraphMemberListResponse:
  """All users with access to a graph.

  Attributes:
      members (list[GraphMemberResponse]):
      total (int):
      graph_id (str):
  """

  members: list[GraphMemberResponse]
  total: int
  graph_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    members = []
    for members_item_data in self.members:
      members_item = members_item_data.to_dict()
      members.append(members_item)

    total = self.total

    graph_id = self.graph_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "members": members,
        "total": total,
        "graph_id": graph_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_member_response import GraphMemberResponse

    d = dict(src_dict)
    members = []
    _members = d.pop("members")
    for members_item_data in _members:
      members_item = GraphMemberResponse.from_dict(members_item_data)

      members.append(members_item)

    total = d.pop("total")

    graph_id = d.pop("graph_id")

    graph_member_list_response = cls(
      members=members,
      total=total,
      graph_id=graph_id,
    )

    graph_member_list_response.additional_properties = d
    return graph_member_list_response

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
