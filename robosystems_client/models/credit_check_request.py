from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditCheckRequest")


@_attrs_define
class CreditCheckRequest:
  """Request to check credit balance.

  Attributes:
      operation_type (str): Type of operation to check
      base_cost (Union[None, Unset, float]): Custom base cost (uses default if not provided)
  """

  operation_type: str
  base_cost: Union[None, Unset, float] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    operation_type = self.operation_type

    base_cost: Union[None, Unset, float]
    if isinstance(self.base_cost, Unset):
      base_cost = UNSET
    else:
      base_cost = self.base_cost

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "operation_type": operation_type,
      }
    )
    if base_cost is not UNSET:
      field_dict["base_cost"] = base_cost

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    operation_type = d.pop("operation_type")

    def _parse_base_cost(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    base_cost = _parse_base_cost(d.pop("base_cost", UNSET))

    credit_check_request = cls(
      operation_type=operation_type,
      base_cost=base_cost,
    )

    credit_check_request.additional_properties = d
    return credit_check_request

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
