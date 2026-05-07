from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenderingPeriodLite")


@_attrs_define
class RenderingPeriodLite:
  """One period column in a rendered statement.

  Attributes:
      start (datetime.date):
      end (datetime.date):
      label (None | str | Unset):
  """

  start: datetime.date
  end: datetime.date
  label: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    start = self.start.isoformat()

    end = self.end.isoformat()

    label: None | str | Unset
    if isinstance(self.label, Unset):
      label = UNSET
    else:
      label = self.label

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "start": start,
        "end": end,
      }
    )
    if label is not UNSET:
      field_dict["label"] = label

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    start = isoparse(d.pop("start")).date()

    end = isoparse(d.pop("end")).date()

    def _parse_label(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    label = _parse_label(d.pop("label", UNSET))

    rendering_period_lite = cls(
      start=start,
      end=end,
      label=label,
    )

    rendering_period_lite.additional_properties = d
    return rendering_period_lite

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
