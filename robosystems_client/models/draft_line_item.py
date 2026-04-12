from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DraftLineItem")


@_attrs_define
class DraftLineItem:
  """A single line item within a draft entry.

  Attributes:
      line_item_id (str):
      element_id (str):
      element_name (str):
      debit_amount (int): Debit amount in cents
      credit_amount (int): Credit amount in cents
      element_code (None | str | Unset):
      description (None | str | Unset):
  """

  line_item_id: str
  element_id: str
  element_name: str
  debit_amount: int
  credit_amount: int
  element_code: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    line_item_id = self.line_item_id

    element_id = self.element_id

    element_name = self.element_name

    debit_amount = self.debit_amount

    credit_amount = self.credit_amount

    element_code: None | str | Unset
    if isinstance(self.element_code, Unset):
      element_code = UNSET
    else:
      element_code = self.element_code

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "line_item_id": line_item_id,
        "element_id": element_id,
        "element_name": element_name,
        "debit_amount": debit_amount,
        "credit_amount": credit_amount,
      }
    )
    if element_code is not UNSET:
      field_dict["element_code"] = element_code
    if description is not UNSET:
      field_dict["description"] = description

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    line_item_id = d.pop("line_item_id")

    element_id = d.pop("element_id")

    element_name = d.pop("element_name")

    debit_amount = d.pop("debit_amount")

    credit_amount = d.pop("credit_amount")

    def _parse_element_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_code = _parse_element_code(d.pop("element_code", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    draft_line_item = cls(
      line_item_id=line_item_id,
      element_id=element_id,
      element_name=element_name,
      debit_amount=debit_amount,
      credit_amount=credit_amount,
      element_code=element_code,
      description=description,
    )

    draft_line_item.additional_properties = d
    return draft_line_item

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
