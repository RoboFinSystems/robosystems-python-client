from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputeForecastRequest")


@_attrs_define
class ComputeForecastRequest:
  """Request body for the ``compute-forecast`` operation.

  Walks the scenario's driver cascade month-by-month forward from the
  forecast block's ``base_period``: lever-driven Derive rules in
  dependency order, carry-forward for unmodeled IS lines, calc-DAG
  subtotals — upserting one scenario IS FactSet (+ a working-capital BS
  set) per forward month, all keyed by the forecast block's
  ``scenario_id``. Re-running replaces each month's values (the
  compute-metrics drift semantics). Deterministic and non-AI — no
  credits consumed.

      Attributes:
          structure_id (str): Forecast block structure (block_type='forecast') to compute.
          months (int | None | Unset): Forward months to compute — defaults to the block's full horizon_months; must not
              exceed it (lever assertions don't extend past the horizon).
          entity_id (None | str | Unset): Entity to compute for. Defaults to the lever FactSet's entity (the entity the
              scenario was authored against).
  """

  structure_id: str
  months: int | None | Unset = UNSET
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    months: int | None | Unset
    if isinstance(self.months, Unset):
      months = UNSET
    else:
      months = self.months

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
      }
    )
    if months is not UNSET:
      field_dict["months"] = months
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    def _parse_months(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    months = _parse_months(d.pop("months", UNSET))

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    compute_forecast_request = cls(
      structure_id=structure_id,
      months=months,
      entity_id=entity_id,
    )

    compute_forecast_request.additional_properties = d
    return compute_forecast_request

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
