from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taxonomy_block_structure_request_structure_type import (
  TaxonomyBlockStructureRequestStructureType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.taxonomy_block_structure_request_metadata import (
    TaxonomyBlockStructureRequestMetadata,
  )


T = TypeVar("T", bound="TaxonomyBlockStructureRequest")


@_attrs_define
class TaxonomyBlockStructureRequest:
  """Structure definition inside a Taxonomy Block envelope.

  Attributes:
      name (str): Envelope-local structure name (unique within envelope).
      structure_type (TaxonomyBlockStructureRequestStructureType): DB ``structures.structure_type`` enum. CoA blocks
          use ``chart_of_accounts``; reporting extensions use the statement family or ``custom``; custom ontology uses
          ``custom``.
      description (None | str | Unset):
      role_uri (None | str | Unset):
      metadata (TaxonomyBlockStructureRequestMetadata | Unset):
  """

  name: str
  structure_type: TaxonomyBlockStructureRequestStructureType
  description: None | str | Unset = UNSET
  role_uri: None | str | Unset = UNSET
  metadata: TaxonomyBlockStructureRequestMetadata | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    structure_type = self.structure_type.value

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    role_uri: None | str | Unset
    if isinstance(self.role_uri, Unset):
      role_uri = UNSET
    else:
      role_uri = self.role_uri

    metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata, Unset):
      metadata = self.metadata.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "structure_type": structure_type,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if role_uri is not UNSET:
      field_dict["role_uri"] = role_uri
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.taxonomy_block_structure_request_metadata import (
      TaxonomyBlockStructureRequestMetadata,
    )

    d = dict(src_dict)
    name = d.pop("name")

    structure_type = TaxonomyBlockStructureRequestStructureType(d.pop("structure_type"))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_role_uri(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    role_uri = _parse_role_uri(d.pop("role_uri", UNSET))

    _metadata = d.pop("metadata", UNSET)
    metadata: TaxonomyBlockStructureRequestMetadata | Unset
    if isinstance(_metadata, Unset):
      metadata = UNSET
    else:
      metadata = TaxonomyBlockStructureRequestMetadata.from_dict(_metadata)

    taxonomy_block_structure_request = cls(
      name=name,
      structure_type=structure_type,
      description=description,
      role_uri=role_uri,
      metadata=metadata,
    )

    taxonomy_block_structure_request.additional_properties = d
    return taxonomy_block_structure_request

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
