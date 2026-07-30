from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.metric_observation import MetricObservation


T = TypeVar("T", bound="AssertMetricsRequest")


@_attrs_define
class AssertMetricsRequest:
  """Request body for the ``assert-metrics`` operation.

  The observation sibling of ``compute-metrics``: writes externally-
  observed values (usage counts, marketing numbers, hand-carried
  figures) into the period's standing ``factset_type='metric'`` FactSet
  with ``AssertedProvenance``. Re-asserting a period replaces its facts
  — one standing FactSet per (structure, entity, period_end), the
  accumulating time series.

  Structures carrying ``Derive`` rules are compute-owned
  (``compute-metrics``) and rejected — asserted and derived metric
  series keep disjoint structures. Asserted series are actuals; there
  is no scenario axis.

      Attributes:
          structure_id (str): Metric block structure (block_type='metric') to assert into.
          period_end (datetime.date): Period end the observations are for — instant concepts (a follower count at month
              end) land as of this date; duration concepts (monthly downloads) end on it.
          source_system (str): Identifier of the asserting system (e.g. 'content-machine') — recorded as the
              AssertedProvenance source_system.
          observations (list[MetricObservation]): Observed values, one per metric concept — duplicates rejected.
          period_start (datetime.date | None | Unset): Window start for duration concepts and the standing FactSet's
              period_start. Instant concepts ignore it.
          entity_id (None | str | Unset): Entity to assert for. Defaults to the graph's earliest-created entity (the
              primary entity for single-entity graphs).
          basis_note (None | str | Unset): Free-text basis / source reference for the observations.
  """

  structure_id: str
  period_end: datetime.date
  source_system: str
  observations: list[MetricObservation]
  period_start: datetime.date | None | Unset = UNSET
  entity_id: None | str | Unset = UNSET
  basis_note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    period_end = self.period_end.isoformat()

    source_system = self.source_system

    observations = []
    for observations_item_data in self.observations:
      observations_item = observations_item_data.to_dict()
      observations.append(observations_item)

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

    basis_note: None | str | Unset
    if isinstance(self.basis_note, Unset):
      basis_note = UNSET
    else:
      basis_note = self.basis_note

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "period_end": period_end,
        "source_system": source_system,
        "observations": observations,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if basis_note is not UNSET:
      field_dict["basis_note"] = basis_note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.metric_observation import MetricObservation

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    source_system = d.pop("source_system")

    observations = []
    _observations = d.pop("observations")
    for observations_item_data in _observations:
      observations_item = MetricObservation.from_dict(observations_item_data)

      observations.append(observations_item)

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

    def _parse_basis_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    basis_note = _parse_basis_note(d.pop("basis_note", UNSET))

    assert_metrics_request = cls(
      structure_id=structure_id,
      period_end=period_end,
      source_system=source_system,
      observations=observations,
      period_start=period_start,
      entity_id=entity_id,
      basis_note=basis_note,
    )

    assert_metrics_request.additional_properties = d
    return assert_metrics_request

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
