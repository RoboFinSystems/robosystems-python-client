from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduleCreatedResponse")


@_attrs_define
class ScheduleCreatedResponse:
  """
  Attributes:
      structure_id (str):
      name (str):
      taxonomy_id (str):
      total_periods (int):
      total_facts (int):
  """

  structure_id: str
  name: str
  taxonomy_id: str
  total_periods: int
  total_facts: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    name = self.name

    taxonomy_id = self.taxonomy_id

    total_periods = self.total_periods

    total_facts = self.total_facts

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "name": name,
        "taxonomy_id": taxonomy_id,
        "total_periods": total_periods,
        "total_facts": total_facts,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    name = d.pop("name")

    taxonomy_id = d.pop("taxonomy_id")

    total_periods = d.pop("total_periods")

    total_facts = d.pop("total_facts")

    schedule_created_response = cls(
      structure_id=structure_id,
      name=name,
      taxonomy_id=taxonomy_id,
      total_periods=total_periods,
      total_facts=total_facts,
    )

    schedule_created_response.additional_properties = d
    return schedule_created_response

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
