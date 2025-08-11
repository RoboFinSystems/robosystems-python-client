from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserLimitsResponse")


@_attrs_define
class UserLimitsResponse:
  """Response model for user limits information.

  UserLimits is now a simple safety valve to prevent runaway graph creation.
  Subscription tiers and rate limits are handled at the graph level.

      Attributes:
          id (str): Unique limits identifier
          user_id (str): Associated user ID
          max_user_graphs (int): Maximum number of user graphs allowed (safety limit)
          created_at (str): Limits creation timestamp
          updated_at (str): Last update timestamp
  """

  id: str
  user_id: str
  max_user_graphs: int
  created_at: str
  updated_at: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    user_id = self.user_id

    max_user_graphs = self.max_user_graphs

    created_at = self.created_at

    updated_at = self.updated_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "user_id": user_id,
        "max_user_graphs": max_user_graphs,
        "created_at": created_at,
        "updated_at": updated_at,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    user_id = d.pop("user_id")

    max_user_graphs = d.pop("max_user_graphs")

    created_at = d.pop("created_at")

    updated_at = d.pop("updated_at")

    user_limits_response = cls(
      id=id,
      user_id=user_id,
      max_user_graphs=max_user_graphs,
      created_at=created_at,
      updated_at=updated_at,
    )

    user_limits_response.additional_properties = d
    return user_limits_response

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
