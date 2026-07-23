from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputedMetricLite")


@_attrs_define
class ComputedMetricLite:
  """One metric computed by a ``compute-metrics`` run.

  Attributes:
      rule_id (str): Derive rule that produced the value.
      element_id (str): Metric element the fact was written for.
      name (str): Metric display name.
      value (float): Computed value.
      unit (str): Fact unit — 'USD' for monetary, 'days' for days, else 'pure'.
      period_type (str): 'instant' or 'duration'.
      element_qname (None | str | Unset): Metric element qname (e.g. rs-metric:CurrentRatio).
      item_type (None | str | Unset): Format family from the metric element (monetary | ratio | percent | multiple |
          days). None means untyped; fall back to unit.
  """

  rule_id: str
  element_id: str
  name: str
  value: float
  unit: str
  period_type: str
  element_qname: None | str | Unset = UNSET
  item_type: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    rule_id = self.rule_id

    element_id = self.element_id

    name = self.name

    value = self.value

    unit = self.unit

    period_type = self.period_type

    element_qname: None | str | Unset
    if isinstance(self.element_qname, Unset):
      element_qname = UNSET
    else:
      element_qname = self.element_qname

    item_type: None | str | Unset
    if isinstance(self.item_type, Unset):
      item_type = UNSET
    else:
      item_type = self.item_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "rule_id": rule_id,
        "element_id": element_id,
        "name": name,
        "value": value,
        "unit": unit,
        "period_type": period_type,
      }
    )
    if element_qname is not UNSET:
      field_dict["element_qname"] = element_qname
    if item_type is not UNSET:
      field_dict["item_type"] = item_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    rule_id = d.pop("rule_id")

    element_id = d.pop("element_id")

    name = d.pop("name")

    value = d.pop("value")

    unit = d.pop("unit")

    period_type = d.pop("period_type")

    def _parse_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_qname = _parse_element_qname(d.pop("element_qname", UNSET))

    def _parse_item_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    item_type = _parse_item_type(d.pop("item_type", UNSET))

    computed_metric_lite = cls(
      rule_id=rule_id,
      element_id=element_id,
      name=name,
      value=value,
      unit=unit,
      period_type=period_type,
      element_qname=element_qname,
      item_type=item_type,
    )

    computed_metric_lite.additional_properties = d
    return computed_metric_lite

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
