from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewAxisConfig")


@_attrs_define
class ViewAxisConfig:
  """Scoping configuration for one aspect of the fact query.

  Filtering only. Ordering and labelling are presentation concerns and
  belong to the consumer that arranges the facts into a table.

      Attributes:
          type_ (str): Axis type: 'element', 'period', 'entity'
          include_null_dimension (bool | Unset): Include facts where this aspect is absent (default: false) Default:
              False.
          selected_members (list[str] | None | Unset): Specific members to include (e.g., ['2024-12-31', '2023-12-31'])
  """

  type_: str
  include_null_dimension: bool | Unset = False
  selected_members: list[str] | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    type_ = self.type_

    include_null_dimension = self.include_null_dimension

    selected_members: list[str] | None | Unset
    if isinstance(self.selected_members, Unset):
      selected_members = UNSET
    elif isinstance(self.selected_members, list):
      selected_members = self.selected_members

    else:
      selected_members = self.selected_members

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "type": type_,
      }
    )
    if include_null_dimension is not UNSET:
      field_dict["include_null_dimension"] = include_null_dimension
    if selected_members is not UNSET:
      field_dict["selected_members"] = selected_members

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    type_ = d.pop("type")

    include_null_dimension = d.pop("include_null_dimension", UNSET)

    def _parse_selected_members(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        selected_members_type_0 = cast(list[str], data)

        return selected_members_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    selected_members = _parse_selected_members(d.pop("selected_members", UNSET))

    view_axis_config = cls(
      type_=type_,
      include_null_dimension=include_null_dimension,
      selected_members=selected_members,
    )

    view_axis_config.additional_properties = d
    return view_axis_config

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
