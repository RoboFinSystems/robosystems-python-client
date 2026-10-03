from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.search_text_response_hits_item import SearchTextResponseHitsItem
  from ..models.search_text_response_resolved_report_type_0 import (
    SearchTextResponseResolvedReportType0,
  )
  from ..models.search_text_response_sections_type_0_item import (
    SearchTextResponseSectionsType0Item,
  )
  from ..models.search_text_response_terms_type_0_item import (
    SearchTextResponseTermsType0Item,
  )


T = TypeVar("T", bound="SearchTextResponse")


@_attrs_define
class SearchTextResponse:
  """The search-text view op's result: matches in document order.

  Attributes:
      graph_id (str):
      query (str):
      total (int):
      text_chars (int):
      report_id (None | str | Unset):
      accession (None | str | Unset):
      resolved_report (None | SearchTextResponseResolvedReportType0 | Unset):
      hits (list[SearchTextResponseHitsItem] | Unset):
      text (None | str | Unset):
      sections (list[SearchTextResponseSectionsType0Item] | None | Unset):
      sections_omitted (int | None | Unset):
      terms (list[SearchTextResponseTermsType0Item] | None | Unset):
      note (None | str | Unset):
  """

  graph_id: str
  query: str
  total: int
  text_chars: int
  report_id: None | str | Unset = UNSET
  accession: None | str | Unset = UNSET
  resolved_report: None | SearchTextResponseResolvedReportType0 | Unset = UNSET
  hits: list[SearchTextResponseHitsItem] | Unset = UNSET
  text: None | str | Unset = UNSET
  sections: list[SearchTextResponseSectionsType0Item] | None | Unset = UNSET
  sections_omitted: int | None | Unset = UNSET
  terms: list[SearchTextResponseTermsType0Item] | None | Unset = UNSET
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.search_text_response_resolved_report_type_0 import (
      SearchTextResponseResolvedReportType0,
    )

    graph_id = self.graph_id

    query = self.query

    total = self.total

    text_chars = self.text_chars

    report_id: None | str | Unset
    if isinstance(self.report_id, Unset):
      report_id = UNSET
    else:
      report_id = self.report_id

    accession: None | str | Unset
    if isinstance(self.accession, Unset):
      accession = UNSET
    else:
      accession = self.accession

    resolved_report: dict[str, Any] | None | Unset
    if isinstance(self.resolved_report, Unset):
      resolved_report = UNSET
    elif isinstance(self.resolved_report, SearchTextResponseResolvedReportType0):
      resolved_report = self.resolved_report.to_dict()
    else:
      resolved_report = self.resolved_report

    hits: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.hits, Unset):
      hits = []
      for hits_item_data in self.hits:
        hits_item = hits_item_data.to_dict()
        hits.append(hits_item)

    text: None | str | Unset
    if isinstance(self.text, Unset):
      text = UNSET
    else:
      text = self.text

    sections: list[dict[str, Any]] | None | Unset
    if isinstance(self.sections, Unset):
      sections = UNSET
    elif isinstance(self.sections, list):
      sections = []
      for sections_type_0_item_data in self.sections:
        sections_type_0_item = sections_type_0_item_data.to_dict()
        sections.append(sections_type_0_item)

    else:
      sections = self.sections

    sections_omitted: int | None | Unset
    if isinstance(self.sections_omitted, Unset):
      sections_omitted = UNSET
    else:
      sections_omitted = self.sections_omitted

    terms: list[dict[str, Any]] | None | Unset
    if isinstance(self.terms, Unset):
      terms = UNSET
    elif isinstance(self.terms, list):
      terms = []
      for terms_type_0_item_data in self.terms:
        terms_type_0_item = terms_type_0_item_data.to_dict()
        terms.append(terms_type_0_item)

    else:
      terms = self.terms

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "query": query,
        "total": total,
        "text_chars": text_chars,
      }
    )
    if report_id is not UNSET:
      field_dict["report_id"] = report_id
    if accession is not UNSET:
      field_dict["accession"] = accession
    if resolved_report is not UNSET:
      field_dict["resolved_report"] = resolved_report
    if hits is not UNSET:
      field_dict["hits"] = hits
    if text is not UNSET:
      field_dict["text"] = text
    if sections is not UNSET:
      field_dict["sections"] = sections
    if sections_omitted is not UNSET:
      field_dict["sections_omitted"] = sections_omitted
    if terms is not UNSET:
      field_dict["terms"] = terms
    if note is not UNSET:
      field_dict["note"] = note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.search_text_response_hits_item import SearchTextResponseHitsItem
    from ..models.search_text_response_resolved_report_type_0 import (
      SearchTextResponseResolvedReportType0,
    )
    from ..models.search_text_response_sections_type_0_item import (
      SearchTextResponseSectionsType0Item,
    )
    from ..models.search_text_response_terms_type_0_item import (
      SearchTextResponseTermsType0Item,
    )

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    query = d.pop("query")

    total = d.pop("total")

    text_chars = d.pop("text_chars")

    def _parse_report_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    report_id = _parse_report_id(d.pop("report_id", UNSET))

    def _parse_accession(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    accession = _parse_accession(d.pop("accession", UNSET))

    def _parse_resolved_report(
      data: object,
    ) -> None | SearchTextResponseResolvedReportType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        resolved_report_type_0 = SearchTextResponseResolvedReportType0.from_dict(data)

        return resolved_report_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | SearchTextResponseResolvedReportType0 | Unset, data)

    resolved_report = _parse_resolved_report(d.pop("resolved_report", UNSET))

    _hits = d.pop("hits", UNSET)
    hits: list[SearchTextResponseHitsItem] | Unset = UNSET
    if _hits is not UNSET:
      hits = []
      for hits_item_data in _hits:
        hits_item = SearchTextResponseHitsItem.from_dict(hits_item_data)

        hits.append(hits_item)

    def _parse_text(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    text = _parse_text(d.pop("text", UNSET))

    def _parse_sections(
      data: object,
    ) -> list[SearchTextResponseSectionsType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        sections_type_0 = []
        _sections_type_0 = data
        for sections_type_0_item_data in _sections_type_0:
          sections_type_0_item = SearchTextResponseSectionsType0Item.from_dict(
            sections_type_0_item_data
          )

          sections_type_0.append(sections_type_0_item)

        return sections_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[SearchTextResponseSectionsType0Item] | None | Unset, data)

    sections = _parse_sections(d.pop("sections", UNSET))

    def _parse_sections_omitted(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    sections_omitted = _parse_sections_omitted(d.pop("sections_omitted", UNSET))

    def _parse_terms(
      data: object,
    ) -> list[SearchTextResponseTermsType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        terms_type_0 = []
        _terms_type_0 = data
        for terms_type_0_item_data in _terms_type_0:
          terms_type_0_item = SearchTextResponseTermsType0Item.from_dict(
            terms_type_0_item_data
          )

          terms_type_0.append(terms_type_0_item)

        return terms_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[SearchTextResponseTermsType0Item] | None | Unset, data)

    terms = _parse_terms(d.pop("terms", UNSET))

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    search_text_response = cls(
      graph_id=graph_id,
      query=query,
      total=total,
      text_chars=text_chars,
      report_id=report_id,
      accession=accession,
      resolved_report=resolved_report,
      hits=hits,
      text=text,
      sections=sections,
      sections_omitted=sections_omitted,
      terms=terms,
      note=note,
    )

    search_text_response.additional_properties = d
    return search_text_response

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
