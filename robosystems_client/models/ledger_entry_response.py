from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.ledger_line_item_response import LedgerLineItemResponse


T = TypeVar("T", bound="LedgerEntryResponse")


@_attrs_define
class LedgerEntryResponse:
  """
  Attributes:
      id (str):
      type_ (str):
      posting_date (datetime.date):
      status (str):
      line_items (list[LedgerLineItemResponse]):
      number (None | str | Unset):
      memo (None | str | Unset):
      posted_at (datetime.datetime | None | Unset):
  """

  id: str
  type_: str
  posting_date: datetime.date
  status: str
  line_items: list[LedgerLineItemResponse]
  number: None | str | Unset = UNSET
  memo: None | str | Unset = UNSET
  posted_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    type_ = self.type_

    posting_date = self.posting_date.isoformat()

    status = self.status

    line_items = []
    for line_items_item_data in self.line_items:
      line_items_item = line_items_item_data.to_dict()
      line_items.append(line_items_item)

    number: None | str | Unset
    if isinstance(self.number, Unset):
      number = UNSET
    else:
      number = self.number

    memo: None | str | Unset
    if isinstance(self.memo, Unset):
      memo = UNSET
    else:
      memo = self.memo

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
        "posting_date": posting_date,
        "status": status,
        "line_items": line_items,
      }
    )
    if number is not UNSET:
      field_dict["number"] = number
    if memo is not UNSET:
      field_dict["memo"] = memo
    if posted_at is not UNSET:
      field_dict["posted_at"] = posted_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.ledger_line_item_response import LedgerLineItemResponse

    d = dict(src_dict)
    id = d.pop("id")

    type_ = d.pop("type")

    posting_date = isoparse(d.pop("posting_date")).date()

    status = d.pop("status")

    line_items = []
    _line_items = d.pop("line_items")
    for line_items_item_data in _line_items:
      line_items_item = LedgerLineItemResponse.from_dict(line_items_item_data)

      line_items.append(line_items_item)

    def _parse_number(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    number = _parse_number(d.pop("number", UNSET))

    def _parse_memo(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    memo = _parse_memo(d.pop("memo", UNSET))

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

    ledger_entry_response = cls(
      id=id,
      type_=type_,
      posting_date=posting_date,
      status=status,
      line_items=line_items,
      number=number,
      memo=memo,
      posted_at=posted_at,
    )

    ledger_entry_response.additional_properties = d
    return ledger_entry_response

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
