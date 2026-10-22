from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.entry_template_request import EntryTemplateRequest
  from ..models.schedule_metadata_request import ScheduleMetadataRequest


T = TypeVar("T", bound="RebuildScheduleRequest")


@_attrs_define
class RebuildScheduleRequest:
  """Re-run the schedule generator in place on an existing schedule.

  Atomic alternative to delete-then-recreate: the structure id and its
  element associations are preserved, the old pending obligation chain
  is voided, the old facts + rules are deleted, and a fresh set of
  forward facts + a fresh obligation chain are regenerated from the
  schedule's stored definition (entry_template / schedule_metadata /
  monthly_amount / period bounds on the Structure's metadata).

  The historical-vs-in-scope split is re-derived from the CURRENT fiscal
  calendar (months through its `closed_through`, or before its first
  month, are history), so a rebuild re-scopes the schedule to today's
  close state. Use this to pick up a fixed generator (e.g. the
  roll-forward direction fix) without orphaning obligations.

  It is also how an edit is saved while nothing has posted: the fields below
  replace the stored definition before it regenerates, as the schedule's
  envelope reads them back (`artifact.mechanics`). Omitted fields keep their
  stored values, inside `schedule_metadata` too.

      Attributes:
          structure_id (str): The schedule structure to regenerate in place.
          period_start (datetime.date | None | Unset): A new first period start.
          period_end (datetime.date | None | Unset): A new last period end.
          monthly_amount (int | None | Unset): A new straight-line monthly amount, in cents.
          entry_template (EntryTemplateRequest | None | Unset): A new entry template, replacing the stored one whole.
          schedule_metadata (None | ScheduleMetadataRequest | Unset): The schedule_metadata fields to change.
  """

  structure_id: str
  period_start: datetime.date | None | Unset = UNSET
  period_end: datetime.date | None | Unset = UNSET
  monthly_amount: int | None | Unset = UNSET
  entry_template: EntryTemplateRequest | None | Unset = UNSET
  schedule_metadata: None | ScheduleMetadataRequest | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.entry_template_request import EntryTemplateRequest
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    structure_id = self.structure_id

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    elif isinstance(self.period_start, datetime.date):
      period_start = self.period_start.isoformat()
    else:
      period_start = self.period_start

    period_end: None | str | Unset
    if isinstance(self.period_end, Unset):
      period_end = UNSET
    elif isinstance(self.period_end, datetime.date):
      period_end = self.period_end.isoformat()
    else:
      period_end = self.period_end

    monthly_amount: int | None | Unset
    if isinstance(self.monthly_amount, Unset):
      monthly_amount = UNSET
    else:
      monthly_amount = self.monthly_amount

    entry_template: dict[str, Any] | None | Unset
    if isinstance(self.entry_template, Unset):
      entry_template = UNSET
    elif isinstance(self.entry_template, EntryTemplateRequest):
      entry_template = self.entry_template.to_dict()
    else:
      entry_template = self.entry_template

    schedule_metadata: dict[str, Any] | None | Unset
    if isinstance(self.schedule_metadata, Unset):
      schedule_metadata = UNSET
    elif isinstance(self.schedule_metadata, ScheduleMetadataRequest):
      schedule_metadata = self.schedule_metadata.to_dict()
    else:
      schedule_metadata = self.schedule_metadata

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if monthly_amount is not UNSET:
      field_dict["monthly_amount"] = monthly_amount
    if entry_template is not UNSET:
      field_dict["entry_template"] = entry_template
    if schedule_metadata is not UNSET:
      field_dict["schedule_metadata"] = schedule_metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.entry_template_request import EntryTemplateRequest
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    def _parse_period_start(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_start_type_0 = datetime.date.fromisoformat(data)

        return period_start_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_start = _parse_period_start(d.pop("period_start", UNSET))

    def _parse_period_end(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_end_type_0 = datetime.date.fromisoformat(data)

        return period_end_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_end = _parse_period_end(d.pop("period_end", UNSET))

    def _parse_monthly_amount(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    monthly_amount = _parse_monthly_amount(d.pop("monthly_amount", UNSET))

    def _parse_entry_template(data: object) -> EntryTemplateRequest | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        entry_template_type_0 = EntryTemplateRequest.from_dict(data)

        return entry_template_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(EntryTemplateRequest | None | Unset, data)

    entry_template = _parse_entry_template(d.pop("entry_template", UNSET))

    def _parse_schedule_metadata(
      data: object,
    ) -> None | ScheduleMetadataRequest | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        schedule_metadata_type_0 = ScheduleMetadataRequest.from_dict(data)

        return schedule_metadata_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ScheduleMetadataRequest | Unset, data)

    schedule_metadata = _parse_schedule_metadata(d.pop("schedule_metadata", UNSET))

    rebuild_schedule_request = cls(
      structure_id=structure_id,
      period_start=period_start,
      period_end=period_end,
      monthly_amount=monthly_amount,
      entry_template=entry_template,
      schedule_metadata=schedule_metadata,
    )

    rebuild_schedule_request.additional_properties = d
    return rebuild_schedule_request

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
