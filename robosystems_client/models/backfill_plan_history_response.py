from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.backfill_period_outcome import BackfillPeriodOutcome
  from ..models.fiscal_calendar_response import FiscalCalendarResponse


T = TypeVar("T", bound="BackfillPlanHistoryResponse")


@_attrs_define
class BackfillPlanHistoryResponse:
  """Response from one chunked plan-history backfill call.

  Attributes:
      fiscal_calendar (FiscalCalendarResponse): Current fiscal calendar state for a graph.
      earliest_available_period (str): First month with ledger data — the hard floor for backfill
      effective_start_period (str): The start actually used after clamping to earliest_available_period
      closed_through (str): The close boundary the backfill runs up to (inclusive)
      period_rows_created (int | Unset): FiscalPeriod rows seeded (baseline-closed) for months the calendar didn't
          cover yet Default: 0.
      processed (list[BackfillPeriodOutcome] | Unset): Months this call attempted, oldest first
      remaining_periods (list[str] | Unset): Months still lacking canonical statement sets that this call did not
          attempt (beyond max_periods, or after a failure halt). Loop until empty.
  """

  fiscal_calendar: FiscalCalendarResponse
  earliest_available_period: str
  effective_start_period: str
  closed_through: str
  period_rows_created: int | Unset = 0
  processed: list[BackfillPeriodOutcome] | Unset = UNSET
  remaining_periods: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    fiscal_calendar = self.fiscal_calendar.to_dict()

    earliest_available_period = self.earliest_available_period

    effective_start_period = self.effective_start_period

    closed_through = self.closed_through

    period_rows_created = self.period_rows_created

    processed: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.processed, Unset):
      processed = []
      for processed_item_data in self.processed:
        processed_item = processed_item_data.to_dict()
        processed.append(processed_item)

    remaining_periods: list[str] | Unset = UNSET
    if not isinstance(self.remaining_periods, Unset):
      remaining_periods = self.remaining_periods

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "fiscal_calendar": fiscal_calendar,
        "earliest_available_period": earliest_available_period,
        "effective_start_period": effective_start_period,
        "closed_through": closed_through,
      }
    )
    if period_rows_created is not UNSET:
      field_dict["period_rows_created"] = period_rows_created
    if processed is not UNSET:
      field_dict["processed"] = processed
    if remaining_periods is not UNSET:
      field_dict["remaining_periods"] = remaining_periods

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.backfill_period_outcome import BackfillPeriodOutcome
    from ..models.fiscal_calendar_response import FiscalCalendarResponse

    d = dict(src_dict)
    fiscal_calendar = FiscalCalendarResponse.from_dict(d.pop("fiscal_calendar"))

    earliest_available_period = d.pop("earliest_available_period")

    effective_start_period = d.pop("effective_start_period")

    closed_through = d.pop("closed_through")

    period_rows_created = d.pop("period_rows_created", UNSET)

    _processed = d.pop("processed", UNSET)
    processed: list[BackfillPeriodOutcome] | Unset = UNSET
    if _processed is not UNSET:
      processed = []
      for processed_item_data in _processed:
        processed_item = BackfillPeriodOutcome.from_dict(processed_item_data)

        processed.append(processed_item)

    remaining_periods = cast(list[str], d.pop("remaining_periods", UNSET))

    backfill_plan_history_response = cls(
      fiscal_calendar=fiscal_calendar,
      earliest_available_period=earliest_available_period,
      effective_start_period=effective_start_period,
      closed_through=closed_through,
      period_rows_created=period_rows_created,
      processed=processed,
      remaining_periods=remaining_periods,
    )

    backfill_plan_history_response.additional_properties = d
    return backfill_plan_history_response

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
