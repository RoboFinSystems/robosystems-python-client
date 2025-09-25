from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APIKeyInfo")


@_attrs_define
class APIKeyInfo:
  """API key information response model.

  Attributes:
      id (str): API key ID
      name (str): API key name
      prefix (str): API key prefix for identification
      is_active (bool): Whether the key is active
      created_at (str): Creation timestamp
      description (Union[None, Unset, str]): API key description
      last_used_at (Union[None, Unset, str]): Last used timestamp
      expires_at (Union[None, Unset, str]): Expiration timestamp
  """

  id: str
  name: str
  prefix: str
  is_active: bool
  created_at: str
  description: Union[None, Unset, str] = UNSET
  last_used_at: Union[None, Unset, str] = UNSET
  expires_at: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    prefix = self.prefix

    is_active = self.is_active

    created_at = self.created_at

    description: Union[None, Unset, str]
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    last_used_at: Union[None, Unset, str]
    if isinstance(self.last_used_at, Unset):
      last_used_at = UNSET
    else:
      last_used_at = self.last_used_at

    expires_at: Union[None, Unset, str]
    if isinstance(self.expires_at, Unset):
      expires_at = UNSET
    else:
      expires_at = self.expires_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "prefix": prefix,
        "is_active": is_active,
        "created_at": created_at,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if last_used_at is not UNSET:
      field_dict["last_used_at"] = last_used_at
    if expires_at is not UNSET:
      field_dict["expires_at"] = expires_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    prefix = d.pop("prefix")

    is_active = d.pop("is_active")

    created_at = d.pop("created_at")

    def _parse_description(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_last_used_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

    def _parse_expires_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

    api_key_info = cls(
      id=id,
      name=name,
      prefix=prefix,
      is_active=is_active,
      created_at=created_at,
      description=description,
      last_used_at=last_used_at,
      expires_at=expires_at,
    )

    api_key_info.additional_properties = d
    return api_key_info

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
