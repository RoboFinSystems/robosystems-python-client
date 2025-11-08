from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutResponse")


@_attrs_define
class CheckoutResponse:
  """Response from checkout session creation.

  Attributes:
      checkout_url (str): URL to redirect user to for payment
      session_id (str): Checkout session ID for status polling
      subscription_id (str): Internal subscription ID
      requires_checkout (Union[Unset, bool]): Whether checkout is required Default: True.
  """

  checkout_url: str
  session_id: str
  subscription_id: str
  requires_checkout: Union[Unset, bool] = True
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    checkout_url = self.checkout_url

    session_id = self.session_id

    subscription_id = self.subscription_id

    requires_checkout = self.requires_checkout

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "checkout_url": checkout_url,
        "session_id": session_id,
        "subscription_id": subscription_id,
      }
    )
    if requires_checkout is not UNSET:
      field_dict["requires_checkout"] = requires_checkout

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    checkout_url = d.pop("checkout_url")

    session_id = d.pop("session_id")

    subscription_id = d.pop("subscription_id")

    requires_checkout = d.pop("requires_checkout", UNSET)

    checkout_response = cls(
      checkout_url=checkout_url,
      session_id=session_id,
      subscription_id=subscription_id,
      requires_checkout=requires_checkout,
    )

    checkout_response.additional_properties = d
    return checkout_response

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
