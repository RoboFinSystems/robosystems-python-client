from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentLimits")


@_attrs_define
class ContentLimits:
  """Graph content limits (nodes, relationships, rows).

  Attributes:
      max_nodes (int): Maximum nodes allowed
      max_relationships (int): Maximum relationships allowed
      max_rows_per_copy (int): Maximum rows per copy/materialization operation
      max_single_table_rows (int): Maximum rows per staging table
      chunk_size_rows (int): Rows per materialization chunk
      current_nodes (int | None | Unset): Current node count
      current_relationships (int | None | Unset): Current relationship count
      approaching_limits (list[str] | Unset): List of limits being approached (>80%)
  """

  max_nodes: int
  max_relationships: int
  max_rows_per_copy: int
  max_single_table_rows: int
  chunk_size_rows: int
  current_nodes: int | None | Unset = UNSET
  current_relationships: int | None | Unset = UNSET
  approaching_limits: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    max_nodes = self.max_nodes

    max_relationships = self.max_relationships

    max_rows_per_copy = self.max_rows_per_copy

    max_single_table_rows = self.max_single_table_rows

    chunk_size_rows = self.chunk_size_rows

    current_nodes: int | None | Unset
    if isinstance(self.current_nodes, Unset):
      current_nodes = UNSET
    else:
      current_nodes = self.current_nodes

    current_relationships: int | None | Unset
    if isinstance(self.current_relationships, Unset):
      current_relationships = UNSET
    else:
      current_relationships = self.current_relationships

    approaching_limits: list[str] | Unset = UNSET
    if not isinstance(self.approaching_limits, Unset):
      approaching_limits = self.approaching_limits

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "max_nodes": max_nodes,
        "max_relationships": max_relationships,
        "max_rows_per_copy": max_rows_per_copy,
        "max_single_table_rows": max_single_table_rows,
        "chunk_size_rows": chunk_size_rows,
      }
    )
    if current_nodes is not UNSET:
      field_dict["current_nodes"] = current_nodes
    if current_relationships is not UNSET:
      field_dict["current_relationships"] = current_relationships
    if approaching_limits is not UNSET:
      field_dict["approaching_limits"] = approaching_limits

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    max_nodes = d.pop("max_nodes")

    max_relationships = d.pop("max_relationships")

    max_rows_per_copy = d.pop("max_rows_per_copy")

    max_single_table_rows = d.pop("max_single_table_rows")

    chunk_size_rows = d.pop("chunk_size_rows")

    def _parse_current_nodes(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    current_nodes = _parse_current_nodes(d.pop("current_nodes", UNSET))

    def _parse_current_relationships(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    current_relationships = _parse_current_relationships(
      d.pop("current_relationships", UNSET)
    )

    approaching_limits = cast(list[str], d.pop("approaching_limits", UNSET))

    content_limits = cls(
      max_nodes=max_nodes,
      max_relationships=max_relationships,
      max_rows_per_copy=max_rows_per_copy,
      max_single_table_rows=max_single_table_rows,
      chunk_size_rows=chunk_size_rows,
      current_nodes=current_nodes,
      current_relationships=current_relationships,
      approaching_limits=approaching_limits,
    )

    content_limits.additional_properties = d
    return content_limits

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
