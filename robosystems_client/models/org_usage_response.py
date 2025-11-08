import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
  from ..models.org_usage_response_daily_trend_item import (
    OrgUsageResponseDailyTrendItem,
  )
  from ..models.org_usage_response_graph_details_item import (
    OrgUsageResponseGraphDetailsItem,
  )
  from ..models.org_usage_summary import OrgUsageSummary


T = TypeVar("T", bound="OrgUsageResponse")


@_attrs_define
class OrgUsageResponse:
  """Organization usage response.

  Attributes:
      org_id (str):
      period_days (int):
      start_date (datetime.datetime):
      end_date (datetime.datetime):
      summary (OrgUsageSummary): Organization usage summary.
      graph_details (list['OrgUsageResponseGraphDetailsItem']):
      daily_trend (list['OrgUsageResponseDailyTrendItem']):
  """

  org_id: str
  period_days: int
  start_date: datetime.datetime
  end_date: datetime.datetime
  summary: "OrgUsageSummary"
  graph_details: list["OrgUsageResponseGraphDetailsItem"]
  daily_trend: list["OrgUsageResponseDailyTrendItem"]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    org_id = self.org_id

    period_days = self.period_days

    start_date = self.start_date.isoformat()

    end_date = self.end_date.isoformat()

    summary = self.summary.to_dict()

    graph_details = []
    for graph_details_item_data in self.graph_details:
      graph_details_item = graph_details_item_data.to_dict()
      graph_details.append(graph_details_item)

    daily_trend = []
    for daily_trend_item_data in self.daily_trend:
      daily_trend_item = daily_trend_item_data.to_dict()
      daily_trend.append(daily_trend_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "org_id": org_id,
        "period_days": period_days,
        "start_date": start_date,
        "end_date": end_date,
        "summary": summary,
        "graph_details": graph_details,
        "daily_trend": daily_trend,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.org_usage_response_daily_trend_item import (
      OrgUsageResponseDailyTrendItem,
    )
    from ..models.org_usage_response_graph_details_item import (
      OrgUsageResponseGraphDetailsItem,
    )
    from ..models.org_usage_summary import OrgUsageSummary

    d = dict(src_dict)
    org_id = d.pop("org_id")

    period_days = d.pop("period_days")

    start_date = isoparse(d.pop("start_date"))

    end_date = isoparse(d.pop("end_date"))

    summary = OrgUsageSummary.from_dict(d.pop("summary"))

    graph_details = []
    _graph_details = d.pop("graph_details")
    for graph_details_item_data in _graph_details:
      graph_details_item = OrgUsageResponseGraphDetailsItem.from_dict(
        graph_details_item_data
      )

      graph_details.append(graph_details_item)

    daily_trend = []
    _daily_trend = d.pop("daily_trend")
    for daily_trend_item_data in _daily_trend:
      daily_trend_item = OrgUsageResponseDailyTrendItem.from_dict(daily_trend_item_data)

      daily_trend.append(daily_trend_item)

    org_usage_response = cls(
      org_id=org_id,
      period_days=period_days,
      start_date=start_date,
      end_date=end_date,
      summary=summary,
      graph_details=graph_details,
      daily_trend=daily_trend,
    )

    org_usage_response.additional_properties = d
    return org_usage_response

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
