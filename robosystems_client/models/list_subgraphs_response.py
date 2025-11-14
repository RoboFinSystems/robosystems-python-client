from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.subgraph_summary import SubgraphSummary


T = TypeVar("T", bound="ListSubgraphsResponse")


@_attrs_define
class ListSubgraphsResponse:
  """Response model for listing subgraphs.

  Attributes:
      parent_graph_id (str): Parent graph identifier
      parent_graph_name (str): Parent graph name
      parent_graph_tier (str): Parent graph tier
      subgraphs_enabled (bool): Whether subgraphs are enabled for this tier (requires Kuzu Large/XLarge or Neo4j
          Enterprise XLarge)
      subgraph_count (int): Total number of subgraphs
      subgraphs (list['SubgraphSummary']): List of subgraphs
      max_subgraphs (Union[None, Unset, int]): Maximum allowed subgraphs for this tier (None = unlimited)
      total_size_mb (Union[None, Unset, float]): Combined size of all subgraphs in megabytes
  """

  parent_graph_id: str
  parent_graph_name: str
  parent_graph_tier: str
  subgraphs_enabled: bool
  subgraph_count: int
  subgraphs: list["SubgraphSummary"]
  max_subgraphs: Union[None, Unset, int] = UNSET
  total_size_mb: Union[None, Unset, float] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    parent_graph_id = self.parent_graph_id

    parent_graph_name = self.parent_graph_name

    parent_graph_tier = self.parent_graph_tier

    subgraphs_enabled = self.subgraphs_enabled

    subgraph_count = self.subgraph_count

    subgraphs = []
    for subgraphs_item_data in self.subgraphs:
      subgraphs_item = subgraphs_item_data.to_dict()
      subgraphs.append(subgraphs_item)

    max_subgraphs: Union[None, Unset, int]
    if isinstance(self.max_subgraphs, Unset):
      max_subgraphs = UNSET
    else:
      max_subgraphs = self.max_subgraphs

    total_size_mb: Union[None, Unset, float]
    if isinstance(self.total_size_mb, Unset):
      total_size_mb = UNSET
    else:
      total_size_mb = self.total_size_mb

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "parent_graph_id": parent_graph_id,
        "parent_graph_name": parent_graph_name,
        "parent_graph_tier": parent_graph_tier,
        "subgraphs_enabled": subgraphs_enabled,
        "subgraph_count": subgraph_count,
        "subgraphs": subgraphs,
      }
    )
    if max_subgraphs is not UNSET:
      field_dict["max_subgraphs"] = max_subgraphs
    if total_size_mb is not UNSET:
      field_dict["total_size_mb"] = total_size_mb

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.subgraph_summary import SubgraphSummary

    d = dict(src_dict)
    parent_graph_id = d.pop("parent_graph_id")

    parent_graph_name = d.pop("parent_graph_name")

    parent_graph_tier = d.pop("parent_graph_tier")

    subgraphs_enabled = d.pop("subgraphs_enabled")

    subgraph_count = d.pop("subgraph_count")

    subgraphs = []
    _subgraphs = d.pop("subgraphs")
    for subgraphs_item_data in _subgraphs:
      subgraphs_item = SubgraphSummary.from_dict(subgraphs_item_data)

      subgraphs.append(subgraphs_item)

    def _parse_max_subgraphs(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    max_subgraphs = _parse_max_subgraphs(d.pop("max_subgraphs", UNSET))

    def _parse_total_size_mb(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    total_size_mb = _parse_total_size_mb(d.pop("total_size_mb", UNSET))

    list_subgraphs_response = cls(
      parent_graph_id=parent_graph_id,
      parent_graph_name=parent_graph_name,
      parent_graph_tier=parent_graph_tier,
      subgraphs_enabled=subgraphs_enabled,
      subgraph_count=subgraph_count,
      subgraphs=subgraphs,
      max_subgraphs=max_subgraphs,
      total_size_mb=total_size_mb,
    )

    list_subgraphs_response.additional_properties = d
    return list_subgraphs_response

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
