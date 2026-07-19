from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FactLite")


@_attrs_define
class FactLite:
  """Fact projection — just the values the envelope caller cares about.

  Attributes:
      id (str):
      element_id (str):
      period_end (datetime.date):
      period_type (str):
      fact_scope (str): historical | in_scope
      element_name (None | str | Unset):
      element_qname (None | str | Unset):
      value (float | None | Unset): Numeric value; null for Nonnumeric (text-block) facts.
      text_value (None | str | Unset): Text payload for Nonnumeric facts; null for numeric.
      fact_type (str | Unset): Numeric | Nonnumeric Default: 'Numeric'.
      content_type (None | str | Unset): MIME type of text_value (e.g. 'text/markdown').
      period_start (datetime.date | None | Unset):
      unit (str | Unset):  Default: 'USD'.
      fact_set_id (None | str | Unset):
  """

  id: str
  element_id: str
  period_end: datetime.date
  period_type: str
  fact_scope: str
  element_name: None | str | Unset = UNSET
  element_qname: None | str | Unset = UNSET
  value: float | None | Unset = UNSET
  text_value: None | str | Unset = UNSET
  fact_type: str | Unset = "Numeric"
  content_type: None | str | Unset = UNSET
  period_start: datetime.date | None | Unset = UNSET
  unit: str | Unset = "USD"
  fact_set_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    element_id = self.element_id

    period_end = self.period_end.isoformat()

    period_type = self.period_type

    fact_scope = self.fact_scope

    element_name: None | str | Unset
    if isinstance(self.element_name, Unset):
      element_name = UNSET
    else:
      element_name = self.element_name

    element_qname: None | str | Unset
    if isinstance(self.element_qname, Unset):
      element_qname = UNSET
    else:
      element_qname = self.element_qname

    value: float | None | Unset
    if isinstance(self.value, Unset):
      value = UNSET
    else:
      value = self.value

    text_value: None | str | Unset
    if isinstance(self.text_value, Unset):
      text_value = UNSET
    else:
      text_value = self.text_value

    fact_type = self.fact_type

    content_type: None | str | Unset
    if isinstance(self.content_type, Unset):
      content_type = UNSET
    else:
      content_type = self.content_type

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
        "period_end": period_end,
        "period_type": period_type,
        "fact_scope": fact_scope,
      }
    )
    if element_name is not UNSET:
      field_dict["element_name"] = element_name
    if element_qname is not UNSET:
      field_dict["element_qname"] = element_qname
    if value is not UNSET:
      field_dict["value"] = value
    if text_value is not UNSET:
      field_dict["text_value"] = text_value
    if fact_type is not UNSET:
      field_dict["fact_type"] = fact_type
    if content_type is not UNSET:
      field_dict["content_type"] = content_type
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

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    period_type = d.pop("period_type")

    fact_scope = d.pop("fact_scope")

    def _parse_element_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_name = _parse_element_name(d.pop("element_name", UNSET))

    def _parse_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_qname = _parse_element_qname(d.pop("element_qname", UNSET))

    def _parse_value(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    value = _parse_value(d.pop("value", UNSET))

    def _parse_text_value(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    text_value = _parse_text_value(d.pop("text_value", UNSET))

    fact_type = d.pop("fact_type", UNSET)

    def _parse_content_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    content_type = _parse_content_type(d.pop("content_type", UNSET))

    def _parse_period_start(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_start_type_0 = datetime.date.fromisoformat(data)

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
      period_end=period_end,
      period_type=period_type,
      fact_scope=fact_scope,
      element_name=element_name,
      element_qname=element_qname,
      value=value,
      text_value=text_value,
      fact_type=fact_type,
      content_type=content_type,
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
