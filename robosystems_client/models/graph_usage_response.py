from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.graph_usage_response_query_statistics import (
    GraphUsageResponseQueryStatistics,
  )
  from ..models.graph_usage_response_recent_activity import (
    GraphUsageResponseRecentActivity,
  )
  from ..models.graph_usage_response_storage_usage import GraphUsageResponseStorageUsage


T = TypeVar("T", bound="GraphUsageResponse")


@_attrs_define
class GraphUsageResponse:
  """Response model for graph usage statistics.

  Attributes:
      graph_id (str): Graph database identifier
      storage_usage (GraphUsageResponseStorageUsage): Storage usage information
      query_statistics (GraphUsageResponseQueryStatistics): Query statistics
      recent_activity (GraphUsageResponseRecentActivity): Recent activity summary
      timestamp (str): Usage collection timestamp
  """

  graph_id: str
  storage_usage: "GraphUsageResponseStorageUsage"
  query_statistics: "GraphUsageResponseQueryStatistics"
  recent_activity: "GraphUsageResponseRecentActivity"
  timestamp: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    storage_usage = self.storage_usage.to_dict()

    query_statistics = self.query_statistics.to_dict()

    recent_activity = self.recent_activity.to_dict()

    timestamp = self.timestamp

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "storage_usage": storage_usage,
        "query_statistics": query_statistics,
        "recent_activity": recent_activity,
        "timestamp": timestamp,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_usage_response_query_statistics import (
      GraphUsageResponseQueryStatistics,
    )
    from ..models.graph_usage_response_recent_activity import (
      GraphUsageResponseRecentActivity,
    )
    from ..models.graph_usage_response_storage_usage import (
      GraphUsageResponseStorageUsage,
    )

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    storage_usage = GraphUsageResponseStorageUsage.from_dict(d.pop("storage_usage"))

    query_statistics = GraphUsageResponseQueryStatistics.from_dict(
      d.pop("query_statistics")
    )

    recent_activity = GraphUsageResponseRecentActivity.from_dict(
      d.pop("recent_activity")
    )

    timestamp = d.pop("timestamp")

    graph_usage_response = cls(
      graph_id=graph_id,
      storage_usage=storage_usage,
      query_statistics=query_statistics,
      recent_activity=recent_activity,
      timestamp=timestamp,
    )

    graph_usage_response.additional_properties = d
    return graph_usage_response

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
