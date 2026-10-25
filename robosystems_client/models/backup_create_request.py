from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupCreateRequest")


@_attrs_define
class BackupCreateRequest:
  """Request model for creating a backup.

  Attributes:
      backup_format (str | Unset): Backup format - only 'full_dump' is supported (complete .lbug database file)
          Default: 'full_dump'.
      backup_type (str | Unset): Backup type - only 'full' is supported Default: 'full'.
      retention_days (int | Unset): Retention period in days, further capped to the graph tier's maximum (7/30/90). 90
          is the hard ceiling: the storage lifecycle expires backup objects then regardless of the requested value.
          Default: 30.
      compression (bool | Unset): Enable compression (always enabled for optimal storage) Default: True.
      schedule (None | str | Unset): Optional cron schedule for automated backups
  """

  backup_format: str | Unset = "full_dump"
  backup_type: str | Unset = "full"
  retention_days: int | Unset = 30
  compression: bool | Unset = True
  schedule: None | str | Unset = UNSET

  def to_dict(self) -> dict[str, Any]:
    backup_format = self.backup_format

    backup_type = self.backup_type

    retention_days = self.retention_days

    compression = self.compression

    schedule: None | str | Unset
    if isinstance(self.schedule, Unset):
      schedule = UNSET
    else:
      schedule = self.schedule

    field_dict: dict[str, Any] = {}

    field_dict.update({})
    if backup_format is not UNSET:
      field_dict["backup_format"] = backup_format
    if backup_type is not UNSET:
      field_dict["backup_type"] = backup_type
    if retention_days is not UNSET:
      field_dict["retention_days"] = retention_days
    if compression is not UNSET:
      field_dict["compression"] = compression
    if schedule is not UNSET:
      field_dict["schedule"] = schedule

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    backup_format = d.pop("backup_format", UNSET)

    backup_type = d.pop("backup_type", UNSET)

    retention_days = d.pop("retention_days", UNSET)

    compression = d.pop("compression", UNSET)

    def _parse_schedule(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    schedule = _parse_schedule(d.pop("schedule", UNSET))

    backup_create_request = cls(
      backup_format=backup_format,
      backup_type=backup_type,
      retention_days=retention_days,
      compression=compression,
      schedule=schedule,
    )

    return backup_create_request
