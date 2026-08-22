from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TerminateScheduleRequest")


@_attrs_define
class TerminateScheduleRequest:
  """End a schedule early at a month-end cutoff — no entry is booked.

  The no-entry half of schedule retirement, for terminations whose GL
  effect is already booked (an asset transferred via a manual journal
  entry, a prepaid refunded in the source system) or where none is
  wanted. In one transaction: deletes forward facts past the cutoff,
  voids the remaining obligation chain past it (pending and classified
  rows), and rewrites the SumEquals rule to prove the truncated curve.
  History at or before the cutoff is untouched.

  When the derecognition entry still needs to be booked, use
  `create-event-block(event_type='asset_disposed')` instead — the
  disposal handler posts it atomically with the same obligation void.

      Attributes:
          structure_id (str): The schedule structure to terminate.
          new_end_date (datetime.date): Last date the schedule covers — must be the last day of a month (schedule facts
              are whole-month). Facts and obligations for periods starting after this date are removed/voided.
          reason (str): Why the schedule is ending early — captured in the audit log.
  """

  structure_id: str
  new_end_date: datetime.date
  reason: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    new_end_date = self.new_end_date.isoformat()

    reason = self.reason

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "new_end_date": new_end_date,
        "reason": reason,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    new_end_date = datetime.date.fromisoformat(d.pop("new_end_date"))

    reason = d.pop("reason")

    terminate_schedule_request = cls(
      structure_id=structure_id,
      new_end_date=new_end_date,
      reason=reason,
    )

    terminate_schedule_request.additional_properties = d
    return terminate_schedule_request

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
