from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.graph_info import GraphInfo


T = TypeVar("T", bound="UserGraphsResponse")


@_attrs_define
class UserGraphsResponse:
  """User graphs response model.

  Attributes:
      graphs (list['GraphInfo']): List of accessible graphs
      selected_graph_id (Union[None, Unset, str]): Currently selected graph ID
  """

  graphs: list["GraphInfo"]
  selected_graph_id: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graphs = []
    for graphs_item_data in self.graphs:
      graphs_item = graphs_item_data.to_dict()
      graphs.append(graphs_item)

    selected_graph_id: Union[None, Unset, str]
    if isinstance(self.selected_graph_id, Unset):
      selected_graph_id = UNSET
    else:
      selected_graph_id = self.selected_graph_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graphs": graphs,
      }
    )
    if selected_graph_id is not UNSET:
      field_dict["selectedGraphId"] = selected_graph_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_info import GraphInfo

    d = dict(src_dict)
    graphs = []
    _graphs = d.pop("graphs")
    for graphs_item_data in _graphs:
      graphs_item = GraphInfo.from_dict(graphs_item_data)

      graphs.append(graphs_item)

    def _parse_selected_graph_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    selected_graph_id = _parse_selected_graph_id(d.pop("selectedGraphId", UNSET))

    user_graphs_response = cls(
      graphs=graphs,
      selected_graph_id=selected_graph_id,
    )

    user_graphs_response.additional_properties = d
    return user_graphs_response

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
