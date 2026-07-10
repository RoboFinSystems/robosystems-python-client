from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.memory_record import MemoryRecord


T = TypeVar("T", bound="MemoryListResponse")


@_attrs_define
class MemoryListResponse:
  """Governance list of memories for a graph.

  Attributes:
      total (int):
      memories (list[MemoryRecord]):
      graph_id (str):
  """

  total: int
  memories: list[MemoryRecord]
  graph_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    total = self.total

    memories = []
    for memories_item_data in self.memories:
      memories_item = memories_item_data.to_dict()
      memories.append(memories_item)

    graph_id = self.graph_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "total": total,
        "memories": memories,
        "graph_id": graph_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.memory_record import MemoryRecord

    d = dict(src_dict)
    total = d.pop("total")

    memories = []
    _memories = d.pop("memories")
    for memories_item_data in _memories:
      memories_item = MemoryRecord.from_dict(memories_item_data)

      memories.append(memories_item)

    graph_id = d.pop("graph_id")

    memory_list_response = cls(
      total=total,
      memories=memories,
      graph_id=graph_id,
    )

    memory_list_response.additional_properties = d
    return memory_list_response

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
