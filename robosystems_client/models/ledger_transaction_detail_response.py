from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.ledger_entry_response import LedgerEntryResponse


T = TypeVar("T", bound="LedgerTransactionDetailResponse")


@_attrs_define
class LedgerTransactionDetailResponse:
  """
  Attributes:
      id (str):
      type_ (str):
      amount (float):
      currency (str):
      date (datetime.date):
      source (str):
      status (str):
      entries (list[LedgerEntryResponse]):
      number (None | str | Unset):
      category (None | str | Unset):
      due_date (datetime.date | None | Unset):
      merchant_name (None | str | Unset):
      reference_number (None | str | Unset):
      description (None | str | Unset):
      source_id (None | str | Unset):
      posted_at (datetime.datetime | None | Unset):
  """

  id: str
  type_: str
  amount: float
  currency: str
  date: datetime.date
  source: str
  status: str
  entries: list[LedgerEntryResponse]
  number: None | str | Unset = UNSET
  category: None | str | Unset = UNSET
  due_date: datetime.date | None | Unset = UNSET
  merchant_name: None | str | Unset = UNSET
  reference_number: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  source_id: None | str | Unset = UNSET
  posted_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    type_ = self.type_

    amount = self.amount

    currency = self.currency

    date = self.date.isoformat()

    source = self.source

    status = self.status

    entries = []
    for entries_item_data in self.entries:
      entries_item = entries_item_data.to_dict()
      entries.append(entries_item)

    number: None | str | Unset
    if isinstance(self.number, Unset):
      number = UNSET
    else:
      number = self.number

    category: None | str | Unset
    if isinstance(self.category, Unset):
      category = UNSET
    else:
      category = self.category

    due_date: None | str | Unset
    if isinstance(self.due_date, Unset):
      due_date = UNSET
    elif isinstance(self.due_date, datetime.date):
      due_date = self.due_date.isoformat()
    else:
      due_date = self.due_date

    merchant_name: None | str | Unset
    if isinstance(self.merchant_name, Unset):
      merchant_name = UNSET
    else:
      merchant_name = self.merchant_name

    reference_number: None | str | Unset
    if isinstance(self.reference_number, Unset):
      reference_number = UNSET
    else:
      reference_number = self.reference_number

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    source_id: None | str | Unset
    if isinstance(self.source_id, Unset):
      source_id = UNSET
    else:
      source_id = self.source_id

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
        "amount": amount,
        "currency": currency,
        "date": date,
        "source": source,
        "status": status,
        "entries": entries,
      }
    )
    if number is not UNSET:
      field_dict["number"] = number
    if category is not UNSET:
      field_dict["category"] = category
    if due_date is not UNSET:
      field_dict["due_date"] = due_date
    if merchant_name is not UNSET:
      field_dict["merchant_name"] = merchant_name
    if reference_number is not UNSET:
      field_dict["reference_number"] = reference_number
    if description is not UNSET:
      field_dict["description"] = description
    if source_id is not UNSET:
      field_dict["source_id"] = source_id
    if posted_at is not UNSET:
      field_dict["posted_at"] = posted_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.ledger_entry_response import LedgerEntryResponse

    d = dict(src_dict)
    id = d.pop("id")

    type_ = d.pop("type")

    amount = d.pop("amount")

    currency = d.pop("currency")

    date = isoparse(d.pop("date")).date()

    source = d.pop("source")

    status = d.pop("status")

    entries = []
    _entries = d.pop("entries")
    for entries_item_data in _entries:
      entries_item = LedgerEntryResponse.from_dict(entries_item_data)

      entries.append(entries_item)

    def _parse_number(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    number = _parse_number(d.pop("number", UNSET))

    def _parse_category(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    category = _parse_category(d.pop("category", UNSET))

    def _parse_due_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        due_date_type_0 = isoparse(data).date()

        return due_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    due_date = _parse_due_date(d.pop("due_date", UNSET))

    def _parse_merchant_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    merchant_name = _parse_merchant_name(d.pop("merchant_name", UNSET))

    def _parse_reference_number(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reference_number = _parse_reference_number(d.pop("reference_number", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_source_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_id = _parse_source_id(d.pop("source_id", UNSET))

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

    ledger_transaction_detail_response = cls(
      id=id,
      type_=type_,
      amount=amount,
      currency=currency,
      date=date,
      source=source,
      status=status,
      entries=entries,
      number=number,
      category=category,
      due_date=due_date,
      merchant_name=merchant_name,
      reference_number=reference_number,
      description=description,
      source_id=source_id,
      posted_at=posted_at,
    )

    ledger_transaction_detail_response.additional_properties = d
    return ledger_transaction_detail_response

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
