from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.graph_metrics_response_estimated_size import (
    GraphMetricsResponseEstimatedSize,
  )
  from ..models.graph_metrics_response_health_status import (
    GraphMetricsResponseHealthStatus,
  )
  from ..models.graph_metrics_response_node_counts import GraphMetricsResponseNodeCounts
  from ..models.graph_metrics_response_relationship_counts import (
    GraphMetricsResponseRelationshipCounts,
  )


T = TypeVar("T", bound="GraphMetricsResponse")


@_attrs_define
class GraphMetricsResponse:
  """Response model for graph metrics.

  Attributes:
      graph_id (str): Graph database identifier
      timestamp (str): Metrics collection timestamp
      total_nodes (int): Total number of nodes
      total_relationships (int): Total number of relationships
      node_counts (GraphMetricsResponseNodeCounts): Node counts by label
      relationship_counts (GraphMetricsResponseRelationshipCounts): Relationship counts by type
      estimated_size (GraphMetricsResponseEstimatedSize): Database size estimates
      health_status (GraphMetricsResponseHealthStatus): Database health information
      graph_name (Union[None, Unset, str]): Display name for the graph
      user_role (Union[None, Unset, str]): User's role in this graph
  """

  graph_id: str
  timestamp: str
  total_nodes: int
  total_relationships: int
  node_counts: "GraphMetricsResponseNodeCounts"
  relationship_counts: "GraphMetricsResponseRelationshipCounts"
  estimated_size: "GraphMetricsResponseEstimatedSize"
  health_status: "GraphMetricsResponseHealthStatus"
  graph_name: Union[None, Unset, str] = UNSET
  user_role: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    timestamp = self.timestamp

    total_nodes = self.total_nodes

    total_relationships = self.total_relationships

    node_counts = self.node_counts.to_dict()

    relationship_counts = self.relationship_counts.to_dict()

    estimated_size = self.estimated_size.to_dict()

    health_status = self.health_status.to_dict()

    graph_name: Union[None, Unset, str]
    if isinstance(self.graph_name, Unset):
      graph_name = UNSET
    else:
      graph_name = self.graph_name

    user_role: Union[None, Unset, str]
    if isinstance(self.user_role, Unset):
      user_role = UNSET
    else:
      user_role = self.user_role

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "timestamp": timestamp,
        "total_nodes": total_nodes,
        "total_relationships": total_relationships,
        "node_counts": node_counts,
        "relationship_counts": relationship_counts,
        "estimated_size": estimated_size,
        "health_status": health_status,
      }
    )
    if graph_name is not UNSET:
      field_dict["graph_name"] = graph_name
    if user_role is not UNSET:
      field_dict["user_role"] = user_role

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_metrics_response_estimated_size import (
      GraphMetricsResponseEstimatedSize,
    )
    from ..models.graph_metrics_response_health_status import (
      GraphMetricsResponseHealthStatus,
    )
    from ..models.graph_metrics_response_node_counts import (
      GraphMetricsResponseNodeCounts,
    )
    from ..models.graph_metrics_response_relationship_counts import (
      GraphMetricsResponseRelationshipCounts,
    )

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    timestamp = d.pop("timestamp")

    total_nodes = d.pop("total_nodes")

    total_relationships = d.pop("total_relationships")

    node_counts = GraphMetricsResponseNodeCounts.from_dict(d.pop("node_counts"))

    relationship_counts = GraphMetricsResponseRelationshipCounts.from_dict(
      d.pop("relationship_counts")
    )

    estimated_size = GraphMetricsResponseEstimatedSize.from_dict(
      d.pop("estimated_size")
    )

    health_status = GraphMetricsResponseHealthStatus.from_dict(d.pop("health_status"))

    def _parse_graph_name(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    graph_name = _parse_graph_name(d.pop("graph_name", UNSET))

    def _parse_user_role(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    user_role = _parse_user_role(d.pop("user_role", UNSET))

    graph_metrics_response = cls(
      graph_id=graph_id,
      timestamp=timestamp,
      total_nodes=total_nodes,
      total_relationships=total_relationships,
      node_counts=node_counts,
      relationship_counts=relationship_counts,
      estimated_size=estimated_size,
      health_status=health_status,
      graph_name=graph_name,
      user_role=user_role,
    )

    graph_metrics_response.additional_properties = d
    return graph_metrics_response

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
