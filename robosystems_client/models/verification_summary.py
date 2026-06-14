from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.verification_category_summary import VerificationCategorySummary


T = TypeVar("T", bound="VerificationSummary")


@_attrs_define
class VerificationSummary:
  """Server-computed aggregate of a block's ``verification_results``.

  Overall counts plus a per-``rule_category`` breakdown, so the viewer
  renders the grouped Verification Results panel
  without a client-side results→rules join. Status closure is
  ``pass | fail | error | skipped`` (the ``public.verification_results``
  CHECK); ``total`` is their sum.

      Attributes:
          total (int | Unset):  Default: 0.
          passed (int | Unset):  Default: 0.
          failed (int | Unset):  Default: 0.
          errored (int | Unset):  Default: 0.
          skipped (int | Unset):  Default: 0.
          by_category (list[VerificationCategorySummary] | Unset):
  """

  total: int | Unset = 0
  passed: int | Unset = 0
  failed: int | Unset = 0
  errored: int | Unset = 0
  skipped: int | Unset = 0
  by_category: list[VerificationCategorySummary] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    total = self.total

    passed = self.passed

    failed = self.failed

    errored = self.errored

    skipped = self.skipped

    by_category: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.by_category, Unset):
      by_category = []
      for by_category_item_data in self.by_category:
        by_category_item = by_category_item_data.to_dict()
        by_category.append(by_category_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
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
    if by_category is not UNSET:
      field_dict["by_category"] = by_category

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.verification_category_summary import VerificationCategorySummary

    d = dict(src_dict)
    total = d.pop("total", UNSET)

    passed = d.pop("passed", UNSET)

    failed = d.pop("failed", UNSET)

    errored = d.pop("errored", UNSET)

    skipped = d.pop("skipped", UNSET)

    _by_category = d.pop("by_category", UNSET)
    by_category: list[VerificationCategorySummary] | Unset = UNSET
    if _by_category is not UNSET:
      by_category = []
      for by_category_item_data in _by_category:
        by_category_item = VerificationCategorySummary.from_dict(by_category_item_data)

        by_category.append(by_category_item)

    verification_summary = cls(
      total=total,
      passed=passed,
      failed=failed,
      errored=errored,
      skipped=skipped,
      by_category=by_category,
    )

    verification_summary.additional_properties = d
    return verification_summary

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
