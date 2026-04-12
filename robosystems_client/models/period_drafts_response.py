from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
  from ..models.draft_entry_response import DraftEntryResponse


T = TypeVar("T", bound="PeriodDraftsResponse")


@_attrs_define
class PeriodDraftsResponse:
  """All draft entries for a fiscal period, ready for review before close.

  Attributes:
      period (str): YYYY-MM period name
      period_start (datetime.date):
      period_end (datetime.date):
      draft_count (int):
      total_debit (int): Sum across all drafts, in cents
      total_credit (int): Sum across all drafts, in cents
      all_balanced (bool): True if every draft entry has debit == credit
      drafts (list[DraftEntryResponse]):
  """

  period: str
  period_start: datetime.date
  period_end: datetime.date
  draft_count: int
  total_debit: int
  total_credit: int
  all_balanced: bool
  drafts: list[DraftEntryResponse]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    draft_count = self.draft_count

    total_debit = self.total_debit

    total_credit = self.total_credit

    all_balanced = self.all_balanced

    drafts = []
    for drafts_item_data in self.drafts:
      drafts_item = drafts_item_data.to_dict()
      drafts.append(drafts_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
        "period_start": period_start,
        "period_end": period_end,
        "draft_count": draft_count,
        "total_debit": total_debit,
        "total_credit": total_credit,
        "all_balanced": all_balanced,
        "drafts": drafts,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.draft_entry_response import DraftEntryResponse

    d = dict(src_dict)
    period = d.pop("period")

    period_start = isoparse(d.pop("period_start")).date()

    period_end = isoparse(d.pop("period_end")).date()

    draft_count = d.pop("draft_count")

    total_debit = d.pop("total_debit")

    total_credit = d.pop("total_credit")

    all_balanced = d.pop("all_balanced")

    drafts = []
    _drafts = d.pop("drafts")
    for drafts_item_data in _drafts:
      drafts_item = DraftEntryResponse.from_dict(drafts_item_data)

      drafts.append(drafts_item)

    period_drafts_response = cls(
      period=period,
      period_start=period_start,
      period_end=period_end,
      draft_count=draft_count,
      total_debit=total_debit,
      total_credit=total_credit,
      all_balanced=all_balanced,
      drafts=drafts,
    )

    period_drafts_response.additional_properties = d
    return period_drafts_response

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
