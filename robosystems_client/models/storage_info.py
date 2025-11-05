from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.storage_info_included_per_tier import StorageInfoIncludedPerTier
  from ..models.storage_info_overage_pricing import StorageInfoOveragePricing


T = TypeVar("T", bound="StorageInfo")


@_attrs_define
class StorageInfo:
  """Storage pricing information.

  Attributes:
      included_per_tier (StorageInfoIncludedPerTier): Storage included per tier in GB
      overage_pricing (StorageInfoOveragePricing): Overage pricing per GB per tier
  """

  included_per_tier: "StorageInfoIncludedPerTier"
  overage_pricing: "StorageInfoOveragePricing"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    included_per_tier = self.included_per_tier.to_dict()

    overage_pricing = self.overage_pricing.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "included_per_tier": included_per_tier,
        "overage_pricing": overage_pricing,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.storage_info_included_per_tier import StorageInfoIncludedPerTier
    from ..models.storage_info_overage_pricing import StorageInfoOveragePricing

    d = dict(src_dict)
    included_per_tier = StorageInfoIncludedPerTier.from_dict(d.pop("included_per_tier"))

    overage_pricing = StorageInfoOveragePricing.from_dict(d.pop("overage_pricing"))

    storage_info = cls(
      included_per_tier=included_per_tier,
      overage_pricing=overage_pricing,
    )

    storage_info.additional_properties = d
    return storage_info

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
