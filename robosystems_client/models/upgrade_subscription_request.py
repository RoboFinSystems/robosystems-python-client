from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpgradeSubscriptionRequest")


@_attrs_define
class UpgradeSubscriptionRequest:
  """Request to upgrade a subscription.

  Attributes:
      new_plan_name (str): New plan name to change to
      user_id (None | str | Unset): Organization member whose subscription to change. Defaults to the caller;
          targeting another member requires org owner or admin.
  """

  new_plan_name: str
  user_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    new_plan_name = self.new_plan_name

    user_id: None | str | Unset
    if isinstance(self.user_id, Unset):
      user_id = UNSET
    else:
      user_id = self.user_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "new_plan_name": new_plan_name,
      }
    )
    if user_id is not UNSET:
      field_dict["user_id"] = user_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    new_plan_name = d.pop("new_plan_name")

    def _parse_user_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    user_id = _parse_user_id(d.pop("user_id", UNSET))

    upgrade_subscription_request = cls(
      new_plan_name=new_plan_name,
      user_id=user_id,
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
