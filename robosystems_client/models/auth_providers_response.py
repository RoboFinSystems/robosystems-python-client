from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.oidc_provider_info import OIDCProviderInfo


T = TypeVar("T", bound="AuthProvidersResponse")


@_attrs_define
class AuthProvidersResponse:
  """Auth posture response model.

  Describes which authentication methods this deployment offers so the
  login surface can render the correct posture from runtime configuration.

      Attributes:
          password_auth (bool): Whether password authentication is available
          oidc (OIDCProviderInfo): OIDC provider availability model.
          registration (bool): Whether self-service registration is open
          passkeys (bool): Whether passkey authentication is available
  """

  password_auth: bool
  oidc: OIDCProviderInfo
  registration: bool
  passkeys: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    password_auth = self.password_auth

    oidc = self.oidc.to_dict()

    registration = self.registration

    passkeys = self.passkeys

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "password_auth": password_auth,
        "oidc": oidc,
        "registration": registration,
        "passkeys": passkeys,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.oidc_provider_info import OIDCProviderInfo

    d = dict(src_dict)
    password_auth = d.pop("password_auth")

    oidc = OIDCProviderInfo.from_dict(d.pop("oidc"))

    registration = d.pop("registration")

    passkeys = d.pop("passkeys")

    auth_providers_response = cls(
      password_auth=password_auth,
      oidc=oidc,
      registration=registration,
      passkeys=passkeys,
    )

    auth_providers_response.additional_properties = d
    return auth_providers_response

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
