from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupCreateRequest")


@_attrs_define
class BackupCreateRequest:
  """Request model for creating a backup.

  Attributes:
      backup_format (Union[Unset, str]): Backup format - only 'full_dump' is supported (complete .kuzu database file)
          Default: 'full_dump'.
      backup_type (Union[Unset, str]): Backup type - only 'full' is supported Default: 'full'.
      retention_days (Union[Unset, int]): Retention period in days Default: 90.
      compression (Union[Unset, bool]): Enable compression (always enabled for optimal storage) Default: True.
      encryption (Union[Unset, bool]): Enable encryption (encrypted backups cannot be downloaded) Default: False.
      schedule (Union[None, Unset, str]): Optional cron schedule for automated backups
  """

  backup_format: Union[Unset, str] = "full_dump"
  backup_type: Union[Unset, str] = "full"
  retention_days: Union[Unset, int] = 90
  compression: Union[Unset, bool] = True
  encryption: Union[Unset, bool] = False
  schedule: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    backup_format = self.backup_format

    backup_type = self.backup_type

    retention_days = self.retention_days

    compression = self.compression

    encryption = self.encryption

    schedule: Union[None, Unset, str]
    if isinstance(self.schedule, Unset):
      schedule = UNSET
    else:
      schedule = self.schedule

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if backup_format is not UNSET:
      field_dict["backup_format"] = backup_format
    if backup_type is not UNSET:
      field_dict["backup_type"] = backup_type
    if retention_days is not UNSET:
      field_dict["retention_days"] = retention_days
    if compression is not UNSET:
      field_dict["compression"] = compression
    if encryption is not UNSET:
      field_dict["encryption"] = encryption
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

    encryption = d.pop("encryption", UNSET)

    def _parse_schedule(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    schedule = _parse_schedule(d.pop("schedule", UNSET))

    backup_create_request = cls(
      backup_format=backup_format,
      backup_type=backup_type,
      retention_days=retention_days,
      compression=compression,
      encryption=encryption,
      schedule=schedule,
    )

    backup_create_request.additional_properties = d
    return backup_create_request

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
