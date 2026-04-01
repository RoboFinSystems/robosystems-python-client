from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.update_security_request_terms_type_0 import (
    UpdateSecurityRequestTermsType0,
  )


T = TypeVar("T", bound="UpdateSecurityRequest")


@_attrs_define
class UpdateSecurityRequest:
  """
  Attributes:
      name (None | str | Unset):
      security_type (None | str | Unset):
      security_subtype (None | str | Unset):
      terms (None | Unset | UpdateSecurityRequestTermsType0):
      is_active (bool | None | Unset):
      authorized_shares (int | None | Unset):
      outstanding_shares (int | None | Unset):
  """

  name: None | str | Unset = UNSET
  security_type: None | str | Unset = UNSET
  security_subtype: None | str | Unset = UNSET
  terms: None | Unset | UpdateSecurityRequestTermsType0 = UNSET
  is_active: bool | None | Unset = UNSET
  authorized_shares: int | None | Unset = UNSET
  outstanding_shares: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.update_security_request_terms_type_0 import (
      UpdateSecurityRequestTermsType0,
    )

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    security_type: None | str | Unset
    if isinstance(self.security_type, Unset):
      security_type = UNSET
    else:
      security_type = self.security_type

    security_subtype: None | str | Unset
    if isinstance(self.security_subtype, Unset):
      security_subtype = UNSET
    else:
      security_subtype = self.security_subtype

    terms: dict[str, Any] | None | Unset
    if isinstance(self.terms, Unset):
      terms = UNSET
    elif isinstance(self.terms, UpdateSecurityRequestTermsType0):
      terms = self.terms.to_dict()
    else:
      terms = self.terms

    is_active: bool | None | Unset
    if isinstance(self.is_active, Unset):
      is_active = UNSET
    else:
      is_active = self.is_active

    authorized_shares: int | None | Unset
    if isinstance(self.authorized_shares, Unset):
      authorized_shares = UNSET
    else:
      authorized_shares = self.authorized_shares

    outstanding_shares: int | None | Unset
    if isinstance(self.outstanding_shares, Unset):
      outstanding_shares = UNSET
    else:
      outstanding_shares = self.outstanding_shares

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if name is not UNSET:
      field_dict["name"] = name
    if security_type is not UNSET:
      field_dict["security_type"] = security_type
    if security_subtype is not UNSET:
      field_dict["security_subtype"] = security_subtype
    if terms is not UNSET:
      field_dict["terms"] = terms
    if is_active is not UNSET:
      field_dict["is_active"] = is_active
    if authorized_shares is not UNSET:
      field_dict["authorized_shares"] = authorized_shares
    if outstanding_shares is not UNSET:
      field_dict["outstanding_shares"] = outstanding_shares

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.update_security_request_terms_type_0 import (
      UpdateSecurityRequestTermsType0,
    )

    d = dict(src_dict)

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_security_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    security_type = _parse_security_type(d.pop("security_type", UNSET))

    def _parse_security_subtype(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    security_subtype = _parse_security_subtype(d.pop("security_subtype", UNSET))

    def _parse_terms(data: object) -> None | Unset | UpdateSecurityRequestTermsType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        terms_type_0 = UpdateSecurityRequestTermsType0.from_dict(data)

        return terms_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateSecurityRequestTermsType0, data)

    terms = _parse_terms(d.pop("terms", UNSET))

    def _parse_is_active(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    is_active = _parse_is_active(d.pop("is_active", UNSET))

    def _parse_authorized_shares(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    authorized_shares = _parse_authorized_shares(d.pop("authorized_shares", UNSET))

    def _parse_outstanding_shares(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    outstanding_shares = _parse_outstanding_shares(d.pop("outstanding_shares", UNSET))

    update_security_request = cls(
      name=name,
      security_type=security_type,
      security_subtype=security_subtype,
      terms=terms,
      is_active=is_active,
      authorized_shares=authorized_shares,
      outstanding_shares=outstanding_shares,
    )

    update_security_request.additional_properties = d
    return update_security_request

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
