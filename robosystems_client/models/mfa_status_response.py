from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MfaStatusResponse")


@_attrs_define
class MfaStatusResponse:
  """The user's MFA posture, for account settings.

  Attributes:
      passkey_count (int): Enrolled passkey count
      recovery_codes_remaining (int): Unused recovery codes remaining
      enforcement_applies (bool): Whether the MFA requirement applies to this user's roles
  """

  passkey_count: int
  recovery_codes_remaining: int
  enforcement_applies: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    passkey_count = self.passkey_count

    recovery_codes_remaining = self.recovery_codes_remaining

    enforcement_applies = self.enforcement_applies

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "passkey_count": passkey_count,
        "recovery_codes_remaining": recovery_codes_remaining,
        "enforcement_applies": enforcement_applies,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    passkey_count = d.pop("passkey_count")

    recovery_codes_remaining = d.pop("recovery_codes_remaining")

    enforcement_applies = d.pop("enforcement_applies")

    mfa_status_response = cls(
      passkey_count=passkey_count,
      recovery_codes_remaining=recovery_codes_remaining,
      enforcement_applies=enforcement_applies,
    )

    mfa_status_response.additional_properties = d
    return mfa_status_response

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
