from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableExtension")


@_attrs_define
class AvailableExtension:
  """
  Attributes:
      name (str):
      description (str):
      display_name (None | str | Unset):
      enabled (bool | Unset):  Default: False.
  """

  name: str
  description: str
  display_name: None | str | Unset = UNSET
  enabled: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    description = self.description

    display_name: None | str | Unset
    if isinstance(self.display_name, Unset):
      display_name = UNSET
    else:
      display_name = self.display_name

    enabled = self.enabled

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "description": description,
      }
    )
    if display_name is not UNSET:
      field_dict["display_name"] = display_name
    if enabled is not UNSET:
      field_dict["enabled"] = enabled

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    description = d.pop("description")

    def _parse_display_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    display_name = _parse_display_name(d.pop("display_name", UNSET))

    enabled = d.pop("enabled", UNSET)

    available_extension = cls(
      name=name,
      description=description,
      display_name=display_name,
      enabled=enabled,
    )

    available_extension.additional_properties = d
    return available_extension

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
