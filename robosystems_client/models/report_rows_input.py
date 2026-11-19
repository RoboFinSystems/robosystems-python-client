from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.report_concept_row import ReportConceptRow
  from ..models.report_fact_row import ReportFactRow
  from ..models.report_rows_input_labels import ReportRowsInputLabels
  from ..models.report_rows_input_namespaces import ReportRowsInputNamespaces
  from ..models.report_section_row import ReportSectionRow


T = TypeVar("T", bound="ReportRowsInput")


@_attrs_define
class ReportRowsInput:
  """A report as rows, for the server to assemble into a holon.

  Attributes:
      period_end (datetime.date): The last day the report covers.
      facts (list[ReportFactRow]): The values.
      kind (str | Unset): What the report is, e.g. `monthly-package`, `quarterly-financials`. A later ingest for the
          same entity, period end and kind replaces this one. Default: 'monthly-package'.
      attributed_to (None | str | Unset): Who or what read the values out of the source document.
      namespaces (ReportRowsInputNamespaces | Unset): Prefix to namespace URI, for concept prefixes that are not a
          library's.
      concepts (list[ReportConceptRow] | Unset): The concepts the library does not have, each declared once. A library
          concept (`rs-gaap:Assets`) needs no entry unless the report words it differently.
      labels (ReportRowsInputLabels | Unset): The document's own wording for a line, by library concept (`rs-
          gaap:LaborAndRelatedExpense`: `Personnel Expense`). The report reads back with this wording; the concept stays
          the library's.
      sections (list[ReportSectionRow] | Unset): The report's statements and tables.
  """

  period_end: datetime.date
  facts: list[ReportFactRow]
  kind: str | Unset = "monthly-package"
  attributed_to: None | str | Unset = UNSET
  namespaces: ReportRowsInputNamespaces | Unset = UNSET
  concepts: list[ReportConceptRow] | Unset = UNSET
  labels: ReportRowsInputLabels | Unset = UNSET
  sections: list[ReportSectionRow] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period_end = self.period_end.isoformat()

    facts = []
    for facts_item_data in self.facts:
      facts_item = facts_item_data.to_dict()
      facts.append(facts_item)

    kind = self.kind

    attributed_to: None | str | Unset
    if isinstance(self.attributed_to, Unset):
      attributed_to = UNSET
    else:
      attributed_to = self.attributed_to

    namespaces: dict[str, Any] | Unset = UNSET
    if not isinstance(self.namespaces, Unset):
      namespaces = self.namespaces.to_dict()

    concepts: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.concepts, Unset):
      concepts = []
      for concepts_item_data in self.concepts:
        concepts_item = concepts_item_data.to_dict()
        concepts.append(concepts_item)

    labels: dict[str, Any] | Unset = UNSET
    if not isinstance(self.labels, Unset):
      labels = self.labels.to_dict()

    sections: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.sections, Unset):
      sections = []
      for sections_item_data in self.sections:
        sections_item = sections_item_data.to_dict()
        sections.append(sections_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period_end": period_end,
        "facts": facts,
      }
    )
    if kind is not UNSET:
      field_dict["kind"] = kind
    if attributed_to is not UNSET:
      field_dict["attributed_to"] = attributed_to
    if namespaces is not UNSET:
      field_dict["namespaces"] = namespaces
    if concepts is not UNSET:
      field_dict["concepts"] = concepts
    if labels is not UNSET:
      field_dict["labels"] = labels
    if sections is not UNSET:
      field_dict["sections"] = sections

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.report_concept_row import ReportConceptRow
    from ..models.report_fact_row import ReportFactRow
    from ..models.report_rows_input_labels import ReportRowsInputLabels
    from ..models.report_rows_input_namespaces import ReportRowsInputNamespaces
    from ..models.report_section_row import ReportSectionRow

    d = dict(src_dict)
    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    facts = []
    _facts = d.pop("facts")
    for facts_item_data in _facts:
      facts_item = ReportFactRow.from_dict(facts_item_data)

      facts.append(facts_item)

    kind = d.pop("kind", UNSET)

    def _parse_attributed_to(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    attributed_to = _parse_attributed_to(d.pop("attributed_to", UNSET))

    _namespaces = d.pop("namespaces", UNSET)
    namespaces: ReportRowsInputNamespaces | Unset
    if isinstance(_namespaces, Unset):
      namespaces = UNSET
    else:
      namespaces = ReportRowsInputNamespaces.from_dict(_namespaces)

    _concepts = d.pop("concepts", UNSET)
    concepts: list[ReportConceptRow] | Unset = UNSET
    if _concepts is not UNSET:
      concepts = []
      for concepts_item_data in _concepts:
        concepts_item = ReportConceptRow.from_dict(concepts_item_data)

        concepts.append(concepts_item)

    _labels = d.pop("labels", UNSET)
    labels: ReportRowsInputLabels | Unset
    if isinstance(_labels, Unset):
      labels = UNSET
    else:
      labels = ReportRowsInputLabels.from_dict(_labels)

    _sections = d.pop("sections", UNSET)
    sections: list[ReportSectionRow] | Unset = UNSET
    if _sections is not UNSET:
      sections = []
      for sections_item_data in _sections:
        sections_item = ReportSectionRow.from_dict(sections_item_data)

        sections.append(sections_item)

    report_rows_input = cls(
      period_end=period_end,
      facts=facts,
      kind=kind,
      attributed_to=attributed_to,
      namespaces=namespaces,
      concepts=concepts,
      labels=labels,
      sections=sections,
    )

    report_rows_input.additional_properties = d
    return report_rows_input

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
