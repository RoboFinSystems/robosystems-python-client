from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGraphSummary")


@_attrs_define
class UserGraphSummary:
  """Summary of a single graph for user analytics.

  Attributes:
      graph_id (str): Graph database identifier
      role (str): User's role in this graph
      total_nodes (int): Total number of nodes
      total_relationships (int): Total number of relationships
      estimated_size_mb (float): Estimated database size in MB
      graph_name (Union[None, Unset, str]): Display name for the graph
      last_accessed (Union[None, Unset, str]): Last access timestamp
  """

  graph_id: str
  role: str
  total_nodes: int
  total_relationships: int
  estimated_size_mb: float
  graph_name: Union[None, Unset, str] = UNSET
  last_accessed: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    role = self.role

    total_nodes = self.total_nodes

    total_relationships = self.total_relationships

    estimated_size_mb = self.estimated_size_mb

    graph_name: Union[None, Unset, str]
    if isinstance(self.graph_name, Unset):
      graph_name = UNSET
    else:
      graph_name = self.graph_name

    last_accessed: Union[None, Unset, str]
    if isinstance(self.last_accessed, Unset):
      last_accessed = UNSET
    else:
      last_accessed = self.last_accessed

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "role": role,
        "total_nodes": total_nodes,
        "total_relationships": total_relationships,
        "estimated_size_mb": estimated_size_mb,
      }
    )
    if graph_name is not UNSET:
      field_dict["graph_name"] = graph_name
    if last_accessed is not UNSET:
      field_dict["last_accessed"] = last_accessed

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    role = d.pop("role")

    total_nodes = d.pop("total_nodes")

    total_relationships = d.pop("total_relationships")

    estimated_size_mb = d.pop("estimated_size_mb")

    def _parse_graph_name(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    graph_name = _parse_graph_name(d.pop("graph_name", UNSET))

    def _parse_last_accessed(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    last_accessed = _parse_last_accessed(d.pop("last_accessed", UNSET))

    user_graph_summary = cls(
      graph_id=graph_id,
      role=role,
      total_nodes=total_nodes,
      total_relationships=total_relationships,
      estimated_size_mb=estimated_size_mb,
      graph_name=graph_name,
      last_accessed=last_accessed,
    )

    user_graph_summary.additional_properties = d
    return user_graph_summary

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
