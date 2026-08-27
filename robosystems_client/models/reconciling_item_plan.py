from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reconciling_item_plan_default_disposition import (
  ReconcilingItemPlanDefaultDisposition,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.reconciling_item_delta_line import ReconcilingItemDeltaLine
  from ..models.reconciling_item_entry_summary import ReconcilingItemEntrySummary


T = TypeVar("T", bound="ReconcilingItemPlan")


@_attrs_define
class ReconcilingItemPlan:
  """What changed upstream, and what each disposition would do about it.

  Attributes:
      event_id (str):
      source (str):
      event_type (str):
      event_status (str):
      default_disposition (ReconcilingItemPlanDefaultDisposition): What resolve would do with no disposition given:
          restate while every affected period is open, catch_up once one is closed.
      external_id (None | str | Unset):
      drift_detected_at (datetime.datetime | None | Unset): When the sync first saw this difference
      default_posting_date (datetime.date | None | Unset): Where a catch-up entry would land by default
      affected_posting_dates (list[datetime.date] | Unset): Posting dates of the event's entries
      closed_periods (list[str] | Unset): Names of closed periods the event's entries sit in
      prior_entries (list[ReconcilingItemEntrySummary] | Unset):
      accepted_entries (list[ReconcilingItemEntrySummary] | Unset):
      delta (list[ReconcilingItemDeltaLine] | Unset): Per-account net change; empty when none
      no_gl_effect (bool | Unset): The change moves no money — a memo or reference edit. catch_up posts nothing;
          restate still regenerates so the entries carry the new text. Default: False.
      restate_blockers (list[str] | Unset): Why restate is unavailable, if it is: a closed period, an entry that was
          reversed or is not posted, or entries from elsewhere sharing this event's transaction.
      unmapped_element_external_ids (list[str] | Unset): Accounts in the new payload with no mapping in this graph.
          Both dispositions that write need them mapped first.
  """

  event_id: str
  source: str
  event_type: str
  event_status: str
  default_disposition: ReconcilingItemPlanDefaultDisposition
  external_id: None | str | Unset = UNSET
  drift_detected_at: datetime.datetime | None | Unset = UNSET
  default_posting_date: datetime.date | None | Unset = UNSET
  affected_posting_dates: list[datetime.date] | Unset = UNSET
  closed_periods: list[str] | Unset = UNSET
  prior_entries: list[ReconcilingItemEntrySummary] | Unset = UNSET
  accepted_entries: list[ReconcilingItemEntrySummary] | Unset = UNSET
  delta: list[ReconcilingItemDeltaLine] | Unset = UNSET
  no_gl_effect: bool | Unset = False
  restate_blockers: list[str] | Unset = UNSET
  unmapped_element_external_ids: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_id = self.event_id

    source = self.source

    event_type = self.event_type

    event_status = self.event_status

    default_disposition = self.default_disposition.value

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

    drift_detected_at: None | str | Unset
    if isinstance(self.drift_detected_at, Unset):
      drift_detected_at = UNSET
    elif isinstance(self.drift_detected_at, datetime.datetime):
      drift_detected_at = self.drift_detected_at.isoformat()
    else:
      drift_detected_at = self.drift_detected_at

    default_posting_date: None | str | Unset
    if isinstance(self.default_posting_date, Unset):
      default_posting_date = UNSET
    elif isinstance(self.default_posting_date, datetime.date):
      default_posting_date = self.default_posting_date.isoformat()
    else:
      default_posting_date = self.default_posting_date

    affected_posting_dates: list[str] | Unset = UNSET
    if not isinstance(self.affected_posting_dates, Unset):
      affected_posting_dates = []
      for affected_posting_dates_item_data in self.affected_posting_dates:
        affected_posting_dates_item = affected_posting_dates_item_data.isoformat()
        affected_posting_dates.append(affected_posting_dates_item)

    closed_periods: list[str] | Unset = UNSET
    if not isinstance(self.closed_periods, Unset):
      closed_periods = self.closed_periods

    prior_entries: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.prior_entries, Unset):
      prior_entries = []
      for prior_entries_item_data in self.prior_entries:
        prior_entries_item = prior_entries_item_data.to_dict()
        prior_entries.append(prior_entries_item)

    accepted_entries: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.accepted_entries, Unset):
      accepted_entries = []
      for accepted_entries_item_data in self.accepted_entries:
        accepted_entries_item = accepted_entries_item_data.to_dict()
        accepted_entries.append(accepted_entries_item)

    delta: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.delta, Unset):
      delta = []
      for delta_item_data in self.delta:
        delta_item = delta_item_data.to_dict()
        delta.append(delta_item)

    no_gl_effect = self.no_gl_effect

    restate_blockers: list[str] | Unset = UNSET
    if not isinstance(self.restate_blockers, Unset):
      restate_blockers = self.restate_blockers

    unmapped_element_external_ids: list[str] | Unset = UNSET
    if not isinstance(self.unmapped_element_external_ids, Unset):
      unmapped_element_external_ids = self.unmapped_element_external_ids

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
        "source": source,
        "event_type": event_type,
        "event_status": event_status,
        "default_disposition": default_disposition,
      }
    )
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if drift_detected_at is not UNSET:
      field_dict["drift_detected_at"] = drift_detected_at
    if default_posting_date is not UNSET:
      field_dict["default_posting_date"] = default_posting_date
    if affected_posting_dates is not UNSET:
      field_dict["affected_posting_dates"] = affected_posting_dates
    if closed_periods is not UNSET:
      field_dict["closed_periods"] = closed_periods
    if prior_entries is not UNSET:
      field_dict["prior_entries"] = prior_entries
    if accepted_entries is not UNSET:
      field_dict["accepted_entries"] = accepted_entries
    if delta is not UNSET:
      field_dict["delta"] = delta
    if no_gl_effect is not UNSET:
      field_dict["no_gl_effect"] = no_gl_effect
    if restate_blockers is not UNSET:
      field_dict["restate_blockers"] = restate_blockers
    if unmapped_element_external_ids is not UNSET:
      field_dict["unmapped_element_external_ids"] = unmapped_element_external_ids

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.reconciling_item_delta_line import ReconcilingItemDeltaLine
    from ..models.reconciling_item_entry_summary import ReconcilingItemEntrySummary

    d = dict(src_dict)
    event_id = d.pop("event_id")

    source = d.pop("source")

    event_type = d.pop("event_type")

    event_status = d.pop("event_status")

    default_disposition = ReconcilingItemPlanDefaultDisposition(
      d.pop("default_disposition")
    )

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

    def _parse_drift_detected_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        drift_detected_at_type_0 = datetime.datetime.fromisoformat(data)

        return drift_detected_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    drift_detected_at = _parse_drift_detected_at(d.pop("drift_detected_at", UNSET))

    def _parse_default_posting_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        default_posting_date_type_0 = datetime.date.fromisoformat(data)

        return default_posting_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    default_posting_date = _parse_default_posting_date(
      d.pop("default_posting_date", UNSET)
    )

    _affected_posting_dates = d.pop("affected_posting_dates", UNSET)
    affected_posting_dates: list[datetime.date] | Unset = UNSET
    if _affected_posting_dates is not UNSET:
      affected_posting_dates = []
      for affected_posting_dates_item_data in _affected_posting_dates:
        affected_posting_dates_item = datetime.date.fromisoformat(
          affected_posting_dates_item_data
        )

        affected_posting_dates.append(affected_posting_dates_item)

    closed_periods = cast(list[str], d.pop("closed_periods", UNSET))

    _prior_entries = d.pop("prior_entries", UNSET)
    prior_entries: list[ReconcilingItemEntrySummary] | Unset = UNSET
    if _prior_entries is not UNSET:
      prior_entries = []
      for prior_entries_item_data in _prior_entries:
        prior_entries_item = ReconcilingItemEntrySummary.from_dict(
          prior_entries_item_data
        )

        prior_entries.append(prior_entries_item)

    _accepted_entries = d.pop("accepted_entries", UNSET)
    accepted_entries: list[ReconcilingItemEntrySummary] | Unset = UNSET
    if _accepted_entries is not UNSET:
      accepted_entries = []
      for accepted_entries_item_data in _accepted_entries:
        accepted_entries_item = ReconcilingItemEntrySummary.from_dict(
          accepted_entries_item_data
        )

        accepted_entries.append(accepted_entries_item)

    _delta = d.pop("delta", UNSET)
    delta: list[ReconcilingItemDeltaLine] | Unset = UNSET
    if _delta is not UNSET:
      delta = []
      for delta_item_data in _delta:
        delta_item = ReconcilingItemDeltaLine.from_dict(delta_item_data)

        delta.append(delta_item)

    no_gl_effect = d.pop("no_gl_effect", UNSET)

    restate_blockers = cast(list[str], d.pop("restate_blockers", UNSET))

    unmapped_element_external_ids = cast(
      list[str], d.pop("unmapped_element_external_ids", UNSET)
    )

    reconciling_item_plan = cls(
      event_id=event_id,
      source=source,
      event_type=event_type,
      event_status=event_status,
      default_disposition=default_disposition,
      external_id=external_id,
      drift_detected_at=drift_detected_at,
      default_posting_date=default_posting_date,
      affected_posting_dates=affected_posting_dates,
      closed_periods=closed_periods,
      prior_entries=prior_entries,
      accepted_entries=accepted_entries,
      delta=delta,
      no_gl_effect=no_gl_effect,
      restate_blockers=restate_blockers,
      unmapped_element_external_ids=unmapped_element_external_ids,
    )

    reconciling_item_plan.additional_properties = d
    return reconciling_item_plan

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
