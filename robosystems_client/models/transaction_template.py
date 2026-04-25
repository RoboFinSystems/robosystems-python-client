from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.transaction_template_item import TransactionTemplateItem


T = TypeVar("T", bound="TransactionTemplate")


@_attrs_define
class TransactionTemplate:
  """The handler's output spec — one or more balanced entries to post.

  Wire shape::

      {
        "transactions": [{
          "entry_template": {
            "debit": {"element_id": "elem_...", "amount": "{{ event.amount }}"},
            "credit": {"element_id": "elem_...", "amount": "{{ event.amount }}"}
          }
        }]
      }

      Attributes:
          transactions (list[TransactionTemplateItem]): At least one debit/credit entry pair
  """

  transactions: list[TransactionTemplateItem]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    transactions = []
    for transactions_item_data in self.transactions:
      transactions_item = transactions_item_data.to_dict()
      transactions.append(transactions_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "transactions": transactions,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.transaction_template_item import TransactionTemplateItem

    d = dict(src_dict)
    transactions = []
    _transactions = d.pop("transactions")
    for transactions_item_data in _transactions:
      transactions_item = TransactionTemplateItem.from_dict(transactions_item_data)

      transactions.append(transactions_item)

    transaction_template = cls(
      transactions=transactions,
    )

    transaction_template.additional_properties = d
    return transaction_template

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
