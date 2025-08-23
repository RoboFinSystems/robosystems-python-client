import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subgraph_type import SubgraphType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.subgraph_response_metadata_type_0 import SubgraphResponseMetadataType0


T = TypeVar("T", bound="SubgraphResponse")


@_attrs_define
class SubgraphResponse:
  """Response model for a subgraph.

  Attributes:
      graph_id (str): Full subgraph identifier (e.g., kg123_dev)
      parent_graph_id (str): Parent graph identifier
      subgraph_index (int): Numeric index of the subgraph
      subgraph_name (str): Alphanumeric name of the subgraph
      display_name (str): Human-readable display name
      subgraph_type (SubgraphType): Types of subgraphs.
      status (str): Current status of the subgraph
      created_at (datetime.datetime): When the subgraph was created
      updated_at (datetime.datetime): When the subgraph was last updated
      description (Union[None, Unset, str]): Description of the subgraph's purpose
      size_mb (Union[None, Unset, float]): Size of the subgraph database in megabytes
      node_count (Union[None, Unset, int]): Number of nodes in the subgraph
      edge_count (Union[None, Unset, int]): Number of edges in the subgraph
      last_accessed (Union[None, Unset, datetime.datetime]): When the subgraph was last accessed
      metadata (Union['SubgraphResponseMetadataType0', None, Unset]): Additional metadata for the subgraph
  """

  graph_id: str
  parent_graph_id: str
  subgraph_index: int
  subgraph_name: str
  display_name: str
  subgraph_type: SubgraphType
  status: str
  created_at: datetime.datetime
  updated_at: datetime.datetime
  description: Union[None, Unset, str] = UNSET
  size_mb: Union[None, Unset, float] = UNSET
  node_count: Union[None, Unset, int] = UNSET
  edge_count: Union[None, Unset, int] = UNSET
  last_accessed: Union[None, Unset, datetime.datetime] = UNSET
  metadata: Union["SubgraphResponseMetadataType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.subgraph_response_metadata_type_0 import SubgraphResponseMetadataType0

    graph_id = self.graph_id

    parent_graph_id = self.parent_graph_id

    subgraph_index = self.subgraph_index

    subgraph_name = self.subgraph_name

    display_name = self.display_name

    subgraph_type = self.subgraph_type.value

    status = self.status

    created_at = self.created_at.isoformat()

    updated_at = self.updated_at.isoformat()

    description: Union[None, Unset, str]
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    size_mb: Union[None, Unset, float]
    if isinstance(self.size_mb, Unset):
      size_mb = UNSET
    else:
      size_mb = self.size_mb

    node_count: Union[None, Unset, int]
    if isinstance(self.node_count, Unset):
      node_count = UNSET
    else:
      node_count = self.node_count

    edge_count: Union[None, Unset, int]
    if isinstance(self.edge_count, Unset):
      edge_count = UNSET
    else:
      edge_count = self.edge_count

    last_accessed: Union[None, Unset, str]
    if isinstance(self.last_accessed, Unset):
      last_accessed = UNSET
    elif isinstance(self.last_accessed, datetime.datetime):
      last_accessed = self.last_accessed.isoformat()
    else:
      last_accessed = self.last_accessed

    metadata: Union[None, Unset, dict[str, Any]]
    if isinstance(self.metadata, Unset):
      metadata = UNSET
    elif isinstance(self.metadata, SubgraphResponseMetadataType0):
      metadata = self.metadata.to_dict()
    else:
      metadata = self.metadata

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "parent_graph_id": parent_graph_id,
        "subgraph_index": subgraph_index,
        "subgraph_name": subgraph_name,
        "display_name": display_name,
        "subgraph_type": subgraph_type,
        "status": status,
        "created_at": created_at,
        "updated_at": updated_at,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if size_mb is not UNSET:
      field_dict["size_mb"] = size_mb
    if node_count is not UNSET:
      field_dict["node_count"] = node_count
    if edge_count is not UNSET:
      field_dict["edge_count"] = edge_count
    if last_accessed is not UNSET:
      field_dict["last_accessed"] = last_accessed
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.subgraph_response_metadata_type_0 import SubgraphResponseMetadataType0

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    parent_graph_id = d.pop("parent_graph_id")

    subgraph_index = d.pop("subgraph_index")

    subgraph_name = d.pop("subgraph_name")

    display_name = d.pop("display_name")

    subgraph_type = SubgraphType(d.pop("subgraph_type"))

    status = d.pop("status")

    created_at = isoparse(d.pop("created_at"))

    updated_at = isoparse(d.pop("updated_at"))

    def _parse_description(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_size_mb(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    size_mb = _parse_size_mb(d.pop("size_mb", UNSET))

    def _parse_node_count(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    node_count = _parse_node_count(d.pop("node_count", UNSET))

    def _parse_edge_count(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    edge_count = _parse_edge_count(d.pop("edge_count", UNSET))

    def _parse_last_accessed(data: object) -> Union[None, Unset, datetime.datetime]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        last_accessed_type_0 = isoparse(data)

        return last_accessed_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, datetime.datetime], data)

    last_accessed = _parse_last_accessed(d.pop("last_accessed", UNSET))

    def _parse_metadata(
      data: object,
    ) -> Union["SubgraphResponseMetadataType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        metadata_type_0 = SubgraphResponseMetadataType0.from_dict(data)

        return metadata_type_0
      except:  # noqa: E722
        pass
      return cast(Union["SubgraphResponseMetadataType0", None, Unset], data)

    metadata = _parse_metadata(d.pop("metadata", UNSET))

    subgraph_response = cls(
      graph_id=graph_id,
      parent_graph_id=parent_graph_id,
      subgraph_index=subgraph_index,
      subgraph_name=subgraph_name,
      display_name=display_name,
      subgraph_type=subgraph_type,
      status=status,
      created_at=created_at,
      updated_at=updated_at,
      description=description,
      size_mb=size_mb,
      node_count=node_count,
      edge_count=edge_count,
      last_accessed=last_accessed,
      metadata=metadata,
    )

    subgraph_response.additional_properties = d
    return subgraph_response

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
