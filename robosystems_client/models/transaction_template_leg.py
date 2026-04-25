from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TransactionTemplateLeg")


@_attrs_define
class TransactionTemplateLeg:
  """One side of a journal entry leg (debit or credit).

  Attributes:
      element_id (str): Element ULID (elem_ prefixed) identifying the account to post to
      amount (str): Amount expression. Supports: '{{ event.amount }}' — raw event amount (cents); '{{ event.amount }}
          / 2' — half of event amount; '{{ event.metadata.fee_cents }}' — field from event metadata
  """

  element_id: str
  amount: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    amount = self.amount

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "amount": amount,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    amount = d.pop("amount")

    transaction_template_leg = cls(
      element_id=element_id,
      amount=amount,
    )

    transaction_template_leg.additional_properties = d
    return transaction_template_leg

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
