from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TransactionPreview")


@_attrs_define
class TransactionPreview:
  """A planned GL entry line from preview-event-block (no rows written).

  Attributes:
      entry_index (int):
      debit_element_id (str):
      credit_element_id (str):
      amount_cents (int):
      interpolated_debit_amount (str):
      interpolated_credit_amount (str):
  """

  entry_index: int
  debit_element_id: str
  credit_element_id: str
  amount_cents: int
  interpolated_debit_amount: str
  interpolated_credit_amount: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entry_index = self.entry_index

    debit_element_id = self.debit_element_id

    credit_element_id = self.credit_element_id

    amount_cents = self.amount_cents

    interpolated_debit_amount = self.interpolated_debit_amount

    interpolated_credit_amount = self.interpolated_credit_amount

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entry_index": entry_index,
        "debit_element_id": debit_element_id,
        "credit_element_id": credit_element_id,
        "amount_cents": amount_cents,
        "interpolated_debit_amount": interpolated_debit_amount,
        "interpolated_credit_amount": interpolated_credit_amount,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entry_index = d.pop("entry_index")

    debit_element_id = d.pop("debit_element_id")

    credit_element_id = d.pop("credit_element_id")

    amount_cents = d.pop("amount_cents")

    interpolated_debit_amount = d.pop("interpolated_debit_amount")

    interpolated_credit_amount = d.pop("interpolated_credit_amount")

    transaction_preview = cls(
      entry_index=entry_index,
      debit_element_id=debit_element_id,
      credit_element_id=credit_element_id,
      amount_cents=amount_cents,
      interpolated_debit_amount=interpolated_debit_amount,
      interpolated_credit_amount=interpolated_credit_amount,
    )

    transaction_preview.additional_properties = d
    return transaction_preview

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
