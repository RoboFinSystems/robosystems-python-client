from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.view_source_type import ViewSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewSource")


@_attrs_define
class ViewSource:
  """
  Attributes:
      type_ (ViewSourceType):
      period_start (None | str | Unset): Start date for transaction aggregation (YYYY-MM-DD)
      period_end (None | str | Unset): End date for transaction aggregation (YYYY-MM-DD)
      fact_set_id (None | str | Unset): FactSet ID for existing facts mode
      entity_id (None | str | Unset): Filter by entity (optional)
  """

  type_: ViewSourceType
  period_start: None | str | Unset = UNSET
  period_end: None | str | Unset = UNSET
  fact_set_id: None | str | Unset = UNSET
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    type_ = self.type_.value

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    else:
      period_start = self.period_start

    period_end: None | str | Unset
    if isinstance(self.period_end, Unset):
      period_end = UNSET
    else:
      period_end = self.period_end

    fact_set_id: None | str | Unset
    if isinstance(self.fact_set_id, Unset):
      fact_set_id = UNSET
    else:
      fact_set_id = self.fact_set_id

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "type": type_,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if fact_set_id is not UNSET:
      field_dict["fact_set_id"] = fact_set_id
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    type_ = ViewSourceType(d.pop("type"))

    def _parse_period_start(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_start = _parse_period_start(d.pop("period_start", UNSET))

    def _parse_period_end(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_end = _parse_period_end(d.pop("period_end", UNSET))

    def _parse_fact_set_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    fact_set_id = _parse_fact_set_id(d.pop("fact_set_id", UNSET))

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    view_source = cls(
      type_=type_,
      period_start=period_start,
      period_end=period_end,
      fact_set_id=fact_set_id,
      entity_id=entity_id,
    )

    view_source.additional_properties = d
    return view_source

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
