from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValidationCheckResponse")


@_attrs_define
class ValidationCheckResponse:
  """
  Attributes:
      passed (bool):
      checks (list[str]):
      failures (list[str]):
      warnings (list[str]):
  """

  passed: bool
  checks: list[str]
  failures: list[str]
  warnings: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    passed = self.passed

    checks = self.checks

    failures = self.failures

    warnings = self.warnings

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "passed": passed,
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

    checks = cast(list[str], d.pop("checks"))

    failures = cast(list[str], d.pop("failures"))

    warnings = cast(list[str], d.pop("warnings"))

    validation_check_response = cls(
      passed=passed,
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
