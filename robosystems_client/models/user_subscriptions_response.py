from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.subscription_info import SubscriptionInfo


T = TypeVar("T", bound="UserSubscriptionsResponse")


@_attrs_define
class UserSubscriptionsResponse:
  """Response for user subscriptions.

  Attributes:
      subscriptions (list['SubscriptionInfo']): List of user subscriptions
      total_count (int): Total number of subscriptions
      active_count (int): Number of active subscriptions
  """

  subscriptions: list["SubscriptionInfo"]
  total_count: int
  active_count: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    subscriptions = []
    for subscriptions_item_data in self.subscriptions:
      subscriptions_item = subscriptions_item_data.to_dict()
      subscriptions.append(subscriptions_item)

    total_count = self.total_count

    active_count = self.active_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "subscriptions": subscriptions,
        "total_count": total_count,
        "active_count": active_count,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.subscription_info import SubscriptionInfo

    d = dict(src_dict)
    subscriptions = []
    _subscriptions = d.pop("subscriptions")
    for subscriptions_item_data in _subscriptions:
      subscriptions_item = SubscriptionInfo.from_dict(subscriptions_item_data)

      subscriptions.append(subscriptions_item)

    total_count = d.pop("total_count")

    active_count = d.pop("active_count")

    user_subscriptions_response = cls(
      subscriptions=subscriptions,
      total_count=total_count,
      active_count=active_count,
    )

    user_subscriptions_response.additional_properties = d
    return user_subscriptions_response

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
