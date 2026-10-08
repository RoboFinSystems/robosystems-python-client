from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkBankAccountResponse")


@_attrs_define
class LinkBankAccountResponse:
  """What `link-bank-account` did.

  Attributes:
      connection_id (str):
      provider (str):
      account_id (str):
      element_id (str): The chart account the feed now books to.
      previous_element_id (str):
      entity_id (str): The entity the feed's lines now belong to.
      account_created (bool | Unset): A new account was created in the entity's chart. Default: False.
      events_repointed (int | Unset): Inbox lines moved to the new account (posted entries stay). Default: 0.
      events_unclassified (int | Unset): Lines returned to `captured`: their classification named an account in the
          previous entity's chart. Default: 0.
      pairs_across_entities (int | Unset): Open transfer pairs whose two legs now sit on two entities, because only
          one leg's account moved. Intercompany; the commit guard refuses them until the other leg follows. Default: 0.
      changed (bool | Unset): False when the link already stood and no line moved. Default: True.
  """

  connection_id: str
  provider: str
  account_id: str
  element_id: str
  previous_element_id: str
  entity_id: str
  account_created: bool | Unset = False
  events_repointed: int | Unset = 0
  events_unclassified: int | Unset = 0
  pairs_across_entities: int | Unset = 0
  changed: bool | Unset = True
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    connection_id = self.connection_id

    provider = self.provider

    account_id = self.account_id

    element_id = self.element_id

    previous_element_id = self.previous_element_id

    entity_id = self.entity_id

    account_created = self.account_created

    events_repointed = self.events_repointed

    events_unclassified = self.events_unclassified

    pairs_across_entities = self.pairs_across_entities

    changed = self.changed

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "connection_id": connection_id,
        "provider": provider,
        "account_id": account_id,
        "element_id": element_id,
        "previous_element_id": previous_element_id,
        "entity_id": entity_id,
      }
    )
    if account_created is not UNSET:
      field_dict["account_created"] = account_created
    if events_repointed is not UNSET:
      field_dict["events_repointed"] = events_repointed
    if events_unclassified is not UNSET:
      field_dict["events_unclassified"] = events_unclassified
    if pairs_across_entities is not UNSET:
      field_dict["pairs_across_entities"] = pairs_across_entities
    if changed is not UNSET:
      field_dict["changed"] = changed

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    connection_id = d.pop("connection_id")

    provider = d.pop("provider")

    account_id = d.pop("account_id")

    element_id = d.pop("element_id")

    previous_element_id = d.pop("previous_element_id")

    entity_id = d.pop("entity_id")

    account_created = d.pop("account_created", UNSET)

    events_repointed = d.pop("events_repointed", UNSET)

    events_unclassified = d.pop("events_unclassified", UNSET)

    pairs_across_entities = d.pop("pairs_across_entities", UNSET)

    changed = d.pop("changed", UNSET)

    link_bank_account_response = cls(
      connection_id=connection_id,
      provider=provider,
      account_id=account_id,
      element_id=element_id,
      previous_element_id=previous_element_id,
      entity_id=entity_id,
      account_created=account_created,
      events_repointed=events_repointed,
      events_unclassified=events_unclassified,
      pairs_across_entities=pairs_across_entities,
      changed=changed,
    )

    link_bank_account_response.additional_properties = d
    return link_bank_account_response

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
