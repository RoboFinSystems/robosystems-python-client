from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.forecast_month_lite import ForecastMonthLite
  from ..models.skipped_forecast_lite import SkippedForecastLite


T = TypeVar("T", bound="ComputeForecastResponse")


@_attrs_define
class ComputeForecastResponse:
  """Response for the ``compute-forecast`` operation.

  Attributes:
      structure_id (str):
      scenario_id (str): The scenario key every emitted FactSet carries — the forecast block's own structure id.
      entity_id (str):
      base_period (str): Seed month the walk projected from.
      months (int): Forward months requested.
      months_computed (list[ForecastMonthLite] | Unset):
      skipped (list[SkippedForecastLite] | Unset):
  """

  structure_id: str
  scenario_id: str
  entity_id: str
  base_period: str
  months: int
  months_computed: list[ForecastMonthLite] | Unset = UNSET
  skipped: list[SkippedForecastLite] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    scenario_id = self.scenario_id

    entity_id = self.entity_id

    base_period = self.base_period

    months = self.months

    months_computed: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.months_computed, Unset):
      months_computed = []
      for months_computed_item_data in self.months_computed:
        months_computed_item = months_computed_item_data.to_dict()
        months_computed.append(months_computed_item)

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
        "scenario_id": scenario_id,
        "entity_id": entity_id,
        "base_period": base_period,
        "months": months,
      }
    )
    if months_computed is not UNSET:
      field_dict["months_computed"] = months_computed
    if skipped is not UNSET:
      field_dict["skipped"] = skipped

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.forecast_month_lite import ForecastMonthLite
    from ..models.skipped_forecast_lite import SkippedForecastLite

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    scenario_id = d.pop("scenario_id")

    entity_id = d.pop("entity_id")

    base_period = d.pop("base_period")

    months = d.pop("months")

    _months_computed = d.pop("months_computed", UNSET)
    months_computed: list[ForecastMonthLite] | Unset = UNSET
    if _months_computed is not UNSET:
      months_computed = []
      for months_computed_item_data in _months_computed:
        months_computed_item = ForecastMonthLite.from_dict(months_computed_item_data)

        months_computed.append(months_computed_item)

    _skipped = d.pop("skipped", UNSET)
    skipped: list[SkippedForecastLite] | Unset = UNSET
    if _skipped is not UNSET:
      skipped = []
      for skipped_item_data in _skipped:
        skipped_item = SkippedForecastLite.from_dict(skipped_item_data)

        skipped.append(skipped_item)

    compute_forecast_response = cls(
      structure_id=structure_id,
      scenario_id=scenario_id,
      entity_id=entity_id,
      base_period=base_period,
      months=months,
      months_computed=months_computed,
      skipped=skipped,
    )

    compute_forecast_response.additional_properties = d
    return compute_forecast_response

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
