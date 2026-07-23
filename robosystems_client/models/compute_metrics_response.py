from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.computed_metric_lite import ComputedMetricLite
  from ..models.skipped_metric_lite import SkippedMetricLite


T = TypeVar("T", bound="ComputeMetricsResponse")


@_attrs_define
class ComputeMetricsResponse:
  """Response for the ``compute-metrics`` operation.

  Attributes:
      structure_id (str):
      entity_id (str):
      period_end (datetime.date):
      fact_set_id (None | str | Unset): Standing metric FactSet for the period — None when every metric was skipped
          and no prior set existed.
      computed (list[ComputedMetricLite] | Unset):
      skipped (list[SkippedMetricLite] | Unset):
  """

  structure_id: str
  entity_id: str
  period_end: datetime.date
  fact_set_id: None | str | Unset = UNSET
  computed: list[ComputedMetricLite] | Unset = UNSET
  skipped: list[SkippedMetricLite] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    entity_id = self.entity_id

    period_end = self.period_end.isoformat()

    fact_set_id: None | str | Unset
    if isinstance(self.fact_set_id, Unset):
      fact_set_id = UNSET
    else:
      fact_set_id = self.fact_set_id

    computed: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.computed, Unset):
      computed = []
      for computed_item_data in self.computed:
        computed_item = computed_item_data.to_dict()
        computed.append(computed_item)

    skipped: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.skipped, Unset):
      skipped = []
      for skipped_item_data in self.skipped:
        skipped_item = skipped_item_data.to_dict()
        skipped.append(skipped_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "entity_id": entity_id,
        "period_end": period_end,
      }
    )
    if fact_set_id is not UNSET:
      field_dict["fact_set_id"] = fact_set_id
    if computed is not UNSET:
      field_dict["computed"] = computed
    if skipped is not UNSET:
      field_dict["skipped"] = skipped

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.computed_metric_lite import ComputedMetricLite
    from ..models.skipped_metric_lite import SkippedMetricLite

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    entity_id = d.pop("entity_id")

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    def _parse_fact_set_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    fact_set_id = _parse_fact_set_id(d.pop("fact_set_id", UNSET))

    _computed = d.pop("computed", UNSET)
    computed: list[ComputedMetricLite] | Unset = UNSET
    if _computed is not UNSET:
      computed = []
      for computed_item_data in _computed:
        computed_item = ComputedMetricLite.from_dict(computed_item_data)

        computed.append(computed_item)

    _skipped = d.pop("skipped", UNSET)
    skipped: list[SkippedMetricLite] | Unset = UNSET
    if _skipped is not UNSET:
      skipped = []
      for skipped_item_data in _skipped:
        skipped_item = SkippedMetricLite.from_dict(skipped_item_data)

        skipped.append(skipped_item)

    compute_metrics_response = cls(
      structure_id=structure_id,
      entity_id=entity_id,
      period_end=period_end,
      fact_set_id=fact_set_id,
      computed=computed,
      skipped=skipped,
    )

    compute_metrics_response.additional_properties = d
    return compute_metrics_response

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
