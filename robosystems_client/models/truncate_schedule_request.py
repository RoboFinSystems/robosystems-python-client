from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="TruncateScheduleRequest")


@_attrs_define
class TruncateScheduleRequest:
  """
  Attributes:
      new_end_date (datetime.date): New last-covered date for the schedule. Facts with period_start > this date are
          deleted (along with any stale draft entries they produced). Historical facts (already posted) are preserved.
      reason (str): Required reason for the truncation (captured in audit log).
  """

  new_end_date: datetime.date
  reason: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    new_end_date = self.new_end_date.isoformat()

    reason = self.reason

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "new_end_date": new_end_date,
        "reason": reason,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    new_end_date = isoparse(d.pop("new_end_date")).date()

    reason = d.pop("reason")

    truncate_schedule_request = cls(
      new_end_date=new_end_date,
      reason=reason,
    )

    truncate_schedule_request.additional_properties = d
    return truncate_schedule_request

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
