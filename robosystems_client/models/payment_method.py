from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentMethod")


@_attrs_define
class PaymentMethod:
  """Payment method information.

  Attributes:
      id (str): Payment method ID
      type_ (str): Payment method type (card, bank_account, etc.)
      is_default (bool): Whether this is the default payment method
      brand (Union[None, Unset, str]): Card brand (visa, mastercard, etc.)
      last4 (Union[None, Unset, str]): Last 4 digits of the card or account number
      exp_month (Union[None, Unset, int]): Expiration month of the card
      exp_year (Union[None, Unset, int]): Expiration year of the card
  """

  id: str
  type_: str
  is_default: bool
  brand: Union[None, Unset, str] = UNSET
  last4: Union[None, Unset, str] = UNSET
  exp_month: Union[None, Unset, int] = UNSET
  exp_year: Union[None, Unset, int] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    type_ = self.type_

    is_default = self.is_default

    brand: Union[None, Unset, str]
    if isinstance(self.brand, Unset):
      brand = UNSET
    else:
      brand = self.brand

    last4: Union[None, Unset, str]
    if isinstance(self.last4, Unset):
      last4 = UNSET
    else:
      last4 = self.last4

    exp_month: Union[None, Unset, int]
    if isinstance(self.exp_month, Unset):
      exp_month = UNSET
    else:
      exp_month = self.exp_month

    exp_year: Union[None, Unset, int]
    if isinstance(self.exp_year, Unset):
      exp_year = UNSET
    else:
      exp_year = self.exp_year

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "type": type_,
        "is_default": is_default,
      }
    )
    if brand is not UNSET:
      field_dict["brand"] = brand
    if last4 is not UNSET:
      field_dict["last4"] = last4
    if exp_month is not UNSET:
      field_dict["exp_month"] = exp_month
    if exp_year is not UNSET:
      field_dict["exp_year"] = exp_year

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    type_ = d.pop("type")

    is_default = d.pop("is_default")

    def _parse_brand(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    brand = _parse_brand(d.pop("brand", UNSET))

    def _parse_last4(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    last4 = _parse_last4(d.pop("last4", UNSET))

    def _parse_exp_month(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    exp_month = _parse_exp_month(d.pop("exp_month", UNSET))

    def _parse_exp_year(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    exp_year = _parse_exp_year(d.pop("exp_year", UNSET))

    payment_method = cls(
      id=id,
      type_=type_,
      is_default=is_default,
      brand=brand,
      last4=last4,
      exp_month=exp_month,
      exp_year=exp_year,
    )

    payment_method.additional_properties = d
    return payment_method

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
