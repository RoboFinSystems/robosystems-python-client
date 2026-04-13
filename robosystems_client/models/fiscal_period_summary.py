from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FiscalPeriodSummary")


@_attrs_define
class FiscalPeriodSummary:
  """
  Attributes:
      name (str): Period name (YYYY-MM)
      start_date (datetime.date):
      end_date (datetime.date):
      status (str): 'open' | 'closing' | 'closed'
      closed_at (datetime.datetime | None | Unset):
  """

  name: str
  start_date: datetime.date
  end_date: datetime.date
  status: str
  closed_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    start_date = self.start_date.isoformat()

    end_date = self.end_date.isoformat()

    status = self.status

    closed_at: None | str | Unset
    if isinstance(self.closed_at, Unset):
      closed_at = UNSET
    elif isinstance(self.closed_at, datetime.datetime):
      closed_at = self.closed_at.isoformat()
    else:
      closed_at = self.closed_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
        "status": status,
      }
    )
    if closed_at is not UNSET:
      field_dict["closed_at"] = closed_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    start_date = isoparse(d.pop("start_date")).date()

    end_date = isoparse(d.pop("end_date")).date()

    status = d.pop("status")

    def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        closed_at_type_0 = isoparse(data)

        return closed_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

    fiscal_period_summary = cls(
      name=name,
      start_date=start_date,
      end_date=end_date,
      status=status,
      closed_at=closed_at,
    )

    fiscal_period_summary.additional_properties = d
    return fiscal_period_summary

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
