from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddPublishListMembersOperation")


@_attrs_define
class AddPublishListMembersOperation:
  """Add recipient graphs to a publish list.

  Attributes:
      target_graph_ids (list[str]): Graph IDs to add. Each must exist and have the same extension (roboledger /
          roboinvestor) enabled. Self-graph rejected.
      list_id (str): The publish list to add members to.
  """

  target_graph_ids: list[str]
  list_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    target_graph_ids = self.target_graph_ids

    list_id = self.list_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "target_graph_ids": target_graph_ids,
        "list_id": list_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    target_graph_ids = cast(list[str], d.pop("target_graph_ids"))

    list_id = d.pop("list_id")

    add_publish_list_members_operation = cls(
      target_graph_ids=target_graph_ids,
      list_id=list_id,
    )

    add_publish_list_members_operation.additional_properties = d
    return add_publish_list_members_operation

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
