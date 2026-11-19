from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportFactRow")


@_attrs_define
class ReportFactRow:
  """One value read from the report.

  Attributes:
      concept (str): The concept qname the value is for.
      value (float | None | str): The number, or the text for a non-numeric concept.
      end (datetime.date): The date the value is as of, or the last day of its period.
      start (datetime.date | None | Unset): The first day of the period; omit for a balance at a date.
      unit (None | str | Unset): A currency code (`USD`), `shares` or `pure`. Required for a number.
      decimals (int | None | Unset): Precision of the number: `0` to the unit, `-3` to the thousand, `2` to the cent.
          Totals are checked to this precision.
      source (None | str | Unset): Where the value was read from: the document, then `#page=3` for a PDF or
          `#sheet=BS&cell=B10` for a workbook, with `&label=` and the line's wording when useful. Kept on the fact.
  """

  concept: str
  value: float | None | str
  end: datetime.date
  start: datetime.date | None | Unset = UNSET
  unit: None | str | Unset = UNSET
  decimals: int | None | Unset = UNSET
  source: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    concept = self.concept

    value: float | None | str
    value = self.value

    end = self.end.isoformat()

    start: None | str | Unset
    if isinstance(self.start, Unset):
      start = UNSET
    elif isinstance(self.start, datetime.date):
      start = self.start.isoformat()
    else:
      start = self.start

    unit: None | str | Unset
    if isinstance(self.unit, Unset):
      unit = UNSET
    else:
      unit = self.unit

    decimals: int | None | Unset
    if isinstance(self.decimals, Unset):
      decimals = UNSET
    else:
      decimals = self.decimals

    source: None | str | Unset
    if isinstance(self.source, Unset):
      source = UNSET
    else:
      source = self.source

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "concept": concept,
        "value": value,
        "end": end,
      }
    )
    if start is not UNSET:
      field_dict["start"] = start
    if unit is not UNSET:
      field_dict["unit"] = unit
    if decimals is not UNSET:
      field_dict["decimals"] = decimals
    if source is not UNSET:
      field_dict["source"] = source

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    concept = d.pop("concept")

    def _parse_value(data: object) -> float | None | str:
      if data is None:
        return data
      return cast(float | None | str, data)

    value = _parse_value(d.pop("value"))

    end = datetime.date.fromisoformat(d.pop("end"))

    def _parse_start(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        start_type_0 = datetime.date.fromisoformat(data)

        return start_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    start = _parse_start(d.pop("start", UNSET))

    def _parse_unit(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    unit = _parse_unit(d.pop("unit", UNSET))

    def _parse_decimals(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    decimals = _parse_decimals(d.pop("decimals", UNSET))

    def _parse_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source = _parse_source(d.pop("source", UNSET))

    report_fact_row = cls(
      concept=concept,
      value=value,
      end=end,
      start=start,
      unit=unit,
      decimals=decimals,
      source=source,
    )

    report_fact_row.additional_properties = d
    return report_fact_row

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
