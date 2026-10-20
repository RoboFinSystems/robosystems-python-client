from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CopyOperationLimits")


@_attrs_define
class CopyOperationLimits:
  """File upload limits.

  Attributes:
      max_file_size_gb (float): Maximum upload file size in GB
      supported_formats (list[str]): Supported file formats
  """

  max_file_size_gb: float
  supported_formats: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    max_file_size_gb = self.max_file_size_gb

    supported_formats = self.supported_formats

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "max_file_size_gb": max_file_size_gb,
        "supported_formats": supported_formats,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    max_file_size_gb = d.pop("max_file_size_gb")

    supported_formats = cast(list[str], d.pop("supported_formats"))

    copy_operation_limits = cls(
      max_file_size_gb=max_file_size_gb,
      supported_formats=supported_formats,
    )

    copy_operation_limits.additional_properties = d
    return copy_operation_limits

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
