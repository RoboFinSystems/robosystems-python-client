from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FactDetail")


@_attrs_define
class FactDetail:
  """
  Attributes:
      fact_id (str):
      element_uri (str):
      element_name (str):
      numeric_value (float):
      unit (str):
      period_start (str):
      period_end (str):
  """

  fact_id: str
  element_uri: str
  element_name: str
  numeric_value: float
  unit: str
  period_start: str
  period_end: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    fact_id = self.fact_id

    element_uri = self.element_uri

    element_name = self.element_name

    numeric_value = self.numeric_value

    unit = self.unit

    period_start = self.period_start

    period_end = self.period_end

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "fact_id": fact_id,
        "element_uri": element_uri,
        "element_name": element_name,
        "numeric_value": numeric_value,
        "unit": unit,
        "period_start": period_start,
        "period_end": period_end,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    fact_id = d.pop("fact_id")

    element_uri = d.pop("element_uri")

    element_name = d.pop("element_name")

    numeric_value = d.pop("numeric_value")

    unit = d.pop("unit")

    period_start = d.pop("period_start")

    period_end = d.pop("period_end")

    fact_detail = cls(
      fact_id=fact_id,
      element_uri=element_uri,
      element_name=element_name,
      numeric_value=numeric_value,
      unit=unit,
      period_start=period_start,
      period_end=period_end,
    )

    fact_detail.additional_properties = d
    return fact_detail

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
