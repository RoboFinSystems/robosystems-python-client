from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
      is_repository (Union[Unset, bool]): Whether this is a shared repository (vs user graph) Default: False.
      repository_type (Union[None, Unset, str]): Repository type if isRepository=true
  """

  graph_id: str
  graph_name: str
  role: str
  is_selected: bool
  created_at: str
  is_repository: Union[Unset, bool] = False
  repository_type: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    graph_name = self.graph_name

    role = self.role

    is_selected = self.is_selected

    created_at = self.created_at

    is_repository = self.is_repository

    repository_type: Union[None, Unset, str]
    if isinstance(self.repository_type, Unset):
      repository_type = UNSET
    else:
      repository_type = self.repository_type

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

    def _parse_repository_type(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    repository_type = _parse_repository_type(d.pop("repositoryType", UNSET))

    graph_info = cls(
      graph_id=graph_id,
      graph_name=graph_name,
      role=role,
      is_selected=is_selected,
      created_at=created_at,
      is_repository=is_repository,
      repository_type=repository_type,
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
