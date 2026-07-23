from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SkippedMetricLite")


@_attrs_define
class SkippedMetricLite:
  """One metric a ``compute-metrics`` run could not compute.

  Soft-fail by design: a missing operand fact (e.g. InterestExpense for a
  debt-free entity) or an undefined ratio (division by zero) skips the
  metric with a reason — it never errors the run.

      Attributes:
          rule_id (str): Derive rule that was skipped.
          reason (str): Why the metric was skipped.
          element_qname (None | str | Unset): Metric element qname the rule targets.
          missing (list[str] | Unset): Operand qnames with no bound fact at the period, when applicable.
  """

  rule_id: str
  reason: str
  element_qname: None | str | Unset = UNSET
  missing: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    rule_id = self.rule_id

    reason = self.reason

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
        "rule_id": rule_id,
        "reason": reason,
      }
    )
    if element_qname is not UNSET:
      field_dict["element_qname"] = element_qname
    if missing is not UNSET:
      field_dict["missing"] = missing

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    rule_id = d.pop("rule_id")

    reason = d.pop("reason")

    def _parse_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_qname = _parse_element_qname(d.pop("element_qname", UNSET))

    missing = cast(list[str], d.pop("missing", UNSET))

    skipped_metric_lite = cls(
      rule_id=rule_id,
      reason=reason,
      element_qname=element_qname,
      missing=missing,
    )

    skipped_metric_lite.additional_properties = d
    return skipped_metric_lite

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
