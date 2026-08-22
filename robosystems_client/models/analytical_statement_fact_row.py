from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticalStatementFactRow")


@_attrs_define
class AnalyticalStatementFactRow:
  """A single fact row from the graph-backed statement analysis.

  Attributes:
      qname (str):
      name (str):
      canonical_concept (None | str | Unset):
      value (float | None | Unset):
      start_date (None | str | Unset):
      end_date (None | str | Unset):
      period_type (None | str | Unset):
      duration_type (None | str | Unset):
  """

  qname: str
  name: str
  canonical_concept: None | str | Unset = UNSET
  value: float | None | Unset = UNSET
  start_date: None | str | Unset = UNSET
  end_date: None | str | Unset = UNSET
  period_type: None | str | Unset = UNSET
  duration_type: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    qname = self.qname

    name = self.name

    canonical_concept: None | str | Unset
    if isinstance(self.canonical_concept, Unset):
      canonical_concept = UNSET
    else:
      canonical_concept = self.canonical_concept

    value: float | None | Unset
    if isinstance(self.value, Unset):
      value = UNSET
    else:
      value = self.value

    start_date: None | str | Unset
    if isinstance(self.start_date, Unset):
      start_date = UNSET
    else:
      start_date = self.start_date

    end_date: None | str | Unset
    if isinstance(self.end_date, Unset):
      end_date = UNSET
    else:
      end_date = self.end_date

    period_type: None | str | Unset
    if isinstance(self.period_type, Unset):
      period_type = UNSET
    else:
      period_type = self.period_type

    duration_type: None | str | Unset
    if isinstance(self.duration_type, Unset):
      duration_type = UNSET
    else:
      duration_type = self.duration_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "qname": qname,
        "name": name,
      }
    )
    if canonical_concept is not UNSET:
      field_dict["canonical_concept"] = canonical_concept
    if value is not UNSET:
      field_dict["value"] = value
    if start_date is not UNSET:
      field_dict["start_date"] = start_date
    if end_date is not UNSET:
      field_dict["end_date"] = end_date
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if duration_type is not UNSET:
      field_dict["duration_type"] = duration_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    qname = d.pop("qname")

    name = d.pop("name")

    def _parse_canonical_concept(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    canonical_concept = _parse_canonical_concept(d.pop("canonical_concept", UNSET))

    def _parse_value(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    value = _parse_value(d.pop("value", UNSET))

    def _parse_start_date(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    start_date = _parse_start_date(d.pop("start_date", UNSET))

    def _parse_end_date(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    end_date = _parse_end_date(d.pop("end_date", UNSET))

    def _parse_period_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_type = _parse_period_type(d.pop("period_type", UNSET))

    def _parse_duration_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    duration_type = _parse_duration_type(d.pop("duration_type", UNSET))

    analytical_statement_fact_row = cls(
      qname=qname,
      name=name,
      canonical_concept=canonical_concept,
      value=value,
      start_date=start_date,
      end_date=end_date,
      period_type=period_type,
      duration_type=duration_type,
    )

    analytical_statement_fact_row.additional_properties = d
    return analytical_statement_fact_row

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
