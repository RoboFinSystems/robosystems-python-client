from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.fiscal_period_summary import FiscalPeriodSummary
  from ..models.pending_obligation_detail_response import (
    PendingObligationDetailResponse,
  )


T = TypeVar("T", bound="FiscalCalendarResponse")


@_attrs_define
class FiscalCalendarResponse:
  """Current fiscal calendar state for a graph.

  Attributes:
      graph_id (str):
      fiscal_year_start_month (int):
      closed_through (None | str | Unset): Latest closed period (YYYY-MM), or null if nothing closed
      close_target (None | str | Unset): Target period the user wants closed through (YYYY-MM)
      gap_periods (int | Unset): Number of periods between closed_through and close_target (inclusive of
          close_target). 0 means caught up. Default: 0.
      catch_up_sequence (list[str] | Unset): Ordered list of periods that a close run would process
      closeable_now (bool | Unset): Whether the next period in the catch-up sequence passes all closeable gates
          Default: False.
      blockers (list[str] | Unset): Structured blocker codes when closeable_now is False: 'sequence_violation',
          'period_incomplete', 'sync_stale', 'calendar_not_initialized', 'period_already_closed', 'pending_obligations'
      pending_obligation_count (int | Unset): Number of pending schedule_entry_due events blocking close. Non-zero
          only when `pending_obligations` is in `blockers`. Default: 0.
      pending_obligation_sample (list[PendingObligationDetailResponse] | Unset): Sample of up to 5 pending obligations
          (schedule_id, schedule_name, period, event_id) ordered by occurred_at. Use `list-event-blocks` with
          event_type=schedule_entry_due&status=pending for the full set.
      earliest_pending_period (None | str | Unset): Earliest period (YYYY-MM) with a pending obligation blocking
          close. Null when no pending_obligations blocker is active.
      sync_stale_days (int | None | Unset): Days the most recent sync is stale relative to the period to close.
          Populated only when `sync_stale` is in `blockers` and last_sync_at exists (null when there's a connection but no
          sync has ever run).
      last_close_at (datetime.datetime | None | Unset):
      initialized_at (datetime.datetime | None | Unset):
      last_sync_at (datetime.datetime | None | Unset): Most recent QB sync timestamp (if connected)
      periods (list[FiscalPeriodSummary] | Unset): Fiscal period rows for this graph
  """

  graph_id: str
  fiscal_year_start_month: int
  closed_through: None | str | Unset = UNSET
  close_target: None | str | Unset = UNSET
  gap_periods: int | Unset = 0
  catch_up_sequence: list[str] | Unset = UNSET
  closeable_now: bool | Unset = False
  blockers: list[str] | Unset = UNSET
  pending_obligation_count: int | Unset = 0
  pending_obligation_sample: list[PendingObligationDetailResponse] | Unset = UNSET
  earliest_pending_period: None | str | Unset = UNSET
  sync_stale_days: int | None | Unset = UNSET
  last_close_at: datetime.datetime | None | Unset = UNSET
  initialized_at: datetime.datetime | None | Unset = UNSET
  last_sync_at: datetime.datetime | None | Unset = UNSET
  periods: list[FiscalPeriodSummary] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    fiscal_year_start_month = self.fiscal_year_start_month

    closed_through: None | str | Unset
    if isinstance(self.closed_through, Unset):
      closed_through = UNSET
    else:
      closed_through = self.closed_through

    close_target: None | str | Unset
    if isinstance(self.close_target, Unset):
      close_target = UNSET
    else:
      close_target = self.close_target

    gap_periods = self.gap_periods

    catch_up_sequence: list[str] | Unset = UNSET
    if not isinstance(self.catch_up_sequence, Unset):
      catch_up_sequence = self.catch_up_sequence

    closeable_now = self.closeable_now

    blockers: list[str] | Unset = UNSET
    if not isinstance(self.blockers, Unset):
      blockers = self.blockers

    pending_obligation_count = self.pending_obligation_count

    pending_obligation_sample: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.pending_obligation_sample, Unset):
      pending_obligation_sample = []
      for pending_obligation_sample_item_data in self.pending_obligation_sample:
        pending_obligation_sample_item = pending_obligation_sample_item_data.to_dict()
        pending_obligation_sample.append(pending_obligation_sample_item)

    earliest_pending_period: None | str | Unset
    if isinstance(self.earliest_pending_period, Unset):
      earliest_pending_period = UNSET
    else:
      earliest_pending_period = self.earliest_pending_period

    sync_stale_days: int | None | Unset
    if isinstance(self.sync_stale_days, Unset):
      sync_stale_days = UNSET
    else:
      sync_stale_days = self.sync_stale_days

    last_close_at: None | str | Unset
    if isinstance(self.last_close_at, Unset):
      last_close_at = UNSET
    elif isinstance(self.last_close_at, datetime.datetime):
      last_close_at = self.last_close_at.isoformat()
    else:
      last_close_at = self.last_close_at

    initialized_at: None | str | Unset
    if isinstance(self.initialized_at, Unset):
      initialized_at = UNSET
    elif isinstance(self.initialized_at, datetime.datetime):
      initialized_at = self.initialized_at.isoformat()
    else:
      initialized_at = self.initialized_at

    last_sync_at: None | str | Unset
    if isinstance(self.last_sync_at, Unset):
      last_sync_at = UNSET
    elif isinstance(self.last_sync_at, datetime.datetime):
      last_sync_at = self.last_sync_at.isoformat()
    else:
      last_sync_at = self.last_sync_at

    periods: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.periods, Unset):
      periods = []
      for periods_item_data in self.periods:
        periods_item = periods_item_data.to_dict()
        periods.append(periods_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "fiscal_year_start_month": fiscal_year_start_month,
      }
    )
    if closed_through is not UNSET:
      field_dict["closed_through"] = closed_through
    if close_target is not UNSET:
      field_dict["close_target"] = close_target
    if gap_periods is not UNSET:
      field_dict["gap_periods"] = gap_periods
    if catch_up_sequence is not UNSET:
      field_dict["catch_up_sequence"] = catch_up_sequence
    if closeable_now is not UNSET:
      field_dict["closeable_now"] = closeable_now
    if blockers is not UNSET:
      field_dict["blockers"] = blockers
    if pending_obligation_count is not UNSET:
      field_dict["pending_obligation_count"] = pending_obligation_count
    if pending_obligation_sample is not UNSET:
      field_dict["pending_obligation_sample"] = pending_obligation_sample
    if earliest_pending_period is not UNSET:
      field_dict["earliest_pending_period"] = earliest_pending_period
    if sync_stale_days is not UNSET:
      field_dict["sync_stale_days"] = sync_stale_days
    if last_close_at is not UNSET:
      field_dict["last_close_at"] = last_close_at
    if initialized_at is not UNSET:
      field_dict["initialized_at"] = initialized_at
    if last_sync_at is not UNSET:
      field_dict["last_sync_at"] = last_sync_at
    if periods is not UNSET:
      field_dict["periods"] = periods

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.fiscal_period_summary import FiscalPeriodSummary
    from ..models.pending_obligation_detail_response import (
      PendingObligationDetailResponse,
    )

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    fiscal_year_start_month = d.pop("fiscal_year_start_month")

    def _parse_closed_through(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    closed_through = _parse_closed_through(d.pop("closed_through", UNSET))

    def _parse_close_target(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    close_target = _parse_close_target(d.pop("close_target", UNSET))

    gap_periods = d.pop("gap_periods", UNSET)

    catch_up_sequence = cast(list[str], d.pop("catch_up_sequence", UNSET))

    closeable_now = d.pop("closeable_now", UNSET)

    blockers = cast(list[str], d.pop("blockers", UNSET))

    pending_obligation_count = d.pop("pending_obligation_count", UNSET)

    _pending_obligation_sample = d.pop("pending_obligation_sample", UNSET)
    pending_obligation_sample: list[PendingObligationDetailResponse] | Unset = UNSET
    if _pending_obligation_sample is not UNSET:
      pending_obligation_sample = []
      for pending_obligation_sample_item_data in _pending_obligation_sample:
        pending_obligation_sample_item = PendingObligationDetailResponse.from_dict(
          pending_obligation_sample_item_data
        )

        pending_obligation_sample.append(pending_obligation_sample_item)

    def _parse_earliest_pending_period(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    earliest_pending_period = _parse_earliest_pending_period(
      d.pop("earliest_pending_period", UNSET)
    )

    def _parse_sync_stale_days(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    sync_stale_days = _parse_sync_stale_days(d.pop("sync_stale_days", UNSET))

    def _parse_last_close_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        last_close_at_type_0 = isoparse(data)

        return last_close_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    last_close_at = _parse_last_close_at(d.pop("last_close_at", UNSET))

    def _parse_initialized_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        initialized_at_type_0 = isoparse(data)

        return initialized_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    initialized_at = _parse_initialized_at(d.pop("initialized_at", UNSET))

    def _parse_last_sync_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        last_sync_at_type_0 = isoparse(data)

        return last_sync_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    last_sync_at = _parse_last_sync_at(d.pop("last_sync_at", UNSET))

    _periods = d.pop("periods", UNSET)
    periods: list[FiscalPeriodSummary] | Unset = UNSET
    if _periods is not UNSET:
      periods = []
      for periods_item_data in _periods:
        periods_item = FiscalPeriodSummary.from_dict(periods_item_data)

        periods.append(periods_item)

    fiscal_calendar_response = cls(
      graph_id=graph_id,
      fiscal_year_start_month=fiscal_year_start_month,
      closed_through=closed_through,
      close_target=close_target,
      gap_periods=gap_periods,
      catch_up_sequence=catch_up_sequence,
      closeable_now=closeable_now,
      blockers=blockers,
      pending_obligation_count=pending_obligation_count,
      pending_obligation_sample=pending_obligation_sample,
      earliest_pending_period=earliest_pending_period,
      sync_stale_days=sync_stale_days,
      last_close_at=last_close_at,
      initialized_at=initialized_at,
      last_sync_at=last_sync_at,
      periods=periods,
    )

    fiscal_calendar_response.additional_properties = d
    return fiscal_calendar_response

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
