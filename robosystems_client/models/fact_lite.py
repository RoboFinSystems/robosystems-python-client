from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FactLite")


@_attrs_define
class FactLite:
  """Fact projection — just the values the envelope caller cares about.

  Attributes:
      id (str):
      element_id (str):
      value (float):
      period_end (datetime.date):
      period_type (str):
      fact_scope (str): historical | in_scope
      period_start (datetime.date | None | Unset):
      unit (str | Unset):  Default: 'USD'.
      fact_set_id (None | str | Unset):
  """

  id: str
  element_id: str
  value: float
  period_end: datetime.date
  period_type: str
  fact_scope: str
  period_start: datetime.date | None | Unset = UNSET
  unit: str | Unset = "USD"
  fact_set_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    element_id = self.element_id

    value = self.value

    period_end = self.period_end.isoformat()

    period_type = self.period_type

    fact_scope = self.fact_scope

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    elif isinstance(self.period_start, datetime.date):
      period_start = self.period_start.isoformat()
    else:
      period_start = self.period_start

    unit = self.unit

    fact_set_id: None | str | Unset
    if isinstance(self.fact_set_id, Unset):
      fact_set_id = UNSET
    else:
      fact_set_id = self.fact_set_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "element_id": element_id,
        "value": value,
        "period_end": period_end,
        "period_type": period_type,
        "fact_scope": fact_scope,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if unit is not UNSET:
      field_dict["unit"] = unit
    if fact_set_id is not UNSET:
      field_dict["fact_set_id"] = fact_set_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    element_id = d.pop("element_id")

    value = d.pop("value")

    period_end = isoparse(d.pop("period_end")).date()

    period_type = d.pop("period_type")

    fact_scope = d.pop("fact_scope")

    def _parse_period_start(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_start_type_0 = isoparse(data).date()

        return period_start_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_start = _parse_period_start(d.pop("period_start", UNSET))

    unit = d.pop("unit", UNSET)

    def _parse_fact_set_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    fact_set_id = _parse_fact_set_id(d.pop("fact_set_id", UNSET))

    fact_lite = cls(
      id=id,
      element_id=element_id,
      value=value,
      period_end=period_end,
      period_type=period_type,
      fact_scope=fact_scope,
      period_start=period_start,
      unit=unit,
      fact_set_id=fact_set_id,
    )

    fact_lite.additional_properties = d
    return fact_lite

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
