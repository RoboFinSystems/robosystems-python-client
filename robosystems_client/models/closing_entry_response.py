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
      outcome (str): What the idempotent call did: 'created' (new draft), 'unchanged' (existing draft still matches),
          'regenerated' (stale draft replaced with fresh one), 'removed' (stale draft deleted; schedule no longer covers
          this period), 'skipped' (nothing to do — no draft and no in-scope fact).
      entry_id (None | str | Unset): The draft entry ID. None for 'removed' and 'skipped' outcomes.
      status (None | str | Unset): Entry status (always 'draft' when present).
      posting_date (datetime.date | None | Unset):
      memo (None | str | Unset):
      debit_element_id (None | str | Unset):
      credit_element_id (None | str | Unset):
      amount (float | None | Unset): Entry amount in dollars. None for 'removed' and 'skipped'.
      reason (None | str | Unset): Explanation for 'removed' and 'skipped' outcomes.
      reversal (ClosingEntryResponse | None | Unset):
  """

  outcome: str
  entry_id: None | str | Unset = UNSET
  status: None | str | Unset = UNSET
  posting_date: datetime.date | None | Unset = UNSET
  memo: None | str | Unset = UNSET
  debit_element_id: None | str | Unset = UNSET
  credit_element_id: None | str | Unset = UNSET
  amount: float | None | Unset = UNSET
  reason: None | str | Unset = UNSET
  reversal: ClosingEntryResponse | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    outcome = self.outcome

    entry_id: None | str | Unset
    if isinstance(self.entry_id, Unset):
      entry_id = UNSET
    else:
      entry_id = self.entry_id

    status: None | str | Unset
    if isinstance(self.status, Unset):
      status = UNSET
    else:
      status = self.status

    posting_date: None | str | Unset
    if isinstance(self.posting_date, Unset):
      posting_date = UNSET
    elif isinstance(self.posting_date, datetime.date):
      posting_date = self.posting_date.isoformat()
    else:
      posting_date = self.posting_date

    memo: None | str | Unset
    if isinstance(self.memo, Unset):
      memo = UNSET
    else:
      memo = self.memo

    debit_element_id: None | str | Unset
    if isinstance(self.debit_element_id, Unset):
      debit_element_id = UNSET
    else:
      debit_element_id = self.debit_element_id

    credit_element_id: None | str | Unset
    if isinstance(self.credit_element_id, Unset):
      credit_element_id = UNSET
    else:
      credit_element_id = self.credit_element_id

    amount: float | None | Unset
    if isinstance(self.amount, Unset):
      amount = UNSET
    else:
      amount = self.amount

    reason: None | str | Unset
    if isinstance(self.reason, Unset):
      reason = UNSET
    else:
      reason = self.reason

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
        "outcome": outcome,
      }
    )
    if entry_id is not UNSET:
      field_dict["entry_id"] = entry_id
    if status is not UNSET:
      field_dict["status"] = status
    if posting_date is not UNSET:
      field_dict["posting_date"] = posting_date
    if memo is not UNSET:
      field_dict["memo"] = memo
    if debit_element_id is not UNSET:
      field_dict["debit_element_id"] = debit_element_id
    if credit_element_id is not UNSET:
      field_dict["credit_element_id"] = credit_element_id
    if amount is not UNSET:
      field_dict["amount"] = amount
    if reason is not UNSET:
      field_dict["reason"] = reason
    if reversal is not UNSET:
      field_dict["reversal"] = reversal

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    outcome = d.pop("outcome")

    def _parse_entry_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entry_id = _parse_entry_id(d.pop("entry_id", UNSET))

    def _parse_status(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    status = _parse_status(d.pop("status", UNSET))

    def _parse_posting_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        posting_date_type_0 = isoparse(data).date()

        return posting_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    posting_date = _parse_posting_date(d.pop("posting_date", UNSET))

    def _parse_memo(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    memo = _parse_memo(d.pop("memo", UNSET))

    def _parse_debit_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    debit_element_id = _parse_debit_element_id(d.pop("debit_element_id", UNSET))

    def _parse_credit_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    credit_element_id = _parse_credit_element_id(d.pop("credit_element_id", UNSET))

    def _parse_amount(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    amount = _parse_amount(d.pop("amount", UNSET))

    def _parse_reason(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reason = _parse_reason(d.pop("reason", UNSET))

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
      outcome=outcome,
      entry_id=entry_id,
      status=status,
      posting_date=posting_date,
      memo=memo,
      debit_element_id=debit_element_id,
      credit_element_id=credit_element_id,
      amount=amount,
      reason=reason,
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
