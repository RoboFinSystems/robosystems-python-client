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
      limit_per_month (int): Maximum downloads allowed per month
      used_this_month (int): Number of downloads used this month
      remaining (int): Downloads remaining this month
      resets_at (datetime.datetime): When the monthly limit resets (UTC)
  """

  limit_per_month: int
  used_this_month: int
  remaining: int
  resets_at: datetime.datetime
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    limit_per_month = self.limit_per_month

    used_this_month = self.used_this_month

    remaining = self.remaining

    resets_at = self.resets_at.isoformat()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "limit_per_month": limit_per_month,
        "used_this_month": used_this_month,
        "remaining": remaining,
        "resets_at": resets_at,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    limit_per_month = d.pop("limit_per_month")

    used_this_month = d.pop("used_this_month")

    remaining = d.pop("remaining")

    resets_at = isoparse(d.pop("resets_at"))

    download_quota = cls(
      limit_per_month=limit_per_month,
      used_this_month=used_this_month,
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
