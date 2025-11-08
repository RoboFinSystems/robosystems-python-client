from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.invoice_line_item import InvoiceLineItem


T = TypeVar("T", bound="UpcomingInvoice")


@_attrs_define
class UpcomingInvoice:
  """Upcoming invoice preview.

  Attributes:
      amount_due (int): Estimated amount due in cents
      currency (str): Currency code
      period_start (str): Billing period start
      period_end (str): Billing period end
      line_items (list['InvoiceLineItem']): Estimated line items
      subscription_id (Union[None, Unset, str]): Associated subscription ID
  """

  amount_due: int
  currency: str
  period_start: str
  period_end: str
  line_items: list["InvoiceLineItem"]
  subscription_id: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    amount_due = self.amount_due

    currency = self.currency

    period_start = self.period_start

    period_end = self.period_end

    line_items = []
    for line_items_item_data in self.line_items:
      line_items_item = line_items_item_data.to_dict()
      line_items.append(line_items_item)

    subscription_id: Union[None, Unset, str]
    if isinstance(self.subscription_id, Unset):
      subscription_id = UNSET
    else:
      subscription_id = self.subscription_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "amount_due": amount_due,
        "currency": currency,
        "period_start": period_start,
        "period_end": period_end,
        "line_items": line_items,
      }
    )
    if subscription_id is not UNSET:
      field_dict["subscription_id"] = subscription_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.invoice_line_item import InvoiceLineItem

    d = dict(src_dict)
    amount_due = d.pop("amount_due")

    currency = d.pop("currency")

    period_start = d.pop("period_start")

    period_end = d.pop("period_end")

    line_items = []
    _line_items = d.pop("line_items")
    for line_items_item_data in _line_items:
      line_items_item = InvoiceLineItem.from_dict(line_items_item_data)

      line_items.append(line_items_item)

    def _parse_subscription_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    subscription_id = _parse_subscription_id(d.pop("subscription_id", UNSET))

    upcoming_invoice = cls(
      amount_due=amount_due,
      currency=currency,
      period_start=period_start,
      period_end=period_end,
      line_items=line_items,
      subscription_id=subscription_id,
    )

    upcoming_invoice.additional_properties = d
    return upcoming_invoice

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
