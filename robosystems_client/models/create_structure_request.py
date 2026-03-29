from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_structure_request_structure_type import (
  CreateStructureRequestStructureType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateStructureRequest")


@_attrs_define
class CreateStructureRequest:
  """
  Attributes:
      name (str):
      structure_type (CreateStructureRequestStructureType):
      taxonomy_id (str):
      description (None | str | Unset):
  """

  name: str
  structure_type: CreateStructureRequestStructureType
  taxonomy_id: str
  description: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    structure_type = self.structure_type.value

    taxonomy_id = self.taxonomy_id

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "structure_type": structure_type,
        "taxonomy_id": taxonomy_id,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    structure_type = CreateStructureRequestStructureType(d.pop("structure_type"))

    taxonomy_id = d.pop("taxonomy_id")

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    create_structure_request = cls(
      name=name,
      structure_type=structure_type,
      taxonomy_id=taxonomy_id,
      description=description,
    )

    create_structure_request.additional_properties = d
    return create_structure_request

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
