from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconcilingItemEntrySummary")


@_attrs_define
class ReconcilingItemEntrySummary:
  """One entry on either side of the comparison.

  Attributes:
      entry_id (None | str | Unset): Entry id; null for the accepted side, which is not posted yet
      external_id (None | str | Unset):
      posting_date (datetime.date | None | Unset):
      memo (None | str | Unset):
      status (None | str | Unset): Entry status; null on the accepted side
      total_debit (int | Unset):  Default: 0.
      total_credit (int | Unset):  Default: 0.
  """

  entry_id: None | str | Unset = UNSET
  external_id: None | str | Unset = UNSET
  posting_date: datetime.date | None | Unset = UNSET
  memo: None | str | Unset = UNSET
  status: None | str | Unset = UNSET
  total_debit: int | Unset = 0
  total_credit: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entry_id: None | str | Unset
    if isinstance(self.entry_id, Unset):
      entry_id = UNSET
    else:
      entry_id = self.entry_id

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

    posting_date: None | str | Unset
    if isinstance(self.posting_date, Unset):
      posting_date = UNSET
    elif isinstance(self.posting_date, datetime.date):
      posting_date = self.posting_date.isoformat()
    else:
      posting_date = self.posting_date

    memo: None | str | Unset
    if isinstance(self.memo, Unset):
      memo = UNSET
    else:
      memo = self.memo

    status: None | str | Unset
    if isinstance(self.status, Unset):
      status = UNSET
    else:
      status = self.status

    total_debit = self.total_debit

    total_credit = self.total_credit

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if entry_id is not UNSET:
      field_dict["entry_id"] = entry_id
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if posting_date is not UNSET:
      field_dict["posting_date"] = posting_date
    if memo is not UNSET:
      field_dict["memo"] = memo
    if status is not UNSET:
      field_dict["status"] = status
    if total_debit is not UNSET:
      field_dict["total_debit"] = total_debit
    if total_credit is not UNSET:
      field_dict["total_credit"] = total_credit

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_entry_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entry_id = _parse_entry_id(d.pop("entry_id", UNSET))

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

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

    def _parse_memo(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    memo = _parse_memo(d.pop("memo", UNSET))

    def _parse_status(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    status = _parse_status(d.pop("status", UNSET))

    total_debit = d.pop("total_debit", UNSET)

    total_credit = d.pop("total_credit", UNSET)

    reconciling_item_entry_summary = cls(
      entry_id=entry_id,
      external_id=external_id,
      posting_date=posting_date,
      memo=memo,
      status=status,
      total_debit=total_debit,
      total_credit=total_credit,
    )

    reconciling_item_entry_summary.additional_properties = d
    return reconciling_item_entry_summary

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
