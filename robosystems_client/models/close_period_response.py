from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.close_period_response_rule_summary_type_0 import (
    ClosePeriodResponseRuleSummaryType0,
  )
  from ..models.fiscal_calendar_response import FiscalCalendarResponse


T = TypeVar("T", bound="ClosePeriodResponse")


@_attrs_define
class ClosePeriodResponse:
  """Response from a single-period close operation.

  Attributes:
      fiscal_calendar (FiscalCalendarResponse): Current fiscal calendar state for a graph.
      period (str):
      entries_posted (int | Unset): Number of draft entries transitioned to posted Default: 0.
      target_auto_advanced (bool | Unset): Whether close_target was auto-advanced because it was reached Default:
          False.
      rule_summary (ClosePeriodResponseRuleSummaryType0 | None | Unset): Aggregated rule-eval outcome across every
          schedule Structure with facts in the closed period — keys: pass/fail/error/skipped. None when no schedules had
          facts in the period (§3.8 auto-run on close).
      evaluated_structure_ids (list[str] | Unset): ids of schedule Structures whose rules were evaluated during the
          close. Pairs with rule_summary.
  """

  fiscal_calendar: FiscalCalendarResponse
  period: str
  entries_posted: int | Unset = 0
  target_auto_advanced: bool | Unset = False
  rule_summary: ClosePeriodResponseRuleSummaryType0 | None | Unset = UNSET
  evaluated_structure_ids: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.close_period_response_rule_summary_type_0 import (
      ClosePeriodResponseRuleSummaryType0,
    )

    fiscal_calendar = self.fiscal_calendar.to_dict()

    period = self.period

    entries_posted = self.entries_posted

    target_auto_advanced = self.target_auto_advanced

    rule_summary: dict[str, Any] | None | Unset
    if isinstance(self.rule_summary, Unset):
      rule_summary = UNSET
    elif isinstance(self.rule_summary, ClosePeriodResponseRuleSummaryType0):
      rule_summary = self.rule_summary.to_dict()
    else:
      rule_summary = self.rule_summary

    evaluated_structure_ids: list[str] | Unset = UNSET
    if not isinstance(self.evaluated_structure_ids, Unset):
      evaluated_structure_ids = self.evaluated_structure_ids

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "fiscal_calendar": fiscal_calendar,
        "period": period,
      }
    )
    if entries_posted is not UNSET:
      field_dict["entries_posted"] = entries_posted
    if target_auto_advanced is not UNSET:
      field_dict["target_auto_advanced"] = target_auto_advanced
    if rule_summary is not UNSET:
      field_dict["rule_summary"] = rule_summary
    if evaluated_structure_ids is not UNSET:
      field_dict["evaluated_structure_ids"] = evaluated_structure_ids

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.close_period_response_rule_summary_type_0 import (
      ClosePeriodResponseRuleSummaryType0,
    )
    from ..models.fiscal_calendar_response import FiscalCalendarResponse

    d = dict(src_dict)
    fiscal_calendar = FiscalCalendarResponse.from_dict(d.pop("fiscal_calendar"))

    period = d.pop("period")

    entries_posted = d.pop("entries_posted", UNSET)

    target_auto_advanced = d.pop("target_auto_advanced", UNSET)

    def _parse_rule_summary(
      data: object,
    ) -> ClosePeriodResponseRuleSummaryType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        rule_summary_type_0 = ClosePeriodResponseRuleSummaryType0.from_dict(data)

        return rule_summary_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(ClosePeriodResponseRuleSummaryType0 | None | Unset, data)

    rule_summary = _parse_rule_summary(d.pop("rule_summary", UNSET))

    evaluated_structure_ids = cast(list[str], d.pop("evaluated_structure_ids", UNSET))

    close_period_response = cls(
      fiscal_calendar=fiscal_calendar,
      period=period,
      entries_posted=entries_posted,
      target_auto_advanced=target_auto_advanced,
      rule_summary=rule_summary,
      evaluated_structure_ids=evaluated_structure_ids,
    )

    close_period_response.additional_properties = d
    return close_period_response

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
