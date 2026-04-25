from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.transaction_template_leg import TransactionTemplateLeg


T = TypeVar("T", bound="TransactionTemplateEntry")


@_attrs_define
class TransactionTemplateEntry:
  """One balanced entry (debit + credit pair) — the inner shape of entry_template.

  Attributes:
      debit (TransactionTemplateLeg): One side of a journal entry leg (debit or credit).
      credit (TransactionTemplateLeg): One side of a journal entry leg (debit or credit).
  """

  debit: TransactionTemplateLeg
  credit: TransactionTemplateLeg
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    debit = self.debit.to_dict()

    credit = self.credit.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "debit": debit,
        "credit": credit,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.transaction_template_leg import TransactionTemplateLeg

    d = dict(src_dict)
    debit = TransactionTemplateLeg.from_dict(d.pop("debit"))

    credit = TransactionTemplateLeg.from_dict(d.pop("credit"))

    transaction_template_entry = cls(
      debit=debit,
      credit=credit,
    )

    transaction_template_entry.additional_properties = d
    return transaction_template_entry

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
