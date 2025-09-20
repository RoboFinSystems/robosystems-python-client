from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditSummary")


@_attrs_define
class CreditSummary:
  """Credit balance summary.

  Attributes:
      current_balance (float): Current credit balance
      monthly_allocation (float): Monthly credit allocation
      consumed_this_month (float): Credits consumed this month
      usage_percentage (float): Usage percentage of monthly allocation
      rollover_credits (float): Credits rolled over from previous month
      allows_rollover (bool): Whether rollover is allowed
      is_active (bool): Whether credit pool is active
      last_allocation_date (Union[None, Unset, str]): Last allocation date (ISO format)
      next_allocation_date (Union[None, Unset, str]): Next allocation date (ISO format)
  """

  current_balance: float
  monthly_allocation: float
  consumed_this_month: float
  usage_percentage: float
  rollover_credits: float
  allows_rollover: bool
  is_active: bool
  last_allocation_date: Union[None, Unset, str] = UNSET
  next_allocation_date: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    current_balance = self.current_balance

    monthly_allocation = self.monthly_allocation

    consumed_this_month = self.consumed_this_month

    usage_percentage = self.usage_percentage

    rollover_credits = self.rollover_credits

    allows_rollover = self.allows_rollover

    is_active = self.is_active

    last_allocation_date: Union[None, Unset, str]
    if isinstance(self.last_allocation_date, Unset):
      last_allocation_date = UNSET
    else:
      last_allocation_date = self.last_allocation_date

    next_allocation_date: Union[None, Unset, str]
    if isinstance(self.next_allocation_date, Unset):
      next_allocation_date = UNSET
    else:
      next_allocation_date = self.next_allocation_date

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "current_balance": current_balance,
        "monthly_allocation": monthly_allocation,
        "consumed_this_month": consumed_this_month,
        "usage_percentage": usage_percentage,
        "rollover_credits": rollover_credits,
        "allows_rollover": allows_rollover,
        "is_active": is_active,
      }
    )
    if last_allocation_date is not UNSET:
      field_dict["last_allocation_date"] = last_allocation_date
    if next_allocation_date is not UNSET:
      field_dict["next_allocation_date"] = next_allocation_date

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    current_balance = d.pop("current_balance")

    monthly_allocation = d.pop("monthly_allocation")

    consumed_this_month = d.pop("consumed_this_month")

    usage_percentage = d.pop("usage_percentage")

    rollover_credits = d.pop("rollover_credits")

    allows_rollover = d.pop("allows_rollover")

    is_active = d.pop("is_active")

    def _parse_last_allocation_date(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    last_allocation_date = _parse_last_allocation_date(
      d.pop("last_allocation_date", UNSET)
    )

    def _parse_next_allocation_date(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    next_allocation_date = _parse_next_allocation_date(
      d.pop("next_allocation_date", UNSET)
    )

    credit_summary = cls(
      current_balance=current_balance,
      monthly_allocation=monthly_allocation,
      consumed_this_month=consumed_this_month,
      usage_percentage=usage_percentage,
      rollover_credits=rollover_credits,
      allows_rollover=allows_rollover,
      is_active=is_active,
      last_allocation_date=last_allocation_date,
      next_allocation_date=next_allocation_date,
    )

    credit_summary.additional_properties = d
    return credit_summary

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
