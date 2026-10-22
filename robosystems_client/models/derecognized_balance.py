from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DerecognizedBalance")


@_attrs_define
class DerecognizedBalance:
  """A balance the consolidation entity held for a member that left, taken
  off by the deconsolidation.

      Attributes:
          concept (str): The rs-gaap concept.
          amount (int): Cents as held: positive a debit (goodwill, a step-up), negative a credit (the outside owners'
              interest, the price above book of the parent's investment).
  """

  concept: str
  amount: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    concept = self.concept

    amount = self.amount

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "concept": concept,
        "amount": amount,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    concept = d.pop("concept")

    amount = d.pop("amount")

    derecognized_balance = cls(
      concept=concept,
      amount=amount,
    )

    derecognized_balance.additional_properties = d
    return derecognized_balance

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
