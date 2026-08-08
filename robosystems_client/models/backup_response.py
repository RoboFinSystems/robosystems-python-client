from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupResponse")


@_attrs_define
class BackupResponse:
  """Response model for backup information.

  Attributes:
      backup_id (str):
      graph_id (str):
      backup_format (str):
      backup_type (str):
      status (str):
      original_size_bytes (int):
      compressed_size_bytes (int):
      compression_ratio (float):
      node_count (int):
      relationship_count (int):
      backup_duration_seconds (float):
      compression_enabled (bool):
      created_at (str):
      completed_at (None | str):
      expires_at (None | str):
      download_extension (None | str | Unset): Extension the download will carry, and therefore how to unpack it:
          '.lbug.zip' is a ZIP holding the LadybugDB database file, '.lbug.zst' is zstd-compressed (`zstd -d`). Null only
          when the backup has no stored object yet.
  """

  backup_id: str
  graph_id: str
  backup_format: str
  backup_type: str
  status: str
  original_size_bytes: int
  compressed_size_bytes: int
  compression_ratio: float
  node_count: int
  relationship_count: int
  backup_duration_seconds: float
  compression_enabled: bool
  created_at: str
  completed_at: None | str
  expires_at: None | str
  download_extension: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    backup_id = self.backup_id

    graph_id = self.graph_id

    backup_format = self.backup_format

    backup_type = self.backup_type

    status = self.status

    original_size_bytes = self.original_size_bytes

    compressed_size_bytes = self.compressed_size_bytes

    compression_ratio = self.compression_ratio

    node_count = self.node_count

    relationship_count = self.relationship_count

    backup_duration_seconds = self.backup_duration_seconds

    compression_enabled = self.compression_enabled

    created_at = self.created_at

    completed_at: None | str
    completed_at = self.completed_at

    expires_at: None | str
    expires_at = self.expires_at

    download_extension: None | str | Unset
    if isinstance(self.download_extension, Unset):
      download_extension = UNSET
    else:
      download_extension = self.download_extension

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "backup_id": backup_id,
        "graph_id": graph_id,
        "backup_format": backup_format,
        "backup_type": backup_type,
        "status": status,
        "original_size_bytes": original_size_bytes,
        "compressed_size_bytes": compressed_size_bytes,
        "compression_ratio": compression_ratio,
        "node_count": node_count,
        "relationship_count": relationship_count,
        "backup_duration_seconds": backup_duration_seconds,
        "compression_enabled": compression_enabled,
        "created_at": created_at,
        "completed_at": completed_at,
        "expires_at": expires_at,
      }
    )
    if download_extension is not UNSET:
      field_dict["download_extension"] = download_extension

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    backup_id = d.pop("backup_id")

    graph_id = d.pop("graph_id")

    backup_format = d.pop("backup_format")

    backup_type = d.pop("backup_type")

    status = d.pop("status")

    original_size_bytes = d.pop("original_size_bytes")

    compressed_size_bytes = d.pop("compressed_size_bytes")

    compression_ratio = d.pop("compression_ratio")

    node_count = d.pop("node_count")

    relationship_count = d.pop("relationship_count")

    backup_duration_seconds = d.pop("backup_duration_seconds")

    compression_enabled = d.pop("compression_enabled")

    created_at = d.pop("created_at")

    def _parse_completed_at(data: object) -> None | str:
      if data is None:
        return data
      return cast(None | str, data)

    completed_at = _parse_completed_at(d.pop("completed_at"))

    def _parse_expires_at(data: object) -> None | str:
      if data is None:
        return data
      return cast(None | str, data)

    expires_at = _parse_expires_at(d.pop("expires_at"))

    def _parse_download_extension(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    download_extension = _parse_download_extension(d.pop("download_extension", UNSET))

    backup_response = cls(
      backup_id=backup_id,
      graph_id=graph_id,
      backup_format=backup_format,
      backup_type=backup_type,
      status=status,
      original_size_bytes=original_size_bytes,
      compressed_size_bytes=compressed_size_bytes,
      compression_ratio=compression_ratio,
      node_count=node_count,
      relationship_count=relationship_count,
      backup_duration_seconds=backup_duration_seconds,
      compression_enabled=compression_enabled,
      created_at=created_at,
      completed_at=completed_at,
      expires_at=expires_at,
      download_extension=download_extension,
    )

    backup_response.additional_properties = d
    return backup_response

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
