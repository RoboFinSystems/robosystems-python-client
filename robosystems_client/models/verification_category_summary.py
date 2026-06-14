from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerificationCategorySummary")


@_attrs_define
class VerificationCategorySummary:
  """Pass/fail/skip counts for one ``rule_category`` within a block's
  verification results.

  Drives the per-category accordions in the Verification Results panel.
  ``category`` is the rule's ``rule_category``
  (one of the cm:VerificationRule subclasses), resolved by joining each
  result to its Rule.

      Attributes:
          category (str):
          total (int | Unset):  Default: 0.
          passed (int | Unset):  Default: 0.
          failed (int | Unset):  Default: 0.
          errored (int | Unset):  Default: 0.
          skipped (int | Unset):  Default: 0.
  """

  category: str
  total: int | Unset = 0
  passed: int | Unset = 0
  failed: int | Unset = 0
  errored: int | Unset = 0
  skipped: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    category = self.category

    total = self.total

    passed = self.passed

    failed = self.failed

    errored = self.errored

    skipped = self.skipped

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "category": category,
      }
    )
    if total is not UNSET:
      field_dict["total"] = total
    if passed is not UNSET:
      field_dict["passed"] = passed
    if failed is not UNSET:
      field_dict["failed"] = failed
    if errored is not UNSET:
      field_dict["errored"] = errored
    if skipped is not UNSET:
      field_dict["skipped"] = skipped

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    category = d.pop("category")

    total = d.pop("total", UNSET)

    passed = d.pop("passed", UNSET)

    failed = d.pop("failed", UNSET)

    errored = d.pop("errored", UNSET)

    skipped = d.pop("skipped", UNSET)

    verification_category_summary = cls(
      category=category,
      total=total,
      passed=passed,
      failed=failed,
      errored=errored,
      skipped=skipped,
    )

    verification_category_summary.additional_properties = d
    return verification_category_summary

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
