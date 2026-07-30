from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MetricObservation")


@_attrs_define
class MetricObservation:
  """One externally-observed value in an ``assert-metrics`` request.

  Attributes:
      qname (str): Metric element qname (e.g. rsx:GithubStars). Must resolve to a concept on the structure's
          presentation catalog.
      value (float): Observed value.
  """

  qname: str
  value: float
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    qname = self.qname

    value = self.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "qname": qname,
        "value": value,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    qname = d.pop("qname")

    value = d.pop("value")

    metric_observation = cls(
      qname=qname,
      value=value,
    )

    metric_observation.additional_properties = d
    return metric_observation

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
