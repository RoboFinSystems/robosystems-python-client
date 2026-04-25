from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.transaction_template_entry import TransactionTemplateEntry


T = TypeVar("T", bound="TransactionTemplateItem")


@_attrs_define
class TransactionTemplateItem:
  """One item in the transactions list — wraps entry_template to match the DSL shape.

  Attributes:
      entry_template (TransactionTemplateEntry): One balanced entry (debit + credit pair) — the inner shape of
          entry_template.
  """

  entry_template: TransactionTemplateEntry
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entry_template = self.entry_template.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entry_template": entry_template,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.transaction_template_entry import TransactionTemplateEntry

    d = dict(src_dict)
    entry_template = TransactionTemplateEntry.from_dict(d.pop("entry_template"))

    transaction_template_item = cls(
      entry_template=entry_template,
    )

    transaction_template_item.additional_properties = d
    return transaction_template_item

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
