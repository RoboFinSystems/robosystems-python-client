from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.schedule_created_response_rule_summary_type_0 import (
    ScheduleCreatedResponseRuleSummaryType0,
  )


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
      rule_summary (None | ScheduleCreatedResponseRuleSummaryType0 | Unset):
      schedule_created_event_id (None | str | Unset):
      pending_event_count (int | Unset):  Default: 0.
  """

  structure_id: str
  name: str
  taxonomy_id: str
  total_periods: int
  total_facts: int
  rule_summary: None | ScheduleCreatedResponseRuleSummaryType0 | Unset = UNSET
  schedule_created_event_id: None | str | Unset = UNSET
  pending_event_count: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.schedule_created_response_rule_summary_type_0 import (
      ScheduleCreatedResponseRuleSummaryType0,
    )

    structure_id = self.structure_id

    name = self.name

    taxonomy_id = self.taxonomy_id

    total_periods = self.total_periods

    total_facts = self.total_facts

    rule_summary: dict[str, Any] | None | Unset
    if isinstance(self.rule_summary, Unset):
      rule_summary = UNSET
    elif isinstance(self.rule_summary, ScheduleCreatedResponseRuleSummaryType0):
      rule_summary = self.rule_summary.to_dict()
    else:
      rule_summary = self.rule_summary

    schedule_created_event_id: None | str | Unset
    if isinstance(self.schedule_created_event_id, Unset):
      schedule_created_event_id = UNSET
    else:
      schedule_created_event_id = self.schedule_created_event_id

    pending_event_count = self.pending_event_count

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
    if rule_summary is not UNSET:
      field_dict["rule_summary"] = rule_summary
    if schedule_created_event_id is not UNSET:
      field_dict["schedule_created_event_id"] = schedule_created_event_id
    if pending_event_count is not UNSET:
      field_dict["pending_event_count"] = pending_event_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.schedule_created_response_rule_summary_type_0 import (
      ScheduleCreatedResponseRuleSummaryType0,
    )

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    name = d.pop("name")

    taxonomy_id = d.pop("taxonomy_id")

    total_periods = d.pop("total_periods")

    total_facts = d.pop("total_facts")

    def _parse_rule_summary(
      data: object,
    ) -> None | ScheduleCreatedResponseRuleSummaryType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        rule_summary_type_0 = ScheduleCreatedResponseRuleSummaryType0.from_dict(data)

        return rule_summary_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ScheduleCreatedResponseRuleSummaryType0 | Unset, data)

    rule_summary = _parse_rule_summary(d.pop("rule_summary", UNSET))

    def _parse_schedule_created_event_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    schedule_created_event_id = _parse_schedule_created_event_id(
      d.pop("schedule_created_event_id", UNSET)
    )

    pending_event_count = d.pop("pending_event_count", UNSET)

    schedule_created_response = cls(
      structure_id=structure_id,
      name=name,
      taxonomy_id=taxonomy_id,
      total_periods=total_periods,
      total_facts=total_facts,
      rule_summary=rule_summary,
      schedule_created_event_id=schedule_created_event_id,
      pending_event_count=pending_event_count,
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
