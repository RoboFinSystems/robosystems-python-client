from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileLayerStatus")


@_attrs_define
class FileLayerStatus:
  """
  Attributes:
      status (str): Layer status
      timestamp (None | str | Unset): Status timestamp
      row_count (int | None | Unset): Row count (if available)
      size_bytes (int | None | Unset): Size in bytes (S3 layer only)
  """

  status: str
  timestamp: None | str | Unset = UNSET
  row_count: int | None | Unset = UNSET
  size_bytes: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    status = self.status

    timestamp: None | str | Unset
    if isinstance(self.timestamp, Unset):
      timestamp = UNSET
    else:
      timestamp = self.timestamp

    row_count: int | None | Unset
    if isinstance(self.row_count, Unset):
      row_count = UNSET
    else:
      row_count = self.row_count

    size_bytes: int | None | Unset
    if isinstance(self.size_bytes, Unset):
      size_bytes = UNSET
    else:
      size_bytes = self.size_bytes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "status": status,
      }
    )
    if timestamp is not UNSET:
      field_dict["timestamp"] = timestamp
    if row_count is not UNSET:
      field_dict["row_count"] = row_count
    if size_bytes is not UNSET:
      field_dict["size_bytes"] = size_bytes

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    status = d.pop("status")

    def _parse_timestamp(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

    def _parse_row_count(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    row_count = _parse_row_count(d.pop("row_count", UNSET))

    def _parse_size_bytes(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    size_bytes = _parse_size_bytes(d.pop("size_bytes", UNSET))

    file_layer_status = cls(
      status=status,
      timestamp=timestamp,
      row_count=row_count,
      size_bytes=size_bytes,
    )

    file_layer_status.additional_properties = d
    return file_layer_status

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
