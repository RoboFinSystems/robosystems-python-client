from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportLineRow")


@_attrs_define
class ReportLineRow:
  """One line of a section, top to bottom.

  Attributes:
      concept (str): The line's concept qname.
      parent (None | str | Unset): The qname of the line this one sits under; omit for a top line.
      weight (float | None | Unset): Set to make the line a term of its parent's total: `1` adds, `-1` subtracts. The
          total is then checked against its terms.
  """

  concept: str
  parent: None | str | Unset = UNSET
  weight: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    concept = self.concept

    parent: None | str | Unset
    if isinstance(self.parent, Unset):
      parent = UNSET
    else:
      parent = self.parent

    weight: float | None | Unset
    if isinstance(self.weight, Unset):
      weight = UNSET
    else:
      weight = self.weight

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "concept": concept,
      }
    )
    if parent is not UNSET:
      field_dict["parent"] = parent
    if weight is not UNSET:
      field_dict["weight"] = weight

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    concept = d.pop("concept")

    def _parse_parent(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent = _parse_parent(d.pop("parent", UNSET))

    def _parse_weight(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    weight = _parse_weight(d.pop("weight", UNSET))

    report_line_row = cls(
      concept=concept,
      parent=parent,
      weight=weight,
    )

    report_line_row.additional_properties = d
    return report_line_row

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
