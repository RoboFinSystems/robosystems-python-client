from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StorageItem")


@_attrs_define
class StorageItem:
  """One itemized piece of a graph's on-disk footprint.

  Attributes:
      type_ (str): One of: graph, memory, subgraph, vectors, staging, transient (blue-green build artifact), orphan (a
          `{parent}_*` database, vector index, or staging file with no row in the graph registry — reclaimable leftover of
          a deleted subgraph)
      id (str): Database or index identifier
      bytes_ (int): Size in bytes
  """

  type_: str
  id: str
  bytes_: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    type_ = self.type_

    id = self.id

    bytes_ = self.bytes_

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "type": type_,
        "id": id,
        "bytes": bytes_,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    type_ = d.pop("type")

    id = d.pop("id")

    bytes_ = d.pop("bytes")

    storage_item = cls(
      type_=type_,
      id=id,
      bytes_=bytes_,
    )

    storage_item.additional_properties = d
    return storage_item

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
