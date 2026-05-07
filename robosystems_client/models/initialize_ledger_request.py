from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InitializeLedgerRequest")


@_attrs_define
class InitializeLedgerRequest:
  """One-time setup for a graph's fiscal calendar.

  Creates the `FiscalCalendar` row, seeds `FiscalPeriod` rows from
  ``earliest_data_period`` (or 24 months ago) through the current month,
  and stamps periods on or before ``closed_through`` as already closed.
  Subsequent calls return 409 — there's no re-initialize.

  The two pointers it sets up:

  - ``closed_through`` (system-maintained): the latest period whose
    books are locked. Set on init for businesses with prior close
    history; null for a fresh start.
  - ``close_target`` (user-controlled): the goal date the user is
    closing toward. Set independently via `set-close-target`.

      Attributes:
          closed_through (None | str | Unset): YYYY-MM period. Periods ≤ this date are treated as historical (already
              closed before the user joined). Set to null for a fresh business with no prior close state.
          fiscal_year_start_month (int | Unset): Fiscal year start month (1-12). Defaults to calendar year. Default: 1.
          auto_seed_schedules (bool | Unset): If true, run the SchedulerAgent to create schedules from historical BS
              activity. NOT YET IMPLEMENTED — returns a warning in v1. Default: False.
          earliest_data_period (None | str | Unset): YYYY-MM period representing the earliest month that has transaction
              data. Used to create FiscalPeriod rows. Defaults to 24 months before the current month.
          note (None | str | Unset): Free-form note attached to the audit event
  """

  closed_through: None | str | Unset = UNSET
  fiscal_year_start_month: int | Unset = 1
  auto_seed_schedules: bool | Unset = False
  earliest_data_period: None | str | Unset = UNSET
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    closed_through: None | str | Unset
    if isinstance(self.closed_through, Unset):
      closed_through = UNSET
    else:
      closed_through = self.closed_through

    fiscal_year_start_month = self.fiscal_year_start_month

    auto_seed_schedules = self.auto_seed_schedules

    earliest_data_period: None | str | Unset
    if isinstance(self.earliest_data_period, Unset):
      earliest_data_period = UNSET
    else:
      earliest_data_period = self.earliest_data_period

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if closed_through is not UNSET:
      field_dict["closed_through"] = closed_through
    if fiscal_year_start_month is not UNSET:
      field_dict["fiscal_year_start_month"] = fiscal_year_start_month
    if auto_seed_schedules is not UNSET:
      field_dict["auto_seed_schedules"] = auto_seed_schedules
    if earliest_data_period is not UNSET:
      field_dict["earliest_data_period"] = earliest_data_period
    if note is not UNSET:
      field_dict["note"] = note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_closed_through(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    closed_through = _parse_closed_through(d.pop("closed_through", UNSET))

    fiscal_year_start_month = d.pop("fiscal_year_start_month", UNSET)

    auto_seed_schedules = d.pop("auto_seed_schedules", UNSET)

    def _parse_earliest_data_period(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    earliest_data_period = _parse_earliest_data_period(
      d.pop("earliest_data_period", UNSET)
    )

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    initialize_ledger_request = cls(
      closed_through=closed_through,
      fiscal_year_start_month=fiscal_year_start_month,
      auto_seed_schedules=auto_seed_schedules,
      earliest_data_period=earliest_data_period,
      note=note,
    )

    initialize_ledger_request.additional_properties = d
    return initialize_ledger_request

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
