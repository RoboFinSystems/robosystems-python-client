from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.line_growth_lite_values_by_period import LineGrowthLiteValuesByPeriod


T = TypeVar("T", bound="LineGrowthLite")


@_attrs_define
class LineGrowthLite:
  """One statement line's persisted growth trajectory inside
  ``ForecastMechanics``.

  The generic per-line form of the revenue growth lever: grows an
  income-statement leaf month-over-month at the asserted rate
  (``line[t] = line[t-1] * (1 + rate[t])``), compounding from the base
  month's value. Months without a rate keep the engine's carry-forward.
  Duration leaves only; disjoint from ``line_assertions`` and from any
  active catalog rule's target (one owner per line).

  Persistence deviates from levers/assertions deliberately: rates are
  NOT duplicated as facts in the scenario FactSet — a growth rate on a
  monetary statement element would be a unit-lying fact. This mechanics
  copy is the single authored store; ``compute-forecast`` binds rates
  from here.

      Attributes:
          qname (str): Grown statement-leaf qname.
          element_id (str): Resolved tenant element id.
          values_by_period (LineGrowthLiteValuesByPeriod): Expanded per-month growth rates keyed by ``YYYY-MM``.
          item_type (str | Unset): Always 'percent' — the grid row renders rates, not values. Default: 'percent'.
  """

  qname: str
  element_id: str
  values_by_period: LineGrowthLiteValuesByPeriod
  item_type: str | Unset = "percent"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    qname = self.qname

    element_id = self.element_id

    values_by_period = self.values_by_period.to_dict()

    item_type = self.item_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "qname": qname,
        "element_id": element_id,
        "values_by_period": values_by_period,
      }
    )
    if item_type is not UNSET:
      field_dict["item_type"] = item_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.line_growth_lite_values_by_period import LineGrowthLiteValuesByPeriod

    d = dict(src_dict)
    qname = d.pop("qname")

    element_id = d.pop("element_id")

    values_by_period = LineGrowthLiteValuesByPeriod.from_dict(d.pop("values_by_period"))

    item_type = d.pop("item_type", UNSET)

    line_growth_lite = cls(
      qname=qname,
      element_id=element_id,
      values_by_period=values_by_period,
      item_type=item_type,
    )

    line_growth_lite.additional_properties = d
    return line_growth_lite

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
