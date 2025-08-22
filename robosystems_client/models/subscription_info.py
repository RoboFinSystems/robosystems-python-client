from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.subscription_info_metadata import SubscriptionInfoMetadata


T = TypeVar("T", bound="SubscriptionInfo")


@_attrs_define
class SubscriptionInfo:
  """User subscription information.

  Attributes:
      id (str): Subscription ID
      user_id (str): User ID
      addon_type (str): Add-on type
      addon_tier (str): Subscription tier
      is_active (bool): Whether subscription is active
      activated_at (str): Activation date (ISO format)
      monthly_price_cents (int): Monthly price in cents
      features (list[str]): List of features
      metadata (SubscriptionInfoMetadata): Additional metadata
      expires_at (Union[None, Unset, str]): Expiration date (ISO format)
  """

  id: str
  user_id: str
  addon_type: str
  addon_tier: str
  is_active: bool
  activated_at: str
  monthly_price_cents: int
  features: list[str]
  metadata: "SubscriptionInfoMetadata"
  expires_at: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    user_id = self.user_id

    addon_type = self.addon_type

    addon_tier = self.addon_tier

    is_active = self.is_active

    activated_at = self.activated_at

    monthly_price_cents = self.monthly_price_cents

    features = self.features

    metadata = self.metadata.to_dict()

    expires_at: Union[None, Unset, str]
    if isinstance(self.expires_at, Unset):
      expires_at = UNSET
    else:
      expires_at = self.expires_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "user_id": user_id,
        "addon_type": addon_type,
        "addon_tier": addon_tier,
        "is_active": is_active,
        "activated_at": activated_at,
        "monthly_price_cents": monthly_price_cents,
        "features": features,
        "metadata": metadata,
      }
    )
    if expires_at is not UNSET:
      field_dict["expires_at"] = expires_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.subscription_info_metadata import SubscriptionInfoMetadata

    d = dict(src_dict)
    id = d.pop("id")

    user_id = d.pop("user_id")

    addon_type = d.pop("addon_type")

    addon_tier = d.pop("addon_tier")

    is_active = d.pop("is_active")

    activated_at = d.pop("activated_at")

    monthly_price_cents = d.pop("monthly_price_cents")

    features = cast(list[str], d.pop("features"))

    metadata = SubscriptionInfoMetadata.from_dict(d.pop("metadata"))

    def _parse_expires_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

    subscription_info = cls(
      id=id,
      user_id=user_id,
      addon_type=addon_type,
      addon_tier=addon_tier,
      is_active=is_active,
      activated_at=activated_at,
      monthly_price_cents=monthly_price_cents,
      features=features,
      metadata=metadata,
      expires_at=expires_at,
    )

    subscription_info.additional_properties = d
    return subscription_info

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
