from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.user_limits_response import UserLimitsResponse
  from ..models.user_usage_response_graphs import UserUsageResponseGraphs


T = TypeVar("T", bound="UserUsageResponse")


@_attrs_define
class UserUsageResponse:
  """Response model for user usage statistics.

  Simplified to only show graph usage as UserLimits is now just a safety valve.
  Other usage tracking (MCP, Agent calls) happens at the graph level.

      Attributes:
          user_id (str): User identifier
          graphs (UserUsageResponseGraphs): Graph usage statistics (current/limit/remaining)
          limits (UserLimitsResponse): Response model for user limits information.

              UserLimits is now a simple safety valve to prevent runaway graph creation.
              Subscription tiers and rate limits are handled at the graph level.
  """

  user_id: str
  graphs: "UserUsageResponseGraphs"
  limits: "UserLimitsResponse"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    user_id = self.user_id

    graphs = self.graphs.to_dict()

    limits = self.limits.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "user_id": user_id,
        "graphs": graphs,
        "limits": limits,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.user_limits_response import UserLimitsResponse
    from ..models.user_usage_response_graphs import UserUsageResponseGraphs

    d = dict(src_dict)
    user_id = d.pop("user_id")

    graphs = UserUsageResponseGraphs.from_dict(d.pop("graphs"))

    limits = UserLimitsResponse.from_dict(d.pop("limits"))

    user_usage_response = cls(
      user_id=user_id,
      graphs=graphs,
      limits=limits,
    )

    user_usage_response.additional_properties = d
    return user_usage_response

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
