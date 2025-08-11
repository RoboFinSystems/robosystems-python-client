from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.user_graph_summary import UserGraphSummary
  from ..models.user_usage_summary_response_usage_vs_limits import (
    UserUsageSummaryResponseUsageVsLimits,
  )


T = TypeVar("T", bound="UserUsageSummaryResponse")


@_attrs_define
class UserUsageSummaryResponse:
  """Response model for user usage summary.

  Attributes:
      user_id (str): User identifier
      graph_count (int): Number of accessible graphs
      total_nodes (int): Total nodes across all graphs
      total_relationships (int): Total relationships across all graphs
      usage_vs_limits (UserUsageSummaryResponseUsageVsLimits): Usage compared to limits
      graphs (list['UserGraphSummary']): Summary of each graph
      timestamp (str): Summary generation timestamp
  """

  user_id: str
  graph_count: int
  total_nodes: int
  total_relationships: int
  usage_vs_limits: "UserUsageSummaryResponseUsageVsLimits"
  graphs: list["UserGraphSummary"]
  timestamp: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    user_id = self.user_id

    graph_count = self.graph_count

    total_nodes = self.total_nodes

    total_relationships = self.total_relationships

    usage_vs_limits = self.usage_vs_limits.to_dict()

    graphs = []
    for graphs_item_data in self.graphs:
      graphs_item = graphs_item_data.to_dict()
      graphs.append(graphs_item)

    timestamp = self.timestamp

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "user_id": user_id,
        "graph_count": graph_count,
        "total_nodes": total_nodes,
        "total_relationships": total_relationships,
        "usage_vs_limits": usage_vs_limits,
        "graphs": graphs,
        "timestamp": timestamp,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.user_graph_summary import UserGraphSummary
    from ..models.user_usage_summary_response_usage_vs_limits import (
      UserUsageSummaryResponseUsageVsLimits,
    )

    d = dict(src_dict)
    user_id = d.pop("user_id")

    graph_count = d.pop("graph_count")

    total_nodes = d.pop("total_nodes")

    total_relationships = d.pop("total_relationships")

    usage_vs_limits = UserUsageSummaryResponseUsageVsLimits.from_dict(
      d.pop("usage_vs_limits")
    )

    graphs = []
    _graphs = d.pop("graphs")
    for graphs_item_data in _graphs:
      graphs_item = UserGraphSummary.from_dict(graphs_item_data)

      graphs.append(graphs_item)

    timestamp = d.pop("timestamp")

    user_usage_summary_response = cls(
      user_id=user_id,
      graph_count=graph_count,
      total_nodes=total_nodes,
      total_relationships=total_relationships,
      usage_vs_limits=usage_vs_limits,
      graphs=graphs,
      timestamp=timestamp,
    )

    user_usage_summary_response.additional_properties = d
    return user_usage_summary_response

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
