from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.user_analytics_response_api_usage import UserAnalyticsResponseApiUsage
  from ..models.user_analytics_response_graph_usage import (
    UserAnalyticsResponseGraphUsage,
  )
  from ..models.user_analytics_response_limits import UserAnalyticsResponseLimits
  from ..models.user_analytics_response_recent_activity_item import (
    UserAnalyticsResponseRecentActivityItem,
  )
  from ..models.user_analytics_response_user_info import UserAnalyticsResponseUserInfo


T = TypeVar("T", bound="UserAnalyticsResponse")


@_attrs_define
class UserAnalyticsResponse:
  """Response model for comprehensive user analytics.

  Attributes:
      user_info (UserAnalyticsResponseUserInfo): User information
      graph_usage (UserAnalyticsResponseGraphUsage): Graph usage statistics
      api_usage (UserAnalyticsResponseApiUsage): API usage statistics
      limits (UserAnalyticsResponseLimits): Current limits and restrictions
      recent_activity (list['UserAnalyticsResponseRecentActivityItem']): Recent user activity
      timestamp (str): Analytics generation timestamp
  """

  user_info: "UserAnalyticsResponseUserInfo"
  graph_usage: "UserAnalyticsResponseGraphUsage"
  api_usage: "UserAnalyticsResponseApiUsage"
  limits: "UserAnalyticsResponseLimits"
  recent_activity: list["UserAnalyticsResponseRecentActivityItem"]
  timestamp: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    user_info = self.user_info.to_dict()

    graph_usage = self.graph_usage.to_dict()

    api_usage = self.api_usage.to_dict()

    limits = self.limits.to_dict()

    recent_activity = []
    for recent_activity_item_data in self.recent_activity:
      recent_activity_item = recent_activity_item_data.to_dict()
      recent_activity.append(recent_activity_item)

    timestamp = self.timestamp

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "user_info": user_info,
        "graph_usage": graph_usage,
        "api_usage": api_usage,
        "limits": limits,
        "recent_activity": recent_activity,
        "timestamp": timestamp,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.user_analytics_response_api_usage import UserAnalyticsResponseApiUsage
    from ..models.user_analytics_response_graph_usage import (
      UserAnalyticsResponseGraphUsage,
    )
    from ..models.user_analytics_response_limits import UserAnalyticsResponseLimits
    from ..models.user_analytics_response_recent_activity_item import (
      UserAnalyticsResponseRecentActivityItem,
    )
    from ..models.user_analytics_response_user_info import UserAnalyticsResponseUserInfo

    d = dict(src_dict)
    user_info = UserAnalyticsResponseUserInfo.from_dict(d.pop("user_info"))

    graph_usage = UserAnalyticsResponseGraphUsage.from_dict(d.pop("graph_usage"))

    api_usage = UserAnalyticsResponseApiUsage.from_dict(d.pop("api_usage"))

    limits = UserAnalyticsResponseLimits.from_dict(d.pop("limits"))

    recent_activity = []
    _recent_activity = d.pop("recent_activity")
    for recent_activity_item_data in _recent_activity:
      recent_activity_item = UserAnalyticsResponseRecentActivityItem.from_dict(
        recent_activity_item_data
      )

      recent_activity.append(recent_activity_item)

    timestamp = d.pop("timestamp")

    user_analytics_response = cls(
      user_info=user_info,
      graph_usage=graph_usage,
      api_usage=api_usage,
      limits=limits,
      recent_activity=recent_activity,
      timestamp=timestamp,
    )

    user_analytics_response.additional_properties = d
    return user_analytics_response

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
