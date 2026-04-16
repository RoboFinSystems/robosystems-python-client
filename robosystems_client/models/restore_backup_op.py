from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestoreBackupOp")


@_attrs_define
class RestoreBackupOp:
  """Body for the restore-backup operation.

  Attributes:
      backup_id (str): Backup identifier to restore from
      create_system_backup (bool | Unset): Create a system backup of existing database before restore Default: True.
      verify_after_restore (bool | Unset): Verify database integrity after restore Default: True.
  """

  backup_id: str
  create_system_backup: bool | Unset = True
  verify_after_restore: bool | Unset = True
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    backup_id = self.backup_id

    create_system_backup = self.create_system_backup

    verify_after_restore = self.verify_after_restore

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "backup_id": backup_id,
      }
    )
    if create_system_backup is not UNSET:
      field_dict["create_system_backup"] = create_system_backup
    if verify_after_restore is not UNSET:
      field_dict["verify_after_restore"] = verify_after_restore

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    backup_id = d.pop("backup_id")

    create_system_backup = d.pop("create_system_backup", UNSET)

    verify_after_restore = d.pop("verify_after_restore", UNSET)

    restore_backup_op = cls(
      backup_id=backup_id,
      create_system_backup=create_system_backup,
      verify_after_restore=verify_after_restore,
    )

    restore_backup_op.additional_properties = d
    return restore_backup_op

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
