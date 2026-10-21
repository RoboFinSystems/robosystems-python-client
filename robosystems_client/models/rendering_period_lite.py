from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenderingPeriodLite")


@_attrs_define
class RenderingPeriodLite:
  """One period column in a rendered statement.

  Attributes:
      start (datetime.date):
      end (datetime.date):
      label (None | str | Unset):
      forecast (bool | None | Unset): True when this column comes from a forecast scenario's FactSet — the machine-
          readable seam marker (labels also carry a '(forecast)' suffix, but consumers should key styling off this flag,
          not label parsing). None/absent = an actuals column.
      presentation (None | str | Unset): 'as_closed' when the column's figures are the ones its month's close stamped,
          kept as the month closed; a live read of the books (live-financial-statement) can differ from them once a
          mapping is reclassified after the close. None for a report's own snapshot or a forecast column.
      stamped_at (datetime.datetime | None | Unset): When the close stamped the column; set with 'as_closed'.
  """

  start: datetime.date
  end: datetime.date
  label: None | str | Unset = UNSET
  forecast: bool | None | Unset = UNSET
  presentation: None | str | Unset = UNSET
  stamped_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    start = self.start.isoformat()

    end = self.end.isoformat()

    label: None | str | Unset
    if isinstance(self.label, Unset):
      label = UNSET
    else:
      label = self.label

    forecast: bool | None | Unset
    if isinstance(self.forecast, Unset):
      forecast = UNSET
    else:
      forecast = self.forecast

    presentation: None | str | Unset
    if isinstance(self.presentation, Unset):
      presentation = UNSET
    else:
      presentation = self.presentation

    stamped_at: None | str | Unset
    if isinstance(self.stamped_at, Unset):
      stamped_at = UNSET
    elif isinstance(self.stamped_at, datetime.datetime):
      stamped_at = self.stamped_at.isoformat()
    else:
      stamped_at = self.stamped_at

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
    if forecast is not UNSET:
      field_dict["forecast"] = forecast
    if presentation is not UNSET:
      field_dict["presentation"] = presentation
    if stamped_at is not UNSET:
      field_dict["stamped_at"] = stamped_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    start = datetime.date.fromisoformat(d.pop("start"))

    end = datetime.date.fromisoformat(d.pop("end"))

    def _parse_label(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    label = _parse_label(d.pop("label", UNSET))

    def _parse_forecast(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    forecast = _parse_forecast(d.pop("forecast", UNSET))

    def _parse_presentation(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    presentation = _parse_presentation(d.pop("presentation", UNSET))

    def _parse_stamped_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        stamped_at_type_0 = datetime.datetime.fromisoformat(data)

        return stamped_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    stamped_at = _parse_stamped_at(d.pop("stamped_at", UNSET))

    rendering_period_lite = cls(
      start=start,
      end=end,
      label=label,
      forecast=forecast,
      presentation=presentation,
      stamped_at=stamped_at,
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
