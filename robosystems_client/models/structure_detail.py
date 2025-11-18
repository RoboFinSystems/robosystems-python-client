from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StructureDetail")


@_attrs_define
class StructureDetail:
  """
  Attributes:
      structure_id (str):
      structure_type (str):
      name (str):
      element_count (int):
  """

  structure_id: str
  structure_type: str
  name: str
  element_count: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    structure_type = self.structure_type

    name = self.name

    element_count = self.element_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "structure_type": structure_type,
        "name": name,
        "element_count": element_count,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    structure_type = d.pop("structure_type")

    name = d.pop("name")

    element_count = d.pop("element_count")

    structure_detail = cls(
      structure_id=structure_id,
      structure_type=structure_type,
      name=name,
      element_count=element_count,
    )

    structure_detail.additional_properties = d
    return structure_detail

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
