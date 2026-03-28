from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StructureResponse")


@_attrs_define
class StructureResponse:
  """
  Attributes:
      id (str):
      name (str):
      structure_type (str):
      taxonomy_id (str):
      is_active (bool):
      description (None | str | Unset):
  """

  id: str
  name: str
  structure_type: str
  taxonomy_id: str
  is_active: bool
  description: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    structure_type = self.structure_type

    taxonomy_id = self.taxonomy_id

    is_active = self.is_active

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "structure_type": structure_type,
        "taxonomy_id": taxonomy_id,
        "is_active": is_active,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    structure_type = d.pop("structure_type")

    taxonomy_id = d.pop("taxonomy_id")

    is_active = d.pop("is_active")

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    structure_response = cls(
      id=id,
      name=name,
      structure_type=structure_type,
      taxonomy_id=taxonomy_id,
      is_active=is_active,
      description=description,
    )

    structure_response.additional_properties = d
    return structure_response

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
