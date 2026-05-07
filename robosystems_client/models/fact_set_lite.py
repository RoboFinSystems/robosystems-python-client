from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FactSetLite")


@_attrs_define
class FactSetLite:
  """FactSet projection — period-specific instantiation of the Structure.

  The envelope carries one ``FactSetLite`` per block when a FactSet row
  exists for the requested period; legacy writes that pre-date FactSet
  stamping leave ``fact_set`` null until the expand pass starts
  populating those rows.

      Attributes:
          id (str):
          period_end (datetime.date):
          factset_type (str): 'report' | 'schedule' | 'custom'. Enum closure enforced by the ``public.fact_sets`` CHECK
              constraint.
          entity_id (str):
          structure_id (None | str | Unset):
          period_start (datetime.date | None | Unset):
          report_id (None | str | Unset): Back-pointer to the ``reports`` table while ``report_id`` still lives on facts.
              Drops out once the retirement migration lands.
  """

  id: str
  period_end: datetime.date
  factset_type: str
  entity_id: str
  structure_id: None | str | Unset = UNSET
  period_start: datetime.date | None | Unset = UNSET
  report_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    period_end = self.period_end.isoformat()

    factset_type = self.factset_type

    entity_id = self.entity_id

    structure_id: None | str | Unset
    if isinstance(self.structure_id, Unset):
      structure_id = UNSET
    else:
      structure_id = self.structure_id

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    elif isinstance(self.period_start, datetime.date):
      period_start = self.period_start.isoformat()
    else:
      period_start = self.period_start

    report_id: None | str | Unset
    if isinstance(self.report_id, Unset):
      report_id = UNSET
    else:
      report_id = self.report_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "period_end": period_end,
        "factset_type": factset_type,
        "entity_id": entity_id,
      }
    )
    if structure_id is not UNSET:
      field_dict["structure_id"] = structure_id
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if report_id is not UNSET:
      field_dict["report_id"] = report_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    period_end = isoparse(d.pop("period_end")).date()

    factset_type = d.pop("factset_type")

    entity_id = d.pop("entity_id")

    def _parse_structure_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    structure_id = _parse_structure_id(d.pop("structure_id", UNSET))

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

    def _parse_report_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    report_id = _parse_report_id(d.pop("report_id", UNSET))

    fact_set_lite = cls(
      id=id,
      period_end=period_end,
      factset_type=factset_type,
      entity_id=entity_id,
      structure_id=structure_id,
      period_start=period_start,
      report_id=report_id,
    )

    fact_set_lite.additional_properties = d
    return fact_set_lite

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
