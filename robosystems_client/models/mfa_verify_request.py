from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.mfa_verify_request_assertion_type_0 import (
    MfaVerifyRequestAssertionType0,
  )


T = TypeVar("T", bound="MfaVerifyRequest")


@_attrs_define
class MfaVerifyRequest:
  """Complete the second factor with an assertion or a recovery code.

  Attributes:
      mfa_token (str): Token from a login that returned mfa_required
      assertion (MfaVerifyRequestAssertionType0 | None | Unset): WebAuthn assertion (browser JSON, opaque)
      recovery_code (None | str | Unset): Single-use recovery code
  """

  mfa_token: str
  assertion: MfaVerifyRequestAssertionType0 | None | Unset = UNSET
  recovery_code: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.mfa_verify_request_assertion_type_0 import (
      MfaVerifyRequestAssertionType0,
    )

    mfa_token = self.mfa_token

    assertion: dict[str, Any] | None | Unset
    if isinstance(self.assertion, Unset):
      assertion = UNSET
    elif isinstance(self.assertion, MfaVerifyRequestAssertionType0):
      assertion = self.assertion.to_dict()
    else:
      assertion = self.assertion

    recovery_code: None | str | Unset
    if isinstance(self.recovery_code, Unset):
      recovery_code = UNSET
    else:
      recovery_code = self.recovery_code

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "mfa_token": mfa_token,
      }
    )
    if assertion is not UNSET:
      field_dict["assertion"] = assertion
    if recovery_code is not UNSET:
      field_dict["recovery_code"] = recovery_code

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.mfa_verify_request_assertion_type_0 import (
      MfaVerifyRequestAssertionType0,
    )

    d = dict(src_dict)
    mfa_token = d.pop("mfa_token")

    def _parse_assertion(data: object) -> MfaVerifyRequestAssertionType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        assertion_type_0 = MfaVerifyRequestAssertionType0.from_dict(data)

        return assertion_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(MfaVerifyRequestAssertionType0 | None | Unset, data)

    assertion = _parse_assertion(d.pop("assertion", UNSET))

    def _parse_recovery_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    recovery_code = _parse_recovery_code(d.pop("recovery_code", UNSET))

    mfa_verify_request = cls(
      mfa_token=mfa_token,
      assertion=assertion,
      recovery_code=recovery_code,
    )

    mfa_verify_request.additional_properties = d
    return mfa_verify_request

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
