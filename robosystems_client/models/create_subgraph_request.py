from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subgraph_type import SubgraphType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_subgraph_request_metadata_type_0 import (
    CreateSubgraphRequestMetadataType0,
  )


T = TypeVar("T", bound="CreateSubgraphRequest")


@_attrs_define
class CreateSubgraphRequest:
  """Request model for creating a subgraph.

  Attributes:
      name (str): Alphanumeric name for the subgraph (e.g., dev, staging, prod1)
      display_name (str): Human-readable display name for the subgraph
      description (Union[None, Unset, str]): Optional description of the subgraph's purpose
      schema_extensions (Union[None, Unset, list[str]]): Schema extensions to include (inherits from parent by
          default)
      subgraph_type (Union[Unset, SubgraphType]): Types of subgraphs.
      metadata (Union['CreateSubgraphRequestMetadataType0', None, Unset]): Additional metadata for the subgraph
  """

  name: str
  display_name: str
  description: Union[None, Unset, str] = UNSET
  schema_extensions: Union[None, Unset, list[str]] = UNSET
  subgraph_type: Union[Unset, SubgraphType] = UNSET
  metadata: Union["CreateSubgraphRequestMetadataType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.create_subgraph_request_metadata_type_0 import (
      CreateSubgraphRequestMetadataType0,
    )

    name = self.name

    display_name = self.display_name

    description: Union[None, Unset, str]
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    schema_extensions: Union[None, Unset, list[str]]
    if isinstance(self.schema_extensions, Unset):
      schema_extensions = UNSET
    elif isinstance(self.schema_extensions, list):
      schema_extensions = self.schema_extensions

    else:
      schema_extensions = self.schema_extensions

    subgraph_type: Union[Unset, str] = UNSET
    if not isinstance(self.subgraph_type, Unset):
      subgraph_type = self.subgraph_type.value

    metadata: Union[None, Unset, dict[str, Any]]
    if isinstance(self.metadata, Unset):
      metadata = UNSET
    elif isinstance(self.metadata, CreateSubgraphRequestMetadataType0):
      metadata = self.metadata.to_dict()
    else:
      metadata = self.metadata

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "display_name": display_name,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if schema_extensions is not UNSET:
      field_dict["schema_extensions"] = schema_extensions
    if subgraph_type is not UNSET:
      field_dict["subgraph_type"] = subgraph_type
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.create_subgraph_request_metadata_type_0 import (
      CreateSubgraphRequestMetadataType0,
    )

    d = dict(src_dict)
    name = d.pop("name")

    display_name = d.pop("display_name")

    def _parse_description(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_schema_extensions(data: object) -> Union[None, Unset, list[str]]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        schema_extensions_type_0 = cast(list[str], data)

        return schema_extensions_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, list[str]], data)

    schema_extensions = _parse_schema_extensions(d.pop("schema_extensions", UNSET))

    _subgraph_type = d.pop("subgraph_type", UNSET)
    subgraph_type: Union[Unset, SubgraphType]
    if isinstance(_subgraph_type, Unset):
      subgraph_type = UNSET
    else:
      subgraph_type = SubgraphType(_subgraph_type)

    def _parse_metadata(
      data: object,
    ) -> Union["CreateSubgraphRequestMetadataType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        metadata_type_0 = CreateSubgraphRequestMetadataType0.from_dict(data)

        return metadata_type_0
      except:  # noqa: E722
        pass
      return cast(Union["CreateSubgraphRequestMetadataType0", None, Unset], data)

    metadata = _parse_metadata(d.pop("metadata", UNSET))

    create_subgraph_request = cls(
      name=name,
      display_name=display_name,
      description=description,
      schema_extensions=schema_extensions,
      subgraph_type=subgraph_type,
      metadata=metadata,
    )

    create_subgraph_request.additional_properties = d
    return create_subgraph_request

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
