from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditSummaryResponse")


@_attrs_define
class CreditSummaryResponse:
  """Credit summary response model.

  Attributes:
      graph_id (str):
      graph_tier (str):
      current_balance (float):
      monthly_allocation (float):
      consumed_this_month (float):
      transaction_count (int):
      usage_percentage (float):
      last_allocation_date (Union[None, Unset, str]):
  """

  graph_id: str
  graph_tier: str
  current_balance: float
  monthly_allocation: float
  consumed_this_month: float
  transaction_count: int
  usage_percentage: float
  last_allocation_date: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    graph_tier = self.graph_tier

    current_balance = self.current_balance

    monthly_allocation = self.monthly_allocation

    consumed_this_month = self.consumed_this_month

    transaction_count = self.transaction_count

    usage_percentage = self.usage_percentage

    last_allocation_date: Union[None, Unset, str]
    if isinstance(self.last_allocation_date, Unset):
      last_allocation_date = UNSET
    else:
      last_allocation_date = self.last_allocation_date

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "graph_tier": graph_tier,
        "current_balance": current_balance,
        "monthly_allocation": monthly_allocation,
        "consumed_this_month": consumed_this_month,
        "transaction_count": transaction_count,
        "usage_percentage": usage_percentage,
      }
    )
    if last_allocation_date is not UNSET:
      field_dict["last_allocation_date"] = last_allocation_date

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    graph_tier = d.pop("graph_tier")

    current_balance = d.pop("current_balance")

    monthly_allocation = d.pop("monthly_allocation")

    consumed_this_month = d.pop("consumed_this_month")

    transaction_count = d.pop("transaction_count")

    usage_percentage = d.pop("usage_percentage")

    def _parse_last_allocation_date(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    last_allocation_date = _parse_last_allocation_date(
      d.pop("last_allocation_date", UNSET)
    )

    credit_summary_response = cls(
      graph_id=graph_id,
      graph_tier=graph_tier,
      current_balance=current_balance,
      monthly_allocation=monthly_allocation,
      consumed_this_month=consumed_this_month,
      transaction_count=transaction_count,
      usage_percentage=usage_percentage,
      last_allocation_date=last_allocation_date,
    )

    credit_summary_response.additional_properties = d
    return credit_summary_response

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
