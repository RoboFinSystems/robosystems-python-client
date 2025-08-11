from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccountInfo")


@_attrs_define
class AccountInfo:
  """Provider account information.

  Example:
      {'provider': 'github', 'provider_account_id': '12345', 'provider_type': 'oauth'}

  Attributes:
      provider (str): Authentication provider ID (e.g., 'github', 'google')
      provider_type (str): Type of provider
      provider_account_id (str): Account ID at the provider
  """

  provider: str
  provider_type: str
  provider_account_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    provider = self.provider

    provider_type = self.provider_type

    provider_account_id = self.provider_account_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "provider": provider,
        "provider_type": provider_type,
        "provider_account_id": provider_account_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    provider = d.pop("provider")

    provider_type = d.pop("provider_type")

    provider_account_id = d.pop("provider_account_id")

    account_info = cls(
      provider=provider,
      provider_type=provider_type,
      provider_account_id=provider_account_id,
    )

    account_info.additional_properties = d
    return account_info

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
