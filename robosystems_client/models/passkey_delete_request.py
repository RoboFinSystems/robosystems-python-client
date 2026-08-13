from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.passkey_delete_request_assertion_type_0 import (
    PasskeyDeleteRequestAssertionType0,
  )


T = TypeVar("T", bound="PasskeyDeleteRequest")


@_attrs_define
class PasskeyDeleteRequest:
  """Re-authentication proof for removing a passkey.

  Attributes:
      password (None | str | Unset): Current password (password-holding users)
      assertion (None | PasskeyDeleteRequestAssertionType0 | Unset): Fresh WebAuthn assertion from the re-auth
          ceremony
  """

  password: None | str | Unset = UNSET
  assertion: None | PasskeyDeleteRequestAssertionType0 | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.passkey_delete_request_assertion_type_0 import (
      PasskeyDeleteRequestAssertionType0,
    )

    password: None | str | Unset
    if isinstance(self.password, Unset):
      password = UNSET
    else:
      password = self.password

    assertion: dict[str, Any] | None | Unset
    if isinstance(self.assertion, Unset):
      assertion = UNSET
    elif isinstance(self.assertion, PasskeyDeleteRequestAssertionType0):
      assertion = self.assertion.to_dict()
    else:
      assertion = self.assertion

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if password is not UNSET:
      field_dict["password"] = password
    if assertion is not UNSET:
      field_dict["assertion"] = assertion

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.passkey_delete_request_assertion_type_0 import (
      PasskeyDeleteRequestAssertionType0,
    )

    d = dict(src_dict)

    def _parse_password(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    password = _parse_password(d.pop("password", UNSET))

    def _parse_assertion(
      data: object,
    ) -> None | PasskeyDeleteRequestAssertionType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        assertion_type_0 = PasskeyDeleteRequestAssertionType0.from_dict(data)

        return assertion_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | PasskeyDeleteRequestAssertionType0 | Unset, data)

    assertion = _parse_assertion(d.pop("assertion", UNSET))

    passkey_delete_request = cls(
      password=password,
      assertion=assertion,
    )

    passkey_delete_request.additional_properties = d
    return passkey_delete_request

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
