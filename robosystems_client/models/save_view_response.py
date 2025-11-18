from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.fact_detail import FactDetail
  from ..models.structure_detail import StructureDetail


T = TypeVar("T", bound="SaveViewResponse")


@_attrs_define
class SaveViewResponse:
  """
  Attributes:
      report_id (str): Unique report identifier (used as parquet export prefix)
      report_type (str):
      entity_id (str):
      entity_name (str):
      period_start (str):
      period_end (str):
      fact_count (int):
      presentation_count (int):
      calculation_count (int):
      facts (list[FactDetail]):
      structures (list[StructureDetail]):
      created_at (str):
      parquet_export_prefix (str): Prefix for parquet file exports
  """

  report_id: str
  report_type: str
  entity_id: str
  entity_name: str
  period_start: str
  period_end: str
  fact_count: int
  presentation_count: int
  calculation_count: int
  facts: list[FactDetail]
  structures: list[StructureDetail]
  created_at: str
  parquet_export_prefix: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    report_id = self.report_id

    report_type = self.report_type

    entity_id = self.entity_id

    entity_name = self.entity_name

    period_start = self.period_start

    period_end = self.period_end

    fact_count = self.fact_count

    presentation_count = self.presentation_count

    calculation_count = self.calculation_count

    facts = []
    for facts_item_data in self.facts:
      facts_item = facts_item_data.to_dict()
      facts.append(facts_item)

    structures = []
    for structures_item_data in self.structures:
      structures_item = structures_item_data.to_dict()
      structures.append(structures_item)

    created_at = self.created_at

    parquet_export_prefix = self.parquet_export_prefix

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "report_id": report_id,
        "report_type": report_type,
        "entity_id": entity_id,
        "entity_name": entity_name,
        "period_start": period_start,
        "period_end": period_end,
        "fact_count": fact_count,
        "presentation_count": presentation_count,
        "calculation_count": calculation_count,
        "facts": facts,
        "structures": structures,
        "created_at": created_at,
        "parquet_export_prefix": parquet_export_prefix,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.fact_detail import FactDetail
    from ..models.structure_detail import StructureDetail

    d = dict(src_dict)
    report_id = d.pop("report_id")

    report_type = d.pop("report_type")

    entity_id = d.pop("entity_id")

    entity_name = d.pop("entity_name")

    period_start = d.pop("period_start")

    period_end = d.pop("period_end")

    fact_count = d.pop("fact_count")

    presentation_count = d.pop("presentation_count")

    calculation_count = d.pop("calculation_count")

    facts = []
    _facts = d.pop("facts")
    for facts_item_data in _facts:
      facts_item = FactDetail.from_dict(facts_item_data)

      facts.append(facts_item)

    structures = []
    _structures = d.pop("structures")
    for structures_item_data in _structures:
      structures_item = StructureDetail.from_dict(structures_item_data)

      structures.append(structures_item)

    created_at = d.pop("created_at")

    parquet_export_prefix = d.pop("parquet_export_prefix")

    save_view_response = cls(
      report_id=report_id,
      report_type=report_type,
      entity_id=entity_id,
      entity_name=entity_name,
      period_start=period_start,
      period_end=period_end,
      fact_count=fact_count,
      presentation_count=presentation_count,
      calculation_count=calculation_count,
      facts=facts,
      structures=structures,
      created_at=created_at,
      parquet_export_prefix=parquet_export_prefix,
    )

    save_view_response.additional_properties = d
    return save_view_response

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
