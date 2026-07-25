from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.line_assertion_lite_values_by_period import (
    LineAssertionLiteValuesByPeriod,
  )


T = TypeVar("T", bound="LineAssertionLite")


@_attrs_define
class LineAssertionLite:
  """One statement line's persisted direct assertion inside
  ``ForecastMechanics``.

  The manual-override sibling of :class:`LeverAssertionLite`: a lever
  asserts a *driver* whose rule derives a line; a line assertion pins
  the **line itself** (a calc-DAG leaf) to typed values for the months
  it names — winning over driver rules and carry-forward for exactly
  those months (a displaced rule surfaces in the compute response's
  ``skipped`` list). Subtotals stay calc-DAG-derived, so a manual line
  still articulates through RollUps, RE, balancing cash, and derived
  CF, and stays verification-gated.

  Same persistence doctrine as levers: values are duplicated as
  authored facts in the scenario's lever FactSet (facts are what
  ``compute-forecast`` binds); this mechanics copy is the
  operator-legible round-trip shape.

      Attributes:
          qname (str): Asserted statement-leaf qname.
          element_id (str): Resolved tenant element id.
          values_by_period (LineAssertionLiteValuesByPeriod): Expanded per-month assertions keyed by ``YYYY-MM``.
          item_type (None | str | Unset): Format family from the element (monetary | ...).
          period_type (str | Unset): The element's period type — duration assertions pin IS lines; instant assertions pin
              BS lines through the roll. Default: 'duration'.
  """

  qname: str
  element_id: str
  values_by_period: LineAssertionLiteValuesByPeriod
  item_type: None | str | Unset = UNSET
  period_type: str | Unset = "duration"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    qname = self.qname

    element_id = self.element_id

    values_by_period = self.values_by_period.to_dict()

    item_type: None | str | Unset
    if isinstance(self.item_type, Unset):
      item_type = UNSET
    else:
      item_type = self.item_type

    period_type = self.period_type

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
    if period_type is not UNSET:
      field_dict["period_type"] = period_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.line_assertion_lite_values_by_period import (
      LineAssertionLiteValuesByPeriod,
    )

    d = dict(src_dict)
    qname = d.pop("qname")

    element_id = d.pop("element_id")

    values_by_period = LineAssertionLiteValuesByPeriod.from_dict(
      d.pop("values_by_period")
    )

    def _parse_item_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    item_type = _parse_item_type(d.pop("item_type", UNSET))

    period_type = d.pop("period_type", UNSET)

    line_assertion_lite = cls(
      qname=qname,
      element_id=element_id,
      values_by_period=values_by_period,
      item_type=item_type,
      period_type=period_type,
    )

    line_assertion_lite.additional_properties = d
    return line_assertion_lite

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
