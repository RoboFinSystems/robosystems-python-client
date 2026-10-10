from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_reconciliation_policy_request_statement_cycle_type_0 import (
  SetReconciliationPolicyRequestStatementCycleType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetReconciliationPolicyRequest")


@_attrs_define
class SetReconciliationPolicyRequest:
  """Change how much the close cares about one reconciliation.

  Attributes:
      structure_id (str): The reconciliation block.
      required_for_close (bool | None | Unset): Whether the period's close waits on it. Omit to keep.
      materiality (float | None | Unset): A difference up to this amount still counts as reconciled. Omit to keep.
      review_required (bool | None | Unset): Whether the close also waits for a sign-off, not just for the two sides
          to reconcile. Omit to keep.
      separate_reviewer (bool | None | Unset): Whether the person who signs off must be someone other than the person
          who ran the comparison. It can only be turned on when the graph has at least two members who can write. Omit to
          keep.
      statement_cycle (None | SetReconciliationPolicyRequestStatementCycleType0 | Unset): `statement` blocks only: how
          often the account's statement is issued. A period is covered by the latest statement ending within the cycle
          that ends with it, so a quarterly statement covers the two months before the next one. Omit to keep.
  """

  structure_id: str
  required_for_close: bool | None | Unset = UNSET
  materiality: float | None | Unset = UNSET
  review_required: bool | None | Unset = UNSET
  separate_reviewer: bool | None | Unset = UNSET
  statement_cycle: None | SetReconciliationPolicyRequestStatementCycleType0 | Unset = (
    UNSET
  )
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    required_for_close: bool | None | Unset
    if isinstance(self.required_for_close, Unset):
      required_for_close = UNSET
    else:
      required_for_close = self.required_for_close

    materiality: float | None | Unset
    if isinstance(self.materiality, Unset):
      materiality = UNSET
    else:
      materiality = self.materiality

    review_required: bool | None | Unset
    if isinstance(self.review_required, Unset):
      review_required = UNSET
    else:
      review_required = self.review_required

    separate_reviewer: bool | None | Unset
    if isinstance(self.separate_reviewer, Unset):
      separate_reviewer = UNSET
    else:
      separate_reviewer = self.separate_reviewer

    statement_cycle: None | str | Unset
    if isinstance(self.statement_cycle, Unset):
      statement_cycle = UNSET
    elif isinstance(
      self.statement_cycle, SetReconciliationPolicyRequestStatementCycleType0
    ):
      statement_cycle = self.statement_cycle.value
    else:
      statement_cycle = self.statement_cycle

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
      }
    )
    if required_for_close is not UNSET:
      field_dict["required_for_close"] = required_for_close
    if materiality is not UNSET:
      field_dict["materiality"] = materiality
    if review_required is not UNSET:
      field_dict["review_required"] = review_required
    if separate_reviewer is not UNSET:
      field_dict["separate_reviewer"] = separate_reviewer
    if statement_cycle is not UNSET:
      field_dict["statement_cycle"] = statement_cycle

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    def _parse_required_for_close(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    required_for_close = _parse_required_for_close(d.pop("required_for_close", UNSET))

    def _parse_materiality(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    materiality = _parse_materiality(d.pop("materiality", UNSET))

    def _parse_review_required(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    review_required = _parse_review_required(d.pop("review_required", UNSET))

    def _parse_separate_reviewer(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    separate_reviewer = _parse_separate_reviewer(d.pop("separate_reviewer", UNSET))

    def _parse_statement_cycle(
      data: object,
    ) -> None | SetReconciliationPolicyRequestStatementCycleType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        statement_cycle_type_0 = SetReconciliationPolicyRequestStatementCycleType0(data)

        return statement_cycle_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(
        None | SetReconciliationPolicyRequestStatementCycleType0 | Unset, data
      )

    statement_cycle = _parse_statement_cycle(d.pop("statement_cycle", UNSET))

    set_reconciliation_policy_request = cls(
      structure_id=structure_id,
      required_for_close=required_for_close,
      materiality=materiality,
      review_required=review_required,
      separate_reviewer=separate_reviewer,
      statement_cycle=statement_cycle,
    )

    set_reconciliation_policy_request.additional_properties = d
    return set_reconciliation_policy_request

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
