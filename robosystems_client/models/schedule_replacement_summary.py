from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_replacement_summary_path import ScheduleReplacementSummaryPath
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleReplacementSummary")


@_attrs_define
class ScheduleReplacementSummary:
  """What an existing schedule's entries mean for replacing it.

  Attributes:
      structure_id (str):
      name (str):
      posted_entry_count (int): Its posted or shadowed closing entries.
      path (ScheduleReplacementSummaryPath): `rebuild` when nothing has posted: rebuild-schedule with the new
          definition replaces it in place. `terminate_and_succeed` once an entry has: terminate it after its last posted
          month and create the successor from the month after.
      posted_periods (list[str] | Unset): The months those entries are in (YYYY-MM).
      draft_entry_count (int | Unset):  Default: 0.
  """

  structure_id: str
  name: str
  posted_entry_count: int
  path: ScheduleReplacementSummaryPath
  posted_periods: list[str] | Unset = UNSET
  draft_entry_count: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    name = self.name

    posted_entry_count = self.posted_entry_count

    path = self.path.value

    posted_periods: list[str] | Unset = UNSET
    if not isinstance(self.posted_periods, Unset):
      posted_periods = self.posted_periods

    draft_entry_count = self.draft_entry_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "name": name,
        "posted_entry_count": posted_entry_count,
        "path": path,
      }
    )
    if posted_periods is not UNSET:
      field_dict["posted_periods"] = posted_periods
    if draft_entry_count is not UNSET:
      field_dict["draft_entry_count"] = draft_entry_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    name = d.pop("name")

    posted_entry_count = d.pop("posted_entry_count")

    path = ScheduleReplacementSummaryPath(d.pop("path"))

    posted_periods = cast(list[str], d.pop("posted_periods", UNSET))

    draft_entry_count = d.pop("draft_entry_count", UNSET)

    schedule_replacement_summary = cls(
      structure_id=structure_id,
      name=name,
      posted_entry_count=posted_entry_count,
      path=path,
      posted_periods=posted_periods,
      draft_entry_count=draft_entry_count,
    )

    schedule_replacement_summary.additional_properties = d
    return schedule_replacement_summary

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
