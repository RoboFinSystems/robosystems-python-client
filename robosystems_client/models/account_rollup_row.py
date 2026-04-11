from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountRollupRow")


@_attrs_define
class AccountRollupRow:
  """
  Attributes:
      element_id (str):
      account_name (str):
      total_debits (float):
      total_credits (float):
      net_balance (float):
      account_code (None | str | Unset):
  """

  element_id: str
  account_name: str
  total_debits: float
  total_credits: float
  net_balance: float
  account_code: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    account_name = self.account_name

    total_debits = self.total_debits

    total_credits = self.total_credits

    net_balance = self.net_balance

    account_code: None | str | Unset
    if isinstance(self.account_code, Unset):
      account_code = UNSET
    else:
      account_code = self.account_code

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "account_name": account_name,
        "total_debits": total_debits,
        "total_credits": total_credits,
        "net_balance": net_balance,
      }
    )
    if account_code is not UNSET:
      field_dict["account_code"] = account_code

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    account_name = d.pop("account_name")

    total_debits = d.pop("total_debits")

    total_credits = d.pop("total_credits")

    net_balance = d.pop("net_balance")

    def _parse_account_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    account_code = _parse_account_code(d.pop("account_code", UNSET))

    account_rollup_row = cls(
      element_id=element_id,
      account_name=account_name,
      total_debits=total_debits,
      total_credits=total_credits,
      net_balance=net_balance,
      account_code=account_code,
    )

    account_rollup_row.additional_properties = d
    return account_rollup_row

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
