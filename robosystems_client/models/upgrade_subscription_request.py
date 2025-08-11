from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpgradeSubscriptionRequest")


@_attrs_define
class UpgradeSubscriptionRequest:
  """Request to upgrade a graph database subscription.

  Attributes:
      plan_name (str):
      payment_method_id (Union[None, Unset, str]):
  """

  plan_name: str
  payment_method_id: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    plan_name = self.plan_name

    payment_method_id: Union[None, Unset, str]
    if isinstance(self.payment_method_id, Unset):
      payment_method_id = UNSET
    else:
      payment_method_id = self.payment_method_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "plan_name": plan_name,
      }
    )
    if payment_method_id is not UNSET:
      field_dict["payment_method_id"] = payment_method_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    plan_name = d.pop("plan_name")

    def _parse_payment_method_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    payment_method_id = _parse_payment_method_id(d.pop("payment_method_id", UNSET))

    upgrade_subscription_request = cls(
      plan_name=plan_name,
      payment_method_id=payment_method_id,
    )

    upgrade_subscription_request.additional_properties = d
    return upgrade_subscription_request

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
