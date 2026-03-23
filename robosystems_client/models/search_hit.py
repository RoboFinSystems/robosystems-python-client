from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchHit")


@_attrs_define
class SearchHit:
  """A single search result with snippet.

  Attributes:
      document_id (str):
      score (float):
      source_type (str):
      snippet (str):
      entity_ticker (None | str | Unset):
      entity_name (None | str | Unset):
      section_label (None | str | Unset):
      section_id (None | str | Unset):
      element_qname (None | str | Unset):
      filing_date (None | str | Unset):
      fiscal_year (int | None | Unset):
      form_type (None | str | Unset):
      xbrl_elements (list[str] | None | Unset):
      content_length (int | Unset):  Default: 0.
      content_url (None | str | Unset):
      document_title (None | str | Unset):
      tags (list[str] | None | Unset):
      folder (None | str | Unset):
  """

  document_id: str
  score: float
  source_type: str
  snippet: str
  entity_ticker: None | str | Unset = UNSET
  entity_name: None | str | Unset = UNSET
  section_label: None | str | Unset = UNSET
  section_id: None | str | Unset = UNSET
  element_qname: None | str | Unset = UNSET
  filing_date: None | str | Unset = UNSET
  fiscal_year: int | None | Unset = UNSET
  form_type: None | str | Unset = UNSET
  xbrl_elements: list[str] | None | Unset = UNSET
  content_length: int | Unset = 0
  content_url: None | str | Unset = UNSET
  document_title: None | str | Unset = UNSET
  tags: list[str] | None | Unset = UNSET
  folder: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    document_id = self.document_id

    score = self.score

    source_type = self.source_type

    snippet = self.snippet

    entity_ticker: None | str | Unset
    if isinstance(self.entity_ticker, Unset):
      entity_ticker = UNSET
    else:
      entity_ticker = self.entity_ticker

    entity_name: None | str | Unset
    if isinstance(self.entity_name, Unset):
      entity_name = UNSET
    else:
      entity_name = self.entity_name

    section_label: None | str | Unset
    if isinstance(self.section_label, Unset):
      section_label = UNSET
    else:
      section_label = self.section_label

    section_id: None | str | Unset
    if isinstance(self.section_id, Unset):
      section_id = UNSET
    else:
      section_id = self.section_id

    element_qname: None | str | Unset
    if isinstance(self.element_qname, Unset):
      element_qname = UNSET
    else:
      element_qname = self.element_qname

    filing_date: None | str | Unset
    if isinstance(self.filing_date, Unset):
      filing_date = UNSET
    else:
      filing_date = self.filing_date

    fiscal_year: int | None | Unset
    if isinstance(self.fiscal_year, Unset):
      fiscal_year = UNSET
    else:
      fiscal_year = self.fiscal_year

    form_type: None | str | Unset
    if isinstance(self.form_type, Unset):
      form_type = UNSET
    else:
      form_type = self.form_type

    xbrl_elements: list[str] | None | Unset
    if isinstance(self.xbrl_elements, Unset):
      xbrl_elements = UNSET
    elif isinstance(self.xbrl_elements, list):
      xbrl_elements = self.xbrl_elements

    else:
      xbrl_elements = self.xbrl_elements

    content_length = self.content_length

    content_url: None | str | Unset
    if isinstance(self.content_url, Unset):
      content_url = UNSET
    else:
      content_url = self.content_url

    document_title: None | str | Unset
    if isinstance(self.document_title, Unset):
      document_title = UNSET
    else:
      document_title = self.document_title

    tags: list[str] | None | Unset
    if isinstance(self.tags, Unset):
      tags = UNSET
    elif isinstance(self.tags, list):
      tags = self.tags

    else:
      tags = self.tags

    folder: None | str | Unset
    if isinstance(self.folder, Unset):
      folder = UNSET
    else:
      folder = self.folder

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "document_id": document_id,
        "score": score,
        "source_type": source_type,
        "snippet": snippet,
      }
    )
    if entity_ticker is not UNSET:
      field_dict["entity_ticker"] = entity_ticker
    if entity_name is not UNSET:
      field_dict["entity_name"] = entity_name
    if section_label is not UNSET:
      field_dict["section_label"] = section_label
    if section_id is not UNSET:
      field_dict["section_id"] = section_id
    if element_qname is not UNSET:
      field_dict["element_qname"] = element_qname
    if filing_date is not UNSET:
      field_dict["filing_date"] = filing_date
    if fiscal_year is not UNSET:
      field_dict["fiscal_year"] = fiscal_year
    if form_type is not UNSET:
      field_dict["form_type"] = form_type
    if xbrl_elements is not UNSET:
      field_dict["xbrl_elements"] = xbrl_elements
    if content_length is not UNSET:
      field_dict["content_length"] = content_length
    if content_url is not UNSET:
      field_dict["content_url"] = content_url
    if document_title is not UNSET:
      field_dict["document_title"] = document_title
    if tags is not UNSET:
      field_dict["tags"] = tags
    if folder is not UNSET:
      field_dict["folder"] = folder

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    document_id = d.pop("document_id")

    score = d.pop("score")

    source_type = d.pop("source_type")

    snippet = d.pop("snippet")

    def _parse_entity_ticker(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_ticker = _parse_entity_ticker(d.pop("entity_ticker", UNSET))

    def _parse_entity_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_name = _parse_entity_name(d.pop("entity_name", UNSET))

    def _parse_section_label(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    section_label = _parse_section_label(d.pop("section_label", UNSET))

    def _parse_section_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    section_id = _parse_section_id(d.pop("section_id", UNSET))

    def _parse_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_qname = _parse_element_qname(d.pop("element_qname", UNSET))

    def _parse_filing_date(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    filing_date = _parse_filing_date(d.pop("filing_date", UNSET))

    def _parse_fiscal_year(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    fiscal_year = _parse_fiscal_year(d.pop("fiscal_year", UNSET))

    def _parse_form_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    form_type = _parse_form_type(d.pop("form_type", UNSET))

    def _parse_xbrl_elements(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        xbrl_elements_type_0 = cast(list[str], data)

        return xbrl_elements_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    xbrl_elements = _parse_xbrl_elements(d.pop("xbrl_elements", UNSET))

    content_length = d.pop("content_length", UNSET)

    def _parse_content_url(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    content_url = _parse_content_url(d.pop("content_url", UNSET))

    def _parse_document_title(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    document_title = _parse_document_title(d.pop("document_title", UNSET))

    def _parse_tags(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        tags_type_0 = cast(list[str], data)

        return tags_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    tags = _parse_tags(d.pop("tags", UNSET))

    def _parse_folder(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    folder = _parse_folder(d.pop("folder", UNSET))

    search_hit = cls(
      document_id=document_id,
      score=score,
      source_type=source_type,
      snippet=snippet,
      entity_ticker=entity_ticker,
      entity_name=entity_name,
      section_label=section_label,
      section_id=section_id,
      element_qname=element_qname,
      filing_date=filing_date,
      fiscal_year=fiscal_year,
      form_type=form_type,
      xbrl_elements=xbrl_elements,
      content_length=content_length,
      content_url=content_url,
      document_title=document_title,
      tags=tags,
      folder=folder,
    )

    search_hit.additional_properties = d
    return search_hit

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
