from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentClassification")


@_attrs_define
class AgentClassification:
  """A counterparty's default account, learned from committed lines or set by
  hand.

      Attributes:
          element_id (str): The default chart account.
          mode (str): `suggest`: offered on each new line. `always_ask`: never offered.
          confirmations (int): Committed lines that went to this account.
          overrides (int): Committed lines that went elsewhere while it was the default.
          account_name (None | str | Unset): The account's name.
          set_by (None | str | Unset): Who set or last moved it.
          set_at (None | str | Unset): When it was set or last moved.
          learned_from (None | str | Unset): The committed line it was learned from, when it was.
  """

  element_id: str
  mode: str
  confirmations: int
  overrides: int
  account_name: None | str | Unset = UNSET
  set_by: None | str | Unset = UNSET
  set_at: None | str | Unset = UNSET
  learned_from: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    mode = self.mode

    confirmations = self.confirmations

    overrides = self.overrides

    account_name: None | str | Unset
    if isinstance(self.account_name, Unset):
      account_name = UNSET
    else:
      account_name = self.account_name

    set_by: None | str | Unset
    if isinstance(self.set_by, Unset):
      set_by = UNSET
    else:
      set_by = self.set_by

    set_at: None | str | Unset
    if isinstance(self.set_at, Unset):
      set_at = UNSET
    else:
      set_at = self.set_at

    learned_from: None | str | Unset
    if isinstance(self.learned_from, Unset):
      learned_from = UNSET
    else:
      learned_from = self.learned_from

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "mode": mode,
        "confirmations": confirmations,
        "overrides": overrides,
      }
    )
    if account_name is not UNSET:
      field_dict["account_name"] = account_name
    if set_by is not UNSET:
      field_dict["set_by"] = set_by
    if set_at is not UNSET:
      field_dict["set_at"] = set_at
    if learned_from is not UNSET:
      field_dict["learned_from"] = learned_from

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    mode = d.pop("mode")

    confirmations = d.pop("confirmations")

    overrides = d.pop("overrides")

    def _parse_account_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    account_name = _parse_account_name(d.pop("account_name", UNSET))

    def _parse_set_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    set_by = _parse_set_by(d.pop("set_by", UNSET))

    def _parse_set_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    set_at = _parse_set_at(d.pop("set_at", UNSET))

    def _parse_learned_from(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    learned_from = _parse_learned_from(d.pop("learned_from", UNSET))

    agent_classification = cls(
      element_id=element_id,
      mode=mode,
      confirmations=confirmations,
      overrides=overrides,
      account_name=account_name,
      set_by=set_by,
      set_at=set_at,
      learned_from=learned_from,
    )

    agent_classification.additional_properties = d
    return agent_classification

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
