from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupExportRequest")


@_attrs_define
class BackupExportRequest:
  """Request model for exporting a backup.

  Attributes:
      backup_id (str): ID of backup to export
      export_format (Union[Unset, str]): Export format - only 'original' is supported (compressed .kuzu file) Default:
          'original'.
  """

  backup_id: str
  export_format: Union[Unset, str] = "original"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    backup_id = self.backup_id

    export_format = self.export_format

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "backup_id": backup_id,
      }
    )
    if export_format is not UNSET:
      field_dict["export_format"] = export_format

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    backup_id = d.pop("backup_id")

    export_format = d.pop("export_format", UNSET)

    backup_export_request = cls(
      backup_id=backup_id,
      export_format=export_format,
    )

    backup_export_request.additional_properties = d
    return backup_export_request

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
