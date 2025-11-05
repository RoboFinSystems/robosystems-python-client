from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GraphTierBackup")


@_attrs_define
class GraphTierBackup:
  """Backup configuration for a tier.

  Attributes:
      max_backup_size_gb (int): Maximum backup size in GB
      backup_retention_days (int): Backup retention period in days
      max_backups_per_day (int): Maximum backups per day
  """

  max_backup_size_gb: int
  backup_retention_days: int
  max_backups_per_day: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    max_backup_size_gb = self.max_backup_size_gb

    backup_retention_days = self.backup_retention_days

    max_backups_per_day = self.max_backups_per_day

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "max_backup_size_gb": max_backup_size_gb,
        "backup_retention_days": backup_retention_days,
        "max_backups_per_day": max_backups_per_day,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    max_backup_size_gb = d.pop("max_backup_size_gb")

    backup_retention_days = d.pop("backup_retention_days")

    max_backups_per_day = d.pop("max_backups_per_day")

    graph_tier_backup = cls(
      max_backup_size_gb=max_backup_size_gb,
      backup_retention_days=backup_retention_days,
      max_backups_per_day=max_backups_per_day,
    )

    graph_tier_backup.additional_properties = d
    return graph_tier_backup

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
