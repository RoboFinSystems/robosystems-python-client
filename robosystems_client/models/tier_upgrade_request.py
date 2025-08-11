from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repository_plan import RepositoryPlan

T = TypeVar("T", bound="TierUpgradeRequest")


@_attrs_define
class TierUpgradeRequest:
  """Request to upgrade subscription tier.

  Attributes:
      new_plan (RepositoryPlan): Repository access plans for shared data.
  """

  new_plan: RepositoryPlan
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    new_plan = self.new_plan.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "new_plan": new_plan,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    new_plan = RepositoryPlan(d.pop("new_plan"))

    tier_upgrade_request = cls(
      new_plan=new_plan,
    )

    tier_upgrade_request.additional_properties = d
    return tier_upgrade_request

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
