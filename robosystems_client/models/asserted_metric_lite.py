from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssertedMetricLite")


@_attrs_define
class AssertedMetricLite:
  """One metric written by an ``assert-metrics`` run.

  Attributes:
      element_id (str): Metric element the fact was written for.
      element_qname (str): Metric element qname.
      name (str): Metric display name.
      value (float): Asserted value.
      unit (str): Fact unit — 'USD' for monetary, 'days' for days, else 'pure'.
      period_type (str): 'instant' or 'duration'.
      item_type (None | str | Unset): Format family from the metric element (monetary | ratio | percent | multiple |
          days). None means untyped; fall back to unit.
  """

  element_id: str
  element_qname: str
  name: str
  value: float
  unit: str
  period_type: str
  item_type: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    element_qname = self.element_qname

    name = self.name

    value = self.value

    unit = self.unit

    period_type = self.period_type

    item_type: None | str | Unset
    if isinstance(self.item_type, Unset):
      item_type = UNSET
    else:
      item_type = self.item_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "element_qname": element_qname,
        "name": name,
        "value": value,
        "unit": unit,
        "period_type": period_type,
      }
    )
    if item_type is not UNSET:
      field_dict["item_type"] = item_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    element_qname = d.pop("element_qname")

    name = d.pop("name")

    value = d.pop("value")

    unit = d.pop("unit")

    period_type = d.pop("period_type")

    def _parse_item_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    item_type = _parse_item_type(d.pop("item_type", UNSET))

    asserted_metric_lite = cls(
      element_id=element_id,
      element_qname=element_qname,
      name=name,
      value=value,
      unit=unit,
      period_type=period_type,
      item_type=item_type,
    )

    asserted_metric_lite.additional_properties = d
    return asserted_metric_lite

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
