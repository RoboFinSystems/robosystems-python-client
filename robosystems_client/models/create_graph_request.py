from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.custom_schema_definition import CustomSchemaDefinition
  from ..models.graph_metadata import GraphMetadata
  from ..models.initial_entity_data import InitialEntityData


T = TypeVar("T", bound="CreateGraphRequest")


@_attrs_define
class CreateGraphRequest:
  """Request model for creating a new graph.

  Use this to create either:
  - **Entity graphs**: Standard graphs with entity schema and optional extensions
  - **Custom graphs**: Generic graphs with fully custom schema definitions

      Attributes:
          metadata (GraphMetadata): Metadata for graph creation.
          instance_tier (str | Unset): Instance tier: ladybug-standard, ladybug-large, ladybug-xlarge, neo4j-community-
              large, neo4j-enterprise-xlarge Default: 'ladybug-standard'.
          custom_schema (CustomSchemaDefinition | None | Unset): Custom schema definition to apply. If provided, creates a
              generic custom graph. If omitted, creates an entity graph using schema_extensions.
          initial_entity (InitialEntityData | None | Unset): Optional initial entity to create in the graph. If provided
              with entity graph, populates the first entity node.
          create_entity (bool | Unset): Whether to create the entity node and upload initial data. Only applies when
              initial_entity is provided. Set to False to create graph without populating entity data (useful for file-based
              ingestion workflows). Default: True.
          tags (list[str] | Unset): Optional tags for organization
  """

  metadata: GraphMetadata
  instance_tier: str | Unset = "ladybug-standard"
  custom_schema: CustomSchemaDefinition | None | Unset = UNSET
  initial_entity: InitialEntityData | None | Unset = UNSET
  create_entity: bool | Unset = True
  tags: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.custom_schema_definition import CustomSchemaDefinition
    from ..models.initial_entity_data import InitialEntityData

    metadata = self.metadata.to_dict()

    instance_tier = self.instance_tier

    custom_schema: dict[str, Any] | None | Unset
    if isinstance(self.custom_schema, Unset):
      custom_schema = UNSET
    elif isinstance(self.custom_schema, CustomSchemaDefinition):
      custom_schema = self.custom_schema.to_dict()
    else:
      custom_schema = self.custom_schema

    initial_entity: dict[str, Any] | None | Unset
    if isinstance(self.initial_entity, Unset):
      initial_entity = UNSET
    elif isinstance(self.initial_entity, InitialEntityData):
      initial_entity = self.initial_entity.to_dict()
    else:
      initial_entity = self.initial_entity

    create_entity = self.create_entity

    tags: list[str] | Unset = UNSET
    if not isinstance(self.tags, Unset):
      tags = self.tags

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "metadata": metadata,
      }
    )
    if instance_tier is not UNSET:
      field_dict["instance_tier"] = instance_tier
    if custom_schema is not UNSET:
      field_dict["custom_schema"] = custom_schema
    if initial_entity is not UNSET:
      field_dict["initial_entity"] = initial_entity
    if create_entity is not UNSET:
      field_dict["create_entity"] = create_entity
    if tags is not UNSET:
      field_dict["tags"] = tags

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.custom_schema_definition import CustomSchemaDefinition
    from ..models.graph_metadata import GraphMetadata
    from ..models.initial_entity_data import InitialEntityData

    d = dict(src_dict)
    metadata = GraphMetadata.from_dict(d.pop("metadata"))

    instance_tier = d.pop("instance_tier", UNSET)

    def _parse_custom_schema(data: object) -> CustomSchemaDefinition | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        custom_schema_type_0 = CustomSchemaDefinition.from_dict(data)

        return custom_schema_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(CustomSchemaDefinition | None | Unset, data)

    custom_schema = _parse_custom_schema(d.pop("custom_schema", UNSET))

    def _parse_initial_entity(data: object) -> InitialEntityData | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        initial_entity_type_0 = InitialEntityData.from_dict(data)

        return initial_entity_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(InitialEntityData | None | Unset, data)

    initial_entity = _parse_initial_entity(d.pop("initial_entity", UNSET))

    create_entity = d.pop("create_entity", UNSET)

    tags = cast(list[str], d.pop("tags", UNSET))

    create_graph_request = cls(
      metadata=metadata,
      instance_tier=instance_tier,
      custom_schema=custom_schema,
      initial_entity=initial_entity,
      create_entity=create_entity,
      tags=tags,
    )

    create_graph_request.additional_properties = d
    return create_graph_request

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
