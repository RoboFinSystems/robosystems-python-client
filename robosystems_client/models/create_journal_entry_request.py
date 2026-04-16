from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_journal_entry_request_type import CreateJournalEntryRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.journal_entry_line_item_input import JournalEntryLineItemInput


T = TypeVar("T", bound="CreateJournalEntryRequest")


@_attrs_define
class CreateJournalEntryRequest:
  """Create a new journal entry with balanced line items.

  The entry is always created as `status='draft'`. Posting a draft
  happens via `close-period` (for batch month-end posting) or — in
  the future — an individual `post-journal-entry` op. This matches
  the existing `create-manual-closing-entry` behavior.

  Total debit amount must equal total credit amount or the request
  is rejected with 422. `line_items` must contain at least two rows
  (at least one debit, at least one credit).

      Attributes:
          posting_date (datetime.date):
          memo (str):
          line_items (list[JournalEntryLineItemInput]):
          type_ (CreateJournalEntryRequestType | Unset):  Default: CreateJournalEntryRequestType.STANDARD.
          transaction_id (None | str | Unset):
  """

  posting_date: datetime.date
  memo: str
  line_items: list[JournalEntryLineItemInput]
  type_: CreateJournalEntryRequestType | Unset = CreateJournalEntryRequestType.STANDARD
  transaction_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    posting_date = self.posting_date.isoformat()

    memo = self.memo

    line_items = []
    for line_items_item_data in self.line_items:
      line_items_item = line_items_item_data.to_dict()
      line_items.append(line_items_item)

    type_: str | Unset = UNSET
    if not isinstance(self.type_, Unset):
      type_ = self.type_.value

    transaction_id: None | str | Unset
    if isinstance(self.transaction_id, Unset):
      transaction_id = UNSET
    else:
      transaction_id = self.transaction_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "posting_date": posting_date,
        "memo": memo,
        "line_items": line_items,
      }
    )
    if type_ is not UNSET:
      field_dict["type"] = type_
    if transaction_id is not UNSET:
      field_dict["transaction_id"] = transaction_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.journal_entry_line_item_input import JournalEntryLineItemInput

    d = dict(src_dict)
    posting_date = isoparse(d.pop("posting_date")).date()

    memo = d.pop("memo")

    line_items = []
    _line_items = d.pop("line_items")
    for line_items_item_data in _line_items:
      line_items_item = JournalEntryLineItemInput.from_dict(line_items_item_data)

      line_items.append(line_items_item)

    _type_ = d.pop("type", UNSET)
    type_: CreateJournalEntryRequestType | Unset
    if isinstance(_type_, Unset):
      type_ = UNSET
    else:
      type_ = CreateJournalEntryRequestType(_type_)

    def _parse_transaction_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    transaction_id = _parse_transaction_id(d.pop("transaction_id", UNSET))

    create_journal_entry_request = cls(
      posting_date=posting_date,
      memo=memo,
      line_items=line_items,
      type_=type_,
      transaction_id=transaction_id,
    )

    create_journal_entry_request.additional_properties = d
    return create_journal_entry_request

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
