from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.plaid_connection_config_accounts_type_0_item import (
    PlaidConnectionConfigAccountsType0Item,
  )
  from ..models.plaid_connection_config_institution_type_0 import (
    PlaidConnectionConfigInstitutionType0,
  )


T = TypeVar("T", bound="PlaidConnectionConfig")


@_attrs_define
class PlaidConnectionConfig:
  """Plaid-specific connection configuration.

  Attributes:
      public_token (None | str | Unset): Plaid public token for exchange
      access_token (None | str | Unset): Plaid access token (set after exchange)
      item_id (None | str | Unset): Plaid item ID
      institution (None | PlaidConnectionConfigInstitutionType0 | Unset): Institution information
      accounts (list[PlaidConnectionConfigAccountsType0Item] | None | Unset): Connected accounts
  """

  public_token: None | str | Unset = UNSET
  access_token: None | str | Unset = UNSET
  item_id: None | str | Unset = UNSET
  institution: None | PlaidConnectionConfigInstitutionType0 | Unset = UNSET
  accounts: list[PlaidConnectionConfigAccountsType0Item] | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.plaid_connection_config_institution_type_0 import (
      PlaidConnectionConfigInstitutionType0,
    )

    public_token: None | str | Unset
    if isinstance(self.public_token, Unset):
      public_token = UNSET
    else:
      public_token = self.public_token

    access_token: None | str | Unset
    if isinstance(self.access_token, Unset):
      access_token = UNSET
    else:
      access_token = self.access_token

    item_id: None | str | Unset
    if isinstance(self.item_id, Unset):
      item_id = UNSET
    else:
      item_id = self.item_id

    institution: dict[str, Any] | None | Unset
    if isinstance(self.institution, Unset):
      institution = UNSET
    elif isinstance(self.institution, PlaidConnectionConfigInstitutionType0):
      institution = self.institution.to_dict()
    else:
      institution = self.institution

    accounts: list[dict[str, Any]] | None | Unset
    if isinstance(self.accounts, Unset):
      accounts = UNSET
    elif isinstance(self.accounts, list):
      accounts = []
      for accounts_type_0_item_data in self.accounts:
        accounts_type_0_item = accounts_type_0_item_data.to_dict()
        accounts.append(accounts_type_0_item)

    else:
      accounts = self.accounts

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if public_token is not UNSET:
      field_dict["public_token"] = public_token
    if access_token is not UNSET:
      field_dict["access_token"] = access_token
    if item_id is not UNSET:
      field_dict["item_id"] = item_id
    if institution is not UNSET:
      field_dict["institution"] = institution
    if accounts is not UNSET:
      field_dict["accounts"] = accounts

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.plaid_connection_config_accounts_type_0_item import (
      PlaidConnectionConfigAccountsType0Item,
    )
    from ..models.plaid_connection_config_institution_type_0 import (
      PlaidConnectionConfigInstitutionType0,
    )

    d = dict(src_dict)

    def _parse_public_token(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    public_token = _parse_public_token(d.pop("public_token", UNSET))

    def _parse_access_token(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    access_token = _parse_access_token(d.pop("access_token", UNSET))

    def _parse_item_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    item_id = _parse_item_id(d.pop("item_id", UNSET))

    def _parse_institution(
      data: object,
    ) -> None | PlaidConnectionConfigInstitutionType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        institution_type_0 = PlaidConnectionConfigInstitutionType0.from_dict(data)

        return institution_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | PlaidConnectionConfigInstitutionType0 | Unset, data)

    institution = _parse_institution(d.pop("institution", UNSET))

    def _parse_accounts(
      data: object,
    ) -> list[PlaidConnectionConfigAccountsType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        accounts_type_0 = []
        _accounts_type_0 = data
        for accounts_type_0_item_data in _accounts_type_0:
          accounts_type_0_item = PlaidConnectionConfigAccountsType0Item.from_dict(
            accounts_type_0_item_data
          )

          accounts_type_0.append(accounts_type_0_item)

        return accounts_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[PlaidConnectionConfigAccountsType0Item] | None | Unset, data)

    accounts = _parse_accounts(d.pop("accounts", UNSET))

    plaid_connection_config = cls(
      public_token=public_token,
      access_token=access_token,
      item_id=item_id,
      institution=institution,
      accounts=accounts,
    )

    plaid_connection_config.additional_properties = d
    return plaid_connection_config

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
