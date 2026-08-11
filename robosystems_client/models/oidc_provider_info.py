from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OIDCProviderInfo")


@_attrs_define
class OIDCProviderInfo:
  """OIDC provider availability model.

  Attributes:
      enabled (bool): Whether OIDC SSO is available
      provider_label (None | str | Unset): Display label for the OIDC provider (e.g. 'Okta')
  """

  enabled: bool
  provider_label: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    enabled = self.enabled

    provider_label: None | str | Unset
    if isinstance(self.provider_label, Unset):
      provider_label = UNSET
    else:
      provider_label = self.provider_label

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "enabled": enabled,
      }
    )
    if provider_label is not UNSET:
      field_dict["provider_label"] = provider_label

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    enabled = d.pop("enabled")

    def _parse_provider_label(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    provider_label = _parse_provider_label(d.pop("provider_label", UNSET))

    oidc_provider_info = cls(
      enabled=enabled,
      provider_label=provider_label,
    )

    oidc_provider_info.additional_properties = d
    return oidc_provider_info

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
