from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HoldingSecuritySummary")


@_attrs_define
class HoldingSecuritySummary:
  """
  Attributes:
      security_id (str):
      security_name (str):
      security_type (str):
      quantity (float):
      quantity_type (str):
      cost_basis_dollars (float):
      current_value_dollars (float | None | Unset):
  """

  security_id: str
  security_name: str
  security_type: str
  quantity: float
  quantity_type: str
  cost_basis_dollars: float
  current_value_dollars: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    security_id = self.security_id

    security_name = self.security_name

    security_type = self.security_type

    quantity = self.quantity

    quantity_type = self.quantity_type

    cost_basis_dollars = self.cost_basis_dollars

    current_value_dollars: float | None | Unset
    if isinstance(self.current_value_dollars, Unset):
      current_value_dollars = UNSET
    else:
      current_value_dollars = self.current_value_dollars

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "security_id": security_id,
        "security_name": security_name,
        "security_type": security_type,
        "quantity": quantity,
        "quantity_type": quantity_type,
        "cost_basis_dollars": cost_basis_dollars,
      }
    )
    if current_value_dollars is not UNSET:
      field_dict["current_value_dollars"] = current_value_dollars

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    security_id = d.pop("security_id")

    security_name = d.pop("security_name")

    security_type = d.pop("security_type")

    quantity = d.pop("quantity")

    quantity_type = d.pop("quantity_type")

    cost_basis_dollars = d.pop("cost_basis_dollars")

    def _parse_current_value_dollars(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    current_value_dollars = _parse_current_value_dollars(
      d.pop("current_value_dollars", UNSET)
    )

    holding_security_summary = cls(
      security_id=security_id,
      security_name=security_name,
      security_type=security_type,
      quantity=quantity,
      quantity_type=quantity_type,
      cost_basis_dollars=cost_basis_dollars,
      current_value_dollars=current_value_dollars,
    )

    holding_security_summary.additional_properties = d
    return holding_security_summary

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
