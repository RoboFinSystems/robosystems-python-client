from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconciliationComponent")


@_attrs_define
class ReconciliationComponent:
  """One part of an account's independent balance: what a single schedule
  says the account carries, a recorded statement balance, or a ledger line
  outstanding at the statement's date.

      Attributes:
          name (str): The schedule's name, the statement and its date, or the outstanding line's description.
          amount (float): What this part says the account holds, debit-positive.
          kind (None | str | Unset): `schedule`, `statement`, or `outstanding`: a ledger line on a bank-fed account that
              did not come from the feed, dated on or before the statement, so the bank had not cleared it.
          posting_date (datetime.date | None | Unset): An `outstanding` line's posting date.
          entry_id (None | str | Unset): The journal entry an `outstanding` line belongs to.
          structure_id (None | str | Unset): The schedule, for a `schedule_register` part.
          event_id (None | str | Unset): The recorded balance, for a `statement` part; the event behind an `outstanding`
              line, when it has one.
          document_id (None | str | Unset): The statement document given as evidence, when one was.
          note (None | str | Unset): Why a schedule carries nothing (disposed of, or ended early), or the note recorded
              with a statement balance.
  """

  name: str
  amount: float
  kind: None | str | Unset = UNSET
  posting_date: datetime.date | None | Unset = UNSET
  entry_id: None | str | Unset = UNSET
  structure_id: None | str | Unset = UNSET
  event_id: None | str | Unset = UNSET
  document_id: None | str | Unset = UNSET
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    amount = self.amount

    kind: None | str | Unset
    if isinstance(self.kind, Unset):
      kind = UNSET
    else:
      kind = self.kind

    posting_date: None | str | Unset
    if isinstance(self.posting_date, Unset):
      posting_date = UNSET
    elif isinstance(self.posting_date, datetime.date):
      posting_date = self.posting_date.isoformat()
    else:
      posting_date = self.posting_date

    entry_id: None | str | Unset
    if isinstance(self.entry_id, Unset):
      entry_id = UNSET
    else:
      entry_id = self.entry_id

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
    if kind is not UNSET:
      field_dict["kind"] = kind
    if posting_date is not UNSET:
      field_dict["posting_date"] = posting_date
    if entry_id is not UNSET:
      field_dict["entry_id"] = entry_id
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

    def _parse_kind(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    kind = _parse_kind(d.pop("kind", UNSET))

    def _parse_posting_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        posting_date_type_0 = datetime.date.fromisoformat(data)

        return posting_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    posting_date = _parse_posting_date(d.pop("posting_date", UNSET))

    def _parse_entry_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entry_id = _parse_entry_id(d.pop("entry_id", UNSET))

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
      kind=kind,
      posting_date=posting_date,
      entry_id=entry_id,
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
