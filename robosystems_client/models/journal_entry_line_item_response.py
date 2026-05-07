from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JournalEntryLineItemResponse")


@_attrs_define
class JournalEntryLineItemResponse:
  """One line in a journal entry response.

  Attributes:
      id (str):
      element_id (str):
      debit_amount (int):
      credit_amount (int):
      line_order (int):
      description (None | str | Unset):
  """

  id: str
  element_id: str
  debit_amount: int
  credit_amount: int
  line_order: int
  description: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    element_id = self.element_id

    debit_amount = self.debit_amount

    credit_amount = self.credit_amount

    line_order = self.line_order

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
        "element_id": element_id,
        "debit_amount": debit_amount,
        "credit_amount": credit_amount,
        "line_order": line_order,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    element_id = d.pop("element_id")

    debit_amount = d.pop("debit_amount")

    credit_amount = d.pop("credit_amount")

    line_order = d.pop("line_order")

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    journal_entry_line_item_response = cls(
      id=id,
      element_id=element_id,
      debit_amount=debit_amount,
      credit_amount=credit_amount,
      line_order=line_order,
      description=description,
    )

    journal_entry_line_item_response.additional_properties = d
    return journal_entry_line_item_response

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
