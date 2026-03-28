from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MappingCoverageResponse")


@_attrs_define
class MappingCoverageResponse:
  """Coverage stats for a mapping.

  Attributes:
      mapping_id (str):
      total_coa_elements (int):
      mapped_count (int):
      unmapped_count (int):
      coverage_percent (float):
      high_confidence (int | Unset):  Default: 0.
      medium_confidence (int | Unset):  Default: 0.
      low_confidence (int | Unset):  Default: 0.
  """

  mapping_id: str
  total_coa_elements: int
  mapped_count: int
  unmapped_count: int
  coverage_percent: float
  high_confidence: int | Unset = 0
  medium_confidence: int | Unset = 0
  low_confidence: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    mapping_id = self.mapping_id

    total_coa_elements = self.total_coa_elements

    mapped_count = self.mapped_count

    unmapped_count = self.unmapped_count

    coverage_percent = self.coverage_percent

    high_confidence = self.high_confidence

    medium_confidence = self.medium_confidence

    low_confidence = self.low_confidence

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "mapping_id": mapping_id,
        "total_coa_elements": total_coa_elements,
        "mapped_count": mapped_count,
        "unmapped_count": unmapped_count,
        "coverage_percent": coverage_percent,
      }
    )
    if high_confidence is not UNSET:
      field_dict["high_confidence"] = high_confidence
    if medium_confidence is not UNSET:
      field_dict["medium_confidence"] = medium_confidence
    if low_confidence is not UNSET:
      field_dict["low_confidence"] = low_confidence

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    mapping_id = d.pop("mapping_id")

    total_coa_elements = d.pop("total_coa_elements")

    mapped_count = d.pop("mapped_count")

    unmapped_count = d.pop("unmapped_count")

    coverage_percent = d.pop("coverage_percent")

    high_confidence = d.pop("high_confidence", UNSET)

    medium_confidence = d.pop("medium_confidence", UNSET)

    low_confidence = d.pop("low_confidence", UNSET)

    mapping_coverage_response = cls(
      mapping_id=mapping_id,
      total_coa_elements=total_coa_elements,
      mapped_count=mapped_count,
      unmapped_count=unmapped_count,
      coverage_percent=coverage_percent,
      high_confidence=high_confidence,
      medium_confidence=medium_confidence,
      low_confidence=low_confidence,
    )

    mapping_coverage_response.additional_properties = d
    return mapping_coverage_response

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
