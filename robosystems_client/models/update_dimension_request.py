from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDimensionRequest")


@_attrs_define
class UpdateDimensionRequest:
  """Rename or retire a member. Members are never deleted: lines reference
  them.

      Attributes:
          dimension_id (str): The member to change.
          name (None | str | Unset): The new label. Refused on a synced member, whose name follows its source.
          is_active (bool | None | Unset): False retires the member: lines that carry it keep it, and it can no longer be
              put on new ones. True brings it back.
  """

  dimension_id: str
  name: None | str | Unset = UNSET
  is_active: bool | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    dimension_id = self.dimension_id

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    is_active: bool | None | Unset
    if isinstance(self.is_active, Unset):
      is_active = UNSET
    else:
      is_active = self.is_active

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "dimension_id": dimension_id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if is_active is not UNSET:
      field_dict["is_active"] = is_active

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    dimension_id = d.pop("dimension_id")

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_is_active(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    is_active = _parse_is_active(d.pop("is_active", UNSET))

    update_dimension_request = cls(
      dimension_id=dimension_id,
      name=name,
      is_active=is_active,
    )

    update_dimension_request.additional_properties = d
    return update_dimension_request

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
