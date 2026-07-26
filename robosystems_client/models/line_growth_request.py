from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.line_growth_request_values_by_period_type_0 import (
    LineGrowthRequestValuesByPeriodType0,
  )


T = TypeVar("T", bound="LineGrowthRequest")


@_attrs_define
class LineGrowthRequest:
  """One statement line's asserted growth trajectory for the scenario.

  The generic per-line sibling of ``rs-driver:RevenueGrowthRate``: where
  the catalog lever grows *revenue* through its seeded rule, a line
  growth entry grows **any income-statement leaf** at a month-over-month
  rate — ``value`` -0.05 cuts the line 5% per month, compounding from
  the base month's value. This is what expense trajectories ("opex +2%/mo
  with inflation", "cut costs 5%/mo starting October") use; without it
  every unmodeled line just carries flat.

  Semantics per month: ``line[t] = line[t-1] * (1 + rate[t])``. Months
  the entry doesn't name keep the engine's carry-forward (grow-then-hold
  ramps fall out of ``values_by_period`` naturally). **Duration leaves
  only**: balance-sheet lines roll from the IS and the working-capital
  levers — grow the driving IS line instead. A line already driven by an
  active catalog rule (e.g. Revenues with ``RevenueGrowthRate`` set) or
  named by a ``line_assertions`` entry is rejected — one owner per line.

      Attributes:
          qname (str): QName of the income-statement leaf to grow (e.g. ``rs-gaap:ResearchAndDevelopmentExpense``). Must
              be a calc-DAG duration leaf.
          value (float | None | Unset): Uniform month-over-month growth rate for every month of the horizon (decimal: 0.02
              = +2%/mo, -0.05 = -5%/mo).
          values_by_period (LineGrowthRequestValuesByPeriodType0 | None | Unset): Per-month rate overrides keyed by
              ``YYYY-MM``. Wins over ``value`` for the months it names; months named by neither carry the line's prior value
              (rate 0).
  """

  qname: str
  value: float | None | Unset = UNSET
  values_by_period: LineGrowthRequestValuesByPeriodType0 | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.line_growth_request_values_by_period_type_0 import (
      LineGrowthRequestValuesByPeriodType0,
    )

    qname = self.qname

    value: float | None | Unset
    if isinstance(self.value, Unset):
      value = UNSET
    else:
      value = self.value

    values_by_period: dict[str, Any] | None | Unset
    if isinstance(self.values_by_period, Unset):
      values_by_period = UNSET
    elif isinstance(self.values_by_period, LineGrowthRequestValuesByPeriodType0):
      values_by_period = self.values_by_period.to_dict()
    else:
      values_by_period = self.values_by_period

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "qname": qname,
      }
    )
    if value is not UNSET:
      field_dict["value"] = value
    if values_by_period is not UNSET:
      field_dict["values_by_period"] = values_by_period

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.line_growth_request_values_by_period_type_0 import (
      LineGrowthRequestValuesByPeriodType0,
    )

    d = dict(src_dict)
    qname = d.pop("qname")

    def _parse_value(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    value = _parse_value(d.pop("value", UNSET))

    def _parse_values_by_period(
      data: object,
    ) -> LineGrowthRequestValuesByPeriodType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        values_by_period_type_0 = LineGrowthRequestValuesByPeriodType0.from_dict(data)

        return values_by_period_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(LineGrowthRequestValuesByPeriodType0 | None | Unset, data)

    values_by_period = _parse_values_by_period(d.pop("values_by_period", UNSET))

    line_growth_request = cls(
      qname=qname,
      value=value,
      values_by_period=values_by_period,
    )

    line_growth_request.additional_properties = d
    return line_growth_request

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
