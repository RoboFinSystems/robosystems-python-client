from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRepositorySubscriptionRequest")


@_attrs_define
class CreateRepositorySubscriptionRequest:
  """Request to create a repository subscription.

  Attributes:
      plan_name (str): Plan name for the repository subscription
      user_id (None | str | Unset): Subscribe this user instead of yourself. Org owners and admins only, and the
          target must belong to the same organization. Omit to subscribe yourself. Repository access is per-user while
          billing is org-level, so the subscriber is what determines who gets access.
  """

  plan_name: str
  user_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    plan_name = self.plan_name

    user_id: None | str | Unset
    if isinstance(self.user_id, Unset):
      user_id = UNSET
    else:
      user_id = self.user_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "plan_name": plan_name,
      }
    )
    if user_id is not UNSET:
      field_dict["user_id"] = user_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    plan_name = d.pop("plan_name")

    def _parse_user_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    user_id = _parse_user_id(d.pop("user_id", UNSET))

    create_repository_subscription_request = cls(
      plan_name=plan_name,
      user_id=user_id,
    )

    create_repository_subscription_request.additional_properties = d
    return create_repository_subscription_request

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
