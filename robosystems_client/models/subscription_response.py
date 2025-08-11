from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.subscription_info import SubscriptionInfo


T = TypeVar("T", bound="SubscriptionResponse")


@_attrs_define
class SubscriptionResponse:
  """Response for subscription creation.

  Attributes:
      message (str): Success message
      subscription (SubscriptionInfo): User subscription information.
      trial_period (int): Trial period in days
  """

  message: str
  subscription: "SubscriptionInfo"
  trial_period: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    message = self.message

    subscription = self.subscription.to_dict()

    trial_period = self.trial_period

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "message": message,
        "subscription": subscription,
        "trial_period": trial_period,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.subscription_info import SubscriptionInfo

    d = dict(src_dict)
    message = d.pop("message")

    subscription = SubscriptionInfo.from_dict(d.pop("subscription"))

    trial_period = d.pop("trial_period")

    subscription_response = cls(
      message=message,
      subscription=subscription,
      trial_period=trial_period,
    )

    subscription_response.additional_properties = d
    return subscription_response

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
