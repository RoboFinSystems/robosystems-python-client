from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_transaction_request_status import CreateTransactionRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransactionRequest")


@_attrs_define
class CreateTransactionRequest:
  """Create a standalone business-event Transaction.

  Use this when you want to record a real-world event (invoice, payment,
  deposit, expense) first and then attach one or more journal entries to
  it via `create-journal-entry` with the returned `transaction_id`.

  `amount` is in minor currency units (cents). `type` is free-form but
  common values are: invoice, payment, bill, expense, deposit, transfer,
  journal_entry.

      Attributes:
          type_ (str):
          date (datetime.date):
          amount (int):
          currency (str | Unset):  Default: 'USD'.
          description (None | str | Unset):
          merchant_name (None | str | Unset):
          reference_number (None | str | Unset):
          number (None | str | Unset):
          category (None | str | Unset):
          due_date (datetime.date | None | Unset):
          status (CreateTransactionRequestStatus | Unset):  Default: CreateTransactionRequestStatus.PENDING.
  """

  type_: str
  date: datetime.date
  amount: int
  currency: str | Unset = "USD"
  description: None | str | Unset = UNSET
  merchant_name: None | str | Unset = UNSET
  reference_number: None | str | Unset = UNSET
  number: None | str | Unset = UNSET
  category: None | str | Unset = UNSET
  due_date: datetime.date | None | Unset = UNSET
  status: CreateTransactionRequestStatus | Unset = (
    CreateTransactionRequestStatus.PENDING
  )
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    type_ = self.type_

    date = self.date.isoformat()

    amount = self.amount

    currency = self.currency

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

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

    status: str | Unset = UNSET
    if not isinstance(self.status, Unset):
      status = self.status.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "type": type_,
        "date": date,
        "amount": amount,
      }
    )
    if currency is not UNSET:
      field_dict["currency"] = currency
    if description is not UNSET:
      field_dict["description"] = description
    if merchant_name is not UNSET:
      field_dict["merchant_name"] = merchant_name
    if reference_number is not UNSET:
      field_dict["reference_number"] = reference_number
    if number is not UNSET:
      field_dict["number"] = number
    if category is not UNSET:
      field_dict["category"] = category
    if due_date is not UNSET:
      field_dict["due_date"] = due_date
    if status is not UNSET:
      field_dict["status"] = status

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    type_ = d.pop("type")

    date = isoparse(d.pop("date")).date()

    amount = d.pop("amount")

    currency = d.pop("currency", UNSET)

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

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

    _status = d.pop("status", UNSET)
    status: CreateTransactionRequestStatus | Unset
    if isinstance(_status, Unset):
      status = UNSET
    else:
      status = CreateTransactionRequestStatus(_status)

    create_transaction_request = cls(
      type_=type_,
      date=date,
      amount=amount,
      currency=currency,
      description=description,
      merchant_name=merchant_name,
      reference_number=reference_number,
      number=number,
      category=category,
      due_date=due_date,
      status=status,
    )

    create_transaction_request.additional_properties = d
    return create_transaction_request

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
