from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DischargeAllocation")


@_attrs_define
class DischargeAllocation:
  """How much of a payment went to one invoice or bill.

  Attributes:
      obligation_event_id (str): The `invoice_issued` or `bill_received` event it settles.
      amount (int): Positive cents of the payment applied to it.
  """

  obligation_event_id: str
  amount: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    obligation_event_id = self.obligation_event_id

    amount = self.amount

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "obligation_event_id": obligation_event_id,
        "amount": amount,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    obligation_event_id = d.pop("obligation_event_id")

    amount = d.pop("amount")

    discharge_allocation = cls(
      obligation_event_id=obligation_event_id,
      amount=amount,
    )

    discharge_allocation.additional_properties = d
    return discharge_allocation

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
