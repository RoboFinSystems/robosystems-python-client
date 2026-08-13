from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.auth_response import AuthResponse
  from ..models.passkey_info import PasskeyInfo


T = TypeVar("T", bound="PasskeyRegisterVerifyResponse")


@_attrs_define
class PasskeyRegisterVerifyResponse:
  """Enrollment result; the first passkey also carries recovery codes and,
  in the forced-enrollment lane, the completed login.

      Attributes:
          passkey (PasskeyInfo): One enrolled passkey, as listed in account settings.
          recovery_codes (list[str] | None | Unset): Single-use recovery codes — returned exactly once, at first
              enrollment
          auth (AuthResponse | None | Unset): Completed login (forced-enrollment lane only)
  """

  passkey: PasskeyInfo
  recovery_codes: list[str] | None | Unset = UNSET
  auth: AuthResponse | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.auth_response import AuthResponse

    passkey = self.passkey.to_dict()

    recovery_codes: list[str] | None | Unset
    if isinstance(self.recovery_codes, Unset):
      recovery_codes = UNSET
    elif isinstance(self.recovery_codes, list):
      recovery_codes = self.recovery_codes

    else:
      recovery_codes = self.recovery_codes

    auth: dict[str, Any] | None | Unset
    if isinstance(self.auth, Unset):
      auth = UNSET
    elif isinstance(self.auth, AuthResponse):
      auth = self.auth.to_dict()
    else:
      auth = self.auth

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "passkey": passkey,
      }
    )
    if recovery_codes is not UNSET:
      field_dict["recovery_codes"] = recovery_codes
    if auth is not UNSET:
      field_dict["auth"] = auth

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.auth_response import AuthResponse
    from ..models.passkey_info import PasskeyInfo

    d = dict(src_dict)
    passkey = PasskeyInfo.from_dict(d.pop("passkey"))

    def _parse_recovery_codes(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        recovery_codes_type_0 = cast(list[str], data)

        return recovery_codes_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    recovery_codes = _parse_recovery_codes(d.pop("recovery_codes", UNSET))

    def _parse_auth(data: object) -> AuthResponse | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        auth_type_0 = AuthResponse.from_dict(data)

        return auth_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(AuthResponse | None | Unset, data)

    auth = _parse_auth(d.pop("auth", UNSET))

    passkey_register_verify_response = cls(
      passkey=passkey,
      recovery_codes=recovery_codes,
      auth=auth,
    )

    passkey_register_verify_response.additional_properties = d
    return passkey_register_verify_response

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
