from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordStatementBalanceRequest")


@_attrs_define
class RecordStatementBalanceRequest:
  """Record the ending balance of a statement for one account.

  Attributes:
      element_id (str): The balance-sheet account the statement is for (a chart-of-accounts element id).
      as_of (datetime.date): The statement's ending date.
      balance (float): The ending balance as the statement shows it, as a positive number in the account's normal
          direction: money in a bank account, or the amount owed on a loan or a card. Negative for the opposite, such as
          an overdrawn bank account.
      document_id (None | str | Unset): The statement itself, as a document already added with create-document. Kept
          on the record as evidence.
      note (None | str | Unset): Anything worth keeping with the recorded balance.
  """

  element_id: str
  as_of: datetime.date
  balance: float
  document_id: None | str | Unset = UNSET
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    as_of = self.as_of.isoformat()

    balance = self.balance

    document_id: None | str | Unset
    if isinstance(self.document_id, Unset):
      document_id = UNSET
    else:
      document_id = self.document_id

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "as_of": as_of,
        "balance": balance,
      }
    )
    if document_id is not UNSET:
      field_dict["document_id"] = document_id
    if note is not UNSET:
      field_dict["note"] = note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    as_of = datetime.date.fromisoformat(d.pop("as_of"))

    balance = d.pop("balance")

    def _parse_document_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    document_id = _parse_document_id(d.pop("document_id", UNSET))

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    record_statement_balance_request = cls(
      element_id=element_id,
      as_of=as_of,
      balance=balance,
      document_id=document_id,
      note=note,
    )

    record_statement_balance_request.additional_properties = d
    return record_statement_balance_request

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
