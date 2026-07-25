from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.backfill_period_outcome_statement_rule_summary_type_0 import (
    BackfillPeriodOutcomeStatementRuleSummaryType0,
  )


T = TypeVar("T", bound="BackfillPeriodOutcome")


@_attrs_define
class BackfillPeriodOutcome:
  """Per-month result of a plan-history backfill pass.

  Attributes:
      period (str): The month, in YYYY-MM
      status (str): stamped: reopen → reclose completed. skipped_drafts: the month holds draft entries the backfill
          refuses to post — review via list-period-drafts, then close-period or re-run. failed: the reclose raised;
          processing halted (see detail).
      statements_stamped (bool | Unset): Whether the reclose stamped canonical statement FactSets. False with a
          statement_stamp_note soft-skip when reporting isn't set up. Default: False.
      statement_stamp_note (None | str | Unset): Soft-skip reason when statements_stamped is false
      statement_rule_summary (BackfillPeriodOutcomeStatementRuleSummaryType0 | None | Unset): Statement-rule
          verification tally for the month's stamped sets (pass/fail/error/skipped); None when no rules ran.
      detail (None | str | Unset): Human-readable detail for skipped/failed months
  """

  period: str
  status: str
  statements_stamped: bool | Unset = False
  statement_stamp_note: None | str | Unset = UNSET
  statement_rule_summary: (
    BackfillPeriodOutcomeStatementRuleSummaryType0 | None | Unset
  ) = UNSET
  detail: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.backfill_period_outcome_statement_rule_summary_type_0 import (
      BackfillPeriodOutcomeStatementRuleSummaryType0,
    )

    period = self.period

    status = self.status

    statements_stamped = self.statements_stamped

    statement_stamp_note: None | str | Unset
    if isinstance(self.statement_stamp_note, Unset):
      statement_stamp_note = UNSET
    else:
      statement_stamp_note = self.statement_stamp_note

    statement_rule_summary: dict[str, Any] | None | Unset
    if isinstance(self.statement_rule_summary, Unset):
      statement_rule_summary = UNSET
    elif isinstance(
      self.statement_rule_summary, BackfillPeriodOutcomeStatementRuleSummaryType0
    ):
      statement_rule_summary = self.statement_rule_summary.to_dict()
    else:
      statement_rule_summary = self.statement_rule_summary

    detail: None | str | Unset
    if isinstance(self.detail, Unset):
      detail = UNSET
    else:
      detail = self.detail

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
        "status": status,
      }
    )
    if statements_stamped is not UNSET:
      field_dict["statements_stamped"] = statements_stamped
    if statement_stamp_note is not UNSET:
      field_dict["statement_stamp_note"] = statement_stamp_note
    if statement_rule_summary is not UNSET:
      field_dict["statement_rule_summary"] = statement_rule_summary
    if detail is not UNSET:
      field_dict["detail"] = detail

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.backfill_period_outcome_statement_rule_summary_type_0 import (
      BackfillPeriodOutcomeStatementRuleSummaryType0,
    )

    d = dict(src_dict)
    period = d.pop("period")

    status = d.pop("status")

    statements_stamped = d.pop("statements_stamped", UNSET)

    def _parse_statement_stamp_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    statement_stamp_note = _parse_statement_stamp_note(
      d.pop("statement_stamp_note", UNSET)
    )

    def _parse_statement_rule_summary(
      data: object,
    ) -> BackfillPeriodOutcomeStatementRuleSummaryType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        statement_rule_summary_type_0 = (
          BackfillPeriodOutcomeStatementRuleSummaryType0.from_dict(data)
        )

        return statement_rule_summary_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(BackfillPeriodOutcomeStatementRuleSummaryType0 | None | Unset, data)

    statement_rule_summary = _parse_statement_rule_summary(
      d.pop("statement_rule_summary", UNSET)
    )

    def _parse_detail(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    detail = _parse_detail(d.pop("detail", UNSET))

    backfill_period_outcome = cls(
      period=period,
      status=status,
      statements_stamped=statements_stamped,
      statement_stamp_note=statement_stamp_note,
      statement_rule_summary=statement_rule_summary,
      detail=detail,
    )

    backfill_period_outcome.additional_properties = d
    return backfill_period_outcome

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
