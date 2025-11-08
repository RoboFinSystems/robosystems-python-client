from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceLineItem")


@_attrs_define
class InvoiceLineItem:
  """Invoice line item.

  Attributes:
      description (str): Line item description
      amount (int): Amount in cents
      quantity (int): Quantity
      period_start (Union[None, Unset, str]): Billing period start
      period_end (Union[None, Unset, str]): Billing period end
  """

  description: str
  amount: int
  quantity: int
  period_start: Union[None, Unset, str] = UNSET
  period_end: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    description = self.description

    amount = self.amount

    quantity = self.quantity

    period_start: Union[None, Unset, str]
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    else:
      period_start = self.period_start

    period_end: Union[None, Unset, str]
    if isinstance(self.period_end, Unset):
      period_end = UNSET
    else:
      period_end = self.period_end

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "description": description,
        "amount": amount,
        "quantity": quantity,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    description = d.pop("description")

    amount = d.pop("amount")

    quantity = d.pop("quantity")

    def _parse_period_start(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    period_start = _parse_period_start(d.pop("period_start", UNSET))

    def _parse_period_end(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    period_end = _parse_period_end(d.pop("period_end", UNSET))

    invoice_line_item = cls(
      description=description,
      amount=amount,
      quantity=quantity,
      period_start=period_start,
      period_end=period_end,
    )

    invoice_line_item.additional_properties = d
    return invoice_line_item

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
