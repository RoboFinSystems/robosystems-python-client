from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="TruncateScheduleOperation")


@_attrs_define
class TruncateScheduleOperation:
  """CQRS-shaped body for `POST /operations/truncate-schedule`.

  Bundles the target schedule's `structure_id` with the update payload so
  the single-body signature matches the registrar/MCP contract. The REST
  handler, GraphQL resolver, and MCP tool all resolve to the same
  `cmd_truncate_schedule(session, body, created_by=...)`.

      Attributes:
          new_end_date (datetime.date): New last-covered date for the schedule. Facts with period_start > this date are
              deleted (along with any stale draft entries they produced). Historical facts (already posted) are preserved.
          reason (str): Required reason for the truncation (captured in audit log).
          structure_id (str): Target schedule structure ID.
  """

  new_end_date: datetime.date
  reason: str
  structure_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    new_end_date = self.new_end_date.isoformat()

    reason = self.reason

    structure_id = self.structure_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "new_end_date": new_end_date,
        "reason": reason,
        "structure_id": structure_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    new_end_date = isoparse(d.pop("new_end_date")).date()

    reason = d.pop("reason")

    structure_id = d.pop("structure_id")

    truncate_schedule_operation = cls(
      new_end_date=new_end_date,
      reason=reason,
      structure_id=structure_id,
    )

    truncate_schedule_operation.additional_properties = d
    return truncate_schedule_operation

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
