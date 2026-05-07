from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationLite")


@_attrs_define
class ValidationLite:
  """Outcome of guard-rail validation on a rendered statement.

  Distinct from :class:`VerificationResultLite` (which surfaces the
  rule-engine outcomes from ``public.verification_results``). This lite
  type carries the synchronous guard-rail checks computed at
  envelope-build time — accounting equation, totals foot, etc.

      Attributes:
          passed (bool | Unset):  Default: True.
          checks (list[str] | Unset):
          failures (list[str] | Unset):
          warnings (list[str] | Unset):
  """

  passed: bool | Unset = True
  checks: list[str] | Unset = UNSET
  failures: list[str] | Unset = UNSET
  warnings: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    passed = self.passed

    checks: list[str] | Unset = UNSET
    if not isinstance(self.checks, Unset):
      checks = self.checks

    failures: list[str] | Unset = UNSET
    if not isinstance(self.failures, Unset):
      failures = self.failures

    warnings: list[str] | Unset = UNSET
    if not isinstance(self.warnings, Unset):
      warnings = self.warnings

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if passed is not UNSET:
      field_dict["passed"] = passed
    if checks is not UNSET:
      field_dict["checks"] = checks
    if failures is not UNSET:
      field_dict["failures"] = failures
    if warnings is not UNSET:
      field_dict["warnings"] = warnings

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    passed = d.pop("passed", UNSET)

    checks = cast(list[str], d.pop("checks", UNSET))

    failures = cast(list[str], d.pop("failures", UNSET))

    warnings = cast(list[str], d.pop("warnings", UNSET))

    validation_lite = cls(
      passed=passed,
      checks=checks,
      failures=failures,
      warnings=warnings,
    )

    validation_lite.additional_properties = d
    return validation_lite

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
