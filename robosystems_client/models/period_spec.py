from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PeriodSpec")


@_attrs_define
class PeriodSpec:
  """A reporting period column.

  Attributes:
      start (datetime.date):
      end (datetime.date):
      label (str):
  """

  start: datetime.date
  end: datetime.date
  label: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    start = self.start.isoformat()

    end = self.end.isoformat()

    label = self.label

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "start": start,
        "end": end,
        "label": label,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    start = isoparse(d.pop("start")).date()

    end = isoparse(d.pop("end")).date()

    label = d.pop("label")

    period_spec = cls(
      start=start,
      end=end,
      label=label,
    )

    period_spec.additional_properties = d
    return period_spec

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
