from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphMetadata")


@_attrs_define
class GraphMetadata:
  """Metadata for graph creation.

  Attributes:
      graph_name (str): Display name for the graph
      description (Union[None, Unset, str]): Optional description
      schema_extensions (Union[Unset, list[str]]): Schema extensions to enable
      tags (Union[Unset, list[str]]): Tags for organizing graphs
  """

  graph_name: str
  description: Union[None, Unset, str] = UNSET
  schema_extensions: Union[Unset, list[str]] = UNSET
  tags: Union[Unset, list[str]] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_name = self.graph_name

    description: Union[None, Unset, str]
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    schema_extensions: Union[Unset, list[str]] = UNSET
    if not isinstance(self.schema_extensions, Unset):
      schema_extensions = self.schema_extensions

    tags: Union[Unset, list[str]] = UNSET
    if not isinstance(self.tags, Unset):
      tags = self.tags

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_name": graph_name,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if schema_extensions is not UNSET:
      field_dict["schema_extensions"] = schema_extensions
    if tags is not UNSET:
      field_dict["tags"] = tags

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_name = d.pop("graph_name")

    def _parse_description(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    description = _parse_description(d.pop("description", UNSET))

    schema_extensions = cast(list[str], d.pop("schema_extensions", UNSET))

    tags = cast(list[str], d.pop("tags", UNSET))

    graph_metadata = cls(
      graph_name=graph_name,
      description=description,
      schema_extensions=schema_extensions,
      tags=tags,
    )

    graph_metadata.additional_properties = d
    return graph_metadata

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
