from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputeMetricsRequest")


@_attrs_define
class ComputeMetricsRequest:
  """Request body for the ``compute-metrics`` operation.

  Resolves the ``Derive`` rules scoped to the metric block, binds each
  rule's operands to the entity's most recent persisted report facts at
  ``period_end``, evaluates, and upserts the period's standing
  ``factset_type='metric'`` FactSet (re-running a period replaces its
  facts). One standing FactSet per (structure, entity, period_end) — the
  accumulating time series.

      Attributes:
          structure_id (str): Metric block structure (block_type='metric') to compute.
          period_end (datetime.date): Period end to compute at. Operands bind to report facts whose period_end matches
              exactly (instant balances as of this date; durations ending on it).
          period_start (datetime.date | None | Unset): Optional lower bound for duration-operand binding and the standing
              FactSet's period_start.
          entity_id (None | str | Unset): Entity to compute for. Defaults to the graph's earliest-created entity (the
              primary entity for single-entity graphs).
  """

  structure_id: str
  period_end: datetime.date
  period_start: datetime.date | None | Unset = UNSET
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    period_end = self.period_end.isoformat()

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    elif isinstance(self.period_start, datetime.date):
      period_start = self.period_start.isoformat()
    else:
      period_start = self.period_start

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "period_end": period_end,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

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

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    compute_metrics_request = cls(
      structure_id=structure_id,
      period_end=period_end,
      period_start=period_start,
      entity_id=entity_id,
    )

    compute_metrics_request.additional_properties = d
    return compute_metrics_request

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
