from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrialBalanceRow")


@_attrs_define
class TrialBalanceRow:
  """
  Attributes:
      account_id (str):
      account_code (str):
      account_name (str):
      classification (str):
      total_debits (float):
      total_credits (float):
      net_balance (float):
      account_type (None | str | Unset):
  """

  account_id: str
  account_code: str
  account_name: str
  classification: str
  total_debits: float
  total_credits: float
  net_balance: float
  account_type: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    account_id = self.account_id

    account_code = self.account_code

    account_name = self.account_name

    classification = self.classification

    total_debits = self.total_debits

    total_credits = self.total_credits

    net_balance = self.net_balance

    account_type: None | str | Unset
    if isinstance(self.account_type, Unset):
      account_type = UNSET
    else:
      account_type = self.account_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "account_id": account_id,
        "account_code": account_code,
        "account_name": account_name,
        "classification": classification,
        "total_debits": total_debits,
        "total_credits": total_credits,
        "net_balance": net_balance,
      }
    )
    if account_type is not UNSET:
      field_dict["account_type"] = account_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    account_id = d.pop("account_id")

    account_code = d.pop("account_code")

    account_name = d.pop("account_name")

    classification = d.pop("classification")

    total_debits = d.pop("total_debits")

    total_credits = d.pop("total_credits")

    net_balance = d.pop("net_balance")

    def _parse_account_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    account_type = _parse_account_type(d.pop("account_type", UNSET))

    trial_balance_row = cls(
      account_id=account_id,
      account_code=account_code,
      account_name=account_name,
      classification=classification,
      total_debits=total_debits,
      total_credits=total_credits,
      net_balance=net_balance,
      account_type=account_type,
    )

    trial_balance_row.additional_properties = d
    return trial_balance_row

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
