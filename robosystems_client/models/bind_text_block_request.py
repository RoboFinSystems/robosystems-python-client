from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BindTextBlockRequest")


@_attrs_define
class BindTextBlockRequest:
  """
  Attributes:
      document_id (str): Platform Document to bind (see list-documents).
      structure_id (str): Disclosure Structure the text block belongs to — must be block_type='regulatory_disclosure'
          with a text-block concept_arrangement (text_block / levelN_textblock).
      period_start (datetime.date): Reporting period start the narrative covers (duration fact).
      period_end (datetime.date): Reporting period end.
      section_id (None | str | Unset): Slugified heading id of one section to bind (the section ids search-documents
          returns); omit to bind the whole document.
      element_id (None | str | Unset): Disclosure element to tag the text to (id form).
      element_qname (None | str | Unset): Disclosure element qname (e.g.
          'acme:SignificantAccountingPoliciesTextBlock') — exactly one of element_id / element_qname.
      entity_id (None | str | Unset): Entity the fact belongs to; defaults to the primary entity.
  """

  document_id: str
  structure_id: str
  period_start: datetime.date
  period_end: datetime.date
  section_id: None | str | Unset = UNSET
  element_id: None | str | Unset = UNSET
  element_qname: None | str | Unset = UNSET
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    document_id = self.document_id

    structure_id = self.structure_id

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    section_id: None | str | Unset
    if isinstance(self.section_id, Unset):
      section_id = UNSET
    else:
      section_id = self.section_id

    element_id: None | str | Unset
    if isinstance(self.element_id, Unset):
      element_id = UNSET
    else:
      element_id = self.element_id

    element_qname: None | str | Unset
    if isinstance(self.element_qname, Unset):
      element_qname = UNSET
    else:
      element_qname = self.element_qname

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "document_id": document_id,
        "structure_id": structure_id,
        "period_start": period_start,
        "period_end": period_end,
      }
    )
    if section_id is not UNSET:
      field_dict["section_id"] = section_id
    if element_id is not UNSET:
      field_dict["element_id"] = element_id
    if element_qname is not UNSET:
      field_dict["element_qname"] = element_qname
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    document_id = d.pop("document_id")

    structure_id = d.pop("structure_id")

    period_start = datetime.date.fromisoformat(d.pop("period_start"))

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    def _parse_section_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    section_id = _parse_section_id(d.pop("section_id", UNSET))

    def _parse_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_id = _parse_element_id(d.pop("element_id", UNSET))

    def _parse_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_qname = _parse_element_qname(d.pop("element_qname", UNSET))

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    bind_text_block_request = cls(
      document_id=document_id,
      structure_id=structure_id,
      period_start=period_start,
      period_end=period_end,
      section_id=section_id,
      element_id=element_id,
      element_qname=element_qname,
      entity_id=entity_id,
    )

    bind_text_block_request.additional_properties = d
    return bind_text_block_request

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
