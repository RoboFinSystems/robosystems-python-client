from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.account_rollup_row import AccountRollupRow


T = TypeVar("T", bound="AccountRollupGroup")


@_attrs_define
class AccountRollupGroup:
  """
  Attributes:
      reporting_element_id (str):
      reporting_name (str):
      reporting_qname (str):
      classification (str):
      balance_type (str):
      total (float):
      accounts (list[AccountRollupRow]):
  """

  reporting_element_id: str
  reporting_name: str
  reporting_qname: str
  classification: str
  balance_type: str
  total: float
  accounts: list[AccountRollupRow]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    reporting_element_id = self.reporting_element_id

    reporting_name = self.reporting_name

    reporting_qname = self.reporting_qname

    classification = self.classification

    balance_type = self.balance_type

    total = self.total

    accounts = []
    for accounts_item_data in self.accounts:
      accounts_item = accounts_item_data.to_dict()
      accounts.append(accounts_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "reporting_element_id": reporting_element_id,
        "reporting_name": reporting_name,
        "reporting_qname": reporting_qname,
        "classification": classification,
        "balance_type": balance_type,
        "total": total,
        "accounts": accounts,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.account_rollup_row import AccountRollupRow

    d = dict(src_dict)
    reporting_element_id = d.pop("reporting_element_id")

    reporting_name = d.pop("reporting_name")

    reporting_qname = d.pop("reporting_qname")

    classification = d.pop("classification")

    balance_type = d.pop("balance_type")

    total = d.pop("total")

    accounts = []
    _accounts = d.pop("accounts")
    for accounts_item_data in _accounts:
      accounts_item = AccountRollupRow.from_dict(accounts_item_data)

      accounts.append(accounts_item)

    account_rollup_group = cls(
      reporting_element_id=reporting_element_id,
      reporting_name=reporting_name,
      reporting_qname=reporting_qname,
      classification=classification,
      balance_type=balance_type,
      total=total,
      accounts=accounts,
    )

    account_rollup_group.additional_properties = d
    return account_rollup_group

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
