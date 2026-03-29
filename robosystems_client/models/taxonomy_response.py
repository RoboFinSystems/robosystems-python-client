from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxonomyResponse")


@_attrs_define
class TaxonomyResponse:
  """
  Attributes:
      id (str):
      name (str):
      taxonomy_type (str):
      is_shared (bool):
      is_active (bool):
      is_locked (bool):
      description (None | str | Unset):
      version (None | str | Unset):
      standard (None | str | Unset):
      namespace_uri (None | str | Unset):
      source_taxonomy_id (None | str | Unset):
      target_taxonomy_id (None | str | Unset):
  """

  id: str
  name: str
  taxonomy_type: str
  is_shared: bool
  is_active: bool
  is_locked: bool
  description: None | str | Unset = UNSET
  version: None | str | Unset = UNSET
  standard: None | str | Unset = UNSET
  namespace_uri: None | str | Unset = UNSET
  source_taxonomy_id: None | str | Unset = UNSET
  target_taxonomy_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    taxonomy_type = self.taxonomy_type

    is_shared = self.is_shared

    is_active = self.is_active

    is_locked = self.is_locked

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

    standard: None | str | Unset
    if isinstance(self.standard, Unset):
      standard = UNSET
    else:
      standard = self.standard

    namespace_uri: None | str | Unset
    if isinstance(self.namespace_uri, Unset):
      namespace_uri = UNSET
    else:
      namespace_uri = self.namespace_uri

    source_taxonomy_id: None | str | Unset
    if isinstance(self.source_taxonomy_id, Unset):
      source_taxonomy_id = UNSET
    else:
      source_taxonomy_id = self.source_taxonomy_id

    target_taxonomy_id: None | str | Unset
    if isinstance(self.target_taxonomy_id, Unset):
      target_taxonomy_id = UNSET
    else:
      target_taxonomy_id = self.target_taxonomy_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "taxonomy_type": taxonomy_type,
        "is_shared": is_shared,
        "is_active": is_active,
        "is_locked": is_locked,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if version is not UNSET:
      field_dict["version"] = version
    if standard is not UNSET:
      field_dict["standard"] = standard
    if namespace_uri is not UNSET:
      field_dict["namespace_uri"] = namespace_uri
    if source_taxonomy_id is not UNSET:
      field_dict["source_taxonomy_id"] = source_taxonomy_id
    if target_taxonomy_id is not UNSET:
      field_dict["target_taxonomy_id"] = target_taxonomy_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    taxonomy_type = d.pop("taxonomy_type")

    is_shared = d.pop("is_shared")

    is_active = d.pop("is_active")

    is_locked = d.pop("is_locked")

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

    def _parse_standard(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    standard = _parse_standard(d.pop("standard", UNSET))

    def _parse_namespace_uri(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    namespace_uri = _parse_namespace_uri(d.pop("namespace_uri", UNSET))

    def _parse_source_taxonomy_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_taxonomy_id = _parse_source_taxonomy_id(d.pop("source_taxonomy_id", UNSET))

    def _parse_target_taxonomy_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    target_taxonomy_id = _parse_target_taxonomy_id(d.pop("target_taxonomy_id", UNSET))

    taxonomy_response = cls(
      id=id,
      name=name,
      taxonomy_type=taxonomy_type,
      is_shared=is_shared,
      is_active=is_active,
      is_locked=is_locked,
      description=description,
      version=version,
      standard=standard,
      namespace_uri=namespace_uri,
      source_taxonomy_id=source_taxonomy_id,
      target_taxonomy_id=target_taxonomy_id,
    )

    taxonomy_response.additional_properties = d
    return taxonomy_response

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
