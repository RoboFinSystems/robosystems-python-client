from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddOnCreditInfo")


@_attrs_define
class AddOnCreditInfo:
  """Credit information for a specific add-on.

  Attributes:
      subscription_id (str): Subscription ID
      addon_type (str): Add-on type (e.g., sec_data)
      name (str): Display name of the add-on
      tier (str): Subscription tier
      credits_remaining (float): Credits remaining
      credits_allocated (float): Monthly credit allocation
      credits_consumed (float): Credits consumed this month
      rollover_amount (Union[Unset, float]): Credits rolled over from previous month Default: 0.0.
  """

  subscription_id: str
  addon_type: str
  name: str
  tier: str
  credits_remaining: float
  credits_allocated: float
  credits_consumed: float
  rollover_amount: Union[Unset, float] = 0.0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    subscription_id = self.subscription_id

    addon_type = self.addon_type

    name = self.name

    tier = self.tier

    credits_remaining = self.credits_remaining

    credits_allocated = self.credits_allocated

    credits_consumed = self.credits_consumed

    rollover_amount = self.rollover_amount

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "subscription_id": subscription_id,
        "addon_type": addon_type,
        "name": name,
        "tier": tier,
        "credits_remaining": credits_remaining,
        "credits_allocated": credits_allocated,
        "credits_consumed": credits_consumed,
      }
    )
    if rollover_amount is not UNSET:
      field_dict["rollover_amount"] = rollover_amount

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    subscription_id = d.pop("subscription_id")

    addon_type = d.pop("addon_type")

    name = d.pop("name")

    tier = d.pop("tier")

    credits_remaining = d.pop("credits_remaining")

    credits_allocated = d.pop("credits_allocated")

    credits_consumed = d.pop("credits_consumed")

    rollover_amount = d.pop("rollover_amount", UNSET)

    add_on_credit_info = cls(
      subscription_id=subscription_id,
      addon_type=addon_type,
      name=name,
      tier=tier,
      credits_remaining=credits_remaining,
      credits_allocated=credits_allocated,
      credits_consumed=credits_consumed,
      rollover_amount=rollover_amount,
    )

    add_on_credit_info.additional_properties = d
    return add_on_credit_info

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
