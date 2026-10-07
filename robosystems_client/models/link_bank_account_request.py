from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkBankAccountRequest")


@_attrs_define
class LinkBankAccountRequest:
  """Point a bank feed's account at a chart account.

  Name `element_id` for an existing active account, or `entity_id` alone to
  create one in that entity's chart. The chart the account is in decides
  whose books the feed's lines go into, so this is also how a feed account
  is bound to a subsidiary. Lines still in the inbox move with it; posted
  entries stay where they were posted.

      Attributes:
          connection_id (str): The feed's connection.
          account_id (str): The provider's id for the account.
          element_id (None | str | Unset): The chart account to link; its chart's entity takes the feed.
          entity_id (None | str | Unset): With `element_id`, the entity the account must belong to. Alone, the entity in
              whose chart a new account is created for the feed account.
  """

  connection_id: str
  account_id: str
  element_id: None | str | Unset = UNSET
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    connection_id = self.connection_id

    account_id = self.account_id

    element_id: None | str | Unset
    if isinstance(self.element_id, Unset):
      element_id = UNSET
    else:
      element_id = self.element_id

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "connection_id": connection_id,
        "account_id": account_id,
      }
    )
    if element_id is not UNSET:
      field_dict["element_id"] = element_id
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    connection_id = d.pop("connection_id")

    account_id = d.pop("account_id")

    def _parse_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_id = _parse_element_id(d.pop("element_id", UNSET))

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    link_bank_account_request = cls(
      connection_id=connection_id,
      account_id=account_id,
      element_id=element_id,
      entity_id=entity_id,
    )

    link_bank_account_request.additional_properties = d
    return link_bank_account_request

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
