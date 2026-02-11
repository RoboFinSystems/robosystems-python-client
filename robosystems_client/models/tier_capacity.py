from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TierCapacity")


@_attrs_define
class TierCapacity:
  """Capacity status for a single tier.

  Attributes:
      tier (str): Tier identifier (e.g. ladybug-standard)
      display_name (str): Human-readable tier name
      status (str): Capacity status: ready, scalable, or at_capacity
      message (str): Human-readable status message for frontend display
  """

  tier: str
  display_name: str
  status: str
  message: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    tier = self.tier

    display_name = self.display_name

    status = self.status

    message = self.message

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "tier": tier,
        "display_name": display_name,
        "status": status,
        "message": message,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    tier = d.pop("tier")

    display_name = d.pop("display_name")

    status = d.pop("status")

    message = d.pop("message")

    tier_capacity = cls(
      tier=tier,
      display_name=display_name,
      status=status,
      message=message,
    )

    tier_capacity.additional_properties = d
    return tier_capacity

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
