from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.custom_schema_definition_metadata import CustomSchemaDefinitionMetadata
  from ..models.custom_schema_definition_nodes_item import (
    CustomSchemaDefinitionNodesItem,
  )
  from ..models.custom_schema_definition_relationships_item import (
    CustomSchemaDefinitionRelationshipsItem,
  )


T = TypeVar("T", bound="CustomSchemaDefinition")


@_attrs_define
class CustomSchemaDefinition:
  """Custom schema definition for custom graphs.

  Attributes:
      name (str): Schema name
      version (Union[Unset, str]): Schema version Default: '1.0.0'.
      description (Union[None, Unset, str]): Schema description
      extends (Union[None, Unset, str]): Base schema to extend (e.g., 'base')
      nodes (Union[Unset, list['CustomSchemaDefinitionNodesItem']]): List of node definitions with properties
      relationships (Union[Unset, list['CustomSchemaDefinitionRelationshipsItem']]): List of relationship definitions
      metadata (Union[Unset, CustomSchemaDefinitionMetadata]): Additional schema metadata
  """

  name: str
  version: Union[Unset, str] = "1.0.0"
  description: Union[None, Unset, str] = UNSET
  extends: Union[None, Unset, str] = UNSET
  nodes: Union[Unset, list["CustomSchemaDefinitionNodesItem"]] = UNSET
  relationships: Union[Unset, list["CustomSchemaDefinitionRelationshipsItem"]] = UNSET
  metadata: Union[Unset, "CustomSchemaDefinitionMetadata"] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    version = self.version

    description: Union[None, Unset, str]
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    extends: Union[None, Unset, str]
    if isinstance(self.extends, Unset):
      extends = UNSET
    else:
      extends = self.extends

    nodes: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(self.nodes, Unset):
      nodes = []
      for nodes_item_data in self.nodes:
        nodes_item = nodes_item_data.to_dict()
        nodes.append(nodes_item)

    relationships: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(self.relationships, Unset):
      relationships = []
      for relationships_item_data in self.relationships:
        relationships_item = relationships_item_data.to_dict()
        relationships.append(relationships_item)

    metadata: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(self.metadata, Unset):
      metadata = self.metadata.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
      }
    )
    if version is not UNSET:
      field_dict["version"] = version
    if description is not UNSET:
      field_dict["description"] = description
    if extends is not UNSET:
      field_dict["extends"] = extends
    if nodes is not UNSET:
      field_dict["nodes"] = nodes
    if relationships is not UNSET:
      field_dict["relationships"] = relationships
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.custom_schema_definition_metadata import (
      CustomSchemaDefinitionMetadata,
    )
    from ..models.custom_schema_definition_nodes_item import (
      CustomSchemaDefinitionNodesItem,
    )
    from ..models.custom_schema_definition_relationships_item import (
      CustomSchemaDefinitionRelationshipsItem,
    )

    d = dict(src_dict)
    name = d.pop("name")

    version = d.pop("version", UNSET)

    def _parse_description(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_extends(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    extends = _parse_extends(d.pop("extends", UNSET))

    nodes = []
    _nodes = d.pop("nodes", UNSET)
    for nodes_item_data in _nodes or []:
      nodes_item = CustomSchemaDefinitionNodesItem.from_dict(nodes_item_data)

      nodes.append(nodes_item)

    relationships = []
    _relationships = d.pop("relationships", UNSET)
    for relationships_item_data in _relationships or []:
      relationships_item = CustomSchemaDefinitionRelationshipsItem.from_dict(
        relationships_item_data
      )

      relationships.append(relationships_item)

    _metadata = d.pop("metadata", UNSET)
    metadata: Union[Unset, CustomSchemaDefinitionMetadata]
    if isinstance(_metadata, Unset):
      metadata = UNSET
    else:
      metadata = CustomSchemaDefinitionMetadata.from_dict(_metadata)

    custom_schema_definition = cls(
      name=name,
      version=version,
      description=description,
      extends=extends,
      nodes=nodes,
      relationships=relationships,
      metadata=metadata,
    )

    custom_schema_definition.additional_properties = d
    return custom_schema_definition

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
