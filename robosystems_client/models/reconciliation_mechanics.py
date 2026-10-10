from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reconciliation_mechanics_method import ReconciliationMechanicsMethod
from ..models.reconciliation_mechanics_scope import ReconciliationMechanicsScope
from ..models.reconciliation_mechanics_statement_cycle_type_0 import (
  ReconciliationMechanicsStatementCycleType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconciliationMechanics")


@_attrs_define
class ReconciliationMechanics:
  """Mechanics for `block_type='reconciliation'`: what is compared, against
  what, and how much the close cares.

  A `ledger`-scope reconciliation checks the whole ledger against one
  source (the synced accounting system's own trial balance). An
  `account`-scope one ties a single account to an independent balance.

      Attributes:
          scope (ReconciliationMechanicsScope): Whether the block covers the whole ledger or one account.
          method (ReconciliationMechanicsMethod): Where the independent side comes from.
          kind (Literal['reconciliation'] | Unset):  Default: 'reconciliation'.
          element_id (None | str | Unset): The account reconciled; null for a ledger-scope block.
          required_for_close (bool | Unset): Whether the period's close waits on this reconciliation. Default: True.
          materiality (float | Unset): A difference up to this amount still counts as reconciled. Zero means the two sides
              must agree to the cent. Default: 0.0.
          review_required (bool | Unset): Whether the close waits for a sign-off as well, not just for the two sides to
              reconcile. Default: False.
          separate_reviewer (bool | Unset): Whether the person who signs off must be someone other than the person who ran
              the comparison. Default: False.
          statement_cycle (None | ReconciliationMechanicsStatementCycleType0 | Unset): `statement` blocks only: how often
              the account's statement is issued; unset is monthly. A period is covered by the latest statement ending within
              the cycle that ends with it.
  """

  scope: ReconciliationMechanicsScope
  method: ReconciliationMechanicsMethod
  kind: Literal["reconciliation"] | Unset = "reconciliation"
  element_id: None | str | Unset = UNSET
  required_for_close: bool | Unset = True
  materiality: float | Unset = 0.0
  review_required: bool | Unset = False
  separate_reviewer: bool | Unset = False
  statement_cycle: None | ReconciliationMechanicsStatementCycleType0 | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    scope = self.scope.value

    method = self.method.value

    kind = self.kind

    element_id: None | str | Unset
    if isinstance(self.element_id, Unset):
      element_id = UNSET
    else:
      element_id = self.element_id

    required_for_close = self.required_for_close

    materiality = self.materiality

    review_required = self.review_required

    separate_reviewer = self.separate_reviewer

    statement_cycle: None | str | Unset
    if isinstance(self.statement_cycle, Unset):
      statement_cycle = UNSET
    elif isinstance(self.statement_cycle, ReconciliationMechanicsStatementCycleType0):
      statement_cycle = self.statement_cycle.value
    else:
      statement_cycle = self.statement_cycle

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "scope": scope,
        "method": method,
      }
    )
    if kind is not UNSET:
      field_dict["kind"] = kind
    if element_id is not UNSET:
      field_dict["element_id"] = element_id
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
    scope = ReconciliationMechanicsScope(d.pop("scope"))

    method = ReconciliationMechanicsMethod(d.pop("method"))

    kind = cast(Literal["reconciliation"] | Unset, d.pop("kind", UNSET))
    if kind != "reconciliation" and not isinstance(kind, Unset):
      raise ValueError(f"kind must match const 'reconciliation', got '{kind}'")

    def _parse_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_id = _parse_element_id(d.pop("element_id", UNSET))

    required_for_close = d.pop("required_for_close", UNSET)

    materiality = d.pop("materiality", UNSET)

    review_required = d.pop("review_required", UNSET)

    separate_reviewer = d.pop("separate_reviewer", UNSET)

    def _parse_statement_cycle(
      data: object,
    ) -> None | ReconciliationMechanicsStatementCycleType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        statement_cycle_type_0 = ReconciliationMechanicsStatementCycleType0(data)

        return statement_cycle_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ReconciliationMechanicsStatementCycleType0 | Unset, data)

    statement_cycle = _parse_statement_cycle(d.pop("statement_cycle", UNSET))

    reconciliation_mechanics = cls(
      scope=scope,
      method=method,
      kind=kind,
      element_id=element_id,
      required_for_close=required_for_close,
      materiality=materiality,
      review_required=review_required,
      separate_reviewer=separate_reviewer,
      statement_cycle=statement_cycle,
    )

    reconciliation_mechanics.additional_properties = d
    return reconciliation_mechanics

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
