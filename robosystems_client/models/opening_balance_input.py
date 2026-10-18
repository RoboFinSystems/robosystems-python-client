from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpeningBalanceInput")


@_attrs_define
class OpeningBalanceInput:
  """One account's balance on the day the books begin, in its normal
  direction: an asset as a debit, a liability or equity account as a credit
  (a contra account the other way).

      Attributes:
          element_id (str): The balance-sheet account, by id.
          debit_amount (int | Unset): Debit balance in cents. Default: 0.
          credit_amount (int | Unset): Credit balance in cents. Default: 0.
  """

  element_id: str
  debit_amount: int | Unset = 0
  credit_amount: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    debit_amount = self.debit_amount

    credit_amount = self.credit_amount

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
      }
    )
    if debit_amount is not UNSET:
      field_dict["debit_amount"] = debit_amount
    if credit_amount is not UNSET:
      field_dict["credit_amount"] = credit_amount

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    debit_amount = d.pop("debit_amount", UNSET)

    credit_amount = d.pop("credit_amount", UNSET)

    opening_balance_input = cls(
      element_id=element_id,
      debit_amount=debit_amount,
      credit_amount=credit_amount,
    )

    opening_balance_input.additional_properties = d
    return opening_balance_input

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
