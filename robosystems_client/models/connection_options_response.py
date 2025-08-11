from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.connection_provider_info import ConnectionProviderInfo


T = TypeVar("T", bound="ConnectionOptionsResponse")


@_attrs_define
class ConnectionOptionsResponse:
  """Response with all available connection options.

  Attributes:
      providers (list['ConnectionProviderInfo']): Available connection providers
      total_providers (int): Total number of providers
  """

  providers: list["ConnectionProviderInfo"]
  total_providers: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    providers = []
    for providers_item_data in self.providers:
      providers_item = providers_item_data.to_dict()
      providers.append(providers_item)

    total_providers = self.total_providers

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "providers": providers,
        "total_providers": total_providers,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.connection_provider_info import ConnectionProviderInfo

    d = dict(src_dict)
    providers = []
    _providers = d.pop("providers")
    for providers_item_data in _providers:
      providers_item = ConnectionProviderInfo.from_dict(providers_item_data)

      providers.append(providers_item)

    total_providers = d.pop("total_providers")

    connection_options_response = cls(
      providers=providers,
      total_providers=total_providers,
    )

    connection_options_response.additional_properties = d
    return connection_options_response

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
