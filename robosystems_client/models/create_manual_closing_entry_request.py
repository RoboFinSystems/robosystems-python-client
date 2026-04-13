from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_manual_closing_entry_request_entry_type import (
  CreateManualClosingEntryRequestEntryType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.manual_line_item_request import ManualLineItemRequest


T = TypeVar("T", bound="CreateManualClosingEntryRequest")


@_attrs_define
class CreateManualClosingEntryRequest:
  """
  Attributes:
      posting_date (datetime.date): Posting date for the entry
      memo (str): Memo describing the business event (e.g., 'Sale of computer to Vendor X on 3/15')
      line_items (list[ManualLineItemRequest]): Line items; must balance (total DR = total CR)
      entry_type (CreateManualClosingEntryRequestEntryType | Unset): Entry type: 'closing' (default), 'adjusting',
          'standard', 'reversing' Default: CreateManualClosingEntryRequestEntryType.CLOSING.
  """

  posting_date: datetime.date
  memo: str
  line_items: list[ManualLineItemRequest]
  entry_type: CreateManualClosingEntryRequestEntryType | Unset = (
    CreateManualClosingEntryRequestEntryType.CLOSING
  )
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    posting_date = self.posting_date.isoformat()

    memo = self.memo

    line_items = []
    for line_items_item_data in self.line_items:
      line_items_item = line_items_item_data.to_dict()
      line_items.append(line_items_item)

    entry_type: str | Unset = UNSET
    if not isinstance(self.entry_type, Unset):
      entry_type = self.entry_type.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "posting_date": posting_date,
        "memo": memo,
        "line_items": line_items,
      }
    )
    if entry_type is not UNSET:
      field_dict["entry_type"] = entry_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.manual_line_item_request import ManualLineItemRequest

    d = dict(src_dict)
    posting_date = isoparse(d.pop("posting_date")).date()

    memo = d.pop("memo")

    line_items = []
    _line_items = d.pop("line_items")
    for line_items_item_data in _line_items:
      line_items_item = ManualLineItemRequest.from_dict(line_items_item_data)

      line_items.append(line_items_item)

    _entry_type = d.pop("entry_type", UNSET)
    entry_type: CreateManualClosingEntryRequestEntryType | Unset
    if isinstance(_entry_type, Unset):
      entry_type = UNSET
    else:
      entry_type = CreateManualClosingEntryRequestEntryType(_entry_type)

    create_manual_closing_entry_request = cls(
      posting_date=posting_date,
      memo=memo,
      line_items=line_items,
      entry_type=entry_type,
    )

    create_manual_closing_entry_request.additional_properties = d
    return create_manual_closing_entry_request

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
