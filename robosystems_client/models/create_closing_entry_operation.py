from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateClosingEntryOperation")


@_attrs_define
class CreateClosingEntryOperation:
  """
  Attributes:
      posting_date (datetime.date): Posting date for the entry
      period_start (datetime.date): Period start
      period_end (datetime.date): Period end
      structure_id (str):
      memo (None | str | Unset): Override memo
  """

  posting_date: datetime.date
  period_start: datetime.date
  period_end: datetime.date
  structure_id: str
  memo: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    posting_date = self.posting_date.isoformat()

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    structure_id = self.structure_id

    memo: None | str | Unset
    if isinstance(self.memo, Unset):
      memo = UNSET
    else:
      memo = self.memo

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "posting_date": posting_date,
        "period_start": period_start,
        "period_end": period_end,
        "structure_id": structure_id,
      }
    )
    if memo is not UNSET:
      field_dict["memo"] = memo

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    posting_date = isoparse(d.pop("posting_date")).date()

    period_start = isoparse(d.pop("period_start")).date()

    period_end = isoparse(d.pop("period_end")).date()

    structure_id = d.pop("structure_id")

    def _parse_memo(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    memo = _parse_memo(d.pop("memo", UNSET))

    create_closing_entry_operation = cls(
      posting_date=posting_date,
      period_start=period_start,
      period_end=period_end,
      structure_id=structure_id,
      memo=memo,
    )

    create_closing_entry_operation.additional_properties = d
    return create_closing_entry_operation

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
