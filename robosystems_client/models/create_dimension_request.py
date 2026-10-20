from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDimensionRequest")


@_attrs_define
class CreateDimensionRequest:
  """Add a member to a management dimension.

  Attributes:
      dimension_type (str): The axis: `department`, `class`, `location` or `project`, or any other lowercase name,
          which starts an axis of its own. `scenario` is reserved for forecasts.
      name (str): The member's label.
      value (None | str | Unset): The member's stable key within the axis; omitted, a slug of the name. Refused (409)
          when the axis already has it.
  """

  dimension_type: str
  name: str
  value: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    dimension_type = self.dimension_type

    name = self.name

    value: None | str | Unset
    if isinstance(self.value, Unset):
      value = UNSET
    else:
      value = self.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "dimension_type": dimension_type,
        "name": name,
      }
    )
    if value is not UNSET:
      field_dict["value"] = value

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    dimension_type = d.pop("dimension_type")

    name = d.pop("name")

    def _parse_value(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    value = _parse_value(d.pop("value", UNSET))

    create_dimension_request = cls(
      dimension_type=dimension_type,
      name=name,
      value=value,
    )

    create_dimension_request.additional_properties = d
    return create_dimension_request

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
