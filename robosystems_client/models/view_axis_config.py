from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.view_axis_config_element_labels_type_0 import (
    ViewAxisConfigElementLabelsType0,
  )
  from ..models.view_axis_config_member_labels_type_0 import (
    ViewAxisConfigMemberLabelsType0,
  )


T = TypeVar("T", bound="ViewAxisConfig")


@_attrs_define
class ViewAxisConfig:
  """
  Attributes:
      type_ (str): Axis type: 'element', 'period', 'dimension', 'entity'
      dimension_axis (None | str | Unset): Dimension axis name for dimension-type axes
      include_null_dimension (bool | Unset): Include facts where this dimension is NULL (default: false) Default:
          False.
      selected_members (list[str] | None | Unset): Specific members to include (e.g., ['2024-12-31', '2023-12-31'])
      member_order (list[str] | None | Unset): Explicit ordering of members (overrides default sort)
      member_labels (None | Unset | ViewAxisConfigMemberLabelsType0): Custom labels for members (e.g., {'2024-12-31':
          'Current Year'})
      element_order (list[str] | None | Unset): Element ordering for hierarchy display (e.g., ['us-gaap:Assets', 'us-
          gaap:Cash', ...])
      element_labels (None | Unset | ViewAxisConfigElementLabelsType0): Custom labels for elements (e.g., {'us-
          gaap:Cash': 'Cash and Cash Equivalents'})
  """

  type_: str
  dimension_axis: None | str | Unset = UNSET
  include_null_dimension: bool | Unset = False
  selected_members: list[str] | None | Unset = UNSET
  member_order: list[str] | None | Unset = UNSET
  member_labels: None | Unset | ViewAxisConfigMemberLabelsType0 = UNSET
  element_order: list[str] | None | Unset = UNSET
  element_labels: None | Unset | ViewAxisConfigElementLabelsType0 = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.view_axis_config_element_labels_type_0 import (
      ViewAxisConfigElementLabelsType0,
    )
    from ..models.view_axis_config_member_labels_type_0 import (
      ViewAxisConfigMemberLabelsType0,
    )

    type_ = self.type_

    dimension_axis: None | str | Unset
    if isinstance(self.dimension_axis, Unset):
      dimension_axis = UNSET
    else:
      dimension_axis = self.dimension_axis

    include_null_dimension = self.include_null_dimension

    selected_members: list[str] | None | Unset
    if isinstance(self.selected_members, Unset):
      selected_members = UNSET
    elif isinstance(self.selected_members, list):
      selected_members = self.selected_members

    else:
      selected_members = self.selected_members

    member_order: list[str] | None | Unset
    if isinstance(self.member_order, Unset):
      member_order = UNSET
    elif isinstance(self.member_order, list):
      member_order = self.member_order

    else:
      member_order = self.member_order

    member_labels: dict[str, Any] | None | Unset
    if isinstance(self.member_labels, Unset):
      member_labels = UNSET
    elif isinstance(self.member_labels, ViewAxisConfigMemberLabelsType0):
      member_labels = self.member_labels.to_dict()
    else:
      member_labels = self.member_labels

    element_order: list[str] | None | Unset
    if isinstance(self.element_order, Unset):
      element_order = UNSET
    elif isinstance(self.element_order, list):
      element_order = self.element_order

    else:
      element_order = self.element_order

    element_labels: dict[str, Any] | None | Unset
    if isinstance(self.element_labels, Unset):
      element_labels = UNSET
    elif isinstance(self.element_labels, ViewAxisConfigElementLabelsType0):
      element_labels = self.element_labels.to_dict()
    else:
      element_labels = self.element_labels

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "type": type_,
      }
    )
    if dimension_axis is not UNSET:
      field_dict["dimension_axis"] = dimension_axis
    if include_null_dimension is not UNSET:
      field_dict["include_null_dimension"] = include_null_dimension
    if selected_members is not UNSET:
      field_dict["selected_members"] = selected_members
    if member_order is not UNSET:
      field_dict["member_order"] = member_order
    if member_labels is not UNSET:
      field_dict["member_labels"] = member_labels
    if element_order is not UNSET:
      field_dict["element_order"] = element_order
    if element_labels is not UNSET:
      field_dict["element_labels"] = element_labels

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.view_axis_config_element_labels_type_0 import (
      ViewAxisConfigElementLabelsType0,
    )
    from ..models.view_axis_config_member_labels_type_0 import (
      ViewAxisConfigMemberLabelsType0,
    )

    d = dict(src_dict)
    type_ = d.pop("type")

    def _parse_dimension_axis(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    dimension_axis = _parse_dimension_axis(d.pop("dimension_axis", UNSET))

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

    def _parse_member_order(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        member_order_type_0 = cast(list[str], data)

        return member_order_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    member_order = _parse_member_order(d.pop("member_order", UNSET))

    def _parse_member_labels(
      data: object,
    ) -> None | Unset | ViewAxisConfigMemberLabelsType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        member_labels_type_0 = ViewAxisConfigMemberLabelsType0.from_dict(data)

        return member_labels_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | ViewAxisConfigMemberLabelsType0, data)

    member_labels = _parse_member_labels(d.pop("member_labels", UNSET))

    def _parse_element_order(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        element_order_type_0 = cast(list[str], data)

        return element_order_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    element_order = _parse_element_order(d.pop("element_order", UNSET))

    def _parse_element_labels(
      data: object,
    ) -> None | Unset | ViewAxisConfigElementLabelsType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        element_labels_type_0 = ViewAxisConfigElementLabelsType0.from_dict(data)

        return element_labels_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | ViewAxisConfigElementLabelsType0, data)

    element_labels = _parse_element_labels(d.pop("element_labels", UNSET))

    view_axis_config = cls(
      type_=type_,
      dimension_axis=dimension_axis,
      include_null_dimension=include_null_dimension,
      selected_members=selected_members,
      member_order=member_order,
      member_labels=member_labels,
      element_order=element_order,
      element_labels=element_labels,
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
