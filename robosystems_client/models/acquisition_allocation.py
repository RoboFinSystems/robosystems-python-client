from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AcquisitionAllocation")


@_attrs_define
class AcquisitionAllocation:
  """Part of an acquisition's excess assigned to an identifiable asset or
  liability at fair value instead of goodwill: a step-up.

      Attributes:
          concept (str): The rs-gaap concept stepped up, e.g. `rs-gaap:PropertyPlantAndEquipmentNet`; the consolidation
              entity needs an account mapped to it.
          amount (int): Cents, debit-positive: fair value less book value at acquisition. Positive raises an asset;
              negative raises a liability.
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

    acquisition_allocation = cls(
      concept=concept,
      amount=amount,
    )

    acquisition_allocation.additional_properties = d
    return acquisition_allocation

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
