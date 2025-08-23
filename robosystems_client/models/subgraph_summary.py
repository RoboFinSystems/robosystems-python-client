import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subgraph_type import SubgraphType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubgraphSummary")


@_attrs_define
class SubgraphSummary:
  """Summary model for listing subgraphs.

  Attributes:
      graph_id (str): Full subgraph identifier
      subgraph_name (str): Alphanumeric name
      display_name (str): Human-readable name
      subgraph_type (SubgraphType): Types of subgraphs.
      status (str): Current status
      created_at (datetime.datetime): Creation timestamp
      size_mb (Union[None, Unset, float]): Size in megabytes
      last_accessed (Union[None, Unset, datetime.datetime]): Last access timestamp
  """

  graph_id: str
  subgraph_name: str
  display_name: str
  subgraph_type: SubgraphType
  status: str
  created_at: datetime.datetime
  size_mb: Union[None, Unset, float] = UNSET
  last_accessed: Union[None, Unset, datetime.datetime] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    subgraph_name = self.subgraph_name

    display_name = self.display_name

    subgraph_type = self.subgraph_type.value

    status = self.status

    created_at = self.created_at.isoformat()

    size_mb: Union[None, Unset, float]
    if isinstance(self.size_mb, Unset):
      size_mb = UNSET
    else:
      size_mb = self.size_mb

    last_accessed: Union[None, Unset, str]
    if isinstance(self.last_accessed, Unset):
      last_accessed = UNSET
    elif isinstance(self.last_accessed, datetime.datetime):
      last_accessed = self.last_accessed.isoformat()
    else:
      last_accessed = self.last_accessed

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "subgraph_name": subgraph_name,
        "display_name": display_name,
        "subgraph_type": subgraph_type,
        "status": status,
        "created_at": created_at,
      }
    )
    if size_mb is not UNSET:
      field_dict["size_mb"] = size_mb
    if last_accessed is not UNSET:
      field_dict["last_accessed"] = last_accessed

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    subgraph_name = d.pop("subgraph_name")

    display_name = d.pop("display_name")

    subgraph_type = SubgraphType(d.pop("subgraph_type"))

    status = d.pop("status")

    created_at = isoparse(d.pop("created_at"))

    def _parse_size_mb(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    size_mb = _parse_size_mb(d.pop("size_mb", UNSET))

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

    subgraph_summary = cls(
      graph_id=graph_id,
      subgraph_name=subgraph_name,
      display_name=display_name,
      subgraph_type=subgraph_type,
      status=status,
      created_at=created_at,
      size_mb=size_mb,
      last_accessed=last_accessed,
    )

    subgraph_summary.additional_properties = d
    return subgraph_summary

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
