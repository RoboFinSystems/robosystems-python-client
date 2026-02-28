from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.view_axis_config import ViewAxisConfig


T = TypeVar("T", bound="ViewConfig")


@_attrs_define
class ViewConfig:
  """
  Attributes:
      rows (list[ViewAxisConfig] | Unset): Row axis configuration
      columns (list[ViewAxisConfig] | Unset): Column axis configuration
      values (str | Unset): Field to use for values (default: numeric_value) Default: 'numeric_value'.
      aggregation_function (str | Unset): Aggregation function: sum, average, count Default: 'sum'.
      fill_value (float | Unset): Value to use for missing data Default: 0.0.
  """

  rows: list[ViewAxisConfig] | Unset = UNSET
  columns: list[ViewAxisConfig] | Unset = UNSET
  values: str | Unset = "numeric_value"
  aggregation_function: str | Unset = "sum"
  fill_value: float | Unset = 0.0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    rows: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.rows, Unset):
      rows = []
      for rows_item_data in self.rows:
        rows_item = rows_item_data.to_dict()
        rows.append(rows_item)

    columns: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.columns, Unset):
      columns = []
      for columns_item_data in self.columns:
        columns_item = columns_item_data.to_dict()
        columns.append(columns_item)

    values = self.values

    aggregation_function = self.aggregation_function

    fill_value = self.fill_value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if rows is not UNSET:
      field_dict["rows"] = rows
    if columns is not UNSET:
      field_dict["columns"] = columns
    if values is not UNSET:
      field_dict["values"] = values
    if aggregation_function is not UNSET:
      field_dict["aggregation_function"] = aggregation_function
    if fill_value is not UNSET:
      field_dict["fill_value"] = fill_value

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.view_axis_config import ViewAxisConfig

    d = dict(src_dict)
    _rows = d.pop("rows", UNSET)
    rows: list[ViewAxisConfig] | Unset = UNSET
    if _rows is not UNSET:
      rows = []
      for rows_item_data in _rows:
        rows_item = ViewAxisConfig.from_dict(rows_item_data)

        rows.append(rows_item)

    _columns = d.pop("columns", UNSET)
    columns: list[ViewAxisConfig] | Unset = UNSET
    if _columns is not UNSET:
      columns = []
      for columns_item_data in _columns:
        columns_item = ViewAxisConfig.from_dict(columns_item_data)

        columns.append(columns_item)

    values = d.pop("values", UNSET)

    aggregation_function = d.pop("aggregation_function", UNSET)

    fill_value = d.pop("fill_value", UNSET)

    view_config = cls(
      rows=rows,
      columns=columns,
      values=values,
      aggregation_function=aggregation_function,
      fill_value=fill_value,
    )

    view_config.additional_properties = d
    return view_config

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
