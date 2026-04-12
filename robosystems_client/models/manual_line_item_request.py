from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManualLineItemRequest")


@_attrs_define
class ManualLineItemRequest:
  """
  Attributes:
      element_id (str): Element ID (chart of accounts)
      debit_amount (int | Unset): Debit in cents Default: 0.
      credit_amount (int | Unset): Credit in cents Default: 0.
      description (None | str | Unset):
  """

  element_id: str
  debit_amount: int | Unset = 0
  credit_amount: int | Unset = 0
  description: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    debit_amount = self.debit_amount

    credit_amount = self.credit_amount

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
      }
    )
    if debit_amount is not UNSET:
      field_dict["debit_amount"] = debit_amount
    if credit_amount is not UNSET:
      field_dict["credit_amount"] = credit_amount
    if description is not UNSET:
      field_dict["description"] = description

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    debit_amount = d.pop("debit_amount", UNSET)

    credit_amount = d.pop("credit_amount", UNSET)

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    manual_line_item_request = cls(
      element_id=element_id,
      debit_amount=debit_amount,
      credit_amount=credit_amount,
      description=description,
    )

    manual_line_item_request.additional_properties = d
    return manual_line_item_request

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
