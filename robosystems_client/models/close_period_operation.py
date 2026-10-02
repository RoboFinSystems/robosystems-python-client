from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClosePeriodOperation")


@_attrs_define
class ClosePeriodOperation:
  """Close a single fiscal period. Carries the YYYY-MM `period` in the
  request body alongside the close-time options inherited from
  :class:`ClosePeriodRequest`.

      Attributes:
          period (str): Period to close, in YYYY-MM. Must be exactly `closed_through + 1` — close runs sequentially.
          note (None | str | Unset): Free-form note attached to the close event
          allow_stale_sync (bool | Unset): Override the sync-currency gate. Only use when you have manually verified that
              the source data for the period is complete. Default: False.
          allow_stranded_obligations (bool | Unset): Override the stranded-obligation gate — close even though matured
              classified obligations have no drafted closing entry, knowingly omitting those adjusting entries from the
              period. Prefer running promote-obligations with dispatch_handlers=true (which drafts them) or voiding the
              obligations instead. The override is recorded in the close audit note. Default: False.
          allow_reconciling_items (bool | Unset): Override the reconciling-item gate — close even though posted events in
              the period are still flagged as changed in the source system, leaving those differences undecided. The next sync
              will still report them, and the statements stamped by this close may disagree with the source. Prefer resolve-
              reconciling-item on each first. The override is recorded in the close audit note. Default: False.
          allow_unposted_source_events (bool | Unset): Override the unposted-source-event gate — close even though source
              events dated in the period (bank-feed lines, QuickBooks transactions whose automatic posting failed) were never
              committed. Once the period closes they cannot post into it, so the stamped statements leave them out. Prefer
              classifying and committing, or voiding, each first. The override is recorded in the close audit note. Default:
              False.
          allow_unreconciled_accounts (bool | Unset): Override the reconciliation gate — close even though a
              reconciliation the close waits on is not reconciled for the period, or was never compared for it. The books are
              then closed without that check. Prefer refresh-reconciliations and clearing what it reports first. The override
              is recorded in the close audit note. Default: False.
  """

  period: str
  note: None | str | Unset = UNSET
  allow_stale_sync: bool | Unset = False
  allow_stranded_obligations: bool | Unset = False
  allow_reconciling_items: bool | Unset = False
  allow_unposted_source_events: bool | Unset = False
  allow_unreconciled_accounts: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    allow_stale_sync = self.allow_stale_sync

    allow_stranded_obligations = self.allow_stranded_obligations

    allow_reconciling_items = self.allow_reconciling_items

    allow_unposted_source_events = self.allow_unposted_source_events

    allow_unreconciled_accounts = self.allow_unreconciled_accounts

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
      }
    )
    if note is not UNSET:
      field_dict["note"] = note
    if allow_stale_sync is not UNSET:
      field_dict["allow_stale_sync"] = allow_stale_sync
    if allow_stranded_obligations is not UNSET:
      field_dict["allow_stranded_obligations"] = allow_stranded_obligations
    if allow_reconciling_items is not UNSET:
      field_dict["allow_reconciling_items"] = allow_reconciling_items
    if allow_unposted_source_events is not UNSET:
      field_dict["allow_unposted_source_events"] = allow_unposted_source_events
    if allow_unreconciled_accounts is not UNSET:
      field_dict["allow_unreconciled_accounts"] = allow_unreconciled_accounts

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    period = d.pop("period")

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    allow_stale_sync = d.pop("allow_stale_sync", UNSET)

    allow_stranded_obligations = d.pop("allow_stranded_obligations", UNSET)

    allow_reconciling_items = d.pop("allow_reconciling_items", UNSET)

    allow_unposted_source_events = d.pop("allow_unposted_source_events", UNSET)

    allow_unreconciled_accounts = d.pop("allow_unreconciled_accounts", UNSET)

    close_period_operation = cls(
      period=period,
      note=note,
      allow_stale_sync=allow_stale_sync,
      allow_stranded_obligations=allow_stranded_obligations,
      allow_reconciling_items=allow_reconciling_items,
      allow_unposted_source_events=allow_unposted_source_events,
      allow_unreconciled_accounts=allow_unreconciled_accounts,
    )

    close_period_operation.additional_properties = d
    return close_period_operation

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
