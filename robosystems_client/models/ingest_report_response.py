from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.report_departure import ReportDeparture


T = TypeVar("T", bound="IngestReportResponse")


@_attrs_define
class IngestReportResponse:
  """What an ingest loaded, or on a dry run what it would load.

  Attributes:
      dry_run (bool): True when nothing was written.
      entity_id (str): The entity the report hangs on.
      period_end (datetime.date): The last day the report covers.
      kind (str): What the report is.
      fact_count (int): Values loaded as facts.
      section_count (int): Statements and tables loaded.
      calculations_checked (int): Totals that were compared with their terms; all agreed.
      balance_checked (bool): Whether total assets were compared with liabilities and equity.
      report_id (None | str | Unset): The report's ID in this graph; null on a dry run.
      concepts_added (list[str] | Unset): Concepts the graph did not have, added to its received-reports vocabulary.
      dimensional_facts_not_loaded (int | Unset): Values broken out by a dimension. They stay in the stored file; the
          graph holds the report's totals. Default: 0.
      replaced_report_ids (list[str] | Unset): Earlier ingests for the same entity, period end and kind, now replaced.
      unplaced_concepts (list[str] | Unset): Library concepts with a value that no section places, for a report sent
          as rows. Their values load, but appear on no statement or table.
      conforms_to_library (bool | None | Unset): For a report sent as rows: true when its balance sheet and income
          statement are arranged as the library arranges them, so their lines mean what the same lines mean in any other
          report. Null for a holon or a Tavi model, which is not compared.
      departures (list[ReportDeparture] | Unset): Each place the report departs from the library's arrangement. The
          report still loads; the list is kept with it.
  """

  dry_run: bool
  entity_id: str
  period_end: datetime.date
  kind: str
  fact_count: int
  section_count: int
  calculations_checked: int
  balance_checked: bool
  report_id: None | str | Unset = UNSET
  concepts_added: list[str] | Unset = UNSET
  dimensional_facts_not_loaded: int | Unset = 0
  replaced_report_ids: list[str] | Unset = UNSET
  unplaced_concepts: list[str] | Unset = UNSET
  conforms_to_library: bool | None | Unset = UNSET
  departures: list[ReportDeparture] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    dry_run = self.dry_run

    entity_id = self.entity_id

    period_end = self.period_end.isoformat()

    kind = self.kind

    fact_count = self.fact_count

    section_count = self.section_count

    calculations_checked = self.calculations_checked

    balance_checked = self.balance_checked

    report_id: None | str | Unset
    if isinstance(self.report_id, Unset):
      report_id = UNSET
    else:
      report_id = self.report_id

    concepts_added: list[str] | Unset = UNSET
    if not isinstance(self.concepts_added, Unset):
      concepts_added = self.concepts_added

    dimensional_facts_not_loaded = self.dimensional_facts_not_loaded

    replaced_report_ids: list[str] | Unset = UNSET
    if not isinstance(self.replaced_report_ids, Unset):
      replaced_report_ids = self.replaced_report_ids

    unplaced_concepts: list[str] | Unset = UNSET
    if not isinstance(self.unplaced_concepts, Unset):
      unplaced_concepts = self.unplaced_concepts

    conforms_to_library: bool | None | Unset
    if isinstance(self.conforms_to_library, Unset):
      conforms_to_library = UNSET
    else:
      conforms_to_library = self.conforms_to_library

    departures: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.departures, Unset):
      departures = []
      for departures_item_data in self.departures:
        departures_item = departures_item_data.to_dict()
        departures.append(departures_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "dry_run": dry_run,
        "entity_id": entity_id,
        "period_end": period_end,
        "kind": kind,
        "fact_count": fact_count,
        "section_count": section_count,
        "calculations_checked": calculations_checked,
        "balance_checked": balance_checked,
      }
    )
    if report_id is not UNSET:
      field_dict["report_id"] = report_id
    if concepts_added is not UNSET:
      field_dict["concepts_added"] = concepts_added
    if dimensional_facts_not_loaded is not UNSET:
      field_dict["dimensional_facts_not_loaded"] = dimensional_facts_not_loaded
    if replaced_report_ids is not UNSET:
      field_dict["replaced_report_ids"] = replaced_report_ids
    if unplaced_concepts is not UNSET:
      field_dict["unplaced_concepts"] = unplaced_concepts
    if conforms_to_library is not UNSET:
      field_dict["conforms_to_library"] = conforms_to_library
    if departures is not UNSET:
      field_dict["departures"] = departures

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.report_departure import ReportDeparture

    d = dict(src_dict)
    dry_run = d.pop("dry_run")

    entity_id = d.pop("entity_id")

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    kind = d.pop("kind")

    fact_count = d.pop("fact_count")

    section_count = d.pop("section_count")

    calculations_checked = d.pop("calculations_checked")

    balance_checked = d.pop("balance_checked")

    def _parse_report_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    report_id = _parse_report_id(d.pop("report_id", UNSET))

    concepts_added = cast(list[str], d.pop("concepts_added", UNSET))

    dimensional_facts_not_loaded = d.pop("dimensional_facts_not_loaded", UNSET)

    replaced_report_ids = cast(list[str], d.pop("replaced_report_ids", UNSET))

    unplaced_concepts = cast(list[str], d.pop("unplaced_concepts", UNSET))

    def _parse_conforms_to_library(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    conforms_to_library = _parse_conforms_to_library(
      d.pop("conforms_to_library", UNSET)
    )

    _departures = d.pop("departures", UNSET)
    departures: list[ReportDeparture] | Unset = UNSET
    if _departures is not UNSET:
      departures = []
      for departures_item_data in _departures:
        departures_item = ReportDeparture.from_dict(departures_item_data)

        departures.append(departures_item)

    ingest_report_response = cls(
      dry_run=dry_run,
      entity_id=entity_id,
      period_end=period_end,
      kind=kind,
      fact_count=fact_count,
      section_count=section_count,
      calculations_checked=calculations_checked,
      balance_checked=balance_checked,
      report_id=report_id,
      concepts_added=concepts_added,
      dimensional_facts_not_loaded=dimensional_facts_not_loaded,
      replaced_report_ids=replaced_report_ids,
      unplaced_concepts=unplaced_concepts,
      conforms_to_library=conforms_to_library,
      departures=departures,
    )

    ingest_report_response.additional_properties = d
    return ingest_report_response

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
