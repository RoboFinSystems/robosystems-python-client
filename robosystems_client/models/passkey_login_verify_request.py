from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.passkey_login_verify_request_assertion import (
    PasskeyLoginVerifyRequestAssertion,
  )


T = TypeVar("T", bound="PasskeyLoginVerifyRequest")


@_attrs_define
class PasskeyLoginVerifyRequest:
  """Complete a passwordless login with a discoverable-credential assertion.

  Attributes:
      assertion (PasskeyLoginVerifyRequestAssertion): WebAuthn assertion (browser JSON, opaque)
  """

  assertion: PasskeyLoginVerifyRequestAssertion
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    assertion = self.assertion.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "assertion": assertion,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.passkey_login_verify_request_assertion import (
      PasskeyLoginVerifyRequestAssertion,
    )

    d = dict(src_dict)
    assertion = PasskeyLoginVerifyRequestAssertion.from_dict(d.pop("assertion"))

    passkey_login_verify_request = cls(
      assertion=assertion,
    )

    passkey_login_verify_request.additional_properties = d
    return passkey_login_verify_request

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
