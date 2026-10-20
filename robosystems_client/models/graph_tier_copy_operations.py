from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GraphTierCopyOperations")


@_attrs_define
class GraphTierCopyOperations:
  """File upload limits for a tier.

  Attributes:
      max_file_size_gb (float): Maximum upload file size in GB
  """

  max_file_size_gb: float
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    max_file_size_gb = self.max_file_size_gb

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "max_file_size_gb": max_file_size_gb,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    max_file_size_gb = d.pop("max_file_size_gb")

    graph_tier_copy_operations = cls(
      max_file_size_gb=max_file_size_gb,
    )

    graph_tier_copy_operations.additional_properties = d
    return graph_tier_copy_operations

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
