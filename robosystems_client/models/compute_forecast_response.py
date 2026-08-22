from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
      base_period (str): Origin month of the block's authored horizon window — where its levers are keyed from. Equal
          to ``anchor_period`` unless the walk re-anchored at the seam.
      anchor_period (str): Month the walk actually seeded its opening balances from. With ``base_anchor='seam'`` this
          advances to the newest closed month as periods close, so the first forward month rolls off real balances instead
          of a stale base; with ``'fixed'`` it always equals ``base_period``.
      months (int): Forward months requested.
      months_computed (list[ForecastMonthLite] | Unset):
      halted_at (None | str | Unset): Month (``YYYY-MM``) where the walk stopped because verification failed, or null
          if it ran the full horizon. Each month's opening balances are the previous month's closing balances, so
          computing past a failure yields months derived from a known-wrong one rather than merely unverified months. When
          set, ``months_computed`` ends at this month and is shorter than ``months``; the failing month's facts are kept
          so the failure can be inspected.
      skipped (list[SkippedForecastLite] | Unset):
      diagnostics (list[str] | Unset): Articulation notes — a missing cash/earnings anchor, schedule contributions
          with no base-set landing spot, an absent cash-flow structure. Informational; the walk still computed.
  """

  structure_id: str
  scenario_id: str
  entity_id: str
  base_period: str
  anchor_period: str
  months: int
  months_computed: list[ForecastMonthLite] | Unset = UNSET
  halted_at: None | str | Unset = UNSET
  skipped: list[SkippedForecastLite] | Unset = UNSET
  diagnostics: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    scenario_id = self.scenario_id

    entity_id = self.entity_id

    base_period = self.base_period

    anchor_period = self.anchor_period

    months = self.months

    months_computed: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.months_computed, Unset):
      months_computed = []
      for months_computed_item_data in self.months_computed:
        months_computed_item = months_computed_item_data.to_dict()
        months_computed.append(months_computed_item)

    halted_at: None | str | Unset
    if isinstance(self.halted_at, Unset):
      halted_at = UNSET
    else:
      halted_at = self.halted_at

    skipped: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.skipped, Unset):
      skipped = []
      for skipped_item_data in self.skipped:
        skipped_item = skipped_item_data.to_dict()
        skipped.append(skipped_item)

    diagnostics: list[str] | Unset = UNSET
    if not isinstance(self.diagnostics, Unset):
      diagnostics = self.diagnostics

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "scenario_id": scenario_id,
        "entity_id": entity_id,
        "base_period": base_period,
        "anchor_period": anchor_period,
        "months": months,
      }
    )
    if months_computed is not UNSET:
      field_dict["months_computed"] = months_computed
    if halted_at is not UNSET:
      field_dict["halted_at"] = halted_at
    if skipped is not UNSET:
      field_dict["skipped"] = skipped
    if diagnostics is not UNSET:
      field_dict["diagnostics"] = diagnostics

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

    anchor_period = d.pop("anchor_period")

    months = d.pop("months")

    _months_computed = d.pop("months_computed", UNSET)
    months_computed: list[ForecastMonthLite] | Unset = UNSET
    if _months_computed is not UNSET:
      months_computed = []
      for months_computed_item_data in _months_computed:
        months_computed_item = ForecastMonthLite.from_dict(months_computed_item_data)

        months_computed.append(months_computed_item)

    def _parse_halted_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    halted_at = _parse_halted_at(d.pop("halted_at", UNSET))

    _skipped = d.pop("skipped", UNSET)
    skipped: list[SkippedForecastLite] | Unset = UNSET
    if _skipped is not UNSET:
      skipped = []
      for skipped_item_data in _skipped:
        skipped_item = SkippedForecastLite.from_dict(skipped_item_data)

        skipped.append(skipped_item)

    diagnostics = cast(list[str], d.pop("diagnostics", UNSET))

    compute_forecast_response = cls(
      structure_id=structure_id,
      scenario_id=scenario_id,
      entity_id=entity_id,
      base_period=base_period,
      anchor_period=anchor_period,
      months=months,
      months_computed=months_computed,
      halted_at=halted_at,
      skipped=skipped,
      diagnostics=diagnostics,
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
