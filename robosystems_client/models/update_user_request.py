from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.update_user_request_reauth_assertion_type_0 import (
    UpdateUserRequestReauthAssertionType0,
  )


T = TypeVar("T", bound="UpdateUserRequest")


@_attrs_define
class UpdateUserRequest:
  """Request model for updating user profile.

  Changing ``email`` re-authenticates: a fresh proof (password re-entry or a
  ``mgmt``-flow passkey assertion) must accompany the request, exactly as
  passkey enrollment and removal require. Name-only updates need no proof.

      Attributes:
          name (None | str | Unset): User's display name
          email (None | str | Unset): User's email address
          reauth_password (None | str | Unset): Password re-entry, required to change email for a password-holding account
          reauth_assertion (None | Unset | UpdateUserRequestReauthAssertionType0): A fresh mgmt-flow passkey assertion,
              required to change email for a passkey-only account
  """

  name: None | str | Unset = UNSET
  email: None | str | Unset = UNSET
  reauth_password: None | str | Unset = UNSET
  reauth_assertion: None | Unset | UpdateUserRequestReauthAssertionType0 = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.update_user_request_reauth_assertion_type_0 import (
      UpdateUserRequestReauthAssertionType0,
    )

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    email: None | str | Unset
    if isinstance(self.email, Unset):
      email = UNSET
    else:
      email = self.email

    reauth_password: None | str | Unset
    if isinstance(self.reauth_password, Unset):
      reauth_password = UNSET
    else:
      reauth_password = self.reauth_password

    reauth_assertion: dict[str, Any] | None | Unset
    if isinstance(self.reauth_assertion, Unset):
      reauth_assertion = UNSET
    elif isinstance(self.reauth_assertion, UpdateUserRequestReauthAssertionType0):
      reauth_assertion = self.reauth_assertion.to_dict()
    else:
      reauth_assertion = self.reauth_assertion

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if name is not UNSET:
      field_dict["name"] = name
    if email is not UNSET:
      field_dict["email"] = email
    if reauth_password is not UNSET:
      field_dict["reauth_password"] = reauth_password
    if reauth_assertion is not UNSET:
      field_dict["reauth_assertion"] = reauth_assertion

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.update_user_request_reauth_assertion_type_0 import (
      UpdateUserRequestReauthAssertionType0,
    )

    d = dict(src_dict)

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_email(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    email = _parse_email(d.pop("email", UNSET))

    def _parse_reauth_password(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reauth_password = _parse_reauth_password(d.pop("reauth_password", UNSET))

    def _parse_reauth_assertion(
      data: object,
    ) -> None | Unset | UpdateUserRequestReauthAssertionType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        reauth_assertion_type_0 = UpdateUserRequestReauthAssertionType0.from_dict(data)

        return reauth_assertion_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateUserRequestReauthAssertionType0, data)

    reauth_assertion = _parse_reauth_assertion(d.pop("reauth_assertion", UNSET))

    update_user_request = cls(
      name=name,
      email=email,
      reauth_password=reauth_password,
      reauth_assertion=reauth_assertion,
    )

    update_user_request.additional_properties = d
    return update_user_request

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
