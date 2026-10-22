from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.entry_template_request import EntryTemplateRequest
  from ..models.schedule_metadata_request import ScheduleMetadataRequest


T = TypeVar("T", bound="ScheduleMechanics")


@_attrs_define
class ScheduleMechanics:
  """Closing-entry generator mechanics for `block_type='schedule'`.

  Reads the typed `structures.artifact_mechanics` JSONB column, falling back
  to `structures.metadata_` for Schedule rows that lack it.
  `entry_template` and `schedule_metadata` reuse the wire-level request
  shapes so OpenAPI emits one canonical type per concept.

      Attributes:
          entry_template (EntryTemplateRequest):
          kind (Literal['closing_entry_generator'] | Unset):  Default: 'closing_entry_generator'.
          schedule_metadata (None | ScheduleMetadataRequest | Unset): Method (straight_line / declining_balance /
              units_of_production), original_amount, residual_value, useful_life_months, optional asset_element_id for net-
              book-value cross-reference.
          periods_with_entries (int | Unset): Number of in-scope periods that have at least one closing entry posted.
              Runtime state derived at envelope-build time from the Entry table. Default: 0.
          period_start (datetime.date | None | Unset): The schedule's first period start, as defined.
          period_end (datetime.date | None | Unset): The schedule's last period end, as defined. An early end is
              `end_date`; rebuild-schedule regenerates to this and ends at it again.
          monthly_amount (int | None | Unset): The straight-line monthly amount in cents. With `period_start`,
              `period_end`, `entry_template` and `schedule_metadata` this is the whole definition: rebuild-schedule takes the
              same fields back.
          end_date (datetime.date | None | Unset): Where terminate-schedule ended it, when it did.
          posted_periods (list[str] | Unset): The months (YYYY-MM) holding a posted or shadowed closing entry of the
              schedule, which no edit may rewrite.
          edit_warning (None | str | Unset): Set once an entry has posted: what deleting, rebuilding or recreating the
              schedule would do to that history, and the path an edit takes instead.
  """

  entry_template: EntryTemplateRequest
  kind: Literal["closing_entry_generator"] | Unset = "closing_entry_generator"
  schedule_metadata: None | ScheduleMetadataRequest | Unset = UNSET
  periods_with_entries: int | Unset = 0
  period_start: datetime.date | None | Unset = UNSET
  period_end: datetime.date | None | Unset = UNSET
  monthly_amount: int | None | Unset = UNSET
  end_date: datetime.date | None | Unset = UNSET
  posted_periods: list[str] | Unset = UNSET
  edit_warning: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    entry_template = self.entry_template.to_dict()

    kind = self.kind

    schedule_metadata: dict[str, Any] | None | Unset
    if isinstance(self.schedule_metadata, Unset):
      schedule_metadata = UNSET
    elif isinstance(self.schedule_metadata, ScheduleMetadataRequest):
      schedule_metadata = self.schedule_metadata.to_dict()
    else:
      schedule_metadata = self.schedule_metadata

    periods_with_entries = self.periods_with_entries

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

    end_date: None | str | Unset
    if isinstance(self.end_date, Unset):
      end_date = UNSET
    elif isinstance(self.end_date, datetime.date):
      end_date = self.end_date.isoformat()
    else:
      end_date = self.end_date

    posted_periods: list[str] | Unset = UNSET
    if not isinstance(self.posted_periods, Unset):
      posted_periods = self.posted_periods

    edit_warning: None | str | Unset
    if isinstance(self.edit_warning, Unset):
      edit_warning = UNSET
    else:
      edit_warning = self.edit_warning

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entry_template": entry_template,
      }
    )
    if kind is not UNSET:
      field_dict["kind"] = kind
    if schedule_metadata is not UNSET:
      field_dict["schedule_metadata"] = schedule_metadata
    if periods_with_entries is not UNSET:
      field_dict["periods_with_entries"] = periods_with_entries
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if monthly_amount is not UNSET:
      field_dict["monthly_amount"] = monthly_amount
    if end_date is not UNSET:
      field_dict["end_date"] = end_date
    if posted_periods is not UNSET:
      field_dict["posted_periods"] = posted_periods
    if edit_warning is not UNSET:
      field_dict["edit_warning"] = edit_warning

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.entry_template_request import EntryTemplateRequest
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    d = dict(src_dict)
    entry_template = EntryTemplateRequest.from_dict(d.pop("entry_template"))

    kind = cast(Literal["closing_entry_generator"] | Unset, d.pop("kind", UNSET))
    if kind != "closing_entry_generator" and not isinstance(kind, Unset):
      raise ValueError(f"kind must match const 'closing_entry_generator', got '{kind}'")

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

    periods_with_entries = d.pop("periods_with_entries", UNSET)

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

    def _parse_end_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        end_date_type_0 = datetime.date.fromisoformat(data)

        return end_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    end_date = _parse_end_date(d.pop("end_date", UNSET))

    posted_periods = cast(list[str], d.pop("posted_periods", UNSET))

    def _parse_edit_warning(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    edit_warning = _parse_edit_warning(d.pop("edit_warning", UNSET))

    schedule_mechanics = cls(
      entry_template=entry_template,
      kind=kind,
      schedule_metadata=schedule_metadata,
      periods_with_entries=periods_with_entries,
      period_start=period_start,
      period_end=period_end,
      monthly_amount=monthly_amount,
      end_date=end_date,
      posted_periods=posted_periods,
      edit_warning=edit_warning,
    )

    schedule_mechanics.additional_properties = d
    return schedule_mechanics

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
