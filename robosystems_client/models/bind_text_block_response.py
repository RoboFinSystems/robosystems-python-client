from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BindTextBlockResponse")


@_attrs_define
class BindTextBlockResponse:
  """
  Attributes:
      fact_id (str): The Nonnumeric Fact created.
      fact_set_id (str): Standing 'disclosure' FactSet holding the fact.
      structure_id (str):
      element_id (str):
      document_id (str):
      content_hash (str): Full sha256 hex of the bound text (drift signal).
      characters (int): Length of the bound text.
      period_start (datetime.date):
      period_end (datetime.date):
      replaced (bool): True when a re-bind replaced this element's existing fact in the standing FactSet (content and
          provenance refreshed).
      section_id (None | str | Unset):
  """

  fact_id: str
  fact_set_id: str
  structure_id: str
  element_id: str
  document_id: str
  content_hash: str
  characters: int
  period_start: datetime.date
  period_end: datetime.date
  replaced: bool
  section_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    fact_id = self.fact_id

    fact_set_id = self.fact_set_id

    structure_id = self.structure_id

    element_id = self.element_id

    document_id = self.document_id

    content_hash = self.content_hash

    characters = self.characters

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    replaced = self.replaced

    section_id: None | str | Unset
    if isinstance(self.section_id, Unset):
      section_id = UNSET
    else:
      section_id = self.section_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "fact_id": fact_id,
        "fact_set_id": fact_set_id,
        "structure_id": structure_id,
        "element_id": element_id,
        "document_id": document_id,
        "content_hash": content_hash,
        "characters": characters,
        "period_start": period_start,
        "period_end": period_end,
        "replaced": replaced,
      }
    )
    if section_id is not UNSET:
      field_dict["section_id"] = section_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    fact_id = d.pop("fact_id")

    fact_set_id = d.pop("fact_set_id")

    structure_id = d.pop("structure_id")

    element_id = d.pop("element_id")

    document_id = d.pop("document_id")

    content_hash = d.pop("content_hash")

    characters = d.pop("characters")

    period_start = datetime.date.fromisoformat(d.pop("period_start"))

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    replaced = d.pop("replaced")

    def _parse_section_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    section_id = _parse_section_id(d.pop("section_id", UNSET))

    bind_text_block_response = cls(
      fact_id=fact_id,
      fact_set_id=fact_set_id,
      structure_id=structure_id,
      element_id=element_id,
      document_id=document_id,
      content_hash=content_hash,
      characters=characters,
      period_start=period_start,
      period_end=period_end,
      replaced=replaced,
      section_id=section_id,
    )

    bind_text_block_response.additional_properties = d
    return bind_text_block_response

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
