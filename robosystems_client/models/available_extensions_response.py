from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.available_extension import AvailableExtension
  from ..models.available_extensions_response_base_info import (
    AvailableExtensionsResponseBaseInfo,
  )


T = TypeVar("T", bound="AvailableExtensionsResponse")


@_attrs_define
class AvailableExtensionsResponse:
  """
  Attributes:
      extensions (list['AvailableExtension']): List of available schema extensions
      default_extensions (list[str]): Default extensions recommended for new companies
      base_info (AvailableExtensionsResponseBaseInfo): Information about the base schema
  """

  extensions: list["AvailableExtension"]
  default_extensions: list[str]
  base_info: "AvailableExtensionsResponseBaseInfo"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    extensions = []
    for extensions_item_data in self.extensions:
      extensions_item = extensions_item_data.to_dict()
      extensions.append(extensions_item)

    default_extensions = self.default_extensions

    base_info = self.base_info.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "extensions": extensions,
        "default_extensions": default_extensions,
        "base_info": base_info,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.available_extension import AvailableExtension
    from ..models.available_extensions_response_base_info import (
      AvailableExtensionsResponseBaseInfo,
    )

    d = dict(src_dict)
    extensions = []
    _extensions = d.pop("extensions")
    for extensions_item_data in _extensions:
      extensions_item = AvailableExtension.from_dict(extensions_item_data)

      extensions.append(extensions_item)

    default_extensions = cast(list[str], d.pop("default_extensions"))

    base_info = AvailableExtensionsResponseBaseInfo.from_dict(d.pop("base_info"))

    available_extensions_response = cls(
      extensions=extensions,
      default_extensions=default_extensions,
      base_info=base_info,
    )

    available_extensions_response.additional_properties = d
    return available_extensions_response

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
