from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatementDimension")


@_attrs_define
class StatementDimension:
  """A management slice of a statement or trial balance.

  Attributes:
      type_ (str): The axis to slice by: `department`, `class`, and so on.
      member_id (None | str | Unset): One member's lines only, by id, or `unallocated` for the lines no member of the
          axis tags. Omitted, a statement returns one column per member, then Unallocated, then Total, for the current
          window.
  """

  type_: str
  member_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    type_ = self.type_

    member_id: None | str | Unset
    if isinstance(self.member_id, Unset):
      member_id = UNSET
    else:
      member_id = self.member_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "type": type_,
      }
    )
    if member_id is not UNSET:
      field_dict["member_id"] = member_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    type_ = d.pop("type")

    def _parse_member_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    member_id = _parse_member_id(d.pop("member_id", UNSET))

    statement_dimension = cls(
      type_=type_,
      member_id=member_id,
    )

    statement_dimension.additional_properties = d
    return statement_dimension

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
