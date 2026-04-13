from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.draft_line_item import DraftLineItem


T = TypeVar("T", bound="DraftEntryResponse")


@_attrs_define
class DraftEntryResponse:
  """A single draft entry with full line item detail for review.

  Attributes:
      entry_id (str):
      posting_date (datetime.date):
      type_ (str): Entry type (e.g., 'closing', 'adjusting')
      line_items (list[DraftLineItem]):
      total_debit (int): Sum of debit amounts in cents
      total_credit (int): Sum of credit amounts in cents
      balanced (bool): True if total_debit == total_credit
      memo (None | str | Unset):
      provenance (None | str | Unset): Where the entry came from: 'ai_generated', 'manual_entry', etc.
      source_structure_id (None | str | Unset): Schedule structure that generated this entry (if any)
      source_structure_name (None | str | Unset): Human-readable name of the source schedule
  """

  entry_id: str
  posting_date: datetime.date
  type_: str
  line_items: list[DraftLineItem]
  total_debit: int
  total_credit: int
  balanced: bool
  memo: None | str | Unset = UNSET
  provenance: None | str | Unset = UNSET
  source_structure_id: None | str | Unset = UNSET
  source_structure_name: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entry_id = self.entry_id

    posting_date = self.posting_date.isoformat()

    type_ = self.type_

    line_items = []
    for line_items_item_data in self.line_items:
      line_items_item = line_items_item_data.to_dict()
      line_items.append(line_items_item)

    total_debit = self.total_debit

    total_credit = self.total_credit

    balanced = self.balanced

    memo: None | str | Unset
    if isinstance(self.memo, Unset):
      memo = UNSET
    else:
      memo = self.memo

    provenance: None | str | Unset
    if isinstance(self.provenance, Unset):
      provenance = UNSET
    else:
      provenance = self.provenance

    source_structure_id: None | str | Unset
    if isinstance(self.source_structure_id, Unset):
      source_structure_id = UNSET
    else:
      source_structure_id = self.source_structure_id

    source_structure_name: None | str | Unset
    if isinstance(self.source_structure_name, Unset):
      source_structure_name = UNSET
    else:
      source_structure_name = self.source_structure_name

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entry_id": entry_id,
        "posting_date": posting_date,
        "type": type_,
        "line_items": line_items,
        "total_debit": total_debit,
        "total_credit": total_credit,
        "balanced": balanced,
      }
    )
    if memo is not UNSET:
      field_dict["memo"] = memo
    if provenance is not UNSET:
      field_dict["provenance"] = provenance
    if source_structure_id is not UNSET:
      field_dict["source_structure_id"] = source_structure_id
    if source_structure_name is not UNSET:
      field_dict["source_structure_name"] = source_structure_name

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.draft_line_item import DraftLineItem

    d = dict(src_dict)
    entry_id = d.pop("entry_id")

    posting_date = isoparse(d.pop("posting_date")).date()

    type_ = d.pop("type")

    line_items = []
    _line_items = d.pop("line_items")
    for line_items_item_data in _line_items:
      line_items_item = DraftLineItem.from_dict(line_items_item_data)

      line_items.append(line_items_item)

    total_debit = d.pop("total_debit")

    total_credit = d.pop("total_credit")

    balanced = d.pop("balanced")

    def _parse_memo(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    memo = _parse_memo(d.pop("memo", UNSET))

    def _parse_provenance(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    provenance = _parse_provenance(d.pop("provenance", UNSET))

    def _parse_source_structure_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_structure_id = _parse_source_structure_id(
      d.pop("source_structure_id", UNSET)
    )

    def _parse_source_structure_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_structure_name = _parse_source_structure_name(
      d.pop("source_structure_name", UNSET)
    )

    draft_entry_response = cls(
      entry_id=entry_id,
      posting_date=posting_date,
      type_=type_,
      line_items=line_items,
      total_debit=total_debit,
      total_credit=total_credit,
      balanced=balanced,
      memo=memo,
      provenance=provenance,
      source_structure_id=source_structure_id,
      source_structure_name=source_structure_name,
    )

    draft_entry_response.additional_properties = d
    return draft_entry_response

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
