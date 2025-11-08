from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.payment_method import PaymentMethod


T = TypeVar("T", bound="BillingCustomer")


@_attrs_define
class BillingCustomer:
  """Billing customer information for an organization.

  Attributes:
      org_id (str): Organization ID
      has_payment_method (bool): Whether organization has a payment method on file
      invoice_billing_enabled (bool): Whether invoice billing is enabled (enterprise customers)
      payment_methods (list['PaymentMethod']): List of payment methods on file
      created_at (str): Customer creation timestamp (ISO format)
      stripe_customer_id (Union[None, Unset, str]): Stripe customer ID if applicable
  """

  org_id: str
  has_payment_method: bool
  invoice_billing_enabled: bool
  payment_methods: list["PaymentMethod"]
  created_at: str
  stripe_customer_id: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    org_id = self.org_id

    has_payment_method = self.has_payment_method

    invoice_billing_enabled = self.invoice_billing_enabled

    payment_methods = []
    for payment_methods_item_data in self.payment_methods:
      payment_methods_item = payment_methods_item_data.to_dict()
      payment_methods.append(payment_methods_item)

    created_at = self.created_at

    stripe_customer_id: Union[None, Unset, str]
    if isinstance(self.stripe_customer_id, Unset):
      stripe_customer_id = UNSET
    else:
      stripe_customer_id = self.stripe_customer_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "org_id": org_id,
        "has_payment_method": has_payment_method,
        "invoice_billing_enabled": invoice_billing_enabled,
        "payment_methods": payment_methods,
        "created_at": created_at,
      }
    )
    if stripe_customer_id is not UNSET:
      field_dict["stripe_customer_id"] = stripe_customer_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.payment_method import PaymentMethod

    d = dict(src_dict)
    org_id = d.pop("org_id")

    has_payment_method = d.pop("has_payment_method")

    invoice_billing_enabled = d.pop("invoice_billing_enabled")

    payment_methods = []
    _payment_methods = d.pop("payment_methods")
    for payment_methods_item_data in _payment_methods:
      payment_methods_item = PaymentMethod.from_dict(payment_methods_item_data)

      payment_methods.append(payment_methods_item)

    created_at = d.pop("created_at")

    def _parse_stripe_customer_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    stripe_customer_id = _parse_stripe_customer_id(d.pop("stripe_customer_id", UNSET))

    billing_customer = cls(
      org_id=org_id,
      has_payment_method=has_payment_method,
      invoice_billing_enabled=invoice_billing_enabled,
      payment_methods=payment_methods,
      created_at=created_at,
      stripe_customer_id=stripe_customer_id,
    )

    billing_customer.additional_properties = d
    return billing_customer

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
