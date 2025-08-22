from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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

  Example:
      {'initial_entity': {'cik': '0001234567', 'name': 'Acme Corp', 'uri': 'https://acme.com'}, 'instance_tier':
          'standard', 'metadata': {'description': 'Main production graph', 'graph_name': 'Production System',
          'schema_extensions': ['roboledger']}, 'tags': ['production', 'finance']}

  Attributes:
      metadata (GraphMetadata): Metadata for graph creation.
      instance_tier (Union[Unset, str]): Instance tier: standard, enterprise, or premium Default: 'standard'.
      custom_schema (Union['CustomSchemaDefinition', None, Unset]): Custom schema definition to apply
      initial_entity (Union['InitialEntityData', None, Unset]): Optional initial entity to create in the graph. If
          provided, creates a entity-focused graph.
      tags (Union[Unset, list[str]]): Optional tags for organization
  """

  metadata: "GraphMetadata"
  instance_tier: Union[Unset, str] = "standard"
  custom_schema: Union["CustomSchemaDefinition", None, Unset] = UNSET
  initial_entity: Union["InitialEntityData", None, Unset] = UNSET
  tags: Union[Unset, list[str]] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.custom_schema_definition import CustomSchemaDefinition
    from ..models.initial_entity_data import InitialEntityData

    metadata = self.metadata.to_dict()

    instance_tier = self.instance_tier

    custom_schema: Union[None, Unset, dict[str, Any]]
    if isinstance(self.custom_schema, Unset):
      custom_schema = UNSET
    elif isinstance(self.custom_schema, CustomSchemaDefinition):
      custom_schema = self.custom_schema.to_dict()
    else:
      custom_schema = self.custom_schema

    initial_entity: Union[None, Unset, dict[str, Any]]
    if isinstance(self.initial_entity, Unset):
      initial_entity = UNSET
    elif isinstance(self.initial_entity, InitialEntityData):
      initial_entity = self.initial_entity.to_dict()
    else:
      initial_entity = self.initial_entity

    tags: Union[Unset, list[str]] = UNSET
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

    def _parse_custom_schema(
      data: object,
    ) -> Union["CustomSchemaDefinition", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        custom_schema_type_0 = CustomSchemaDefinition.from_dict(data)

        return custom_schema_type_0
      except:  # noqa: E722
        pass
      return cast(Union["CustomSchemaDefinition", None, Unset], data)

    custom_schema = _parse_custom_schema(d.pop("custom_schema", UNSET))

    def _parse_initial_entity(data: object) -> Union["InitialEntityData", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        initial_entity_type_0 = InitialEntityData.from_dict(data)

        return initial_entity_type_0
      except:  # noqa: E722
        pass
      return cast(Union["InitialEntityData", None, Unset], data)

    initial_entity = _parse_initial_entity(d.pop("initial_entity", UNSET))

    tags = cast(list[str], d.pop("tags", UNSET))

    create_graph_request = cls(
      metadata=metadata,
      instance_tier=instance_tier,
      custom_schema=custom_schema,
      initial_entity=initial_entity,
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
