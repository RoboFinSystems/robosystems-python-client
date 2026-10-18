from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.opening_balance_input import OpeningBalanceInput


T = TypeVar("T", bound="RecordOpeningBalanceRequest")


@_attrs_define
class RecordOpeningBalanceRequest:
  """The balance sheet a ledger starts from.

  Attributes:
      balances (list[OpeningBalanceInput]): One balance per balance-sheet account (assets, liabilities, equity). An
          income or expense account is refused: income before the books begin is already in retained earnings.
      entity_id (None | str | Unset): The entity whose books start here; omit for the group parent.
      equity_element_id (None | str | Unset): The equity account that takes any difference between debits and credits,
          usually Opening Balance Equity. Required when the balances do not balance; a non-zero balance left there is a
          review item.
      memo (None | str | Unset): The entry's memo; defaults to 'Opening balances'.
  """

  balances: list[OpeningBalanceInput]
  entity_id: None | str | Unset = UNSET
  equity_element_id: None | str | Unset = UNSET
  memo: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    balances = []
    for balances_item_data in self.balances:
      balances_item = balances_item_data.to_dict()
      balances.append(balances_item)

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    equity_element_id: None | str | Unset
    if isinstance(self.equity_element_id, Unset):
      equity_element_id = UNSET
    else:
      equity_element_id = self.equity_element_id

    memo: None | str | Unset
    if isinstance(self.memo, Unset):
      memo = UNSET
    else:
      memo = self.memo

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "balances": balances,
      }
    )
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if equity_element_id is not UNSET:
      field_dict["equity_element_id"] = equity_element_id
    if memo is not UNSET:
      field_dict["memo"] = memo

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.opening_balance_input import OpeningBalanceInput

    d = dict(src_dict)
    balances = []
    _balances = d.pop("balances")
    for balances_item_data in _balances:
      balances_item = OpeningBalanceInput.from_dict(balances_item_data)

      balances.append(balances_item)

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    def _parse_equity_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    equity_element_id = _parse_equity_element_id(d.pop("equity_element_id", UNSET))

    def _parse_memo(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    memo = _parse_memo(d.pop("memo", UNSET))

    record_opening_balance_request = cls(
      balances=balances,
      entity_id=entity_id,
      equity_element_id=equity_element_id,
      memo=memo,
    )

    record_opening_balance_request.additional_properties = d
    return record_opening_balance_request

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
