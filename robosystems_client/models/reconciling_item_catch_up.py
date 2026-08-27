from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconcilingItemCatchUp")


@_attrs_define
class ReconcilingItemCatchUp:
  """The catch-up entry a resolution posted.

  Attributes:
      event_id (str):
      posting_date (datetime.date):
      status (str):
      entry_id (None | str | Unset):
      transaction_id (None | str | Unset):
  """

  event_id: str
  posting_date: datetime.date
  status: str
  entry_id: None | str | Unset = UNSET
  transaction_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_id = self.event_id

    posting_date = self.posting_date.isoformat()

    status = self.status

    entry_id: None | str | Unset
    if isinstance(self.entry_id, Unset):
      entry_id = UNSET
    else:
      entry_id = self.entry_id

    transaction_id: None | str | Unset
    if isinstance(self.transaction_id, Unset):
      transaction_id = UNSET
    else:
      transaction_id = self.transaction_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
        "posting_date": posting_date,
        "status": status,
      }
    )
    if entry_id is not UNSET:
      field_dict["entry_id"] = entry_id
    if transaction_id is not UNSET:
      field_dict["transaction_id"] = transaction_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    event_id = d.pop("event_id")

    posting_date = datetime.date.fromisoformat(d.pop("posting_date"))

    status = d.pop("status")

    def _parse_entry_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entry_id = _parse_entry_id(d.pop("entry_id", UNSET))

    def _parse_transaction_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    transaction_id = _parse_transaction_id(d.pop("transaction_id", UNSET))

    reconciling_item_catch_up = cls(
      event_id=event_id,
      posting_date=posting_date,
      status=status,
      entry_id=entry_id,
      transaction_id=transaction_id,
    )

    reconciling_item_catch_up.additional_properties = d
    return reconciling_item_catch_up

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
