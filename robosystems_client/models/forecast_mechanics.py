from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.forecast_mechanics_scenario_kind import ForecastMechanicsScenarioKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.lever_assertion_lite import LeverAssertionLite
  from ..models.line_assertion_lite import LineAssertionLite
  from ..models.line_growth_lite import LineGrowthLite


T = TypeVar("T", bound="ForecastMechanics")


@_attrs_define
class ForecastMechanics:
  """Authored scenario container for ``block_type='forecast'`` (FP&A F-1).

  The block IS the scenario: its structure id is the ``scenario_id``
  every derived forward FactSet carries (NULL = actuals). The authored
  surface is exactly this — scenario identity, horizon, base period,
  lever assertions; everything downstream is derived by
  ``compute-forecast`` (levers → driven rs-gaap anchors via the
  rs-driver Derive rules → carry-forward for unmodeled IS lines →
  calc-DAG subtotals), landing in the EXISTING statement/metric block
  types stamped with the scenario. Reads directly from the typed
  ``structures.artifact_mechanics`` JSONB column.

      Attributes:
          horizon_months (int): Forward months projected past the base period.
          base_period (str): Seed month (``YYYY-MM``) the walk projects forward from — resolved at create time (request →
              fiscal calendar closed-through → newest actual report month) and stored so recompute is deterministic.
          levers (list[LeverAssertionLite]): Expanded lever assertions (authoring order).
          kind (Literal['forecast'] | Unset):  Default: 'forecast'.
          scenario_kind (ForecastMechanicsScenarioKind | Unset): Scenario kind — display/filter metadata, not machinery.
              Default: ForecastMechanicsScenarioKind.FORECAST.
          line_assertions (list[LineAssertionLite] | Unset): Direct statement-line assertions (authoring order) — manual
              overrides that win over driver rules and carry-forward for the months they name.
          line_growth (list[LineGrowthLite] | Unset): Per-line growth trajectories (authoring order) — each grows an
              income-statement leaf month-over-month at the asserted rate, compounding from the base month.
          computed_months (int | Unset): Number of forward months with computed scenario FactSets. Runtime state filled at
              envelope-build time — 0 until the first compute-forecast run. Default: 0.
  """

  horizon_months: int
  base_period: str
  levers: list[LeverAssertionLite]
  kind: Literal["forecast"] | Unset = "forecast"
  scenario_kind: ForecastMechanicsScenarioKind | Unset = (
    ForecastMechanicsScenarioKind.FORECAST
  )
  line_assertions: list[LineAssertionLite] | Unset = UNSET
  line_growth: list[LineGrowthLite] | Unset = UNSET
  computed_months: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    horizon_months = self.horizon_months

    base_period = self.base_period

    levers = []
    for levers_item_data in self.levers:
      levers_item = levers_item_data.to_dict()
      levers.append(levers_item)

    kind = self.kind

    scenario_kind: str | Unset = UNSET
    if not isinstance(self.scenario_kind, Unset):
      scenario_kind = self.scenario_kind.value

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

    computed_months = self.computed_months

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "horizon_months": horizon_months,
        "base_period": base_period,
        "levers": levers,
      }
    )
    if kind is not UNSET:
      field_dict["kind"] = kind
    if scenario_kind is not UNSET:
      field_dict["scenario_kind"] = scenario_kind
    if line_assertions is not UNSET:
      field_dict["line_assertions"] = line_assertions
    if line_growth is not UNSET:
      field_dict["line_growth"] = line_growth
    if computed_months is not UNSET:
      field_dict["computed_months"] = computed_months

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.lever_assertion_lite import LeverAssertionLite
    from ..models.line_assertion_lite import LineAssertionLite
    from ..models.line_growth_lite import LineGrowthLite

    d = dict(src_dict)
    horizon_months = d.pop("horizon_months")

    base_period = d.pop("base_period")

    levers = []
    _levers = d.pop("levers")
    for levers_item_data in _levers:
      levers_item = LeverAssertionLite.from_dict(levers_item_data)

      levers.append(levers_item)

    kind = cast(Literal["forecast"] | Unset, d.pop("kind", UNSET))
    if kind != "forecast" and not isinstance(kind, Unset):
      raise ValueError(f"kind must match const 'forecast', got '{kind}'")

    _scenario_kind = d.pop("scenario_kind", UNSET)
    scenario_kind: ForecastMechanicsScenarioKind | Unset
    if isinstance(_scenario_kind, Unset):
      scenario_kind = UNSET
    else:
      scenario_kind = ForecastMechanicsScenarioKind(_scenario_kind)

    _line_assertions = d.pop("line_assertions", UNSET)
    line_assertions: list[LineAssertionLite] | Unset = UNSET
    if _line_assertions is not UNSET:
      line_assertions = []
      for line_assertions_item_data in _line_assertions:
        line_assertions_item = LineAssertionLite.from_dict(line_assertions_item_data)

        line_assertions.append(line_assertions_item)

    _line_growth = d.pop("line_growth", UNSET)
    line_growth: list[LineGrowthLite] | Unset = UNSET
    if _line_growth is not UNSET:
      line_growth = []
      for line_growth_item_data in _line_growth:
        line_growth_item = LineGrowthLite.from_dict(line_growth_item_data)

        line_growth.append(line_growth_item)

    computed_months = d.pop("computed_months", UNSET)

    forecast_mechanics = cls(
      horizon_months=horizon_months,
      base_period=base_period,
      levers=levers,
      kind=kind,
      scenario_kind=scenario_kind,
      line_assertions=line_assertions,
      line_growth=line_growth,
      computed_months=computed_months,
    )

    forecast_mechanics.additional_properties = d
    return forecast_mechanics

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
