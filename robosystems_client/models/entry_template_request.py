from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntryTemplateRequest")


@_attrs_define
class EntryTemplateRequest:
  """
  Attributes:
      debit_element_id (str): Element to debit (e.g., Depreciation Expense)
      credit_element_id (str): Element to credit (e.g., Accumulated Depreciation)
      entry_type (str | Unset): Entry type for generated entries Default: 'closing'.
      memo_template (str | Unset): Memo template ({structure_name} is replaced) Default: ''.
  """

  debit_element_id: str
  credit_element_id: str
  entry_type: str | Unset = "closing"
  memo_template: str | Unset = ""
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    debit_element_id = self.debit_element_id

    credit_element_id = self.credit_element_id

    entry_type = self.entry_type

    memo_template = self.memo_template

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "debit_element_id": debit_element_id,
        "credit_element_id": credit_element_id,
      }
    )
    if entry_type is not UNSET:
      field_dict["entry_type"] = entry_type
    if memo_template is not UNSET:
      field_dict["memo_template"] = memo_template

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    debit_element_id = d.pop("debit_element_id")

    credit_element_id = d.pop("credit_element_id")

    entry_type = d.pop("entry_type", UNSET)

    memo_template = d.pop("memo_template", UNSET)

    entry_template_request = cls(
      debit_element_id=debit_element_id,
      credit_element_id=credit_element_id,
      entry_type=entry_type,
      memo_template=memo_template,
    )

    entry_template_request.additional_properties = d
    return entry_template_request

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
