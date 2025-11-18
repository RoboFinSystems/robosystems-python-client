from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
  """Custom schema definition for generic graphs.

  This model allows you to define custom node types, relationship types, and properties
  for graphs that don't fit the standard entity-based schema. Perfect for domain-specific
  applications like inventory systems, org charts, project management, etc.

      Attributes:
          name (str): Schema name
          version (str | Unset): Schema version Default: '1.0.0'.
          description (None | str | Unset): Schema description
          extends (None | str | Unset): Base schema to extend (e.g., 'base' for common utilities)
          nodes (list[CustomSchemaDefinitionNodesItem] | Unset): List of node definitions with properties
          relationships (list[CustomSchemaDefinitionRelationshipsItem] | Unset): List of relationship definitions
          metadata (CustomSchemaDefinitionMetadata | Unset): Additional schema metadata
  """

  name: str
  version: str | Unset = "1.0.0"
  description: None | str | Unset = UNSET
  extends: None | str | Unset = UNSET
  nodes: list[CustomSchemaDefinitionNodesItem] | Unset = UNSET
  relationships: list[CustomSchemaDefinitionRelationshipsItem] | Unset = UNSET
  metadata: CustomSchemaDefinitionMetadata | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    version = self.version

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    extends: None | str | Unset
    if isinstance(self.extends, Unset):
      extends = UNSET
    else:
      extends = self.extends

    nodes: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.nodes, Unset):
      nodes = []
      for nodes_item_data in self.nodes:
        nodes_item = nodes_item_data.to_dict()
        nodes.append(nodes_item)

    relationships: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.relationships, Unset):
      relationships = []
      for relationships_item_data in self.relationships:
        relationships_item = relationships_item_data.to_dict()
        relationships.append(relationships_item)

    metadata: dict[str, Any] | Unset = UNSET
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

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_extends(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    extends = _parse_extends(d.pop("extends", UNSET))

    _nodes = d.pop("nodes", UNSET)
    nodes: list[CustomSchemaDefinitionNodesItem] | Unset = UNSET
    if _nodes is not UNSET:
      nodes = []
      for nodes_item_data in _nodes:
        nodes_item = CustomSchemaDefinitionNodesItem.from_dict(nodes_item_data)

        nodes.append(nodes_item)

    _relationships = d.pop("relationships", UNSET)
    relationships: list[CustomSchemaDefinitionRelationshipsItem] | Unset = UNSET
    if _relationships is not UNSET:
      relationships = []
      for relationships_item_data in _relationships:
        relationships_item = CustomSchemaDefinitionRelationshipsItem.from_dict(
          relationships_item_data
        )

        relationships.append(relationships_item)

    _metadata = d.pop("metadata", UNSET)
    metadata: CustomSchemaDefinitionMetadata | Unset
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
