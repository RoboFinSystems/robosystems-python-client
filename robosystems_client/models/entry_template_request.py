from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entry_template_request_entry_type import EntryTemplateRequestEntryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EntryTemplateRequest")


@_attrs_define
class EntryTemplateRequest:
  """
  Attributes:
      debit_element_id (str): Element to debit (e.g., Depreciation Expense)
      credit_element_id (str): Element to credit (e.g., Accumulated Depreciation)
      entry_type (EntryTemplateRequestEntryType | Unset): Entry type for generated entries Default:
          EntryTemplateRequestEntryType.CLOSING.
      memo_template (str | Unset): Memo template ({structure_name} is replaced) Default: ''.
      auto_reverse (bool | Unset): Auto-generate a reversing entry on the first day of the next period Default: False.
  """

  debit_element_id: str
  credit_element_id: str
  entry_type: EntryTemplateRequestEntryType | Unset = (
    EntryTemplateRequestEntryType.CLOSING
  )
  memo_template: str | Unset = ""
  auto_reverse: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    debit_element_id = self.debit_element_id

    credit_element_id = self.credit_element_id

    entry_type: str | Unset = UNSET
    if not isinstance(self.entry_type, Unset):
      entry_type = self.entry_type.value

    memo_template = self.memo_template

    auto_reverse = self.auto_reverse

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
    if auto_reverse is not UNSET:
      field_dict["auto_reverse"] = auto_reverse

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    debit_element_id = d.pop("debit_element_id")

    credit_element_id = d.pop("credit_element_id")

    _entry_type = d.pop("entry_type", UNSET)
    entry_type: EntryTemplateRequestEntryType | Unset
    if isinstance(_entry_type, Unset):
      entry_type = UNSET
    else:
      entry_type = EntryTemplateRequestEntryType(_entry_type)

    memo_template = d.pop("memo_template", UNSET)

    auto_reverse = d.pop("auto_reverse", UNSET)

    entry_template_request = cls(
      debit_element_id=debit_element_id,
      credit_element_id=credit_element_id,
      entry_type=entry_type,
      memo_template=memo_template,
      auto_reverse=auto_reverse,
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
