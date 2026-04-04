from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ClosingEntryResponse")


@_attrs_define
class ClosingEntryResponse:
  """
  Attributes:
      entry_id (str):
      status (str):
      posting_date (datetime.date):
      memo (str):
      debit_element_id (str):
      credit_element_id (str):
      amount (float):
  """

  entry_id: str
  status: str
  posting_date: datetime.date
  memo: str
  debit_element_id: str
  credit_element_id: str
  amount: float
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entry_id = self.entry_id

    status = self.status

    posting_date = self.posting_date.isoformat()

    memo = self.memo

    debit_element_id = self.debit_element_id

    credit_element_id = self.credit_element_id

    amount = self.amount

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entry_id": entry_id,
        "status": status,
        "posting_date": posting_date,
        "memo": memo,
        "debit_element_id": debit_element_id,
        "credit_element_id": credit_element_id,
        "amount": amount,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entry_id = d.pop("entry_id")

    status = d.pop("status")

    posting_date = isoparse(d.pop("posting_date")).date()

    memo = d.pop("memo")

    debit_element_id = d.pop("debit_element_id")

    credit_element_id = d.pop("credit_element_id")

    amount = d.pop("amount")

    closing_entry_response = cls(
      entry_id=entry_id,
      status=status,
      posting_date=posting_date,
      memo=memo,
      debit_element_id=debit_element_id,
      credit_element_id=credit_element_id,
      amount=amount,
    )

    closing_entry_response.additional_properties = d
    return closing_entry_response

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
