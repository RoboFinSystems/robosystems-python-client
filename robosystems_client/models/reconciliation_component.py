from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconciliationComponent")


@_attrs_define
class ReconciliationComponent:
  """One part of an account's independent balance: what a single schedule
  says the account carries, or a recorded statement balance.

      Attributes:
          name (str): The schedule's name, or the statement and its date.
          amount (float): What this part says the account holds, debit-positive.
          structure_id (None | str | Unset): The schedule, for a `schedule_register` part.
          event_id (None | str | Unset): The recorded balance, for a `statement` part.
          document_id (None | str | Unset): The statement document given as evidence, when one was.
          note (None | str | Unset): Why a schedule carries nothing (disposed of, or ended early), or the note recorded
              with a statement balance.
  """

  name: str
  amount: float
  structure_id: None | str | Unset = UNSET
  event_id: None | str | Unset = UNSET
  document_id: None | str | Unset = UNSET
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    amount = self.amount

    structure_id: None | str | Unset
    if isinstance(self.structure_id, Unset):
      structure_id = UNSET
    else:
      structure_id = self.structure_id

    event_id: None | str | Unset
    if isinstance(self.event_id, Unset):
      event_id = UNSET
    else:
      event_id = self.event_id

    document_id: None | str | Unset
    if isinstance(self.document_id, Unset):
      document_id = UNSET
    else:
      document_id = self.document_id

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "amount": amount,
      }
    )
    if structure_id is not UNSET:
      field_dict["structure_id"] = structure_id
    if event_id is not UNSET:
      field_dict["event_id"] = event_id
    if document_id is not UNSET:
      field_dict["document_id"] = document_id
    if note is not UNSET:
      field_dict["note"] = note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    amount = d.pop("amount")

    def _parse_structure_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    structure_id = _parse_structure_id(d.pop("structure_id", UNSET))

    def _parse_event_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    event_id = _parse_event_id(d.pop("event_id", UNSET))

    def _parse_document_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    document_id = _parse_document_id(d.pop("document_id", UNSET))

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    reconciliation_component = cls(
      name=name,
      amount=amount,
      structure_id=structure_id,
      event_id=event_id,
      document_id=document_id,
      note=note,
    )

    reconciliation_component.additional_properties = d
    return reconciliation_component

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
