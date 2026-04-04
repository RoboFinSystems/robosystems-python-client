from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ScheduleFactResponse")


@_attrs_define
class ScheduleFactResponse:
  """
  Attributes:
      element_id (str):
      element_name (str):
      value (float):
      period_start (datetime.date):
      period_end (datetime.date):
  """

  element_id: str
  element_name: str
  value: float
  period_start: datetime.date
  period_end: datetime.date
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    element_name = self.element_name

    value = self.value

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "element_name": element_name,
        "value": value,
        "period_start": period_start,
        "period_end": period_end,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    element_name = d.pop("element_name")

    value = d.pop("value")

    period_start = isoparse(d.pop("period_start")).date()

    period_end = isoparse(d.pop("period_end")).date()

    schedule_fact_response = cls(
      element_id=element_id,
      element_name=element_name,
      value=value,
      period_start=period_start,
      period_end=period_end,
    )

    schedule_fact_response.additional_properties = d
    return schedule_fact_response

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
