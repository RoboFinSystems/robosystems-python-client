from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.passkey_register_verify_request_credential import (
    PasskeyRegisterVerifyRequestCredential,
  )


T = TypeVar("T", bound="PasskeyRegisterVerifyRequest")


@_attrs_define
class PasskeyRegisterVerifyRequest:
  """Finish enrollment with the authenticator's attestation response.

  Attributes:
      credential (PasskeyRegisterVerifyRequestCredential): WebAuthn registration credential (browser JSON, opaque)
      name (None | str | Unset): User-facing label for this passkey
      mfa_token (None | str | Unset): Enrollment token when finishing a forced enrollment
  """

  credential: PasskeyRegisterVerifyRequestCredential
  name: None | str | Unset = UNSET
  mfa_token: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    credential = self.credential.to_dict()

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    mfa_token: None | str | Unset
    if isinstance(self.mfa_token, Unset):
      mfa_token = UNSET
    else:
      mfa_token = self.mfa_token

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "credential": credential,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if mfa_token is not UNSET:
      field_dict["mfa_token"] = mfa_token

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.passkey_register_verify_request_credential import (
      PasskeyRegisterVerifyRequestCredential,
    )

    d = dict(src_dict)
    credential = PasskeyRegisterVerifyRequestCredential.from_dict(d.pop("credential"))

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_mfa_token(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    mfa_token = _parse_mfa_token(d.pop("mfa_token", UNSET))

    passkey_register_verify_request = cls(
      credential=credential,
      name=name,
      mfa_token=mfa_token,
    )

    passkey_register_verify_request.additional_properties = d
    return passkey_register_verify_request

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
