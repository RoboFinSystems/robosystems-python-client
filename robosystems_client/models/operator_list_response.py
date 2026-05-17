from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.operator_list_response_operators import OperatorListResponseOperators


T = TypeVar("T", bound="OperatorListResponse")


@_attrs_define
class OperatorListResponse:
  """Response for listing available operators.

  Attributes:
      operators (OperatorListResponseOperators): Dictionary of available operators with metadata
      total (int): Total number of operators
  """

  operators: OperatorListResponseOperators
  total: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    operators = self.operators.to_dict()

    total = self.total

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "operators": operators,
        "total": total,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.operator_list_response_operators import OperatorListResponseOperators

    d = dict(src_dict)
    operators = OperatorListResponseOperators.from_dict(d.pop("operators"))

    total = d.pop("total")

    operator_list_response = cls(
      operators=operators,
      total=total,
    )

    operator_list_response.additional_properties = d
    return operator_list_response

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
