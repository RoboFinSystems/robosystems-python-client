from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RateLimits")


@_attrs_define
class RateLimits:
  """API rate limits.

  Attributes:
      requests_per_minute (int): Requests per minute limit
      requests_per_hour (int): Requests per hour limit
      burst_capacity (int): Burst capacity for short spikes
  """

  requests_per_minute: int
  requests_per_hour: int
  burst_capacity: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    requests_per_minute = self.requests_per_minute

    requests_per_hour = self.requests_per_hour

    burst_capacity = self.burst_capacity

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "requests_per_minute": requests_per_minute,
        "requests_per_hour": requests_per_hour,
        "burst_capacity": burst_capacity,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    requests_per_minute = d.pop("requests_per_minute")

    requests_per_hour = d.pop("requests_per_hour")

    burst_capacity = d.pop("burst_capacity")

    rate_limits = cls(
      requests_per_minute=requests_per_minute,
      requests_per_hour=requests_per_hour,
      burst_capacity=burst_capacity,
    )

    rate_limits.additional_properties = d
    return rate_limits

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
