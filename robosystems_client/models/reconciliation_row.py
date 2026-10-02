from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.reconciliation_component import ReconciliationComponent


T = TypeVar("T", bound="ReconciliationRow")


@_attrs_define
class ReconciliationRow:
  """One account: the ledger's balance, the independent balance, the difference.

  Balances are debit-positive, so a credit balance is negative on both sides.

      Attributes:
          account_name (str): The account's name in the ledger, else in the source.
          ledger_balance (float): What the ledger holds. For `source_ledger`, landed entries only. For
              `schedule_register`, the balance as the period's close will leave it: landed entries, drafts awaiting the close,
              and schedule entries not yet drafted.
          independent_balance (float): What the independent source says.
          difference (float): Ledger minus independent.
          status (str): `tied`: both sides agree to the cent. `different`: both know the account and disagree.
              `not_in_ledger`: the source reports an account the ledger has none for. `not_in_source`: the ledger holds a
              balance on an account the source does not have.
          element_id (None | str | Unset): The chart account; null when the ledger has none for it.
          account_code (None | str | Unset): The chart account's code.
          source_account_id (None | str | Unset): The account's id in the source system, when it has one.
          statement (None | str | Unset): `balance_sheet` or `income_statement`. Balance-sheet accounts are compared
              cumulatively to the period end; income-statement accounts from the start of the fiscal year. Null when the
              ledger has no account.
          as_of (datetime.date | None | Unset): The date both balances are stated at, when it is not the period's last
              day: a statement that ends mid-period is compared with the ledger at the statement's own date.
          components (list[ReconciliationComponent] | Unset): Account-scope methods only: what makes up the independent
              balance. One entry per schedule for `schedule_register`; the recorded statement for `statement`.
  """

  account_name: str
  ledger_balance: float
  independent_balance: float
  difference: float
  status: str
  element_id: None | str | Unset = UNSET
  account_code: None | str | Unset = UNSET
  source_account_id: None | str | Unset = UNSET
  statement: None | str | Unset = UNSET
  as_of: datetime.date | None | Unset = UNSET
  components: list[ReconciliationComponent] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    account_name = self.account_name

    ledger_balance = self.ledger_balance

    independent_balance = self.independent_balance

    difference = self.difference

    status = self.status

    element_id: None | str | Unset
    if isinstance(self.element_id, Unset):
      element_id = UNSET
    else:
      element_id = self.element_id

    account_code: None | str | Unset
    if isinstance(self.account_code, Unset):
      account_code = UNSET
    else:
      account_code = self.account_code

    source_account_id: None | str | Unset
    if isinstance(self.source_account_id, Unset):
      source_account_id = UNSET
    else:
      source_account_id = self.source_account_id

    statement: None | str | Unset
    if isinstance(self.statement, Unset):
      statement = UNSET
    else:
      statement = self.statement

    as_of: None | str | Unset
    if isinstance(self.as_of, Unset):
      as_of = UNSET
    elif isinstance(self.as_of, datetime.date):
      as_of = self.as_of.isoformat()
    else:
      as_of = self.as_of

    components: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.components, Unset):
      components = []
      for components_item_data in self.components:
        components_item = components_item_data.to_dict()
        components.append(components_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "account_name": account_name,
        "ledger_balance": ledger_balance,
        "independent_balance": independent_balance,
        "difference": difference,
        "status": status,
      }
    )
    if element_id is not UNSET:
      field_dict["element_id"] = element_id
    if account_code is not UNSET:
      field_dict["account_code"] = account_code
    if source_account_id is not UNSET:
      field_dict["source_account_id"] = source_account_id
    if statement is not UNSET:
      field_dict["statement"] = statement
    if as_of is not UNSET:
      field_dict["as_of"] = as_of
    if components is not UNSET:
      field_dict["components"] = components

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.reconciliation_component import ReconciliationComponent

    d = dict(src_dict)
    account_name = d.pop("account_name")

    ledger_balance = d.pop("ledger_balance")

    independent_balance = d.pop("independent_balance")

    difference = d.pop("difference")

    status = d.pop("status")

    def _parse_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_id = _parse_element_id(d.pop("element_id", UNSET))

    def _parse_account_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    account_code = _parse_account_code(d.pop("account_code", UNSET))

    def _parse_source_account_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_account_id = _parse_source_account_id(d.pop("source_account_id", UNSET))

    def _parse_statement(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    statement = _parse_statement(d.pop("statement", UNSET))

    def _parse_as_of(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        as_of_type_0 = datetime.date.fromisoformat(data)

        return as_of_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    as_of = _parse_as_of(d.pop("as_of", UNSET))

    _components = d.pop("components", UNSET)
    components: list[ReconciliationComponent] | Unset = UNSET
    if _components is not UNSET:
      components = []
      for components_item_data in _components:
        components_item = ReconciliationComponent.from_dict(components_item_data)

        components.append(components_item)

    reconciliation_row = cls(
      account_name=account_name,
      ledger_balance=ledger_balance,
      independent_balance=independent_balance,
      difference=difference,
      status=status,
      element_id=element_id,
      account_code=account_code,
      source_account_id=source_account_id,
      statement=statement,
      as_of=as_of,
      components=components,
    )

    reconciliation_row.additional_properties = d
    return reconciliation_row

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
