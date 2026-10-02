from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.reconciliation_component import ReconciliationComponent
  from ..models.reconciliation_row import ReconciliationRow


T = TypeVar("T", bound="ReconciliationSummary")


@_attrs_define
class ReconciliationSummary:
  """One reconciliation's standing for a period.

  Attributes:
      structure_id (str): The reconciliation block.
      name (str): The block's name.
      scope (str): `ledger`: the whole ledger against one source. `account`: one account against an independent
          balance.
      method (str): Where the independent side comes from. `source_ledger` is the synced accounting system's own trial
          balance. `schedule_register` is what the account's schedules say it carries. `statement` is the ending balance
          of a statement recorded for the account.
      required_for_close (bool): Whether the period's close waits on this reconciliation.
      materiality (float): A difference up to this amount still counts as reconciled.
      period (str): The period, as YYYY-MM.
      as_of (datetime.date): The period's last day.
      status (str): `not_started`: not compared for this period. `stale`: the books have changed since it was
          compared, so run refresh-reconciliations. `unreconciled`: the sides differ by more than the materiality.
          `reconciled`: they agree within it. `reviewed`: reconciled and signed off.
      review_required (bool): Whether the close also waits for a sign-off.
      separate_reviewer (bool): Whether the reviewer must be someone other than the person who ran the comparison.
      element_id (None | str | Unset): The account reconciled; null for a ledger-scope block.
      unreconciled_difference (float | None | Unset): What is left unexplained at the last comparison; null when the
          period has not been compared. For a ledger-scope block, the sum of every account's absolute difference. For an
          account-scope block, the ledger balance minus the independent one.
      accounts_compared (int | None | Unset): Ledger-scope only: accounts with a balance on either side.
      accounts_different (int | None | Unset): Ledger-scope only: accounts that do not tie.
      ledger_balance (float | None | Unset): Account-scope only: the account's balance at the last comparison, debit-
          positive, as the period's close will leave it.
      independent_balance (float | None | Unset): Account-scope only: what the independent source said at the last
          comparison, debit-positive.
      balance_as_of (datetime.date | None | Unset): Account-scope only: the date the two balances are stated at. The
          period's last day, unless a statement ended earlier in the period.
      components (list[ReconciliationComponent] | Unset): Account-scope only: what makes up the independent balance.
          One entry per schedule for `schedule_register`; the recorded statement for `statement`.
      source (None | str | Unset): The system the independent side was read from.
      compared_at (datetime.datetime | None | Unset): When the two sides were last compared.
      fact_set_id (None | str | Unset): The FactSet holding the period's comparison.
      compared_by (None | str | Unset): The user whose action ran the last comparison.
      compared_via (None | str | Unset): `operation` when someone ran refresh-reconciliations; `sync` when a source
          sync refreshed it.
      reviewed_by (None | str | Unset): The user who signed off the comparison as it stands. Null when nobody has, or
          when the balances changed after the sign-off.
      reviewed_at (datetime.datetime | None | Unset): When the standing sign-off was made.
      self_reviewed (bool | None | Unset): True when the reviewer is the person who ran the comparison they signed
          off. Null when there is no standing sign-off.
      differences (list[ReconciliationRow] | Unset): Ledger-scope only: the accounts that did not tie at the last
          comparison, largest difference first.
  """

  structure_id: str
  name: str
  scope: str
  method: str
  required_for_close: bool
  materiality: float
  period: str
  as_of: datetime.date
  status: str
  review_required: bool
  separate_reviewer: bool
  element_id: None | str | Unset = UNSET
  unreconciled_difference: float | None | Unset = UNSET
  accounts_compared: int | None | Unset = UNSET
  accounts_different: int | None | Unset = UNSET
  ledger_balance: float | None | Unset = UNSET
  independent_balance: float | None | Unset = UNSET
  balance_as_of: datetime.date | None | Unset = UNSET
  components: list[ReconciliationComponent] | Unset = UNSET
  source: None | str | Unset = UNSET
  compared_at: datetime.datetime | None | Unset = UNSET
  fact_set_id: None | str | Unset = UNSET
  compared_by: None | str | Unset = UNSET
  compared_via: None | str | Unset = UNSET
  reviewed_by: None | str | Unset = UNSET
  reviewed_at: datetime.datetime | None | Unset = UNSET
  self_reviewed: bool | None | Unset = UNSET
  differences: list[ReconciliationRow] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    name = self.name

    scope = self.scope

    method = self.method

    required_for_close = self.required_for_close

    materiality = self.materiality

    period = self.period

    as_of = self.as_of.isoformat()

    status = self.status

    review_required = self.review_required

    separate_reviewer = self.separate_reviewer

    element_id: None | str | Unset
    if isinstance(self.element_id, Unset):
      element_id = UNSET
    else:
      element_id = self.element_id

    unreconciled_difference: float | None | Unset
    if isinstance(self.unreconciled_difference, Unset):
      unreconciled_difference = UNSET
    else:
      unreconciled_difference = self.unreconciled_difference

    accounts_compared: int | None | Unset
    if isinstance(self.accounts_compared, Unset):
      accounts_compared = UNSET
    else:
      accounts_compared = self.accounts_compared

    accounts_different: int | None | Unset
    if isinstance(self.accounts_different, Unset):
      accounts_different = UNSET
    else:
      accounts_different = self.accounts_different

    ledger_balance: float | None | Unset
    if isinstance(self.ledger_balance, Unset):
      ledger_balance = UNSET
    else:
      ledger_balance = self.ledger_balance

    independent_balance: float | None | Unset
    if isinstance(self.independent_balance, Unset):
      independent_balance = UNSET
    else:
      independent_balance = self.independent_balance

    balance_as_of: None | str | Unset
    if isinstance(self.balance_as_of, Unset):
      balance_as_of = UNSET
    elif isinstance(self.balance_as_of, datetime.date):
      balance_as_of = self.balance_as_of.isoformat()
    else:
      balance_as_of = self.balance_as_of

    components: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.components, Unset):
      components = []
      for components_item_data in self.components:
        components_item = components_item_data.to_dict()
        components.append(components_item)

    source: None | str | Unset
    if isinstance(self.source, Unset):
      source = UNSET
    else:
      source = self.source

    compared_at: None | str | Unset
    if isinstance(self.compared_at, Unset):
      compared_at = UNSET
    elif isinstance(self.compared_at, datetime.datetime):
      compared_at = self.compared_at.isoformat()
    else:
      compared_at = self.compared_at

    fact_set_id: None | str | Unset
    if isinstance(self.fact_set_id, Unset):
      fact_set_id = UNSET
    else:
      fact_set_id = self.fact_set_id

    compared_by: None | str | Unset
    if isinstance(self.compared_by, Unset):
      compared_by = UNSET
    else:
      compared_by = self.compared_by

    compared_via: None | str | Unset
    if isinstance(self.compared_via, Unset):
      compared_via = UNSET
    else:
      compared_via = self.compared_via

    reviewed_by: None | str | Unset
    if isinstance(self.reviewed_by, Unset):
      reviewed_by = UNSET
    else:
      reviewed_by = self.reviewed_by

    reviewed_at: None | str | Unset
    if isinstance(self.reviewed_at, Unset):
      reviewed_at = UNSET
    elif isinstance(self.reviewed_at, datetime.datetime):
      reviewed_at = self.reviewed_at.isoformat()
    else:
      reviewed_at = self.reviewed_at

    self_reviewed: bool | None | Unset
    if isinstance(self.self_reviewed, Unset):
      self_reviewed = UNSET
    else:
      self_reviewed = self.self_reviewed

    differences: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.differences, Unset):
      differences = []
      for differences_item_data in self.differences:
        differences_item = differences_item_data.to_dict()
        differences.append(differences_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "name": name,
        "scope": scope,
        "method": method,
        "required_for_close": required_for_close,
        "materiality": materiality,
        "period": period,
        "as_of": as_of,
        "status": status,
        "review_required": review_required,
        "separate_reviewer": separate_reviewer,
      }
    )
    if element_id is not UNSET:
      field_dict["element_id"] = element_id
    if unreconciled_difference is not UNSET:
      field_dict["unreconciled_difference"] = unreconciled_difference
    if accounts_compared is not UNSET:
      field_dict["accounts_compared"] = accounts_compared
    if accounts_different is not UNSET:
      field_dict["accounts_different"] = accounts_different
    if ledger_balance is not UNSET:
      field_dict["ledger_balance"] = ledger_balance
    if independent_balance is not UNSET:
      field_dict["independent_balance"] = independent_balance
    if balance_as_of is not UNSET:
      field_dict["balance_as_of"] = balance_as_of
    if components is not UNSET:
      field_dict["components"] = components
    if source is not UNSET:
      field_dict["source"] = source
    if compared_at is not UNSET:
      field_dict["compared_at"] = compared_at
    if fact_set_id is not UNSET:
      field_dict["fact_set_id"] = fact_set_id
    if compared_by is not UNSET:
      field_dict["compared_by"] = compared_by
    if compared_via is not UNSET:
      field_dict["compared_via"] = compared_via
    if reviewed_by is not UNSET:
      field_dict["reviewed_by"] = reviewed_by
    if reviewed_at is not UNSET:
      field_dict["reviewed_at"] = reviewed_at
    if self_reviewed is not UNSET:
      field_dict["self_reviewed"] = self_reviewed
    if differences is not UNSET:
      field_dict["differences"] = differences

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.reconciliation_component import ReconciliationComponent
    from ..models.reconciliation_row import ReconciliationRow

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    name = d.pop("name")

    scope = d.pop("scope")

    method = d.pop("method")

    required_for_close = d.pop("required_for_close")

    materiality = d.pop("materiality")

    period = d.pop("period")

    as_of = datetime.date.fromisoformat(d.pop("as_of"))

    status = d.pop("status")

    review_required = d.pop("review_required")

    separate_reviewer = d.pop("separate_reviewer")

    def _parse_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_id = _parse_element_id(d.pop("element_id", UNSET))

    def _parse_unreconciled_difference(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    unreconciled_difference = _parse_unreconciled_difference(
      d.pop("unreconciled_difference", UNSET)
    )

    def _parse_accounts_compared(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    accounts_compared = _parse_accounts_compared(d.pop("accounts_compared", UNSET))

    def _parse_accounts_different(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    accounts_different = _parse_accounts_different(d.pop("accounts_different", UNSET))

    def _parse_ledger_balance(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    ledger_balance = _parse_ledger_balance(d.pop("ledger_balance", UNSET))

    def _parse_independent_balance(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    independent_balance = _parse_independent_balance(
      d.pop("independent_balance", UNSET)
    )

    def _parse_balance_as_of(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        balance_as_of_type_0 = datetime.date.fromisoformat(data)

        return balance_as_of_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    balance_as_of = _parse_balance_as_of(d.pop("balance_as_of", UNSET))

    _components = d.pop("components", UNSET)
    components: list[ReconciliationComponent] | Unset = UNSET
    if _components is not UNSET:
      components = []
      for components_item_data in _components:
        components_item = ReconciliationComponent.from_dict(components_item_data)

        components.append(components_item)

    def _parse_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source = _parse_source(d.pop("source", UNSET))

    def _parse_compared_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        compared_at_type_0 = datetime.datetime.fromisoformat(data)

        return compared_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    compared_at = _parse_compared_at(d.pop("compared_at", UNSET))

    def _parse_fact_set_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    fact_set_id = _parse_fact_set_id(d.pop("fact_set_id", UNSET))

    def _parse_compared_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    compared_by = _parse_compared_by(d.pop("compared_by", UNSET))

    def _parse_compared_via(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    compared_via = _parse_compared_via(d.pop("compared_via", UNSET))

    def _parse_reviewed_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reviewed_by = _parse_reviewed_by(d.pop("reviewed_by", UNSET))

    def _parse_reviewed_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        reviewed_at_type_0 = datetime.datetime.fromisoformat(data)

        return reviewed_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    reviewed_at = _parse_reviewed_at(d.pop("reviewed_at", UNSET))

    def _parse_self_reviewed(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    self_reviewed = _parse_self_reviewed(d.pop("self_reviewed", UNSET))

    _differences = d.pop("differences", UNSET)
    differences: list[ReconciliationRow] | Unset = UNSET
    if _differences is not UNSET:
      differences = []
      for differences_item_data in _differences:
        differences_item = ReconciliationRow.from_dict(differences_item_data)

        differences.append(differences_item)

    reconciliation_summary = cls(
      structure_id=structure_id,
      name=name,
      scope=scope,
      method=method,
      required_for_close=required_for_close,
      materiality=materiality,
      period=period,
      as_of=as_of,
      status=status,
      review_required=review_required,
      separate_reviewer=separate_reviewer,
      element_id=element_id,
      unreconciled_difference=unreconciled_difference,
      accounts_compared=accounts_compared,
      accounts_different=accounts_different,
      ledger_balance=ledger_balance,
      independent_balance=independent_balance,
      balance_as_of=balance_as_of,
      components=components,
      source=source,
      compared_at=compared_at,
      fact_set_id=fact_set_id,
      compared_by=compared_by,
      compared_via=compared_via,
      reviewed_by=reviewed_by,
      reviewed_at=reviewed_at,
      self_reviewed=self_reviewed,
      differences=differences,
    )

    reconciliation_summary.additional_properties = d
    return reconciliation_summary

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
