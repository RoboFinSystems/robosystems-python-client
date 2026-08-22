from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TerminateScheduleResponse")


@_attrs_define
class TerminateScheduleResponse:
  """
  Attributes:
      structure_id (str):
      name (str):
      new_end_date (datetime.date):
      facts_deleted (int):
      obligations_voided (int):
      rule_updated (bool):
      reason (str):
  """

  structure_id: str
  name: str
  new_end_date: datetime.date
  facts_deleted: int
  obligations_voided: int
  rule_updated: bool
  reason: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    name = self.name

    new_end_date = self.new_end_date.isoformat()

    facts_deleted = self.facts_deleted

    obligations_voided = self.obligations_voided

    rule_updated = self.rule_updated

    reason = self.reason

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "name": name,
        "new_end_date": new_end_date,
        "facts_deleted": facts_deleted,
        "obligations_voided": obligations_voided,
        "rule_updated": rule_updated,
        "reason": reason,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    name = d.pop("name")

    new_end_date = datetime.date.fromisoformat(d.pop("new_end_date"))

    facts_deleted = d.pop("facts_deleted")

    obligations_voided = d.pop("obligations_voided")

    rule_updated = d.pop("rule_updated")

    reason = d.pop("reason")

    terminate_schedule_response = cls(
      structure_id=structure_id,
      name=name,
      new_end_date=new_end_date,
      facts_deleted=facts_deleted,
      obligations_voided=obligations_voided,
      rule_updated=rule_updated,
      reason=reason,
    )

    terminate_schedule_response.additional_properties = d
    return terminate_schedule_response

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
