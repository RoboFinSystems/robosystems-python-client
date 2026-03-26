from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerLineItemResponse")


@_attrs_define
class LedgerLineItemResponse:
  """
  Attributes:
      id (str):
      account_id (str):
      debit_amount (float):
      credit_amount (float):
      line_order (int):
      account_name (None | str | Unset):
      account_code (None | str | Unset):
      description (None | str | Unset):
  """

  id: str
  account_id: str
  debit_amount: float
  credit_amount: float
  line_order: int
  account_name: None | str | Unset = UNSET
  account_code: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    account_id = self.account_id

    debit_amount = self.debit_amount

    credit_amount = self.credit_amount

    line_order = self.line_order

    account_name: None | str | Unset
    if isinstance(self.account_name, Unset):
      account_name = UNSET
    else:
      account_name = self.account_name

    account_code: None | str | Unset
    if isinstance(self.account_code, Unset):
      account_code = UNSET
    else:
      account_code = self.account_code

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "account_id": account_id,
        "debit_amount": debit_amount,
        "credit_amount": credit_amount,
        "line_order": line_order,
      }
    )
    if account_name is not UNSET:
      field_dict["account_name"] = account_name
    if account_code is not UNSET:
      field_dict["account_code"] = account_code
    if description is not UNSET:
      field_dict["description"] = description

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    account_id = d.pop("account_id")

    debit_amount = d.pop("debit_amount")

    credit_amount = d.pop("credit_amount")

    line_order = d.pop("line_order")

    def _parse_account_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    account_name = _parse_account_name(d.pop("account_name", UNSET))

    def _parse_account_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    account_code = _parse_account_code(d.pop("account_code", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    ledger_line_item_response = cls(
      id=id,
      account_id=account_id,
      debit_amount=debit_amount,
      credit_amount=credit_amount,
      line_order=line_order,
      account_name=account_name,
      account_code=account_code,
      description=description,
    )

    ledger_line_item_response.additional_properties = d
    return ledger_line_item_response

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
