from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

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
      reversal (ClosingEntryResponse | None | Unset):
  """

  entry_id: str
  status: str
  posting_date: datetime.date
  memo: str
  debit_element_id: str
  credit_element_id: str
  amount: float
  reversal: ClosingEntryResponse | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entry_id = self.entry_id

    status = self.status

    posting_date = self.posting_date.isoformat()

    memo = self.memo

    debit_element_id = self.debit_element_id

    credit_element_id = self.credit_element_id

    amount = self.amount

    reversal: dict[str, Any] | None | Unset
    if isinstance(self.reversal, Unset):
      reversal = UNSET
    elif isinstance(self.reversal, ClosingEntryResponse):
      reversal = self.reversal.to_dict()
    else:
      reversal = self.reversal

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
    if reversal is not UNSET:
      field_dict["reversal"] = reversal

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

    def _parse_reversal(data: object) -> ClosingEntryResponse | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        reversal_type_0 = ClosingEntryResponse.from_dict(data)

        return reversal_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(ClosingEntryResponse | None | Unset, data)

    reversal = _parse_reversal(d.pop("reversal", UNSET))

    closing_entry_response = cls(
      entry_id=entry_id,
      status=status,
      posting_date=posting_date,
      memo=memo,
      debit_element_id=debit_element_id,
      credit_element_id=credit_element_id,
      amount=amount,
      reversal=reversal,
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
