from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTaxonomyRequest")


@_attrs_define
class UpdateTaxonomyRequest:
  """Update mutable fields on a taxonomy. `taxonomy_type` is immutable —
  changing it is not the same operation as editing a taxonomy; deactivate
  and create a new one instead. Only provided (non-null) fields are
  applied.

      Attributes:
          taxonomy_id (str):
          name (None | str | Unset):
          description (None | str | Unset):
          version (None | str | Unset):
  """

  taxonomy_id: str
  name: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  version: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    taxonomy_id = self.taxonomy_id

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    version: None | str | Unset
    if isinstance(self.version, Unset):
      version = UNSET
    else:
      version = self.version

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "taxonomy_id": taxonomy_id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if description is not UNSET:
      field_dict["description"] = description
    if version is not UNSET:
      field_dict["version"] = version

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    taxonomy_id = d.pop("taxonomy_id")

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_version(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    version = _parse_version(d.pop("version", UNSET))

    update_taxonomy_request = cls(
      taxonomy_id=taxonomy_id,
      name=name,
      description=description,
      version=version,
    )

    update_taxonomy_request.additional_properties = d
    return update_taxonomy_request

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
