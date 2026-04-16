from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upgrade_tier_op_new_tier import UpgradeTierOpNewTier

T = TypeVar("T", bound="UpgradeTierOp")


@_attrs_define
class UpgradeTierOp:
  """Body for the upgrade-tier operation.

  Attributes:
      new_tier (UpgradeTierOpNewTier): Target infrastructure tier
  """

  new_tier: UpgradeTierOpNewTier
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    new_tier = self.new_tier.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "new_tier": new_tier,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    new_tier = UpgradeTierOpNewTier(d.pop("new_tier"))

    upgrade_tier_op = cls(
      new_tier=new_tier,
    )

    upgrade_tier_op.additional_properties = d
    return upgrade_tier_op

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
