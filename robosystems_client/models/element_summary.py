from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ElementSummary")


@_attrs_define
class ElementSummary:
  """
  Attributes:
      count (int): Number of facts for this element
      min_ (float): Minimum value across the returned facts
      max_ (float): Maximum value across the returned facts
      total (float | None | Unset): Sum of values across the returned facts. Duration elements only — a balance summed
          across periods is not a balance, so instants omit it.
      average (float | None | Unset): Mean value across the returned facts. Duration elements only; omitted for
          instants.
  """

  count: int
  min_: float
  max_: float
  total: float | None | Unset = UNSET
  average: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    count = self.count

    min_ = self.min_

    max_ = self.max_

    total: float | None | Unset
    if isinstance(self.total, Unset):
      total = UNSET
    else:
      total = self.total

    average: float | None | Unset
    if isinstance(self.average, Unset):
      average = UNSET
    else:
      average = self.average

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "count": count,
        "min": min_,
        "max": max_,
      }
    )
    if total is not UNSET:
      field_dict["total"] = total
    if average is not UNSET:
      field_dict["average"] = average

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    count = d.pop("count")

    min_ = d.pop("min")

    max_ = d.pop("max")

    def _parse_total(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    total = _parse_total(d.pop("total", UNSET))

    def _parse_average(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    average = _parse_average(d.pop("average", UNSET))

    element_summary = cls(
      count=count,
      min_=min_,
      max_=max_,
      total=total,
      average=average,
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
