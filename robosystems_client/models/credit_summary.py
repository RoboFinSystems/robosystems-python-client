from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.credit_summary_operation_breakdown import (
    CreditSummaryOperationBreakdown,
  )


T = TypeVar("T", bound="CreditSummary")


@_attrs_define
class CreditSummary:
  """Credit consumption summary.

  Attributes:
      graph_tier (str): Subscription tier
      total_credits_consumed (float): Total credits consumed
      total_base_cost (float): Total base cost before multipliers
      operation_breakdown (CreditSummaryOperationBreakdown): Credit usage by operation type
      cached_operations (int): Number of cached operations
      billable_operations (int): Number of billable operations
      transaction_count (int): Total transaction count
  """

  graph_tier: str
  total_credits_consumed: float
  total_base_cost: float
  operation_breakdown: "CreditSummaryOperationBreakdown"
  cached_operations: int
  billable_operations: int
  transaction_count: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_tier = self.graph_tier

    total_credits_consumed = self.total_credits_consumed

    total_base_cost = self.total_base_cost

    operation_breakdown = self.operation_breakdown.to_dict()

    cached_operations = self.cached_operations

    billable_operations = self.billable_operations

    transaction_count = self.transaction_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_tier": graph_tier,
        "total_credits_consumed": total_credits_consumed,
        "total_base_cost": total_base_cost,
        "operation_breakdown": operation_breakdown,
        "cached_operations": cached_operations,
        "billable_operations": billable_operations,
        "transaction_count": transaction_count,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.credit_summary_operation_breakdown import (
      CreditSummaryOperationBreakdown,
    )

    d = dict(src_dict)
    graph_tier = d.pop("graph_tier")

    total_credits_consumed = d.pop("total_credits_consumed")

    total_base_cost = d.pop("total_base_cost")

    operation_breakdown = CreditSummaryOperationBreakdown.from_dict(
      d.pop("operation_breakdown")
    )

    cached_operations = d.pop("cached_operations")

    billable_operations = d.pop("billable_operations")

    transaction_count = d.pop("transaction_count")

    credit_summary = cls(
      graph_tier=graph_tier,
      total_credits_consumed=total_credits_consumed,
      total_base_cost=total_base_cost,
      operation_breakdown=operation_breakdown,
      cached_operations=cached_operations,
      billable_operations=billable_operations,
      transaction_count=transaction_count,
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
