from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupRestoreRequest")


@_attrs_define
class BackupRestoreRequest:
  """Request model for restoring from a backup.

  Attributes:
      create_system_backup (Union[Unset, bool]): Create a system backup of existing database before restore Default:
          True.
      verify_after_restore (Union[Unset, bool]): Verify database integrity after restore Default: True.
  """

  create_system_backup: Union[Unset, bool] = True
  verify_after_restore: Union[Unset, bool] = True
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    create_system_backup = self.create_system_backup

    verify_after_restore = self.verify_after_restore

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if create_system_backup is not UNSET:
      field_dict["create_system_backup"] = create_system_backup
    if verify_after_restore is not UNSET:
      field_dict["verify_after_restore"] = verify_after_restore

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    create_system_backup = d.pop("create_system_backup", UNSET)

    verify_after_restore = d.pop("verify_after_restore", UNSET)

    backup_restore_request = cls(
      create_system_backup=create_system_backup,
      verify_after_restore=verify_after_restore,
    )

    backup_restore_request.additional_properties = d
    return backup_restore_request

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
