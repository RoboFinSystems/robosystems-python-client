from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ElementSummary")


@_attrs_define
class ElementSummary:
  """
  Attributes:
      count (int): Number of facts for this element
      total (float): Sum of values across the returned facts
      average (float): Mean value across the returned facts
      min_ (float): Minimum value across the returned facts
      max_ (float): Maximum value across the returned facts
  """

  count: int
  total: float
  average: float
  min_: float
  max_: float
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    count = self.count

    total = self.total

    average = self.average

    min_ = self.min_

    max_ = self.max_

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "count": count,
        "total": total,
        "average": average,
        "min": min_,
        "max": max_,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    count = d.pop("count")

    total = d.pop("total")

    average = d.pop("average")

    min_ = d.pop("min")

    max_ = d.pop("max")

    element_summary = cls(
      count=count,
      total=total,
      average=average,
      min_=min_,
      max_=max_,
    )

    element_summary.additional_properties = d
    return element_summary

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
