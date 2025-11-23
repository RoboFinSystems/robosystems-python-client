from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphInfo")


@_attrs_define
class GraphInfo:
  """Graph information for user.

  Attributes:
      graph_id (str): Graph database identifier
      graph_name (str): Display name for the graph
      role (str): User's role/access level
      is_selected (bool): Whether this is the currently selected graph
      created_at (str): Creation timestamp
      is_repository (bool | Unset): Whether this is a shared repository (vs user graph) Default: False.
      repository_type (None | str | Unset): Repository type if isRepository=true
      schema_extensions (list[str] | Unset): List of schema extensions installed on this graph
      is_subgraph (bool | Unset): Whether this is a subgraph (vs a main graph) Default: False.
      parent_graph_id (None | str | Unset): Parent graph ID if this is a subgraph
      graph_type (str | Unset): Type of graph: generic, entity, or repository Default: 'entity'.
  """

  graph_id: str
  graph_name: str
  role: str
  is_selected: bool
  created_at: str
  is_repository: bool | Unset = False
  repository_type: None | str | Unset = UNSET
  schema_extensions: list[str] | Unset = UNSET
  is_subgraph: bool | Unset = False
  parent_graph_id: None | str | Unset = UNSET
  graph_type: str | Unset = "entity"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    graph_name = self.graph_name

    role = self.role

    is_selected = self.is_selected

    created_at = self.created_at

    is_repository = self.is_repository

    repository_type: None | str | Unset
    if isinstance(self.repository_type, Unset):
      repository_type = UNSET
    else:
      repository_type = self.repository_type

    schema_extensions: list[str] | Unset = UNSET
    if not isinstance(self.schema_extensions, Unset):
      schema_extensions = self.schema_extensions

    is_subgraph = self.is_subgraph

    parent_graph_id: None | str | Unset
    if isinstance(self.parent_graph_id, Unset):
      parent_graph_id = UNSET
    else:
      parent_graph_id = self.parent_graph_id

    graph_type = self.graph_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graphId": graph_id,
        "graphName": graph_name,
        "role": role,
        "isSelected": is_selected,
        "createdAt": created_at,
      }
    )
    if is_repository is not UNSET:
      field_dict["isRepository"] = is_repository
    if repository_type is not UNSET:
      field_dict["repositoryType"] = repository_type
    if schema_extensions is not UNSET:
      field_dict["schemaExtensions"] = schema_extensions
    if is_subgraph is not UNSET:
      field_dict["isSubgraph"] = is_subgraph
    if parent_graph_id is not UNSET:
      field_dict["parentGraphId"] = parent_graph_id
    if graph_type is not UNSET:
      field_dict["graphType"] = graph_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graphId")

    graph_name = d.pop("graphName")

    role = d.pop("role")

    is_selected = d.pop("isSelected")

    created_at = d.pop("createdAt")

    is_repository = d.pop("isRepository", UNSET)

    def _parse_repository_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    repository_type = _parse_repository_type(d.pop("repositoryType", UNSET))

    schema_extensions = cast(list[str], d.pop("schemaExtensions", UNSET))

    is_subgraph = d.pop("isSubgraph", UNSET)

    def _parse_parent_graph_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_graph_id = _parse_parent_graph_id(d.pop("parentGraphId", UNSET))

    graph_type = d.pop("graphType", UNSET)

    graph_info = cls(
      graph_id=graph_id,
      graph_name=graph_name,
      role=role,
      is_selected=is_selected,
      created_at=created_at,
      is_repository=is_repository,
      repository_type=repository_type,
      schema_extensions=schema_extensions,
      is_subgraph=is_subgraph,
      parent_graph_id=parent_graph_id,
      graph_type=graph_type,
    )

    graph_info.additional_properties = d
    return graph_info

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
