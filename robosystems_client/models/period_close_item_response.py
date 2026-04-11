from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeriodCloseItemResponse")


@_attrs_define
class PeriodCloseItemResponse:
  """
  Attributes:
      structure_id (str):
      structure_name (str):
      amount (float):
      status (str):
      entry_id (None | str | Unset):
      reversal_entry_id (None | str | Unset):
      reversal_status (None | str | Unset):
  """

  structure_id: str
  structure_name: str
  amount: float
  status: str
  entry_id: None | str | Unset = UNSET
  reversal_entry_id: None | str | Unset = UNSET
  reversal_status: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    structure_name = self.structure_name

    amount = self.amount

    status = self.status

    entry_id: None | str | Unset
    if isinstance(self.entry_id, Unset):
      entry_id = UNSET
    else:
      entry_id = self.entry_id

    reversal_entry_id: None | str | Unset
    if isinstance(self.reversal_entry_id, Unset):
      reversal_entry_id = UNSET
    else:
      reversal_entry_id = self.reversal_entry_id

    reversal_status: None | str | Unset
    if isinstance(self.reversal_status, Unset):
      reversal_status = UNSET
    else:
      reversal_status = self.reversal_status

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "structure_name": structure_name,
        "amount": amount,
        "status": status,
      }
    )
    if entry_id is not UNSET:
      field_dict["entry_id"] = entry_id
    if reversal_entry_id is not UNSET:
      field_dict["reversal_entry_id"] = reversal_entry_id
    if reversal_status is not UNSET:
      field_dict["reversal_status"] = reversal_status

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    structure_name = d.pop("structure_name")

    amount = d.pop("amount")

    status = d.pop("status")

    def _parse_entry_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entry_id = _parse_entry_id(d.pop("entry_id", UNSET))

    def _parse_reversal_entry_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reversal_entry_id = _parse_reversal_entry_id(d.pop("reversal_entry_id", UNSET))

    def _parse_reversal_status(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reversal_status = _parse_reversal_status(d.pop("reversal_status", UNSET))

    period_close_item_response = cls(
      structure_id=structure_id,
      structure_name=structure_name,
      amount=amount,
      status=status,
      entry_id=entry_id,
      reversal_entry_id=reversal_entry_id,
      reversal_status=reversal_status,
    )

    period_close_item_response.additional_properties = d
    return period_close_item_response

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
