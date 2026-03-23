from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
  """Request model for document search.

  Attributes:
      query (str): Search query
      entity (None | str | Unset): Filter by ticker, CIK, or entity name
      form_type (None | str | Unset): Filter by SEC form type (10-K, 10-Q)
      section (None | str | Unset): Filter by section ID (item_1, item_1a, item_7, etc.)
      element (None | str | Unset): Filter by XBRL element qname (e.g., us-gaap:Goodwill)
      source_type (None | str | Unset): Filter by source type (xbrl_textblock, narrative_section, ixbrl_disclosure,
          uploaded_doc, memory)
      fiscal_year (int | None | Unset): Filter by fiscal year
      date_from (None | str | Unset): Filter filings on or after date (YYYY-MM-DD)
      date_to (None | str | Unset): Filter filings on or before date (YYYY-MM-DD)
      semantic (bool | Unset): Enable semantic (vector) search if available Default: False.
      size (int | Unset): Max results to return Default: 10.
      offset (int | Unset): Pagination offset Default: 0.
  """

  query: str
  entity: None | str | Unset = UNSET
  form_type: None | str | Unset = UNSET
  section: None | str | Unset = UNSET
  element: None | str | Unset = UNSET
  source_type: None | str | Unset = UNSET
  fiscal_year: int | None | Unset = UNSET
  date_from: None | str | Unset = UNSET
  date_to: None | str | Unset = UNSET
  semantic: bool | Unset = False
  size: int | Unset = 10
  offset: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    query = self.query

    entity: None | str | Unset
    if isinstance(self.entity, Unset):
      entity = UNSET
    else:
      entity = self.entity

    form_type: None | str | Unset
    if isinstance(self.form_type, Unset):
      form_type = UNSET
    else:
      form_type = self.form_type

    section: None | str | Unset
    if isinstance(self.section, Unset):
      section = UNSET
    else:
      section = self.section

    element: None | str | Unset
    if isinstance(self.element, Unset):
      element = UNSET
    else:
      element = self.element

    source_type: None | str | Unset
    if isinstance(self.source_type, Unset):
      source_type = UNSET
    else:
      source_type = self.source_type

    fiscal_year: int | None | Unset
    if isinstance(self.fiscal_year, Unset):
      fiscal_year = UNSET
    else:
      fiscal_year = self.fiscal_year

    date_from: None | str | Unset
    if isinstance(self.date_from, Unset):
      date_from = UNSET
    else:
      date_from = self.date_from

    date_to: None | str | Unset
    if isinstance(self.date_to, Unset):
      date_to = UNSET
    else:
      date_to = self.date_to

    semantic = self.semantic

    size = self.size

    offset = self.offset

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "query": query,
      }
    )
    if entity is not UNSET:
      field_dict["entity"] = entity
    if form_type is not UNSET:
      field_dict["form_type"] = form_type
    if section is not UNSET:
      field_dict["section"] = section
    if element is not UNSET:
      field_dict["element"] = element
    if source_type is not UNSET:
      field_dict["source_type"] = source_type
    if fiscal_year is not UNSET:
      field_dict["fiscal_year"] = fiscal_year
    if date_from is not UNSET:
      field_dict["date_from"] = date_from
    if date_to is not UNSET:
      field_dict["date_to"] = date_to
    if semantic is not UNSET:
      field_dict["semantic"] = semantic
    if size is not UNSET:
      field_dict["size"] = size
    if offset is not UNSET:
      field_dict["offset"] = offset

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    query = d.pop("query")

    def _parse_entity(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity = _parse_entity(d.pop("entity", UNSET))

    def _parse_form_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    form_type = _parse_form_type(d.pop("form_type", UNSET))

    def _parse_section(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    section = _parse_section(d.pop("section", UNSET))

    def _parse_element(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element = _parse_element(d.pop("element", UNSET))

    def _parse_source_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_type = _parse_source_type(d.pop("source_type", UNSET))

    def _parse_fiscal_year(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    fiscal_year = _parse_fiscal_year(d.pop("fiscal_year", UNSET))

    def _parse_date_from(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    date_from = _parse_date_from(d.pop("date_from", UNSET))

    def _parse_date_to(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    date_to = _parse_date_to(d.pop("date_to", UNSET))

    semantic = d.pop("semantic", UNSET)

    size = d.pop("size", UNSET)

    offset = d.pop("offset", UNSET)

    search_request = cls(
      query=query,
      entity=entity,
      form_type=form_type,
      section=section,
      element=element,
      source_type=source_type,
      fiscal_year=fiscal_year,
      date_from=date_from,
      date_to=date_to,
      semantic=semantic,
      size=size,
      offset=offset,
    )

    search_request.additional_properties = d
    return search_request

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
