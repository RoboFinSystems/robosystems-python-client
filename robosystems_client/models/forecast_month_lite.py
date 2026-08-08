from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForecastMonthLite")


@_attrs_define
class ForecastMonthLite:
  """One computed forward month in a ``compute-forecast`` response.

  Attributes:
      period (str): Month key (``YYYY-MM``).
      period_start (datetime.date):
      period_end (datetime.date):
      income_statement_fact_set_id (None | str | Unset): Scenario IS FactSet upserted for the month.
      balance_sheet_fact_set_id (None | str | Unset): Scenario BS FactSet upserted for the month — the full roll:
          carry-forward, rule-driven working capital, schedule movements, RE roll, balancing cash (A = L + E by
          construction).
      cash_flow_fact_set_id (None | str | Unset): Scenario CF FactSet upserted for the month — indirect-method,
          derived from BS deltas + NI, reconciled to the balancing ΔCash.
      computed_count (int | Unset): Number of facts emitted for the month across all sets. Default: 0.
      verification_passed (bool | None | Unset): Whether every rule evaluated against the month's scenario sets
          passed. Three states, and the third is not the first: ``true`` = rules ran and all passed; ``false`` = at least
          one failed or errored, which halts the walk (see ``halted_at``); ``null`` = **no rules ran**, so the month is
          unverified rather than verified. Treat null as absence of evidence, never as a pass.
      verification_failures (list[str] | Unset): Failed/errored rule messages for the month (capped).
  """

  period: str
  period_start: datetime.date
  period_end: datetime.date
  income_statement_fact_set_id: None | str | Unset = UNSET
  balance_sheet_fact_set_id: None | str | Unset = UNSET
  cash_flow_fact_set_id: None | str | Unset = UNSET
  computed_count: int | Unset = 0
  verification_passed: bool | None | Unset = UNSET
  verification_failures: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    income_statement_fact_set_id: None | str | Unset
    if isinstance(self.income_statement_fact_set_id, Unset):
      income_statement_fact_set_id = UNSET
    else:
      income_statement_fact_set_id = self.income_statement_fact_set_id

    balance_sheet_fact_set_id: None | str | Unset
    if isinstance(self.balance_sheet_fact_set_id, Unset):
      balance_sheet_fact_set_id = UNSET
    else:
      balance_sheet_fact_set_id = self.balance_sheet_fact_set_id

    cash_flow_fact_set_id: None | str | Unset
    if isinstance(self.cash_flow_fact_set_id, Unset):
      cash_flow_fact_set_id = UNSET
    else:
      cash_flow_fact_set_id = self.cash_flow_fact_set_id

    computed_count = self.computed_count

    verification_passed: bool | None | Unset
    if isinstance(self.verification_passed, Unset):
      verification_passed = UNSET
    else:
      verification_passed = self.verification_passed

    verification_failures: list[str] | Unset = UNSET
    if not isinstance(self.verification_failures, Unset):
      verification_failures = self.verification_failures

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
        "period_start": period_start,
        "period_end": period_end,
      }
    )
    if income_statement_fact_set_id is not UNSET:
      field_dict["income_statement_fact_set_id"] = income_statement_fact_set_id
    if balance_sheet_fact_set_id is not UNSET:
      field_dict["balance_sheet_fact_set_id"] = balance_sheet_fact_set_id
    if cash_flow_fact_set_id is not UNSET:
      field_dict["cash_flow_fact_set_id"] = cash_flow_fact_set_id
    if computed_count is not UNSET:
      field_dict["computed_count"] = computed_count
    if verification_passed is not UNSET:
      field_dict["verification_passed"] = verification_passed
    if verification_failures is not UNSET:
      field_dict["verification_failures"] = verification_failures

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    period = d.pop("period")

    period_start = datetime.date.fromisoformat(d.pop("period_start"))

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    def _parse_income_statement_fact_set_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    income_statement_fact_set_id = _parse_income_statement_fact_set_id(
      d.pop("income_statement_fact_set_id", UNSET)
    )

    def _parse_balance_sheet_fact_set_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    balance_sheet_fact_set_id = _parse_balance_sheet_fact_set_id(
      d.pop("balance_sheet_fact_set_id", UNSET)
    )

    def _parse_cash_flow_fact_set_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    cash_flow_fact_set_id = _parse_cash_flow_fact_set_id(
      d.pop("cash_flow_fact_set_id", UNSET)
    )

    computed_count = d.pop("computed_count", UNSET)

    def _parse_verification_passed(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    verification_passed = _parse_verification_passed(
      d.pop("verification_passed", UNSET)
    )

    verification_failures = cast(list[str], d.pop("verification_failures", UNSET))

    forecast_month_lite = cls(
      period=period,
      period_start=period_start,
      period_end=period_end,
      income_statement_fact_set_id=income_statement_fact_set_id,
      balance_sheet_fact_set_id=balance_sheet_fact_set_id,
      cash_flow_fact_set_id=cash_flow_fact_set_id,
      computed_count=computed_count,
      verification_passed=verification_passed,
      verification_failures=verification_failures,
    )

    forecast_month_lite.additional_properties = d
    return forecast_month_lite

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
