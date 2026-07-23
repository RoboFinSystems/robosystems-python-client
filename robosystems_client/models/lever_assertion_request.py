from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.lever_assertion_request_values_by_period_type_0 import (
    LeverAssertionRequestValuesByPeriodType0,
  )


T = TypeVar("T", bound="LeverAssertionRequest")


@_attrs_define
class LeverAssertionRequest:
  """One lever's asserted values for the scenario.

  ``qname`` must resolve to an ``rs-driver:*`` catalog element (the
  create handler rejects anything else). Value conventions follow the
  catalog: percent levers are decimals per month (0.03 = 3%/month),
  days levers are day counts.

  ``value`` is a uniform fill across the whole horizon;
  ``values_by_period`` overrides individual months (``"YYYY-MM"``
  keys). At least one of the two must be provided. Months covered by
  neither carry no assertion — the lever's rule is inactive for that
  month and its target falls to the engine's carry-forward default.

      Attributes:
          qname (str): QName of the rs-driver lever element (e.g. ``rs-driver:RevenueGrowthRate``).
          value (float | None | Unset): Uniform value asserted for every month of the horizon.
          values_by_period (LeverAssertionRequestValuesByPeriodType0 | None | Unset): Per-month overrides keyed by ``YYYY-
              MM``. Wins over ``value`` for the months it names.
  """

  qname: str
  value: float | None | Unset = UNSET
  values_by_period: LeverAssertionRequestValuesByPeriodType0 | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.lever_assertion_request_values_by_period_type_0 import (
      LeverAssertionRequestValuesByPeriodType0,
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
    elif isinstance(self.values_by_period, LeverAssertionRequestValuesByPeriodType0):
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
    from ..models.lever_assertion_request_values_by_period_type_0 import (
      LeverAssertionRequestValuesByPeriodType0,
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
    ) -> LeverAssertionRequestValuesByPeriodType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        values_by_period_type_0 = LeverAssertionRequestValuesByPeriodType0.from_dict(
          data
        )

        return values_by_period_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(LeverAssertionRequestValuesByPeriodType0 | None | Unset, data)

    values_by_period = _parse_values_by_period(d.pop("values_by_period", UNSET))

    lever_assertion_request = cls(
      qname=qname,
      value=value,
      values_by_period=values_by_period,
    )

    lever_assertion_request.additional_properties = d
    return lever_assertion_request

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
