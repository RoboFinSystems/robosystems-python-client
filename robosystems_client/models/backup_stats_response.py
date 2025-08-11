from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.backup_stats_response_backup_formats import (
    BackupStatsResponseBackupFormats,
  )


T = TypeVar("T", bound="BackupStatsResponse")


@_attrs_define
class BackupStatsResponse:
  """Response model for backup statistics.

  Attributes:
      graph_id (str):
      total_backups (int):
      successful_backups (int):
      failed_backups (int):
      success_rate (float):
      total_original_size_bytes (int):
      total_compressed_size_bytes (int):
      storage_saved_bytes (int):
      average_compression_ratio (float):
      latest_backup_date (Union[None, str]):
      backup_formats (BackupStatsResponseBackupFormats):
  """

  graph_id: str
  total_backups: int
  successful_backups: int
  failed_backups: int
  success_rate: float
  total_original_size_bytes: int
  total_compressed_size_bytes: int
  storage_saved_bytes: int
  average_compression_ratio: float
  latest_backup_date: Union[None, str]
  backup_formats: "BackupStatsResponseBackupFormats"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    total_backups = self.total_backups

    successful_backups = self.successful_backups

    failed_backups = self.failed_backups

    success_rate = self.success_rate

    total_original_size_bytes = self.total_original_size_bytes

    total_compressed_size_bytes = self.total_compressed_size_bytes

    storage_saved_bytes = self.storage_saved_bytes

    average_compression_ratio = self.average_compression_ratio

    latest_backup_date: Union[None, str]
    latest_backup_date = self.latest_backup_date

    backup_formats = self.backup_formats.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "total_backups": total_backups,
        "successful_backups": successful_backups,
        "failed_backups": failed_backups,
        "success_rate": success_rate,
        "total_original_size_bytes": total_original_size_bytes,
        "total_compressed_size_bytes": total_compressed_size_bytes,
        "storage_saved_bytes": storage_saved_bytes,
        "average_compression_ratio": average_compression_ratio,
        "latest_backup_date": latest_backup_date,
        "backup_formats": backup_formats,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.backup_stats_response_backup_formats import (
      BackupStatsResponseBackupFormats,
    )

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    total_backups = d.pop("total_backups")

    successful_backups = d.pop("successful_backups")

    failed_backups = d.pop("failed_backups")

    success_rate = d.pop("success_rate")

    total_original_size_bytes = d.pop("total_original_size_bytes")

    total_compressed_size_bytes = d.pop("total_compressed_size_bytes")

    storage_saved_bytes = d.pop("storage_saved_bytes")

    average_compression_ratio = d.pop("average_compression_ratio")

    def _parse_latest_backup_date(data: object) -> Union[None, str]:
      if data is None:
        return data
      return cast(Union[None, str], data)

    latest_backup_date = _parse_latest_backup_date(d.pop("latest_backup_date"))

    backup_formats = BackupStatsResponseBackupFormats.from_dict(d.pop("backup_formats"))

    backup_stats_response = cls(
      graph_id=graph_id,
      total_backups=total_backups,
      successful_backups=successful_backups,
      failed_backups=failed_backups,
      success_rate=success_rate,
      total_original_size_bytes=total_original_size_bytes,
      total_compressed_size_bytes=total_compressed_size_bytes,
      storage_saved_bytes=storage_saved_bytes,
      average_compression_ratio=average_compression_ratio,
      latest_backup_date=latest_backup_date,
      backup_formats=backup_formats,
    )

    backup_stats_response.additional_properties = d
    return backup_stats_response

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
