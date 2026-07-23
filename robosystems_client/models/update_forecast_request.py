from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_forecast_request_scenario_kind_type_0 import (
  UpdateForecastRequestScenarioKindType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.lever_assertion_request import LeverAssertionRequest


T = TypeVar("T", bound="UpdateForecastRequest")


@_attrs_define
class UpdateForecastRequest:
  """Update a forecast block in place.

  Mutable: name, scenario_kind, horizon_months, base_period, levers.
  ``levers`` is a **full replace** when provided (partial lever edits
  would make the asserted set ambiguous). Updating does NOT recompute —
  previously computed scenario months go stale until the next
  ``compute-forecast`` run (the compute-metrics drift semantics).

      Attributes:
          structure_id (str): Structure ID of the forecast block.
          name (None | str | Unset):
          scenario_kind (None | Unset | UpdateForecastRequestScenarioKindType0):
          horizon_months (int | None | Unset):
          base_period (None | str | Unset):
          levers (list[LeverAssertionRequest] | None | Unset): Full replacement of the lever set when provided.
  """

  structure_id: str
  name: None | str | Unset = UNSET
  scenario_kind: None | Unset | UpdateForecastRequestScenarioKindType0 = UNSET
  horizon_months: int | None | Unset = UNSET
  base_period: None | str | Unset = UNSET
  levers: list[LeverAssertionRequest] | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    scenario_kind: None | str | Unset
    if isinstance(self.scenario_kind, Unset):
      scenario_kind = UNSET
    elif isinstance(self.scenario_kind, UpdateForecastRequestScenarioKindType0):
      scenario_kind = self.scenario_kind.value
    else:
      scenario_kind = self.scenario_kind

    horizon_months: int | None | Unset
    if isinstance(self.horizon_months, Unset):
      horizon_months = UNSET
    else:
      horizon_months = self.horizon_months

    base_period: None | str | Unset
    if isinstance(self.base_period, Unset):
      base_period = UNSET
    else:
      base_period = self.base_period

    levers: list[dict[str, Any]] | None | Unset
    if isinstance(self.levers, Unset):
      levers = UNSET
    elif isinstance(self.levers, list):
      levers = []
      for levers_type_0_item_data in self.levers:
        levers_type_0_item = levers_type_0_item_data.to_dict()
        levers.append(levers_type_0_item)

    else:
      levers = self.levers

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if scenario_kind is not UNSET:
      field_dict["scenario_kind"] = scenario_kind
    if horizon_months is not UNSET:
      field_dict["horizon_months"] = horizon_months
    if base_period is not UNSET:
      field_dict["base_period"] = base_period
    if levers is not UNSET:
      field_dict["levers"] = levers

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.lever_assertion_request import LeverAssertionRequest

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_scenario_kind(
      data: object,
    ) -> None | Unset | UpdateForecastRequestScenarioKindType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        scenario_kind_type_0 = UpdateForecastRequestScenarioKindType0(data)

        return scenario_kind_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateForecastRequestScenarioKindType0, data)

    scenario_kind = _parse_scenario_kind(d.pop("scenario_kind", UNSET))

    def _parse_horizon_months(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    horizon_months = _parse_horizon_months(d.pop("horizon_months", UNSET))

    def _parse_base_period(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    base_period = _parse_base_period(d.pop("base_period", UNSET))

    def _parse_levers(data: object) -> list[LeverAssertionRequest] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        levers_type_0 = []
        _levers_type_0 = data
        for levers_type_0_item_data in _levers_type_0:
          levers_type_0_item = LeverAssertionRequest.from_dict(levers_type_0_item_data)

          levers_type_0.append(levers_type_0_item)

        return levers_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[LeverAssertionRequest] | None | Unset, data)

    levers = _parse_levers(d.pop("levers", UNSET))

    update_forecast_request = cls(
      structure_id=structure_id,
      name=name,
      scenario_kind=scenario_kind,
      horizon_months=horizon_months,
      base_period=base_period,
      levers=levers,
    )

    update_forecast_request.additional_properties = d
    return update_forecast_request

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
