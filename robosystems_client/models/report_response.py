from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.period_spec import PeriodSpec
  from ..models.structure_summary import StructureSummary


T = TypeVar("T", bound="ReportResponse")


@_attrs_define
class ReportResponse:
  """Report definition summary.

  Attributes:
      id (str):
      name (str):
      taxonomy_id (str):
      generation_status (str):
      period_type (str):
      comparative (bool):
      created_at (datetime.datetime):
      period_start (datetime.date | None | Unset):
      period_end (datetime.date | None | Unset):
      periods (list[PeriodSpec] | None | Unset):
      mapping_id (None | str | Unset):
      ai_generated (bool | Unset):  Default: False.
      last_generated (datetime.datetime | None | Unset):
      structures (list[StructureSummary] | Unset):
      entity_name (None | str | Unset):
      source_graph_id (None | str | Unset):
      source_report_id (None | str | Unset):
      shared_at (datetime.datetime | None | Unset):
  """

  id: str
  name: str
  taxonomy_id: str
  generation_status: str
  period_type: str
  comparative: bool
  created_at: datetime.datetime
  period_start: datetime.date | None | Unset = UNSET
  period_end: datetime.date | None | Unset = UNSET
  periods: list[PeriodSpec] | None | Unset = UNSET
  mapping_id: None | str | Unset = UNSET
  ai_generated: bool | Unset = False
  last_generated: datetime.datetime | None | Unset = UNSET
  structures: list[StructureSummary] | Unset = UNSET
  entity_name: None | str | Unset = UNSET
  source_graph_id: None | str | Unset = UNSET
  source_report_id: None | str | Unset = UNSET
  shared_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    taxonomy_id = self.taxonomy_id

    generation_status = self.generation_status

    period_type = self.period_type

    comparative = self.comparative

    created_at = self.created_at.isoformat()

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    elif isinstance(self.period_start, datetime.date):
      period_start = self.period_start.isoformat()
    else:
      period_start = self.period_start

    period_end: None | str | Unset
    if isinstance(self.period_end, Unset):
      period_end = UNSET
    elif isinstance(self.period_end, datetime.date):
      period_end = self.period_end.isoformat()
    else:
      period_end = self.period_end

    periods: list[dict[str, Any]] | None | Unset
    if isinstance(self.periods, Unset):
      periods = UNSET
    elif isinstance(self.periods, list):
      periods = []
      for periods_type_0_item_data in self.periods:
        periods_type_0_item = periods_type_0_item_data.to_dict()
        periods.append(periods_type_0_item)

    else:
      periods = self.periods

    mapping_id: None | str | Unset
    if isinstance(self.mapping_id, Unset):
      mapping_id = UNSET
    else:
      mapping_id = self.mapping_id

    ai_generated = self.ai_generated

    last_generated: None | str | Unset
    if isinstance(self.last_generated, Unset):
      last_generated = UNSET
    elif isinstance(self.last_generated, datetime.datetime):
      last_generated = self.last_generated.isoformat()
    else:
      last_generated = self.last_generated

    structures: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.structures, Unset):
      structures = []
      for structures_item_data in self.structures:
        structures_item = structures_item_data.to_dict()
        structures.append(structures_item)

    entity_name: None | str | Unset
    if isinstance(self.entity_name, Unset):
      entity_name = UNSET
    else:
      entity_name = self.entity_name

    source_graph_id: None | str | Unset
    if isinstance(self.source_graph_id, Unset):
      source_graph_id = UNSET
    else:
      source_graph_id = self.source_graph_id

    source_report_id: None | str | Unset
    if isinstance(self.source_report_id, Unset):
      source_report_id = UNSET
    else:
      source_report_id = self.source_report_id

    shared_at: None | str | Unset
    if isinstance(self.shared_at, Unset):
      shared_at = UNSET
    elif isinstance(self.shared_at, datetime.datetime):
      shared_at = self.shared_at.isoformat()
    else:
      shared_at = self.shared_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "taxonomy_id": taxonomy_id,
        "generation_status": generation_status,
        "period_type": period_type,
        "comparative": comparative,
        "created_at": created_at,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if periods is not UNSET:
      field_dict["periods"] = periods
    if mapping_id is not UNSET:
      field_dict["mapping_id"] = mapping_id
    if ai_generated is not UNSET:
      field_dict["ai_generated"] = ai_generated
    if last_generated is not UNSET:
      field_dict["last_generated"] = last_generated
    if structures is not UNSET:
      field_dict["structures"] = structures
    if entity_name is not UNSET:
      field_dict["entity_name"] = entity_name
    if source_graph_id is not UNSET:
      field_dict["source_graph_id"] = source_graph_id
    if source_report_id is not UNSET:
      field_dict["source_report_id"] = source_report_id
    if shared_at is not UNSET:
      field_dict["shared_at"] = shared_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.period_spec import PeriodSpec
    from ..models.structure_summary import StructureSummary

    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    taxonomy_id = d.pop("taxonomy_id")

    generation_status = d.pop("generation_status")

    period_type = d.pop("period_type")

    comparative = d.pop("comparative")

    created_at = isoparse(d.pop("created_at"))

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

    def _parse_period_end(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_end_type_0 = isoparse(data).date()

        return period_end_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_end = _parse_period_end(d.pop("period_end", UNSET))

    def _parse_periods(data: object) -> list[PeriodSpec] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        periods_type_0 = []
        _periods_type_0 = data
        for periods_type_0_item_data in _periods_type_0:
          periods_type_0_item = PeriodSpec.from_dict(periods_type_0_item_data)

          periods_type_0.append(periods_type_0_item)

        return periods_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[PeriodSpec] | None | Unset, data)

    periods = _parse_periods(d.pop("periods", UNSET))

    def _parse_mapping_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    mapping_id = _parse_mapping_id(d.pop("mapping_id", UNSET))

    ai_generated = d.pop("ai_generated", UNSET)

    def _parse_last_generated(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        last_generated_type_0 = isoparse(data)

        return last_generated_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    last_generated = _parse_last_generated(d.pop("last_generated", UNSET))

    _structures = d.pop("structures", UNSET)
    structures: list[StructureSummary] | Unset = UNSET
    if _structures is not UNSET:
      structures = []
      for structures_item_data in _structures:
        structures_item = StructureSummary.from_dict(structures_item_data)

        structures.append(structures_item)

    def _parse_entity_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_name = _parse_entity_name(d.pop("entity_name", UNSET))

    def _parse_source_graph_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_graph_id = _parse_source_graph_id(d.pop("source_graph_id", UNSET))

    def _parse_source_report_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_report_id = _parse_source_report_id(d.pop("source_report_id", UNSET))

    def _parse_shared_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        shared_at_type_0 = isoparse(data)

        return shared_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    shared_at = _parse_shared_at(d.pop("shared_at", UNSET))

    report_response = cls(
      id=id,
      name=name,
      taxonomy_id=taxonomy_id,
      generation_status=generation_status,
      period_type=period_type,
      comparative=comparative,
      created_at=created_at,
      period_start=period_start,
      period_end=period_end,
      periods=periods,
      mapping_id=mapping_id,
      ai_generated=ai_generated,
      last_generated=last_generated,
      structures=structures,
      entity_name=entity_name,
      source_graph_id=source_graph_id,
      source_report_id=source_report_id,
      shared_at=shared_at,
    )

    report_response.additional_properties = d
    return report_response

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
