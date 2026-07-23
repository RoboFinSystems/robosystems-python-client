from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SkippedForecastLite")


@_attrs_define
class SkippedForecastLite:
  """One rule/month soft-skip in a ``compute-forecast`` response.

  A skipped rule never aborts the walk — its target falls back to the
  carry-forward value for that month (when a prior value exists).

      Attributes:
          period (str): Month key (``YYYY-MM``) of the skip.
          reason (str):
          rule_id (None | str | Unset):
          element_qname (None | str | Unset):
          missing (list[str] | Unset):
  """

  period: str
  reason: str
  rule_id: None | str | Unset = UNSET
  element_qname: None | str | Unset = UNSET
  missing: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    reason = self.reason

    rule_id: None | str | Unset
    if isinstance(self.rule_id, Unset):
      rule_id = UNSET
    else:
      rule_id = self.rule_id

    element_qname: None | str | Unset
    if isinstance(self.element_qname, Unset):
      element_qname = UNSET
    else:
      element_qname = self.element_qname

    missing: list[str] | Unset = UNSET
    if not isinstance(self.missing, Unset):
      missing = self.missing

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
        "reason": reason,
      }
    )
    if rule_id is not UNSET:
      field_dict["rule_id"] = rule_id
    if element_qname is not UNSET:
      field_dict["element_qname"] = element_qname
    if missing is not UNSET:
      field_dict["missing"] = missing

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    period = d.pop("period")

    reason = d.pop("reason")

    def _parse_rule_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    rule_id = _parse_rule_id(d.pop("rule_id", UNSET))

    def _parse_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_qname = _parse_element_qname(d.pop("element_qname", UNSET))

    missing = cast(list[str], d.pop("missing", UNSET))

    skipped_forecast_lite = cls(
      period=period,
      reason=reason,
      rule_id=rule_id,
      element_qname=element_qname,
      missing=missing,
    )

    skipped_forecast_lite.additional_properties = d
    return skipped_forecast_lite

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
