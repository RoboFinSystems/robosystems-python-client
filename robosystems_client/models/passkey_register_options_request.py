from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasskeyRegisterOptionsRequest")


@_attrs_define
class PasskeyRegisterOptionsRequest:
  """Begin enrollment. mfa_token is the forced-enrollment lane; omitted for
  an authenticated settings-flow enrollment.

      Attributes:
          mfa_token (None | str | Unset): Enrollment token from a login that returned mfa_enrollment_required
  """

  mfa_token: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    mfa_token: None | str | Unset
    if isinstance(self.mfa_token, Unset):
      mfa_token = UNSET
    else:
      mfa_token = self.mfa_token

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if mfa_token is not UNSET:
      field_dict["mfa_token"] = mfa_token

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_mfa_token(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    mfa_token = _parse_mfa_token(d.pop("mfa_token", UNSET))

    passkey_register_options_request = cls(
      mfa_token=mfa_token,
    )

    passkey_register_options_request.additional_properties = d
    return passkey_register_options_request

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
