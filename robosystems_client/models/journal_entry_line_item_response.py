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
      flow_qname (None | str | Unset): The cash flow row this line carries, when tagged; null means the account's
          default flow.
      dimension_ids (list[str] | Unset): The management dimension members the line carries, by id.
  """

  id: str
  element_id: str
  debit_amount: int
  credit_amount: int
  line_order: int
  description: None | str | Unset = UNSET
  flow_qname: None | str | Unset = UNSET
  dimension_ids: list[str] | Unset = UNSET
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

    flow_qname: None | str | Unset
    if isinstance(self.flow_qname, Unset):
      flow_qname = UNSET
    else:
      flow_qname = self.flow_qname

    dimension_ids: list[str] | Unset = UNSET
    if not isinstance(self.dimension_ids, Unset):
      dimension_ids = self.dimension_ids

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
    if flow_qname is not UNSET:
      field_dict["flow_qname"] = flow_qname
    if dimension_ids is not UNSET:
      field_dict["dimension_ids"] = dimension_ids

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

    def _parse_flow_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    flow_qname = _parse_flow_qname(d.pop("flow_qname", UNSET))

    dimension_ids = cast(list[str], d.pop("dimension_ids", UNSET))

    journal_entry_line_item_response = cls(
      id=id,
      element_id=element_id,
      debit_amount=debit_amount,
      credit_amount=credit_amount,
      line_order=line_order,
      description=description,
      flow_qname=flow_qname,
      dimension_ids=dimension_ids,
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
