from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
  from ..models.period_close_item_response import PeriodCloseItemResponse


T = TypeVar("T", bound="PeriodCloseStatusResponse")


@_attrs_define
class PeriodCloseStatusResponse:
  """
  Attributes:
      fiscal_period_start (datetime.date):
      fiscal_period_end (datetime.date):
      period_status (str):
      schedules (list[PeriodCloseItemResponse]):
      total_draft (int):
      total_posted (int):
  """

  fiscal_period_start: datetime.date
  fiscal_period_end: datetime.date
  period_status: str
  schedules: list[PeriodCloseItemResponse]
  total_draft: int
  total_posted: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    fiscal_period_start = self.fiscal_period_start.isoformat()

    fiscal_period_end = self.fiscal_period_end.isoformat()

    period_status = self.period_status

    schedules = []
    for schedules_item_data in self.schedules:
      schedules_item = schedules_item_data.to_dict()
      schedules.append(schedules_item)

    total_draft = self.total_draft

    total_posted = self.total_posted

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "fiscal_period_start": fiscal_period_start,
        "fiscal_period_end": fiscal_period_end,
        "period_status": period_status,
        "schedules": schedules,
        "total_draft": total_draft,
        "total_posted": total_posted,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.period_close_item_response import PeriodCloseItemResponse

    d = dict(src_dict)
    fiscal_period_start = isoparse(d.pop("fiscal_period_start")).date()

    fiscal_period_end = isoparse(d.pop("fiscal_period_end")).date()

    period_status = d.pop("period_status")

    schedules = []
    _schedules = d.pop("schedules")
    for schedules_item_data in _schedules:
      schedules_item = PeriodCloseItemResponse.from_dict(schedules_item_data)

      schedules.append(schedules_item)

    total_draft = d.pop("total_draft")

    total_posted = d.pop("total_posted")

    period_close_status_response = cls(
      fiscal_period_start=fiscal_period_start,
      fiscal_period_end=fiscal_period_end,
      period_status=period_status,
      schedules=schedules,
      total_draft=total_draft,
      total_posted=total_posted,
    )

    period_close_status_response.additional_properties = d
    return period_close_status_response

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
