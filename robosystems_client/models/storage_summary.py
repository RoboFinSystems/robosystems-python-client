from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StorageSummary")


@_attrs_define
class StorageSummary:
  """Storage usage summary.

  Attributes:
      graph_tier (str): Subscription tier
      avg_storage_gb (float): Average storage in GB
      max_storage_gb (float): Peak storage in GB
      min_storage_gb (float): Minimum storage in GB
      total_gb_hours (float): Total GB-hours for billing
      measurement_count (int): Number of measurements taken
  """

  graph_tier: str
  avg_storage_gb: float
  max_storage_gb: float
  min_storage_gb: float
  total_gb_hours: float
  measurement_count: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_tier = self.graph_tier

    avg_storage_gb = self.avg_storage_gb

    max_storage_gb = self.max_storage_gb

    min_storage_gb = self.min_storage_gb

    total_gb_hours = self.total_gb_hours

    measurement_count = self.measurement_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_tier": graph_tier,
        "avg_storage_gb": avg_storage_gb,
        "max_storage_gb": max_storage_gb,
        "min_storage_gb": min_storage_gb,
        "total_gb_hours": total_gb_hours,
        "measurement_count": measurement_count,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_tier = d.pop("graph_tier")

    avg_storage_gb = d.pop("avg_storage_gb")

    max_storage_gb = d.pop("max_storage_gb")

    min_storage_gb = d.pop("min_storage_gb")

    total_gb_hours = d.pop("total_gb_hours")

    measurement_count = d.pop("measurement_count")

    storage_summary = cls(
      graph_tier=graph_tier,
      avg_storage_gb=avg_storage_gb,
      max_storage_gb=max_storage_gb,
      min_storage_gb=min_storage_gb,
      total_gb_hours=total_gb_hours,
      measurement_count=measurement_count,
    )

    storage_summary.additional_properties = d
    return storage_summary

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
