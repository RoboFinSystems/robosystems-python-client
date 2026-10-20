from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupLimits")


@_attrs_define
class BackupLimits:
  """Backup operation limits.

  Attributes:
      backup_retention_days (int): Backup retention period in days
      max_backups_per_day (int): Maximum user-initiated backups per day (-1 for unlimited)
      max_downloads_per_month (int | None | Unset): Backup downloads allowed per user per calendar month (UTC)
  """

  backup_retention_days: int
  max_backups_per_day: int
  max_downloads_per_month: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    backup_retention_days = self.backup_retention_days

    max_backups_per_day = self.max_backups_per_day

    max_downloads_per_month: int | None | Unset
    if isinstance(self.max_downloads_per_month, Unset):
      max_downloads_per_month = UNSET
    else:
      max_downloads_per_month = self.max_downloads_per_month

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "backup_retention_days": backup_retention_days,
        "max_backups_per_day": max_backups_per_day,
      }
    )
    if max_downloads_per_month is not UNSET:
      field_dict["max_downloads_per_month"] = max_downloads_per_month

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    backup_retention_days = d.pop("backup_retention_days")

    max_backups_per_day = d.pop("max_backups_per_day")

    def _parse_max_downloads_per_month(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    max_downloads_per_month = _parse_max_downloads_per_month(
      d.pop("max_downloads_per_month", UNSET)
    )

    backup_limits = cls(
      backup_retention_days=backup_retention_days,
      max_backups_per_day=max_backups_per_day,
      max_downloads_per_month=max_downloads_per_month,
    )

    backup_limits.additional_properties = d
    return backup_limits

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
