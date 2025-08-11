from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
      encryption_enabled (bool):
      compression_enabled (bool):
      allow_export (bool):
      created_at (str):
      completed_at (Union[None, str]):
      expires_at (Union[None, str]):
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
  encryption_enabled: bool
  compression_enabled: bool
  allow_export: bool
  created_at: str
  completed_at: Union[None, str]
  expires_at: Union[None, str]
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

    encryption_enabled = self.encryption_enabled

    compression_enabled = self.compression_enabled

    allow_export = self.allow_export

    created_at = self.created_at

    completed_at: Union[None, str]
    completed_at = self.completed_at

    expires_at: Union[None, str]
    expires_at = self.expires_at

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
        "encryption_enabled": encryption_enabled,
        "compression_enabled": compression_enabled,
        "allow_export": allow_export,
        "created_at": created_at,
        "completed_at": completed_at,
        "expires_at": expires_at,
      }
    )

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

    encryption_enabled = d.pop("encryption_enabled")

    compression_enabled = d.pop("compression_enabled")

    allow_export = d.pop("allow_export")

    created_at = d.pop("created_at")

    def _parse_completed_at(data: object) -> Union[None, str]:
      if data is None:
        return data
      return cast(Union[None, str], data)

    completed_at = _parse_completed_at(d.pop("completed_at"))

    def _parse_expires_at(data: object) -> Union[None, str]:
      if data is None:
        return data
      return cast(Union[None, str], data)

    expires_at = _parse_expires_at(d.pop("expires_at"))

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
      encryption_enabled=encryption_enabled,
      compression_enabled=compression_enabled,
      allow_export=allow_export,
      created_at=created_at,
      completed_at=completed_at,
      expires_at=expires_at,
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
