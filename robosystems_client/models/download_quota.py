from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DownloadQuota")


@_attrs_define
class DownloadQuota:
  """Download quota information for shared repository backups.

  Attributes:
      limit_per_day (int): Maximum downloads allowed per day
      used_today (int): Number of downloads used today
      remaining (int): Downloads remaining today
      resets_at (datetime.datetime): When the daily limit resets (UTC)
  """

  limit_per_day: int
  used_today: int
  remaining: int
  resets_at: datetime.datetime
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    limit_per_day = self.limit_per_day

    used_today = self.used_today

    remaining = self.remaining

    resets_at = self.resets_at.isoformat()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "limit_per_day": limit_per_day,
        "used_today": used_today,
        "remaining": remaining,
        "resets_at": resets_at,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    limit_per_day = d.pop("limit_per_day")

    used_today = d.pop("used_today")

    remaining = d.pop("remaining")

    resets_at = isoparse(d.pop("resets_at"))

    download_quota = cls(
      limit_per_day=limit_per_day,
      used_today=used_today,
      remaining=remaining,
      resets_at=resets_at,
    )

    download_quota.additional_properties = d
    return download_quota

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
