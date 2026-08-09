from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrgUsageSummary")


@_attrs_define
class OrgUsageSummary:
  """Organization usage summary.

  Attributes:
      total_credits_used (float):
      total_ai_operations (int):
      total_storage_gb (float):
      daily_avg_credits (float):
      projected_monthly_credits (float):
      credits_limit (int | None):
      storage_limit_gb (int | None):
  """

  total_credits_used: float
  total_ai_operations: int
  total_storage_gb: float
  daily_avg_credits: float
  projected_monthly_credits: float
  credits_limit: int | None
  storage_limit_gb: int | None
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    total_credits_used = self.total_credits_used

    total_ai_operations = self.total_ai_operations

    total_storage_gb = self.total_storage_gb

    daily_avg_credits = self.daily_avg_credits

    projected_monthly_credits = self.projected_monthly_credits

    credits_limit: int | None
    credits_limit = self.credits_limit

    storage_limit_gb: int | None
    storage_limit_gb = self.storage_limit_gb

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "total_credits_used": total_credits_used,
        "total_ai_operations": total_ai_operations,
        "total_storage_gb": total_storage_gb,
        "daily_avg_credits": daily_avg_credits,
        "projected_monthly_credits": projected_monthly_credits,
        "credits_limit": credits_limit,
        "storage_limit_gb": storage_limit_gb,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    total_credits_used = d.pop("total_credits_used")

    total_ai_operations = d.pop("total_ai_operations")

    total_storage_gb = d.pop("total_storage_gb")

    daily_avg_credits = d.pop("daily_avg_credits")

    projected_monthly_credits = d.pop("projected_monthly_credits")

    def _parse_credits_limit(data: object) -> int | None:
      if data is None:
        return data
      return cast(int | None, data)

    credits_limit = _parse_credits_limit(d.pop("credits_limit"))

    def _parse_storage_limit_gb(data: object) -> int | None:
      if data is None:
        return data
      return cast(int | None, data)

    storage_limit_gb = _parse_storage_limit_gb(d.pop("storage_limit_gb"))

    org_usage_summary = cls(
      total_credits_used=total_credits_used,
      total_ai_operations=total_ai_operations,
      total_storage_gb=total_storage_gb,
      daily_avg_credits=daily_avg_credits,
      projected_monthly_credits=projected_monthly_credits,
      credits_limit=credits_limit,
      storage_limit_gb=storage_limit_gb,
    )

    org_usage_summary.additional_properties = d
    return org_usage_summary

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
