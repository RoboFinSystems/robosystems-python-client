from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.schedule_fact_response import ScheduleFactResponse


T = TypeVar("T", bound="ScheduleFactsResponse")


@_attrs_define
class ScheduleFactsResponse:
  """
  Attributes:
      structure_id (str):
      facts (list[ScheduleFactResponse]):
  """

  structure_id: str
  facts: list[ScheduleFactResponse]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    facts = []
    for facts_item_data in self.facts:
      facts_item = facts_item_data.to_dict()
      facts.append(facts_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "facts": facts,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.schedule_fact_response import ScheduleFactResponse

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    facts = []
    _facts = d.pop("facts")
    for facts_item_data in _facts:
      facts_item = ScheduleFactResponse.from_dict(facts_item_data)

      facts.append(facts_item)

    schedule_facts_response = cls(
      structure_id=structure_id,
      facts=facts,
    )

    schedule_facts_response.additional_properties = d
    return schedule_facts_response

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
