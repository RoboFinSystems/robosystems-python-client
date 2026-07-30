from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dimension_type import DimensionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Dimension")


@_attrs_define
class Dimension:
  """
  Attributes:
      name (str): Dimension name (e.g., 'Element', 'Period')
      type_ (DimensionType):
      members (list[str] | Unset): List of dimension members
  """

  name: str
  type_: DimensionType
  members: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    type_ = self.type_.value

    members: list[str] | Unset = UNSET
    if not isinstance(self.members, Unset):
      members = self.members

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "type": type_,
      }
    )
    if members is not UNSET:
      field_dict["members"] = members

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    type_ = DimensionType(d.pop("type"))

    members = cast(list[str], d.pop("members", UNSET))

    dimension = cls(
      name=name,
      type_=type_,
      members=members,
    )

    dimension.additional_properties = d
    return dimension

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
