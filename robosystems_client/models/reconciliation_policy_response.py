from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReconciliationPolicyResponse")


@_attrs_define
class ReconciliationPolicyResponse:
  """A reconciliation's policy after a change.

  Attributes:
      structure_id (str):
      required_for_close (bool):
      materiality (float):
      review_required (bool):
      separate_reviewer (bool):
  """

  structure_id: str
  required_for_close: bool
  materiality: float
  review_required: bool
  separate_reviewer: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    required_for_close = self.required_for_close

    materiality = self.materiality

    review_required = self.review_required

    separate_reviewer = self.separate_reviewer

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "required_for_close": required_for_close,
        "materiality": materiality,
        "review_required": review_required,
        "separate_reviewer": separate_reviewer,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    required_for_close = d.pop("required_for_close")

    materiality = d.pop("materiality")

    review_required = d.pop("review_required")

    separate_reviewer = d.pop("separate_reviewer")

    reconciliation_policy_response = cls(
      structure_id=structure_id,
      required_for_close=required_for_close,
      materiality=materiality,
      review_required=review_required,
      separate_reviewer=separate_reviewer,
    )

    reconciliation_policy_response.additional_properties = d
    return reconciliation_policy_response

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
