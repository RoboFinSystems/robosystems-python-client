from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.analytical_statement_fact_row import AnalyticalStatementFactRow
  from ..models.resolved_report_info import ResolvedReportInfo


T = TypeVar("T", bound="FinancialStatementAnalysisResponse")


@_attrs_define
class FinancialStatementAnalysisResponse:
  """Results of the financial-statement-analysis view op.

  Attributes:
      graph_id (str):
      statement_type (str):
      facts (list[AnalyticalStatementFactRow]):
      fact_count (int):
      ticker (None | str | Unset):
      report_id (None | str | Unset):
      resolved_report (None | ResolvedReportInfo | Unset):
  """

  graph_id: str
  statement_type: str
  facts: list[AnalyticalStatementFactRow]
  fact_count: int
  ticker: None | str | Unset = UNSET
  report_id: None | str | Unset = UNSET
  resolved_report: None | ResolvedReportInfo | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.resolved_report_info import ResolvedReportInfo

    graph_id = self.graph_id

    statement_type = self.statement_type

    facts = []
    for facts_item_data in self.facts:
      facts_item = facts_item_data.to_dict()
      facts.append(facts_item)

    fact_count = self.fact_count

    ticker: None | str | Unset
    if isinstance(self.ticker, Unset):
      ticker = UNSET
    else:
      ticker = self.ticker

    report_id: None | str | Unset
    if isinstance(self.report_id, Unset):
      report_id = UNSET
    else:
      report_id = self.report_id

    resolved_report: dict[str, Any] | None | Unset
    if isinstance(self.resolved_report, Unset):
      resolved_report = UNSET
    elif isinstance(self.resolved_report, ResolvedReportInfo):
      resolved_report = self.resolved_report.to_dict()
    else:
      resolved_report = self.resolved_report

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "statement_type": statement_type,
        "facts": facts,
        "fact_count": fact_count,
      }
    )
    if ticker is not UNSET:
      field_dict["ticker"] = ticker
    if report_id is not UNSET:
      field_dict["report_id"] = report_id
    if resolved_report is not UNSET:
      field_dict["resolved_report"] = resolved_report

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.analytical_statement_fact_row import AnalyticalStatementFactRow
    from ..models.resolved_report_info import ResolvedReportInfo

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    statement_type = d.pop("statement_type")

    facts = []
    _facts = d.pop("facts")
    for facts_item_data in _facts:
      facts_item = AnalyticalStatementFactRow.from_dict(facts_item_data)

      facts.append(facts_item)

    fact_count = d.pop("fact_count")

    def _parse_ticker(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    ticker = _parse_ticker(d.pop("ticker", UNSET))

    def _parse_report_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    report_id = _parse_report_id(d.pop("report_id", UNSET))

    def _parse_resolved_report(data: object) -> None | ResolvedReportInfo | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        resolved_report_type_0 = ResolvedReportInfo.from_dict(data)

        return resolved_report_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ResolvedReportInfo | Unset, data)

    resolved_report = _parse_resolved_report(d.pop("resolved_report", UNSET))

    financial_statement_analysis_response = cls(
      graph_id=graph_id,
      statement_type=statement_type,
      facts=facts,
      fact_count=fact_count,
      ticker=ticker,
      report_id=report_id,
      resolved_report=resolved_report,
    )

    financial_statement_analysis_response.additional_properties = d
    return financial_statement_analysis_response

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
