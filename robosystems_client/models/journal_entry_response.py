from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.journal_entry_line_item_response import JournalEntryLineItemResponse


T = TypeVar("T", bound="JournalEntryResponse")


@_attrs_define
class JournalEntryResponse:
  """The common response shape for journal entry write operations.

  Attributes:
      id (str):
      type_ (str):
      status (str):
      posting_date (datetime.date):
      line_items (list[JournalEntryLineItemResponse]):
      total_debit (int):
      total_credit (int):
      transaction_id (None | str | Unset):
      memo (None | str | Unset):
      provenance (None | str | Unset):
      reversal_of (None | str | Unset):
      posted_at (datetime.datetime | None | Unset):
  """

  id: str
  type_: str
  status: str
  posting_date: datetime.date
  line_items: list[JournalEntryLineItemResponse]
  total_debit: int
  total_credit: int
  transaction_id: None | str | Unset = UNSET
  memo: None | str | Unset = UNSET
  provenance: None | str | Unset = UNSET
  reversal_of: None | str | Unset = UNSET
  posted_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    type_ = self.type_

    status = self.status

    posting_date = self.posting_date.isoformat()

    line_items = []
    for line_items_item_data in self.line_items:
      line_items_item = line_items_item_data.to_dict()
      line_items.append(line_items_item)

    total_debit = self.total_debit

    total_credit = self.total_credit

    transaction_id: None | str | Unset
    if isinstance(self.transaction_id, Unset):
      transaction_id = UNSET
    else:
      transaction_id = self.transaction_id

    memo: None | str | Unset
    if isinstance(self.memo, Unset):
      memo = UNSET
    else:
      memo = self.memo

    provenance: None | str | Unset
    if isinstance(self.provenance, Unset):
      provenance = UNSET
    else:
      provenance = self.provenance

    reversal_of: None | str | Unset
    if isinstance(self.reversal_of, Unset):
      reversal_of = UNSET
    else:
      reversal_of = self.reversal_of

    posted_at: None | str | Unset
    if isinstance(self.posted_at, Unset):
      posted_at = UNSET
    elif isinstance(self.posted_at, datetime.datetime):
      posted_at = self.posted_at.isoformat()
    else:
      posted_at = self.posted_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "type": type_,
        "status": status,
        "posting_date": posting_date,
        "line_items": line_items,
        "total_debit": total_debit,
        "total_credit": total_credit,
      }
    )
    if transaction_id is not UNSET:
      field_dict["transaction_id"] = transaction_id
    if memo is not UNSET:
      field_dict["memo"] = memo
    if provenance is not UNSET:
      field_dict["provenance"] = provenance
    if reversal_of is not UNSET:
      field_dict["reversal_of"] = reversal_of
    if posted_at is not UNSET:
      field_dict["posted_at"] = posted_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.journal_entry_line_item_response import JournalEntryLineItemResponse

    d = dict(src_dict)
    id = d.pop("id")

    type_ = d.pop("type")

    status = d.pop("status")

    posting_date = isoparse(d.pop("posting_date")).date()

    line_items = []
    _line_items = d.pop("line_items")
    for line_items_item_data in _line_items:
      line_items_item = JournalEntryLineItemResponse.from_dict(line_items_item_data)

      line_items.append(line_items_item)

    total_debit = d.pop("total_debit")

    total_credit = d.pop("total_credit")

    def _parse_transaction_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    transaction_id = _parse_transaction_id(d.pop("transaction_id", UNSET))

    def _parse_memo(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    memo = _parse_memo(d.pop("memo", UNSET))

    def _parse_provenance(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    provenance = _parse_provenance(d.pop("provenance", UNSET))

    def _parse_reversal_of(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reversal_of = _parse_reversal_of(d.pop("reversal_of", UNSET))

    def _parse_posted_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        posted_at_type_0 = isoparse(data)

        return posted_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    posted_at = _parse_posted_at(d.pop("posted_at", UNSET))

    journal_entry_response = cls(
      id=id,
      type_=type_,
      status=status,
      posting_date=posting_date,
      line_items=line_items,
      total_debit=total_debit,
      total_credit=total_credit,
      transaction_id=transaction_id,
      memo=memo,
      provenance=provenance,
      reversal_of=reversal_of,
      posted_at=posted_at,
    )

    journal_entry_response.additional_properties = d
    return journal_entry_response

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
