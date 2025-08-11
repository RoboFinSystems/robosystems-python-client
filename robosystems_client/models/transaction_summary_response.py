from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionSummaryResponse")


@_attrs_define
class TransactionSummaryResponse:
  """Summary of transactions by operation type.

  Attributes:
      operation_type (str):
      total_amount (float):
      transaction_count (int):
      average_amount (float):
      first_transaction (Union[None, Unset, str]):
      last_transaction (Union[None, Unset, str]):
  """

  operation_type: str
  total_amount: float
  transaction_count: int
  average_amount: float
  first_transaction: Union[None, Unset, str] = UNSET
  last_transaction: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    operation_type = self.operation_type

    total_amount = self.total_amount

    transaction_count = self.transaction_count

    average_amount = self.average_amount

    first_transaction: Union[None, Unset, str]
    if isinstance(self.first_transaction, Unset):
      first_transaction = UNSET
    else:
      first_transaction = self.first_transaction

    last_transaction: Union[None, Unset, str]
    if isinstance(self.last_transaction, Unset):
      last_transaction = UNSET
    else:
      last_transaction = self.last_transaction

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "operation_type": operation_type,
        "total_amount": total_amount,
        "transaction_count": transaction_count,
        "average_amount": average_amount,
      }
    )
    if first_transaction is not UNSET:
      field_dict["first_transaction"] = first_transaction
    if last_transaction is not UNSET:
      field_dict["last_transaction"] = last_transaction

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    operation_type = d.pop("operation_type")

    total_amount = d.pop("total_amount")

    transaction_count = d.pop("transaction_count")

    average_amount = d.pop("average_amount")

    def _parse_first_transaction(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    first_transaction = _parse_first_transaction(d.pop("first_transaction", UNSET))

    def _parse_last_transaction(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    last_transaction = _parse_last_transaction(d.pop("last_transaction", UNSET))

    transaction_summary_response = cls(
      operation_type=operation_type,
      total_amount=total_amount,
      transaction_count=transaction_count,
      average_amount=average_amount,
      first_transaction=first_transaction,
      last_transaction=last_transaction,
    )

    transaction_summary_response.additional_properties = d
    return transaction_summary_response

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
