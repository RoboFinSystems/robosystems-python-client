from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.available_extension import AvailableExtension


T = TypeVar("T", bound="AvailableExtensionsResponse")


@_attrs_define
class AvailableExtensionsResponse:
  """
  Attributes:
      extensions (list['AvailableExtension']):
  """

  extensions: list["AvailableExtension"]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    extensions = []
    for extensions_item_data in self.extensions:
      extensions_item = extensions_item_data.to_dict()
      extensions.append(extensions_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "extensions": extensions,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.available_extension import AvailableExtension

    d = dict(src_dict)
    extensions = []
    _extensions = d.pop("extensions")
    for extensions_item_data in _extensions:
      extensions_item = AvailableExtension.from_dict(extensions_item_data)

      extensions.append(extensions_item)

    available_extensions_response = cls(
      extensions=extensions,
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
