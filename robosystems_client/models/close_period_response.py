from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.close_period_response_gate_finding_counts import (
    ClosePeriodResponseGateFindingCounts,
  )
  from ..models.close_period_response_rule_summary_type_0 import (
    ClosePeriodResponseRuleSummaryType0,
  )
  from ..models.close_period_response_stamped_statement_sets import (
    ClosePeriodResponseStampedStatementSets,
  )
  from ..models.close_period_response_statement_rule_summary_type_0 import (
    ClosePeriodResponseStatementRuleSummaryType0,
  )
  from ..models.fiscal_calendar_response import FiscalCalendarResponse


T = TypeVar("T", bound="ClosePeriodResponse")


@_attrs_define
class ClosePeriodResponse:
  """Response from a single-period close operation.

  Attributes:
      fiscal_calendar (FiscalCalendarResponse): Current fiscal calendar state for one entity of a graph.
      period (str):
      entries_posted (int | Unset): Total draft entries the close transitioned to posted, across both post paths (QB
          pre-publish + local bulk transition). See entries_published_to_qb / entries_posted_locally for the split.
          Default: 0.
      entries_published_to_qb (int | Unset): Drafts published to QuickBooks by the close's pre-publish step (each is
          promoted to posted at publish time). Default: 0.
      entries_posted_locally (int | Unset): Drafts posted by the local bulk transition (entries that don't publish to
          QuickBooks, e.g. native-only graphs or local-only sources). Default: 0.
      target_auto_advanced (bool | Unset): Whether close_target was auto-advanced because it was reached Default:
          False.
      rule_summary (ClosePeriodResponseRuleSummaryType0 | None | Unset): Aggregated rule-eval outcome across every
          schedule Structure with facts in the closed period — keys: pass/fail/error/skipped. None when no schedules had
          facts in the period (auto-run on close).
      evaluated_structure_ids (list[str] | Unset): ids of schedule Structures whose rules were evaluated during the
          close. Pairs with rule_summary.
      statements_stamped (bool | Unset): Whether the close stamped the period's canonical statement FactSets (the
          close-time pivot). False when the tenant hasn't set up reporting yet — see statement_stamp_note. Default: False.
      shadow (bool | Unset): True when the close ran in shadow (the QuickBooks connection's write_policy is 'shadow'):
          nothing was written to QuickBooks, nothing posted, the in-window drafts were shadowed, and the gates that would
          have blocked the close are in gate_findings. Default: False.
      entries_shadowed (int | Unset): Drafts a shadow close took as expectations (status 'shadowed') instead of
          posting. Always 0 outside shadow. Default: 0.
      gate_findings (list[str] | Unset): Blocker codes a shadow close recorded instead of enforcing: sync_stale,
          pending_obligations, stranded_obligations, reconciling_items, unposted_source_events, unreconciled_accounts.
          Empty outside shadow.
      gate_finding_counts (ClosePeriodResponseGateFindingCounts | Unset): Each finding's size: days stale for
          sync_stale, a count for the rest.
      statement_stamp_note (None | str | Unset): Soft-skip reason when statements_stamped is false: no_coa_mapping |
          no_entity | no_statement_structures | no_taxonomy.
      stamped_statement_sets (ClosePeriodResponseStampedStatementSets | Unset): structure_id -> fact_set_id for every
          canonical statement FactSet minted by this close (report_id NULL; replaced on reclose).
      statement_rule_summary (ClosePeriodResponseStatementRuleSummaryType0 | None | Unset): Aggregated statement-rule
          verification outcome across the stamped structures — keys: pass/fail/error/skipped. None when no statement rules
          exist. Distinct from rule_summary (the schedule-rule pass).
  """

  fiscal_calendar: FiscalCalendarResponse
  period: str
  entries_posted: int | Unset = 0
  entries_published_to_qb: int | Unset = 0
  entries_posted_locally: int | Unset = 0
  target_auto_advanced: bool | Unset = False
  rule_summary: ClosePeriodResponseRuleSummaryType0 | None | Unset = UNSET
  evaluated_structure_ids: list[str] | Unset = UNSET
  statements_stamped: bool | Unset = False
  shadow: bool | Unset = False
  entries_shadowed: int | Unset = 0
  gate_findings: list[str] | Unset = UNSET
  gate_finding_counts: ClosePeriodResponseGateFindingCounts | Unset = UNSET
  statement_stamp_note: None | str | Unset = UNSET
  stamped_statement_sets: ClosePeriodResponseStampedStatementSets | Unset = UNSET
  statement_rule_summary: (
    ClosePeriodResponseStatementRuleSummaryType0 | None | Unset
  ) = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.close_period_response_rule_summary_type_0 import (
      ClosePeriodResponseRuleSummaryType0,
    )
    from ..models.close_period_response_statement_rule_summary_type_0 import (
      ClosePeriodResponseStatementRuleSummaryType0,
    )

    fiscal_calendar = self.fiscal_calendar.to_dict()

    period = self.period

    entries_posted = self.entries_posted

    entries_published_to_qb = self.entries_published_to_qb

    entries_posted_locally = self.entries_posted_locally

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

    statements_stamped = self.statements_stamped

    shadow = self.shadow

    entries_shadowed = self.entries_shadowed

    gate_findings: list[str] | Unset = UNSET
    if not isinstance(self.gate_findings, Unset):
      gate_findings = self.gate_findings

    gate_finding_counts: dict[str, Any] | Unset = UNSET
    if not isinstance(self.gate_finding_counts, Unset):
      gate_finding_counts = self.gate_finding_counts.to_dict()

    statement_stamp_note: None | str | Unset
    if isinstance(self.statement_stamp_note, Unset):
      statement_stamp_note = UNSET
    else:
      statement_stamp_note = self.statement_stamp_note

    stamped_statement_sets: dict[str, Any] | Unset = UNSET
    if not isinstance(self.stamped_statement_sets, Unset):
      stamped_statement_sets = self.stamped_statement_sets.to_dict()

    statement_rule_summary: dict[str, Any] | None | Unset
    if isinstance(self.statement_rule_summary, Unset):
      statement_rule_summary = UNSET
    elif isinstance(
      self.statement_rule_summary, ClosePeriodResponseStatementRuleSummaryType0
    ):
      statement_rule_summary = self.statement_rule_summary.to_dict()
    else:
      statement_rule_summary = self.statement_rule_summary

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
    if entries_published_to_qb is not UNSET:
      field_dict["entries_published_to_qb"] = entries_published_to_qb
    if entries_posted_locally is not UNSET:
      field_dict["entries_posted_locally"] = entries_posted_locally
    if target_auto_advanced is not UNSET:
      field_dict["target_auto_advanced"] = target_auto_advanced
    if rule_summary is not UNSET:
      field_dict["rule_summary"] = rule_summary
    if evaluated_structure_ids is not UNSET:
      field_dict["evaluated_structure_ids"] = evaluated_structure_ids
    if statements_stamped is not UNSET:
      field_dict["statements_stamped"] = statements_stamped
    if shadow is not UNSET:
      field_dict["shadow"] = shadow
    if entries_shadowed is not UNSET:
      field_dict["entries_shadowed"] = entries_shadowed
    if gate_findings is not UNSET:
      field_dict["gate_findings"] = gate_findings
    if gate_finding_counts is not UNSET:
      field_dict["gate_finding_counts"] = gate_finding_counts
    if statement_stamp_note is not UNSET:
      field_dict["statement_stamp_note"] = statement_stamp_note
    if stamped_statement_sets is not UNSET:
      field_dict["stamped_statement_sets"] = stamped_statement_sets
    if statement_rule_summary is not UNSET:
      field_dict["statement_rule_summary"] = statement_rule_summary

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.close_period_response_gate_finding_counts import (
      ClosePeriodResponseGateFindingCounts,
    )
    from ..models.close_period_response_rule_summary_type_0 import (
      ClosePeriodResponseRuleSummaryType0,
    )
    from ..models.close_period_response_stamped_statement_sets import (
      ClosePeriodResponseStampedStatementSets,
    )
    from ..models.close_period_response_statement_rule_summary_type_0 import (
      ClosePeriodResponseStatementRuleSummaryType0,
    )
    from ..models.fiscal_calendar_response import FiscalCalendarResponse

    d = dict(src_dict)
    fiscal_calendar = FiscalCalendarResponse.from_dict(d.pop("fiscal_calendar"))

    period = d.pop("period")

    entries_posted = d.pop("entries_posted", UNSET)

    entries_published_to_qb = d.pop("entries_published_to_qb", UNSET)

    entries_posted_locally = d.pop("entries_posted_locally", UNSET)

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

    statements_stamped = d.pop("statements_stamped", UNSET)

    shadow = d.pop("shadow", UNSET)

    entries_shadowed = d.pop("entries_shadowed", UNSET)

    gate_findings = cast(list[str], d.pop("gate_findings", UNSET))

    _gate_finding_counts = d.pop("gate_finding_counts", UNSET)
    gate_finding_counts: ClosePeriodResponseGateFindingCounts | Unset
    if isinstance(_gate_finding_counts, Unset):
      gate_finding_counts = UNSET
    else:
      gate_finding_counts = ClosePeriodResponseGateFindingCounts.from_dict(
        _gate_finding_counts
      )

    def _parse_statement_stamp_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    statement_stamp_note = _parse_statement_stamp_note(
      d.pop("statement_stamp_note", UNSET)
    )

    _stamped_statement_sets = d.pop("stamped_statement_sets", UNSET)
    stamped_statement_sets: ClosePeriodResponseStampedStatementSets | Unset
    if isinstance(_stamped_statement_sets, Unset):
      stamped_statement_sets = UNSET
    else:
      stamped_statement_sets = ClosePeriodResponseStampedStatementSets.from_dict(
        _stamped_statement_sets
      )

    def _parse_statement_rule_summary(
      data: object,
    ) -> ClosePeriodResponseStatementRuleSummaryType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        statement_rule_summary_type_0 = (
          ClosePeriodResponseStatementRuleSummaryType0.from_dict(data)
        )

        return statement_rule_summary_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(ClosePeriodResponseStatementRuleSummaryType0 | None | Unset, data)

    statement_rule_summary = _parse_statement_rule_summary(
      d.pop("statement_rule_summary", UNSET)
    )

    close_period_response = cls(
      fiscal_calendar=fiscal_calendar,
      period=period,
      entries_posted=entries_posted,
      entries_published_to_qb=entries_published_to_qb,
      entries_posted_locally=entries_posted_locally,
      target_auto_advanced=target_auto_advanced,
      rule_summary=rule_summary,
      evaluated_structure_ids=evaluated_structure_ids,
      statements_stamped=statements_stamped,
      shadow=shadow,
      entries_shadowed=entries_shadowed,
      gate_findings=gate_findings,
      gate_finding_counts=gate_finding_counts,
      statement_stamp_note=statement_stamp_note,
      stamped_statement_sets=stamped_statement_sets,
      statement_rule_summary=statement_rule_summary,
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
