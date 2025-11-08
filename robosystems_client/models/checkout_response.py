from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutResponse")


@_attrs_define
class CheckoutResponse:
  """Response from checkout session creation.

  Attributes:
      checkout_url (Union[None, Unset, str]): URL to redirect user to for payment
      session_id (Union[None, Unset, str]): Checkout session ID for status polling
      subscription_id (Union[None, Unset, str]): Internal subscription ID
      requires_checkout (Union[Unset, bool]): Whether checkout is required Default: True.
      billing_disabled (Union[Unset, bool]): Whether billing is disabled on this instance Default: False.
  """

  checkout_url: Union[None, Unset, str] = UNSET
  session_id: Union[None, Unset, str] = UNSET
  subscription_id: Union[None, Unset, str] = UNSET
  requires_checkout: Union[Unset, bool] = True
  billing_disabled: Union[Unset, bool] = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    checkout_url: Union[None, Unset, str]
    if isinstance(self.checkout_url, Unset):
      checkout_url = UNSET
    else:
      checkout_url = self.checkout_url

    session_id: Union[None, Unset, str]
    if isinstance(self.session_id, Unset):
      session_id = UNSET
    else:
      session_id = self.session_id

    subscription_id: Union[None, Unset, str]
    if isinstance(self.subscription_id, Unset):
      subscription_id = UNSET
    else:
      subscription_id = self.subscription_id

    requires_checkout = self.requires_checkout

    billing_disabled = self.billing_disabled

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if checkout_url is not UNSET:
      field_dict["checkout_url"] = checkout_url
    if session_id is not UNSET:
      field_dict["session_id"] = session_id
    if subscription_id is not UNSET:
      field_dict["subscription_id"] = subscription_id
    if requires_checkout is not UNSET:
      field_dict["requires_checkout"] = requires_checkout
    if billing_disabled is not UNSET:
      field_dict["billing_disabled"] = billing_disabled

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_checkout_url(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    checkout_url = _parse_checkout_url(d.pop("checkout_url", UNSET))

    def _parse_session_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    session_id = _parse_session_id(d.pop("session_id", UNSET))

    def _parse_subscription_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    subscription_id = _parse_subscription_id(d.pop("subscription_id", UNSET))

    requires_checkout = d.pop("requires_checkout", UNSET)

    billing_disabled = d.pop("billing_disabled", UNSET)

    checkout_response = cls(
      checkout_url=checkout_url,
      session_id=session_id,
      subscription_id=subscription_id,
      requires_checkout=requires_checkout,
      billing_disabled=billing_disabled,
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
