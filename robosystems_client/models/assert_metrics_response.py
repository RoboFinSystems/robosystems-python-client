from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.asserted_metric_lite import AssertedMetricLite


T = TypeVar("T", bound="AssertMetricsResponse")


@_attrs_define
class AssertMetricsResponse:
  """Response for the ``assert-metrics`` operation.

  Attributes:
      structure_id (str):
      entity_id (str):
      period_end (datetime.date):
      fact_set_id (str): Standing metric FactSet the observations were written to.
      asserted (list[AssertedMetricLite] | Unset):
      replaced (bool | Unset): True when a prior standing set existed for the period and its facts were replaced.
          Default: False.
  """

  structure_id: str
  entity_id: str
  period_end: datetime.date
  fact_set_id: str
  asserted: list[AssertedMetricLite] | Unset = UNSET
  replaced: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    entity_id = self.entity_id

    period_end = self.period_end.isoformat()

    fact_set_id = self.fact_set_id

    asserted: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.asserted, Unset):
      asserted = []
      for asserted_item_data in self.asserted:
        asserted_item = asserted_item_data.to_dict()
        asserted.append(asserted_item)

    replaced = self.replaced

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "entity_id": entity_id,
        "period_end": period_end,
        "fact_set_id": fact_set_id,
      }
    )
    if asserted is not UNSET:
      field_dict["asserted"] = asserted
    if replaced is not UNSET:
      field_dict["replaced"] = replaced

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.asserted_metric_lite import AssertedMetricLite

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    entity_id = d.pop("entity_id")

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    fact_set_id = d.pop("fact_set_id")

    _asserted = d.pop("asserted", UNSET)
    asserted: list[AssertedMetricLite] | Unset = UNSET
    if _asserted is not UNSET:
      asserted = []
      for asserted_item_data in _asserted:
        asserted_item = AssertedMetricLite.from_dict(asserted_item_data)

        asserted.append(asserted_item)

    replaced = d.pop("replaced", UNSET)

    assert_metrics_response = cls(
      structure_id=structure_id,
      entity_id=entity_id,
      period_end=period_end,
      fact_set_id=fact_set_id,
      asserted=asserted,
      replaced=replaced,
    )

    assert_metrics_response.additional_properties = d
    return assert_metrics_response

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
