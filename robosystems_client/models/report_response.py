from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.period_spec import PeriodSpec
  from ..models.report_response_rule_summary_type_0 import (
    ReportResponseRuleSummaryType0,
  )
  from ..models.structure_summary import StructureSummary


T = TypeVar("T", bound="ReportResponse")


@_attrs_define
class ReportResponse:
  """Report definition summary — header metadata, no facts.

  Returned by ``create-report``, ``regenerate-report``,
  ``file-report``, and ``transition-filing-status``. Use the package
  read endpoint to retrieve a Report rehydrated with its rendered
  ``InformationBlockEnvelope`` items.

      Attributes:
          id (str): Report identifier (ULID).
          name (str): Human-readable report name.
          taxonomy_id (str): Taxonomy this report renders against.
          generation_status (str): Computation lifecycle: `generating`, `published`, `failed`. Orthogonal to
              `filing_status`.
          period_type (str): Period cadence: `monthly`, `quarterly`, `annual`.
          comparative (bool): True when an auto-generated prior-period column is included.
          created_at (datetime.datetime): When the report row was created.
          period_start (datetime.date | None | Unset): Current-period start.
          period_end (datetime.date | None | Unset): Current-period end.
          periods (list[PeriodSpec] | None | Unset): Explicit period columns when the report was created with a multi-
              period layout.
          mapping_id (None | str | Unset): CoA → taxonomy mapping the facts were rolled up through.
          ai_generated (bool | Unset): True when the report was created by an AI agent rather than a user. Default: False.
          last_generated (datetime.datetime | None | Unset): When the facts were last (re)generated.
          structures (list[StructureSummary] | Unset): Structures available for this report's taxonomy — renderable
              sections (BS / IS / CF / Equity / Schedules).
          entity_name (None | str | Unset): Display name of the primary entity the report is tagged to.
          filing_status (str | Unset): Filing lifecycle (orthogonal to `generation_status`): `draft`, `under_review`,
              `filed`, `archived`. Default: 'draft'.
          filed_at (datetime.datetime | None | Unset): When the report was transitioned to `filed`.
          filed_by (None | str | Unset): User ID that transitioned the report to `filed`.
          supersedes_id (None | str | Unset): When this report restates an earlier filing, the predecessor's report ID.
          superseded_by_id (None | str | Unset): When this report has been restated, the successor's report ID.
          source_graph_id (None | str | Unset): Origin graph for received (shared) reports — populated only on the
              recipient's copy.
          source_report_id (None | str | Unset): Origin report ID for received (shared) reports — populated only on the
              recipient's copy.
          shared_at (datetime.datetime | None | Unset): When the report was shared into this graph (recipient side).
          rule_summary (None | ReportResponseRuleSummaryType0 | Unset): Counts by rule outcome (e.g. `{'passed': 12,
              'failed': 1}`) from the most recent evaluation. Null until rules run.
  """

  id: str
  name: str
  taxonomy_id: str
  generation_status: str
  period_type: str
  comparative: bool
  created_at: datetime.datetime
  period_start: datetime.date | None | Unset = UNSET
  period_end: datetime.date | None | Unset = UNSET
  periods: list[PeriodSpec] | None | Unset = UNSET
  mapping_id: None | str | Unset = UNSET
  ai_generated: bool | Unset = False
  last_generated: datetime.datetime | None | Unset = UNSET
  structures: list[StructureSummary] | Unset = UNSET
  entity_name: None | str | Unset = UNSET
  filing_status: str | Unset = "draft"
  filed_at: datetime.datetime | None | Unset = UNSET
  filed_by: None | str | Unset = UNSET
  supersedes_id: None | str | Unset = UNSET
  superseded_by_id: None | str | Unset = UNSET
  source_graph_id: None | str | Unset = UNSET
  source_report_id: None | str | Unset = UNSET
  shared_at: datetime.datetime | None | Unset = UNSET
  rule_summary: None | ReportResponseRuleSummaryType0 | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.report_response_rule_summary_type_0 import (
      ReportResponseRuleSummaryType0,
    )

    id = self.id

    name = self.name

    taxonomy_id = self.taxonomy_id

    generation_status = self.generation_status

    period_type = self.period_type

    comparative = self.comparative

    created_at = self.created_at.isoformat()

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    elif isinstance(self.period_start, datetime.date):
      period_start = self.period_start.isoformat()
    else:
      period_start = self.period_start

    period_end: None | str | Unset
    if isinstance(self.period_end, Unset):
      period_end = UNSET
    elif isinstance(self.period_end, datetime.date):
      period_end = self.period_end.isoformat()
    else:
      period_end = self.period_end

    periods: list[dict[str, Any]] | None | Unset
    if isinstance(self.periods, Unset):
      periods = UNSET
    elif isinstance(self.periods, list):
      periods = []
      for periods_type_0_item_data in self.periods:
        periods_type_0_item = periods_type_0_item_data.to_dict()
        periods.append(periods_type_0_item)

    else:
      periods = self.periods

    mapping_id: None | str | Unset
    if isinstance(self.mapping_id, Unset):
      mapping_id = UNSET
    else:
      mapping_id = self.mapping_id

    ai_generated = self.ai_generated

    last_generated: None | str | Unset
    if isinstance(self.last_generated, Unset):
      last_generated = UNSET
    elif isinstance(self.last_generated, datetime.datetime):
      last_generated = self.last_generated.isoformat()
    else:
      last_generated = self.last_generated

    structures: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.structures, Unset):
      structures = []
      for structures_item_data in self.structures:
        structures_item = structures_item_data.to_dict()
        structures.append(structures_item)

    entity_name: None | str | Unset
    if isinstance(self.entity_name, Unset):
      entity_name = UNSET
    else:
      entity_name = self.entity_name

    filing_status = self.filing_status

    filed_at: None | str | Unset
    if isinstance(self.filed_at, Unset):
      filed_at = UNSET
    elif isinstance(self.filed_at, datetime.datetime):
      filed_at = self.filed_at.isoformat()
    else:
      filed_at = self.filed_at

    filed_by: None | str | Unset
    if isinstance(self.filed_by, Unset):
      filed_by = UNSET
    else:
      filed_by = self.filed_by

    supersedes_id: None | str | Unset
    if isinstance(self.supersedes_id, Unset):
      supersedes_id = UNSET
    else:
      supersedes_id = self.supersedes_id

    superseded_by_id: None | str | Unset
    if isinstance(self.superseded_by_id, Unset):
      superseded_by_id = UNSET
    else:
      superseded_by_id = self.superseded_by_id

    source_graph_id: None | str | Unset
    if isinstance(self.source_graph_id, Unset):
      source_graph_id = UNSET
    else:
      source_graph_id = self.source_graph_id

    source_report_id: None | str | Unset
    if isinstance(self.source_report_id, Unset):
      source_report_id = UNSET
    else:
      source_report_id = self.source_report_id

    shared_at: None | str | Unset
    if isinstance(self.shared_at, Unset):
      shared_at = UNSET
    elif isinstance(self.shared_at, datetime.datetime):
      shared_at = self.shared_at.isoformat()
    else:
      shared_at = self.shared_at

    rule_summary: dict[str, Any] | None | Unset
    if isinstance(self.rule_summary, Unset):
      rule_summary = UNSET
    elif isinstance(self.rule_summary, ReportResponseRuleSummaryType0):
      rule_summary = self.rule_summary.to_dict()
    else:
      rule_summary = self.rule_summary

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "taxonomy_id": taxonomy_id,
        "generation_status": generation_status,
        "period_type": period_type,
        "comparative": comparative,
        "created_at": created_at,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if periods is not UNSET:
      field_dict["periods"] = periods
    if mapping_id is not UNSET:
      field_dict["mapping_id"] = mapping_id
    if ai_generated is not UNSET:
      field_dict["ai_generated"] = ai_generated
    if last_generated is not UNSET:
      field_dict["last_generated"] = last_generated
    if structures is not UNSET:
      field_dict["structures"] = structures
    if entity_name is not UNSET:
      field_dict["entity_name"] = entity_name
    if filing_status is not UNSET:
      field_dict["filing_status"] = filing_status
    if filed_at is not UNSET:
      field_dict["filed_at"] = filed_at
    if filed_by is not UNSET:
      field_dict["filed_by"] = filed_by
    if supersedes_id is not UNSET:
      field_dict["supersedes_id"] = supersedes_id
    if superseded_by_id is not UNSET:
      field_dict["superseded_by_id"] = superseded_by_id
    if source_graph_id is not UNSET:
      field_dict["source_graph_id"] = source_graph_id
    if source_report_id is not UNSET:
      field_dict["source_report_id"] = source_report_id
    if shared_at is not UNSET:
      field_dict["shared_at"] = shared_at
    if rule_summary is not UNSET:
      field_dict["rule_summary"] = rule_summary

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.period_spec import PeriodSpec
    from ..models.report_response_rule_summary_type_0 import (
      ReportResponseRuleSummaryType0,
    )
    from ..models.structure_summary import StructureSummary

    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    taxonomy_id = d.pop("taxonomy_id")

    generation_status = d.pop("generation_status")

    period_type = d.pop("period_type")

    comparative = d.pop("comparative")

    created_at = isoparse(d.pop("created_at"))

    def _parse_period_start(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_start_type_0 = isoparse(data).date()

        return period_start_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_start = _parse_period_start(d.pop("period_start", UNSET))

    def _parse_period_end(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_end_type_0 = isoparse(data).date()

        return period_end_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_end = _parse_period_end(d.pop("period_end", UNSET))

    def _parse_periods(data: object) -> list[PeriodSpec] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        periods_type_0 = []
        _periods_type_0 = data
        for periods_type_0_item_data in _periods_type_0:
          periods_type_0_item = PeriodSpec.from_dict(periods_type_0_item_data)

          periods_type_0.append(periods_type_0_item)

        return periods_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[PeriodSpec] | None | Unset, data)

    periods = _parse_periods(d.pop("periods", UNSET))

    def _parse_mapping_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    mapping_id = _parse_mapping_id(d.pop("mapping_id", UNSET))

    ai_generated = d.pop("ai_generated", UNSET)

    def _parse_last_generated(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        last_generated_type_0 = isoparse(data)

        return last_generated_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    last_generated = _parse_last_generated(d.pop("last_generated", UNSET))

    _structures = d.pop("structures", UNSET)
    structures: list[StructureSummary] | Unset = UNSET
    if _structures is not UNSET:
      structures = []
      for structures_item_data in _structures:
        structures_item = StructureSummary.from_dict(structures_item_data)

        structures.append(structures_item)

    def _parse_entity_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_name = _parse_entity_name(d.pop("entity_name", UNSET))

    filing_status = d.pop("filing_status", UNSET)

    def _parse_filed_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        filed_at_type_0 = isoparse(data)

        return filed_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    filed_at = _parse_filed_at(d.pop("filed_at", UNSET))

    def _parse_filed_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    filed_by = _parse_filed_by(d.pop("filed_by", UNSET))

    def _parse_supersedes_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    supersedes_id = _parse_supersedes_id(d.pop("supersedes_id", UNSET))

    def _parse_superseded_by_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    superseded_by_id = _parse_superseded_by_id(d.pop("superseded_by_id", UNSET))

    def _parse_source_graph_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_graph_id = _parse_source_graph_id(d.pop("source_graph_id", UNSET))

    def _parse_source_report_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_report_id = _parse_source_report_id(d.pop("source_report_id", UNSET))

    def _parse_shared_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        shared_at_type_0 = isoparse(data)

        return shared_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    shared_at = _parse_shared_at(d.pop("shared_at", UNSET))

    def _parse_rule_summary(
      data: object,
    ) -> None | ReportResponseRuleSummaryType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        rule_summary_type_0 = ReportResponseRuleSummaryType0.from_dict(data)

        return rule_summary_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ReportResponseRuleSummaryType0 | Unset, data)

    rule_summary = _parse_rule_summary(d.pop("rule_summary", UNSET))

    report_response = cls(
      id=id,
      name=name,
      taxonomy_id=taxonomy_id,
      generation_status=generation_status,
      period_type=period_type,
      comparative=comparative,
      created_at=created_at,
      period_start=period_start,
      period_end=period_end,
      periods=periods,
      mapping_id=mapping_id,
      ai_generated=ai_generated,
      last_generated=last_generated,
      structures=structures,
      entity_name=entity_name,
      filing_status=filing_status,
      filed_at=filed_at,
      filed_by=filed_by,
      supersedes_id=supersedes_id,
      superseded_by_id=superseded_by_id,
      source_graph_id=source_graph_id,
      source_report_id=source_report_id,
      shared_at=shared_at,
      rule_summary=rule_summary,
    )

    report_response.additional_properties = d
    return report_response

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
