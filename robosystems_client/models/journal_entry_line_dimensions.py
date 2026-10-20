from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JournalEntryLineDimensions")


@_attrs_define
class JournalEntryLineDimensions:
  """A line's management dimension members, set in place.

  Attributes:
      line_id (str): The line to re-tag, by id.
      dimension_ids (list[str]): The members the line carries from now on, replacing what it carried; empty clears
          them. At most one per axis.
  """

  line_id: str
  dimension_ids: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    line_id = self.line_id

    dimension_ids = self.dimension_ids

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "line_id": line_id,
        "dimension_ids": dimension_ids,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    line_id = d.pop("line_id")

    dimension_ids = cast(list[str], d.pop("dimension_ids"))

    journal_entry_line_dimensions = cls(
      line_id=line_id,
      dimension_ids=dimension_ids,
    )

    journal_entry_line_dimensions.additional_properties = d
    return journal_entry_line_dimensions

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
