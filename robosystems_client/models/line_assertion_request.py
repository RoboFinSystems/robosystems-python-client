from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.line_assertion_request_values_by_period_type_0 import (
    LineAssertionRequestValuesByPeriodType0,
  )


T = TypeVar("T", bound="LineAssertionRequest")


@_attrs_define
class LineAssertionRequest:
  """One statement line's directly asserted values for the scenario.

  The manual-override half of the authored surface: where a lever
  asserts a *driver* (growth %, DSO) whose rule derives the line, a
  line assertion asserts the **line itself** — an rs-gaap (or tenant
  extension) statement leaf pinned to typed values for the months it
  names. Assertions win over driver rules and carry-forward for those
  months (a displaced rule lands in ``skipped``, legibly); months the
  assertion doesn't name keep the engine's normal derivation.

  **Leaves only** — subtotals stay calc-DAG-derived, so a manually set
  line still articulates through RollUps, RE, balancing cash, and the
  derived CF, and stays verification-gated (the whole pitch vs a
  spreadsheet cell). The create handler rejects calc-parent qnames.

  Value/period grammar is identical to levers: ``value`` is a uniform
  fill across the horizon, ``values_by_period`` overrides individual
  months. The canonical uses: zero out a base-month one-off so
  carry-forward stops replicating it, or hold a line at a known budget
  number no driver models.

      Attributes:
          qname (str): QName of the statement leaf to assert (e.g. ``rs-gaap:NonoperatingIncomeExpense``). Must be a calc-
              DAG leaf; rs-driver concepts belong in ``levers``.
          value (float | None | Unset): Uniform value asserted for every month of the horizon.
          values_by_period (LineAssertionRequestValuesByPeriodType0 | None | Unset): Per-month overrides keyed by ``YYYY-
              MM``. Wins over ``value`` for the months it names.
  """

  qname: str
  value: float | None | Unset = UNSET
  values_by_period: LineAssertionRequestValuesByPeriodType0 | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.line_assertion_request_values_by_period_type_0 import (
      LineAssertionRequestValuesByPeriodType0,
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
    elif isinstance(self.values_by_period, LineAssertionRequestValuesByPeriodType0):
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
    from ..models.line_assertion_request_values_by_period_type_0 import (
      LineAssertionRequestValuesByPeriodType0,
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
    ) -> LineAssertionRequestValuesByPeriodType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        values_by_period_type_0 = LineAssertionRequestValuesByPeriodType0.from_dict(
          data
        )

        return values_by_period_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(LineAssertionRequestValuesByPeriodType0 | None | Unset, data)

    values_by_period = _parse_values_by_period(d.pop("values_by_period", UNSET))

    line_assertion_request = cls(
      qname=qname,
      value=value,
      values_by_period=values_by_period,
    )

    line_assertion_request.additional_properties = d
    return line_assertion_request

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
