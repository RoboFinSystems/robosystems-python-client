from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreditLimits")


@_attrs_define
class CreditLimits:
  """AI credit limits (optional).

  Attributes:
      monthly_ai_credits (int): Monthly AI credits allocation
      current_balance (int): Current credit balance
      storage_billing_enabled (bool): Whether storage billing is enabled
      storage_rate_per_gb_per_day (int): Storage billing rate per GB per day
  """

  monthly_ai_credits: int
  current_balance: int
  storage_billing_enabled: bool
  storage_rate_per_gb_per_day: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    monthly_ai_credits = self.monthly_ai_credits

    current_balance = self.current_balance

    storage_billing_enabled = self.storage_billing_enabled

    storage_rate_per_gb_per_day = self.storage_rate_per_gb_per_day

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "monthly_ai_credits": monthly_ai_credits,
        "current_balance": current_balance,
        "storage_billing_enabled": storage_billing_enabled,
        "storage_rate_per_gb_per_day": storage_rate_per_gb_per_day,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    monthly_ai_credits = d.pop("monthly_ai_credits")

    current_balance = d.pop("current_balance")

    storage_billing_enabled = d.pop("storage_billing_enabled")

    storage_rate_per_gb_per_day = d.pop("storage_rate_per_gb_per_day")

    credit_limits = cls(
      monthly_ai_credits=monthly_ai_credits,
      current_balance=current_balance,
      storage_billing_enabled=storage_billing_enabled,
      storage_rate_per_gb_per_day=storage_rate_per_gb_per_day,
    )

    credit_limits.additional_properties = d
    return credit_limits

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
