from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseStorageEntry")


@_attrs_define
class DatabaseStorageEntry:
  """Storage for a single database on the instance.

  Attributes:
      graph_id (str): Database identifier
      is_parent (bool | Unset): Whether this is the parent graph Default: False.
      size_mb (float | None | Unset): Database size in MB
  """

  graph_id: str
  is_parent: bool | Unset = False
  size_mb: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    is_parent = self.is_parent

    size_mb: float | None | Unset
    if isinstance(self.size_mb, Unset):
      size_mb = UNSET
    else:
      size_mb = self.size_mb

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
      }
    )
    if is_parent is not UNSET:
      field_dict["is_parent"] = is_parent
    if size_mb is not UNSET:
      field_dict["size_mb"] = size_mb

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    is_parent = d.pop("is_parent", UNSET)

    def _parse_size_mb(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    size_mb = _parse_size_mb(d.pop("size_mb", UNSET))

    database_storage_entry = cls(
      graph_id=graph_id,
      is_parent=is_parent,
      size_mb=size_mb,
    )

    database_storage_entry.additional_properties = d
    return database_storage_entry

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
