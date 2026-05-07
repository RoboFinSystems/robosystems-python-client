from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxonomyBlockStructure")


@_attrs_define
class TaxonomyBlockStructure:
  """Structure projection for the Taxonomy Block envelope.

  Attributes:
      id (str):
      name (str):
      structure_type (str):
      description (None | str | Unset):
      role_uri (None | str | Unset):
  """

  id: str
  name: str
  structure_type: str
  description: None | str | Unset = UNSET
  role_uri: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    structure_type = self.structure_type

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

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "structure_type": structure_type,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if role_uri is not UNSET:
      field_dict["role_uri"] = role_uri

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    structure_type = d.pop("structure_type")

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

    taxonomy_block_structure = cls(
      id=id,
      name=name,
      structure_type=structure_type,
      description=description,
      role_uri=role_uri,
    )

    taxonomy_block_structure.additional_properties = d
    return taxonomy_block_structure

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
