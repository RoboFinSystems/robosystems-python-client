from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
      total_api_calls (int):
      daily_avg_credits (float):
      daily_avg_api_calls (float):
      projected_monthly_credits (float):
      projected_monthly_api_calls (int):
      credits_limit (Union[None, int]):
      api_calls_limit (Union[None, int]):
      storage_limit_gb (Union[None, int]):
  """

  total_credits_used: float
  total_ai_operations: int
  total_storage_gb: float
  total_api_calls: int
  daily_avg_credits: float
  daily_avg_api_calls: float
  projected_monthly_credits: float
  projected_monthly_api_calls: int
  credits_limit: Union[None, int]
  api_calls_limit: Union[None, int]
  storage_limit_gb: Union[None, int]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    total_credits_used = self.total_credits_used

    total_ai_operations = self.total_ai_operations

    total_storage_gb = self.total_storage_gb

    total_api_calls = self.total_api_calls

    daily_avg_credits = self.daily_avg_credits

    daily_avg_api_calls = self.daily_avg_api_calls

    projected_monthly_credits = self.projected_monthly_credits

    projected_monthly_api_calls = self.projected_monthly_api_calls

    credits_limit: Union[None, int]
    credits_limit = self.credits_limit

    api_calls_limit: Union[None, int]
    api_calls_limit = self.api_calls_limit

    storage_limit_gb: Union[None, int]
    storage_limit_gb = self.storage_limit_gb

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "total_credits_used": total_credits_used,
        "total_ai_operations": total_ai_operations,
        "total_storage_gb": total_storage_gb,
        "total_api_calls": total_api_calls,
        "daily_avg_credits": daily_avg_credits,
        "daily_avg_api_calls": daily_avg_api_calls,
        "projected_monthly_credits": projected_monthly_credits,
        "projected_monthly_api_calls": projected_monthly_api_calls,
        "credits_limit": credits_limit,
        "api_calls_limit": api_calls_limit,
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

    total_api_calls = d.pop("total_api_calls")

    daily_avg_credits = d.pop("daily_avg_credits")

    daily_avg_api_calls = d.pop("daily_avg_api_calls")

    projected_monthly_credits = d.pop("projected_monthly_credits")

    projected_monthly_api_calls = d.pop("projected_monthly_api_calls")

    def _parse_credits_limit(data: object) -> Union[None, int]:
      if data is None:
        return data
      return cast(Union[None, int], data)

    credits_limit = _parse_credits_limit(d.pop("credits_limit"))

    def _parse_api_calls_limit(data: object) -> Union[None, int]:
      if data is None:
        return data
      return cast(Union[None, int], data)

    api_calls_limit = _parse_api_calls_limit(d.pop("api_calls_limit"))

    def _parse_storage_limit_gb(data: object) -> Union[None, int]:
      if data is None:
        return data
      return cast(Union[None, int], data)

    storage_limit_gb = _parse_storage_limit_gb(d.pop("storage_limit_gb"))

    org_usage_summary = cls(
      total_credits_used=total_credits_used,
      total_ai_operations=total_ai_operations,
      total_storage_gb=total_storage_gb,
      total_api_calls=total_api_calls,
      daily_avg_credits=daily_avg_credits,
      daily_avg_api_calls=daily_avg_api_calls,
      projected_monthly_credits=projected_monthly_credits,
      projected_monthly_api_calls=projected_monthly_api_calls,
      credits_limit=credits_limit,
      api_calls_limit=api_calls_limit,
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
