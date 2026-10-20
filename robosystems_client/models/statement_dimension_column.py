from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatementDimensionColumn")


@_attrs_define
class StatementDimensionColumn:
  """One column of a statement read by dimension.

  Attributes:
      name (str): The column's label.
      member_id (None | str | Unset): The member the column reads, `unallocated` for the untagged lines, null for the
          Total.
  """

  name: str
  member_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    member_id: None | str | Unset
    if isinstance(self.member_id, Unset):
      member_id = UNSET
    else:
      member_id = self.member_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
      }
    )
    if member_id is not UNSET:
      field_dict["member_id"] = member_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    def _parse_member_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    member_id = _parse_member_id(d.pop("member_id", UNSET))

    statement_dimension_column = cls(
      name=name,
      member_id=member_id,
    )

    statement_dimension_column.additional_properties = d
    return statement_dimension_column

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
