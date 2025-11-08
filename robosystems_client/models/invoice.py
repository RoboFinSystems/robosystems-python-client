from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.invoice_line_item import InvoiceLineItem


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
  """Invoice information.

  Attributes:
      id (str): Invoice ID
      status (str): Invoice status (paid, open, void, uncollectible)
      amount_due (int): Amount due in cents
      amount_paid (int): Amount paid in cents
      currency (str): Currency code (usd)
      created (str): Invoice creation date (ISO format)
      line_items (list['InvoiceLineItem']): Invoice line items
      number (Union[None, Unset, str]): Invoice number
      due_date (Union[None, Unset, str]): Invoice due date (ISO format)
      paid_at (Union[None, Unset, str]): Payment date (ISO format)
      invoice_pdf (Union[None, Unset, str]): PDF download URL
      hosted_invoice_url (Union[None, Unset, str]): Hosted invoice URL
      subscription_id (Union[None, Unset, str]): Associated subscription ID
  """

  id: str
  status: str
  amount_due: int
  amount_paid: int
  currency: str
  created: str
  line_items: list["InvoiceLineItem"]
  number: Union[None, Unset, str] = UNSET
  due_date: Union[None, Unset, str] = UNSET
  paid_at: Union[None, Unset, str] = UNSET
  invoice_pdf: Union[None, Unset, str] = UNSET
  hosted_invoice_url: Union[None, Unset, str] = UNSET
  subscription_id: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    status = self.status

    amount_due = self.amount_due

    amount_paid = self.amount_paid

    currency = self.currency

    created = self.created

    line_items = []
    for line_items_item_data in self.line_items:
      line_items_item = line_items_item_data.to_dict()
      line_items.append(line_items_item)

    number: Union[None, Unset, str]
    if isinstance(self.number, Unset):
      number = UNSET
    else:
      number = self.number

    due_date: Union[None, Unset, str]
    if isinstance(self.due_date, Unset):
      due_date = UNSET
    else:
      due_date = self.due_date

    paid_at: Union[None, Unset, str]
    if isinstance(self.paid_at, Unset):
      paid_at = UNSET
    else:
      paid_at = self.paid_at

    invoice_pdf: Union[None, Unset, str]
    if isinstance(self.invoice_pdf, Unset):
      invoice_pdf = UNSET
    else:
      invoice_pdf = self.invoice_pdf

    hosted_invoice_url: Union[None, Unset, str]
    if isinstance(self.hosted_invoice_url, Unset):
      hosted_invoice_url = UNSET
    else:
      hosted_invoice_url = self.hosted_invoice_url

    subscription_id: Union[None, Unset, str]
    if isinstance(self.subscription_id, Unset):
      subscription_id = UNSET
    else:
      subscription_id = self.subscription_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "status": status,
        "amount_due": amount_due,
        "amount_paid": amount_paid,
        "currency": currency,
        "created": created,
        "line_items": line_items,
      }
    )
    if number is not UNSET:
      field_dict["number"] = number
    if due_date is not UNSET:
      field_dict["due_date"] = due_date
    if paid_at is not UNSET:
      field_dict["paid_at"] = paid_at
    if invoice_pdf is not UNSET:
      field_dict["invoice_pdf"] = invoice_pdf
    if hosted_invoice_url is not UNSET:
      field_dict["hosted_invoice_url"] = hosted_invoice_url
    if subscription_id is not UNSET:
      field_dict["subscription_id"] = subscription_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.invoice_line_item import InvoiceLineItem

    d = dict(src_dict)
    id = d.pop("id")

    status = d.pop("status")

    amount_due = d.pop("amount_due")

    amount_paid = d.pop("amount_paid")

    currency = d.pop("currency")

    created = d.pop("created")

    line_items = []
    _line_items = d.pop("line_items")
    for line_items_item_data in _line_items:
      line_items_item = InvoiceLineItem.from_dict(line_items_item_data)

      line_items.append(line_items_item)

    def _parse_number(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    number = _parse_number(d.pop("number", UNSET))

    def _parse_due_date(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    due_date = _parse_due_date(d.pop("due_date", UNSET))

    def _parse_paid_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    paid_at = _parse_paid_at(d.pop("paid_at", UNSET))

    def _parse_invoice_pdf(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    invoice_pdf = _parse_invoice_pdf(d.pop("invoice_pdf", UNSET))

    def _parse_hosted_invoice_url(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    hosted_invoice_url = _parse_hosted_invoice_url(d.pop("hosted_invoice_url", UNSET))

    def _parse_subscription_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    subscription_id = _parse_subscription_id(d.pop("subscription_id", UNSET))

    invoice = cls(
      id=id,
      status=status,
      amount_due=amount_due,
      amount_paid=amount_paid,
      currency=currency,
      created=created,
      line_items=line_items,
      number=number,
      due_date=due_date,
      paid_at=paid_at,
      invoice_pdf=invoice_pdf,
      hosted_invoice_url=hosted_invoice_url,
      subscription_id=subscription_id,
    )

    invoice.additional_properties = d
    return invoice

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
