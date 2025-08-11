from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.detailed_transactions_response_date_range import (
    DetailedTransactionsResponseDateRange,
  )
  from ..models.detailed_transactions_response_summary import (
    DetailedTransactionsResponseSummary,
  )
  from ..models.enhanced_credit_transaction_response import (
    EnhancedCreditTransactionResponse,
  )


T = TypeVar("T", bound="DetailedTransactionsResponse")


@_attrs_define
class DetailedTransactionsResponse:
  """Detailed response for transaction queries.

  Attributes:
      transactions (list['EnhancedCreditTransactionResponse']):
      summary (DetailedTransactionsResponseSummary):
      total_count (int):
      filtered_count (int):
      date_range (DetailedTransactionsResponseDateRange):
  """

  transactions: list["EnhancedCreditTransactionResponse"]
  summary: "DetailedTransactionsResponseSummary"
  total_count: int
  filtered_count: int
  date_range: "DetailedTransactionsResponseDateRange"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    transactions = []
    for transactions_item_data in self.transactions:
      transactions_item = transactions_item_data.to_dict()
      transactions.append(transactions_item)

    summary = self.summary.to_dict()

    total_count = self.total_count

    filtered_count = self.filtered_count

    date_range = self.date_range.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "transactions": transactions,
        "summary": summary,
        "total_count": total_count,
        "filtered_count": filtered_count,
        "date_range": date_range,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.detailed_transactions_response_date_range import (
      DetailedTransactionsResponseDateRange,
    )
    from ..models.detailed_transactions_response_summary import (
      DetailedTransactionsResponseSummary,
    )
    from ..models.enhanced_credit_transaction_response import (
      EnhancedCreditTransactionResponse,
    )

    d = dict(src_dict)
    transactions = []
    _transactions = d.pop("transactions")
    for transactions_item_data in _transactions:
      transactions_item = EnhancedCreditTransactionResponse.from_dict(
        transactions_item_data
      )

      transactions.append(transactions_item)

    summary = DetailedTransactionsResponseSummary.from_dict(d.pop("summary"))

    total_count = d.pop("total_count")

    filtered_count = d.pop("filtered_count")

    date_range = DetailedTransactionsResponseDateRange.from_dict(d.pop("date_range"))

    detailed_transactions_response = cls(
      transactions=transactions,
      summary=summary,
      total_count=total_count,
      filtered_count=filtered_count,
      date_range=date_range,
    )

    detailed_transactions_response.additional_properties = d
    return detailed_transactions_response

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
