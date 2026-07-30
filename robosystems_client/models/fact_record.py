from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FactRecord")


@_attrs_define
class FactRecord:
  """
  Attributes:
      element_id (str): Element qname (e.g., 'us-gaap:Assets')
      element_name (None | str | Unset): Element local name
      period_end (None | str | Unset): Period end date (YYYY-MM-DD)
      value (float | None | Unset): Numeric fact value
      unit (None | str | Unset): Unit of measure (e.g., 'USD')
      entity_ticker (None | str | Unset): Entity ticker; present only when an entity filter was applied
      entity_name (None | str | Unset): Entity name; present only when an entity filter was applied
  """

  element_id: str
  element_name: None | str | Unset = UNSET
  period_end: None | str | Unset = UNSET
  value: float | None | Unset = UNSET
  unit: None | str | Unset = UNSET
  entity_ticker: None | str | Unset = UNSET
  entity_name: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    element_name: None | str | Unset
    if isinstance(self.element_name, Unset):
      element_name = UNSET
    else:
      element_name = self.element_name

    period_end: None | str | Unset
    if isinstance(self.period_end, Unset):
      period_end = UNSET
    else:
      period_end = self.period_end

    value: float | None | Unset
    if isinstance(self.value, Unset):
      value = UNSET
    else:
      value = self.value

    unit: None | str | Unset
    if isinstance(self.unit, Unset):
      unit = UNSET
    else:
      unit = self.unit

    entity_ticker: None | str | Unset
    if isinstance(self.entity_ticker, Unset):
      entity_ticker = UNSET
    else:
      entity_ticker = self.entity_ticker

    entity_name: None | str | Unset
    if isinstance(self.entity_name, Unset):
      entity_name = UNSET
    else:
      entity_name = self.entity_name

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
      }
    )
    if element_name is not UNSET:
      field_dict["element_name"] = element_name
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if value is not UNSET:
      field_dict["value"] = value
    if unit is not UNSET:
      field_dict["unit"] = unit
    if entity_ticker is not UNSET:
      field_dict["entity_ticker"] = entity_ticker
    if entity_name is not UNSET:
      field_dict["entity_name"] = entity_name

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    def _parse_element_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_name = _parse_element_name(d.pop("element_name", UNSET))

    def _parse_period_end(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_end = _parse_period_end(d.pop("period_end", UNSET))

    def _parse_value(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    value = _parse_value(d.pop("value", UNSET))

    def _parse_unit(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    unit = _parse_unit(d.pop("unit", UNSET))

    def _parse_entity_ticker(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_ticker = _parse_entity_ticker(d.pop("entity_ticker", UNSET))

    def _parse_entity_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_name = _parse_entity_name(d.pop("entity_name", UNSET))

    fact_record = cls(
      element_id=element_id,
      element_name=element_name,
      period_end=period_end,
      value=value,
      unit=unit,
      entity_ticker=entity_ticker,
      entity_name=entity_name,
    )

    fact_record.additional_properties = d
    return fact_record

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
