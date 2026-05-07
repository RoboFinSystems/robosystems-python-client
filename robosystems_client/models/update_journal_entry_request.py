from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_journal_entry_request_type_type_0 import (
  UpdateJournalEntryRequestTypeType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.journal_entry_line_item_input import JournalEntryLineItemInput


T = TypeVar("T", bound="UpdateJournalEntryRequest")


@_attrs_define
class UpdateJournalEntryRequest:
  """Update a draft journal entry. Posted entries cannot be updated —
  create a reversal and a corrected entry instead.

  Omitted fields are left unchanged. If `line_items` is provided, the
  existing line items are replaced entirely (atomic delete + insert)
  and the new set must still balance. If `line_items` is omitted, the
  existing line items are left untouched.

      Attributes:
          entry_id (str): The draft entry to update.
          posting_date (datetime.date | None | Unset): New posting date.
          memo (None | str | Unset): New entry-level memo.
          type_ (None | Unset | UpdateJournalEntryRequestTypeType0): New entry type. `closing` should normally only be set
              by close-period.
          line_items (list[JournalEntryLineItemInput] | None | Unset): Replacement line items. Whole-list replacement (not
              patch). The new set must still balance (total_debit == total_credit). Omit to leave existing lines untouched.
  """

  entry_id: str
  posting_date: datetime.date | None | Unset = UNSET
  memo: None | str | Unset = UNSET
  type_: None | Unset | UpdateJournalEntryRequestTypeType0 = UNSET
  line_items: list[JournalEntryLineItemInput] | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entry_id = self.entry_id

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

    type_: None | str | Unset
    if isinstance(self.type_, Unset):
      type_ = UNSET
    elif isinstance(self.type_, UpdateJournalEntryRequestTypeType0):
      type_ = self.type_.value
    else:
      type_ = self.type_

    line_items: list[dict[str, Any]] | None | Unset
    if isinstance(self.line_items, Unset):
      line_items = UNSET
    elif isinstance(self.line_items, list):
      line_items = []
      for line_items_type_0_item_data in self.line_items:
        line_items_type_0_item = line_items_type_0_item_data.to_dict()
        line_items.append(line_items_type_0_item)

    else:
      line_items = self.line_items

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entry_id": entry_id,
      }
    )
    if posting_date is not UNSET:
      field_dict["posting_date"] = posting_date
    if memo is not UNSET:
      field_dict["memo"] = memo
    if type_ is not UNSET:
      field_dict["type"] = type_
    if line_items is not UNSET:
      field_dict["line_items"] = line_items

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.journal_entry_line_item_input import JournalEntryLineItemInput

    d = dict(src_dict)
    entry_id = d.pop("entry_id")

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

    def _parse_type_(data: object) -> None | Unset | UpdateJournalEntryRequestTypeType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        type_type_0 = UpdateJournalEntryRequestTypeType0(data)

        return type_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateJournalEntryRequestTypeType0, data)

    type_ = _parse_type_(d.pop("type", UNSET))

    def _parse_line_items(
      data: object,
    ) -> list[JournalEntryLineItemInput] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        line_items_type_0 = []
        _line_items_type_0 = data
        for line_items_type_0_item_data in _line_items_type_0:
          line_items_type_0_item = JournalEntryLineItemInput.from_dict(
            line_items_type_0_item_data
          )

          line_items_type_0.append(line_items_type_0_item)

        return line_items_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[JournalEntryLineItemInput] | None | Unset, data)

    line_items = _parse_line_items(d.pop("line_items", UNSET))

    update_journal_entry_request = cls(
      entry_id=entry_id,
      posting_date=posting_date,
      memo=memo,
      type_=type_,
      line_items=line_items,
    )

    update_journal_entry_request.additional_properties = d
    return update_journal_entry_request

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
