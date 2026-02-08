from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.backup_response import BackupResponse
  from ..models.download_quota import DownloadQuota


T = TypeVar("T", bound="BackupListResponse")


@_attrs_define
class BackupListResponse:
  """Response model for backup list.

  Attributes:
      backups (list[BackupResponse]):
      total_count (int):
      graph_id (str):
      is_shared_repository (bool | Unset): Whether this is a shared repository (limits apply) Default: False.
      download_quota (DownloadQuota | None | Unset): Download quota for shared repositories
  """

  backups: list[BackupResponse]
  total_count: int
  graph_id: str
  is_shared_repository: bool | Unset = False
  download_quota: DownloadQuota | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.download_quota import DownloadQuota

    backups = []
    for backups_item_data in self.backups:
      backups_item = backups_item_data.to_dict()
      backups.append(backups_item)

    total_count = self.total_count

    graph_id = self.graph_id

    is_shared_repository = self.is_shared_repository

    download_quota: dict[str, Any] | None | Unset
    if isinstance(self.download_quota, Unset):
      download_quota = UNSET
    elif isinstance(self.download_quota, DownloadQuota):
      download_quota = self.download_quota.to_dict()
    else:
      download_quota = self.download_quota

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "backups": backups,
        "total_count": total_count,
        "graph_id": graph_id,
      }
    )
    if is_shared_repository is not UNSET:
      field_dict["is_shared_repository"] = is_shared_repository
    if download_quota is not UNSET:
      field_dict["download_quota"] = download_quota

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.backup_response import BackupResponse
    from ..models.download_quota import DownloadQuota

    d = dict(src_dict)
    backups = []
    _backups = d.pop("backups")
    for backups_item_data in _backups:
      backups_item = BackupResponse.from_dict(backups_item_data)

      backups.append(backups_item)

    total_count = d.pop("total_count")

    graph_id = d.pop("graph_id")

    is_shared_repository = d.pop("is_shared_repository", UNSET)

    def _parse_download_quota(data: object) -> DownloadQuota | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        download_quota_type_0 = DownloadQuota.from_dict(data)

        return download_quota_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(DownloadQuota | None | Unset, data)

    download_quota = _parse_download_quota(d.pop("download_quota", UNSET))

    backup_list_response = cls(
      backups=backups,
      total_count=total_count,
      graph_id=graph_id,
      is_shared_repository=is_shared_repository,
      download_quota=download_quota,
    )

    backup_list_response.additional_properties = d
    return backup_list_response

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
