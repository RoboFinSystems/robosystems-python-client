from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconcilingItemRegenerated")


@_attrs_define
class ReconcilingItemRegenerated:
  """The entries a restate rebuilt.

  Attributes:
      transaction_ids (list[str] | Unset):
      entry_ids (list[str] | Unset):
  """

  transaction_ids: list[str] | Unset = UNSET
  entry_ids: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    transaction_ids: list[str] | Unset = UNSET
    if not isinstance(self.transaction_ids, Unset):
      transaction_ids = self.transaction_ids

    entry_ids: list[str] | Unset = UNSET
    if not isinstance(self.entry_ids, Unset):
      entry_ids = self.entry_ids

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if transaction_ids is not UNSET:
      field_dict["transaction_ids"] = transaction_ids
    if entry_ids is not UNSET:
      field_dict["entry_ids"] = entry_ids

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    transaction_ids = cast(list[str], d.pop("transaction_ids", UNSET))

    entry_ids = cast(list[str], d.pop("entry_ids", UNSET))

    reconciling_item_regenerated = cls(
      transaction_ids=transaction_ids,
      entry_ids=entry_ids,
    )

    reconciling_item_regenerated.additional_properties = d
    return reconciling_item_regenerated

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
