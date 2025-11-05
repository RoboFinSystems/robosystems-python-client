from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BackupDownloadUrlResponse")


@_attrs_define
class BackupDownloadUrlResponse:
  """Response model for backup download URL generation.

  Attributes:
      download_url (str): Pre-signed S3 URL for downloading the backup file
      expires_in (int): URL expiration time in seconds from now
      expires_at (float): Unix timestamp when the URL expires
      backup_id (str): Backup identifier
      graph_id (str): Graph database identifier
  """

  download_url: str
  expires_in: int
  expires_at: float
  backup_id: str
  graph_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    download_url = self.download_url

    expires_in = self.expires_in

    expires_at = self.expires_at

    backup_id = self.backup_id

    graph_id = self.graph_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "download_url": download_url,
        "expires_in": expires_in,
        "expires_at": expires_at,
        "backup_id": backup_id,
        "graph_id": graph_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    download_url = d.pop("download_url")

    expires_in = d.pop("expires_in")

    expires_at = d.pop("expires_at")

    backup_id = d.pop("backup_id")

    graph_id = d.pop("graph_id")

    backup_download_url_response = cls(
      download_url=download_url,
      expires_in=expires_in,
      expires_at=expires_at,
      backup_id=backup_id,
      graph_id=graph_id,
    )

    backup_download_url_response.additional_properties = d
    return backup_download_url_response

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
