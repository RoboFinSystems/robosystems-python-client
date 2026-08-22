from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_forecast_request_base_anchor import CreateForecastRequestBaseAnchor
from ..models.create_forecast_request_scenario_kind import (
  CreateForecastRequestScenarioKind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.lever_assertion_request import LeverAssertionRequest
  from ..models.line_assertion_request import LineAssertionRequest
  from ..models.line_growth_request import LineGrowthRequest


T = TypeVar("T", bound="CreateForecastRequest")


@_attrs_define
class CreateForecastRequest:
  """Create a forecast block — the authored scenario container.

  ``base_period`` defaults to the fiscal calendar's
  ``closed_through_period`` (else the newest actual report month) —
  the walk projects forward from the last closed actuals. The resolved
  value is stored in the mechanics so recompute is deterministic.

      Attributes:
          name (str): Human-readable scenario name.
          levers (list[LeverAssertionRequest]): Lever assertions — at least one.
          scenario_kind (CreateForecastRequestScenarioKind | Unset): What kind of scenario this is — metadata for
              display/filtering, not machinery. All kinds compute identically. Default:
              CreateForecastRequestScenarioKind.FORECAST.
          horizon_months (int | Unset): Forward months to project past the base period. Default: 12.
          base_period (None | str | Unset): Seed month (``YYYY-MM``) the walk projects forward from. Defaults to the
              fiscal calendar's closed-through period, else the newest actual report month. Resolved and stored at create
              time, and it never moves afterwards — every lever is keyed to a month inside ``base_period + 1 … +
              horizon_months``, so moving it would mean restating all of them. ``base_anchor`` decides whether the walk still
              *seeds* here once months close under it.
          base_anchor (CreateForecastRequestBaseAnchor | Unset): Where the walk takes its opening balances as periods
              close. ``seam`` (default) re-anchors on the newest closed month inside the horizon, so the scenario survives a
              close untouched and its first forward month rolls off real balances. ``fixed`` pins the walk to ``base_period``
              — the deliberate counterfactual, whose balances are meant to diverge from actuals. Default:
              CreateForecastRequestBaseAnchor.SEAM.
          line_assertions (list[LineAssertionRequest] | Unset): Direct statement-line assertions (manual overrides). Each
              names a calc-DAG leaf and wins over driver rules and carry-forward for the months it asserts.
          line_growth (list[LineGrowthRequest] | Unset): Per-line growth trajectories. Each names an income-statement leaf
              and grows it month-over-month at the asserted rate — the generic form of the revenue growth lever, for lines the
              catalog doesn't drive (opex trajectories, cost-cut ramps).
          entity_id (None | str | Unset): Entity the scenario belongs to. Defaults to the graph's earliest-created entity
              (single-entity convention).
  """

  name: str
  levers: list[LeverAssertionRequest]
  scenario_kind: CreateForecastRequestScenarioKind | Unset = (
    CreateForecastRequestScenarioKind.FORECAST
  )
  horizon_months: int | Unset = 12
  base_period: None | str | Unset = UNSET
  base_anchor: CreateForecastRequestBaseAnchor | Unset = (
    CreateForecastRequestBaseAnchor.SEAM
  )
  line_assertions: list[LineAssertionRequest] | Unset = UNSET
  line_growth: list[LineGrowthRequest] | Unset = UNSET
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    levers = []
    for levers_item_data in self.levers:
      levers_item = levers_item_data.to_dict()
      levers.append(levers_item)

    scenario_kind: str | Unset = UNSET
    if not isinstance(self.scenario_kind, Unset):
      scenario_kind = self.scenario_kind.value

    horizon_months = self.horizon_months

    base_period: None | str | Unset
    if isinstance(self.base_period, Unset):
      base_period = UNSET
    else:
      base_period = self.base_period

    base_anchor: str | Unset = UNSET
    if not isinstance(self.base_anchor, Unset):
      base_anchor = self.base_anchor.value

    line_assertions: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.line_assertions, Unset):
      line_assertions = []
      for line_assertions_item_data in self.line_assertions:
        line_assertions_item = line_assertions_item_data.to_dict()
        line_assertions.append(line_assertions_item)

    line_growth: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.line_growth, Unset):
      line_growth = []
      for line_growth_item_data in self.line_growth:
        line_growth_item = line_growth_item_data.to_dict()
        line_growth.append(line_growth_item)

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "levers": levers,
      }
    )
    if scenario_kind is not UNSET:
      field_dict["scenario_kind"] = scenario_kind
    if horizon_months is not UNSET:
      field_dict["horizon_months"] = horizon_months
    if base_period is not UNSET:
      field_dict["base_period"] = base_period
    if base_anchor is not UNSET:
      field_dict["base_anchor"] = base_anchor
    if line_assertions is not UNSET:
      field_dict["line_assertions"] = line_assertions
    if line_growth is not UNSET:
      field_dict["line_growth"] = line_growth
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.lever_assertion_request import LeverAssertionRequest
    from ..models.line_assertion_request import LineAssertionRequest
    from ..models.line_growth_request import LineGrowthRequest

    d = dict(src_dict)
    name = d.pop("name")

    levers = []
    _levers = d.pop("levers")
    for levers_item_data in _levers:
      levers_item = LeverAssertionRequest.from_dict(levers_item_data)

      levers.append(levers_item)

    _scenario_kind = d.pop("scenario_kind", UNSET)
    scenario_kind: CreateForecastRequestScenarioKind | Unset
    if isinstance(_scenario_kind, Unset):
      scenario_kind = UNSET
    else:
      scenario_kind = CreateForecastRequestScenarioKind(_scenario_kind)

    horizon_months = d.pop("horizon_months", UNSET)

    def _parse_base_period(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    base_period = _parse_base_period(d.pop("base_period", UNSET))

    _base_anchor = d.pop("base_anchor", UNSET)
    base_anchor: CreateForecastRequestBaseAnchor | Unset
    if isinstance(_base_anchor, Unset):
      base_anchor = UNSET
    else:
      base_anchor = CreateForecastRequestBaseAnchor(_base_anchor)

    _line_assertions = d.pop("line_assertions", UNSET)
    line_assertions: list[LineAssertionRequest] | Unset = UNSET
    if _line_assertions is not UNSET:
      line_assertions = []
      for line_assertions_item_data in _line_assertions:
        line_assertions_item = LineAssertionRequest.from_dict(line_assertions_item_data)

        line_assertions.append(line_assertions_item)

    _line_growth = d.pop("line_growth", UNSET)
    line_growth: list[LineGrowthRequest] | Unset = UNSET
    if _line_growth is not UNSET:
      line_growth = []
      for line_growth_item_data in _line_growth:
        line_growth_item = LineGrowthRequest.from_dict(line_growth_item_data)

        line_growth.append(line_growth_item)

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    create_forecast_request = cls(
      name=name,
      levers=levers,
      scenario_kind=scenario_kind,
      horizon_months=horizon_months,
      base_period=base_period,
      base_anchor=base_anchor,
      line_assertions=line_assertions,
      line_growth=line_growth,
      entity_id=entity_id,
    )

    create_forecast_request.additional_properties = d
    return create_forecast_request

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
