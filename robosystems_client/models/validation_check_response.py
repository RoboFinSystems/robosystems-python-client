from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValidationCheckResponse")


@_attrs_define
class ValidationCheckResponse:
  """Aggregate result of running reporting rules over a structure.

  Every rule runs once per rendered period column; on a multi-column
  statement each failure and warning is prefixed with the column it was
  found in (``[Prior] …``).

      Attributes:
          passed (bool): True iff at least one rule ran and every rule produced zero failures on every rendered column.
              False when nothing was checked (`status == 'inconclusive'`).
          status (str): `passed` — every rule ran on every column with zero failures; `failed` — at least one rule failed;
              `inconclusive` — no validation rules exist for this block type, so nothing was checked.
          checks (list[str]): Names of rules that were evaluated.
          failures (list[str]): Human-readable descriptions of rule failures.
          warnings (list[str]): Non-blocking advisories from rule evaluation.
  """

  passed: bool
  status: str
  checks: list[str]
  failures: list[str]
  warnings: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    passed = self.passed

    status = self.status

    checks = self.checks

    failures = self.failures

    warnings = self.warnings

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "passed": passed,
        "status": status,
        "checks": checks,
        "failures": failures,
        "warnings": warnings,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    passed = d.pop("passed")

    status = d.pop("status")

    checks = cast(list[str], d.pop("checks"))

    failures = cast(list[str], d.pop("failures"))

    warnings = cast(list[str], d.pop("warnings"))

    validation_check_response = cls(
      passed=passed,
      status=status,
      checks=checks,
      failures=failures,
      warnings=warnings,
    )

    validation_check_response.additional_properties = d
    return validation_check_response

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
