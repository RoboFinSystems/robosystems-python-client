from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.ledger_transaction_summary_response import (
    LedgerTransactionSummaryResponse,
  )
  from ..models.pagination_info import PaginationInfo


T = TypeVar("T", bound="LedgerTransactionListResponse")


@_attrs_define
class LedgerTransactionListResponse:
  """
  Attributes:
      transactions (list[LedgerTransactionSummaryResponse]):
      pagination (PaginationInfo): Pagination information for list responses. Example: {'has_more': True, 'limit': 20,
          'offset': 0, 'total': 100}.
  """

  transactions: list[LedgerTransactionSummaryResponse]
  pagination: PaginationInfo
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    transactions = []
    for transactions_item_data in self.transactions:
      transactions_item = transactions_item_data.to_dict()
      transactions.append(transactions_item)

    pagination = self.pagination.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "transactions": transactions,
        "pagination": pagination,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.ledger_transaction_summary_response import (
      LedgerTransactionSummaryResponse,
    )
    from ..models.pagination_info import PaginationInfo

    d = dict(src_dict)
    transactions = []
    _transactions = d.pop("transactions")
    for transactions_item_data in _transactions:
      transactions_item = LedgerTransactionSummaryResponse.from_dict(
        transactions_item_data
      )

      transactions.append(transactions_item)

    pagination = PaginationInfo.from_dict(d.pop("pagination"))

    ledger_transaction_list_response = cls(
      transactions=transactions,
      pagination=pagination,
    )

    ledger_transaction_list_response.additional_properties = d
    return ledger_transaction_list_response

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
