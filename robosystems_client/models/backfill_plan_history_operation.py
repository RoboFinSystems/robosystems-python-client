from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackfillPlanHistoryOperation")


@_attrs_define
class BackfillPlanHistoryOperation:
  """Compile monthly statement history behind the close boundary.

  Attributes:
      start_period (None | str | Unset): YYYY-MM period to backfill from. Clamped to the earliest month with ledger
          data; defaults to that month when omitted. Must be on or before `closed_through`.
      max_periods (int | Unset): Maximum months to restamp in this call. Each month runs a full reopen → reclose
          cycle; keep chunks modest and loop on `remaining_periods`. Default: 12.
      allow_stale_sync (bool | Unset): Override the sync-currency gate on each reclose. Historical months predate the
          last sync in the normal case, so this is rarely needed. Default: False.
      allow_stranded_obligations (bool | Unset): Override the stranded-obligation gate on each reclose. Only needed
          when a matured classified obligation without a drafted entry exists inside the backfill window and you have
          decided not to draft or void it first. Default: False.
      allow_reconciling_items (bool | Unset): Override the reconciling-item gate on each reclose. Only needed when an
          event inside the backfill window is still flagged as changed upstream and you have decided not to resolve it
          first. Default: False.
      restamp (bool | Unset): Also re-derive months that ALREADY have canonical statement sets (default: skip them).
          Use after an engine improvement changes what a stamp produces — each month reruns the full reopen → reclose
          cycle and replaces its sets. A restamp run is not self-resuming (every month in range stays a candidate);
          advance `start_period` between chunks. Default: False.
      note (None | str | Unset): Free-form note attached to each close audit event
  """

  start_period: None | str | Unset = UNSET
  max_periods: int | Unset = 12
  allow_stale_sync: bool | Unset = False
  allow_stranded_obligations: bool | Unset = False
  allow_reconciling_items: bool | Unset = False
  restamp: bool | Unset = False
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    start_period: None | str | Unset
    if isinstance(self.start_period, Unset):
      start_period = UNSET
    else:
      start_period = self.start_period

    max_periods = self.max_periods

    allow_stale_sync = self.allow_stale_sync

    allow_stranded_obligations = self.allow_stranded_obligations

    allow_reconciling_items = self.allow_reconciling_items

    restamp = self.restamp

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if start_period is not UNSET:
      field_dict["start_period"] = start_period
    if max_periods is not UNSET:
      field_dict["max_periods"] = max_periods
    if allow_stale_sync is not UNSET:
      field_dict["allow_stale_sync"] = allow_stale_sync
    if allow_stranded_obligations is not UNSET:
      field_dict["allow_stranded_obligations"] = allow_stranded_obligations
    if allow_reconciling_items is not UNSET:
      field_dict["allow_reconciling_items"] = allow_reconciling_items
    if restamp is not UNSET:
      field_dict["restamp"] = restamp
    if note is not UNSET:
      field_dict["note"] = note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_start_period(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    start_period = _parse_start_period(d.pop("start_period", UNSET))

    max_periods = d.pop("max_periods", UNSET)

    allow_stale_sync = d.pop("allow_stale_sync", UNSET)

    allow_stranded_obligations = d.pop("allow_stranded_obligations", UNSET)

    allow_reconciling_items = d.pop("allow_reconciling_items", UNSET)

    restamp = d.pop("restamp", UNSET)

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    backfill_plan_history_operation = cls(
      start_period=start_period,
      max_periods=max_periods,
      allow_stale_sync=allow_stale_sync,
      allow_stranded_obligations=allow_stranded_obligations,
      allow_reconciling_items=allow_reconciling_items,
      restamp=restamp,
      note=note,
    )

    backfill_plan_history_operation.additional_properties = d
    return backfill_plan_history_operation

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
