from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.credit_summary import CreditSummary
  from ..models.graph_usage_response_recent_events_item import (
    GraphUsageResponseRecentEventsItem,
  )
  from ..models.performance_insights import PerformanceInsights
  from ..models.storage_summary import StorageSummary


T = TypeVar("T", bound="GraphUsageResponse")


@_attrs_define
class GraphUsageResponse:
  """Response model for graph usage statistics.

  Attributes:
      graph_id (str): Graph database identifier
      time_range (str): Time range for usage data
      timestamp (str): Usage collection timestamp
      storage_summary (None | StorageSummary | Unset): Storage usage summary
      credit_summary (CreditSummary | None | Unset): Credit consumption summary
      performance_insights (None | PerformanceInsights | Unset): Performance analytics
      recent_events (list[GraphUsageResponseRecentEventsItem] | Unset): Recent usage events
  """

  graph_id: str
  time_range: str
  timestamp: str
  storage_summary: None | StorageSummary | Unset = UNSET
  credit_summary: CreditSummary | None | Unset = UNSET
  performance_insights: None | PerformanceInsights | Unset = UNSET
  recent_events: list[GraphUsageResponseRecentEventsItem] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.credit_summary import CreditSummary
    from ..models.performance_insights import PerformanceInsights
    from ..models.storage_summary import StorageSummary

    graph_id = self.graph_id

    time_range = self.time_range

    timestamp = self.timestamp

    storage_summary: dict[str, Any] | None | Unset
    if isinstance(self.storage_summary, Unset):
      storage_summary = UNSET
    elif isinstance(self.storage_summary, StorageSummary):
      storage_summary = self.storage_summary.to_dict()
    else:
      storage_summary = self.storage_summary

    credit_summary: dict[str, Any] | None | Unset
    if isinstance(self.credit_summary, Unset):
      credit_summary = UNSET
    elif isinstance(self.credit_summary, CreditSummary):
      credit_summary = self.credit_summary.to_dict()
    else:
      credit_summary = self.credit_summary

    performance_insights: dict[str, Any] | None | Unset
    if isinstance(self.performance_insights, Unset):
      performance_insights = UNSET
    elif isinstance(self.performance_insights, PerformanceInsights):
      performance_insights = self.performance_insights.to_dict()
    else:
      performance_insights = self.performance_insights

    recent_events: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.recent_events, Unset):
      recent_events = []
      for recent_events_item_data in self.recent_events:
        recent_events_item = recent_events_item_data.to_dict()
        recent_events.append(recent_events_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "time_range": time_range,
        "timestamp": timestamp,
      }
    )
    if storage_summary is not UNSET:
      field_dict["storage_summary"] = storage_summary
    if credit_summary is not UNSET:
      field_dict["credit_summary"] = credit_summary
    if performance_insights is not UNSET:
      field_dict["performance_insights"] = performance_insights
    if recent_events is not UNSET:
      field_dict["recent_events"] = recent_events

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.credit_summary import CreditSummary
    from ..models.graph_usage_response_recent_events_item import (
      GraphUsageResponseRecentEventsItem,
    )
    from ..models.performance_insights import PerformanceInsights
    from ..models.storage_summary import StorageSummary

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    time_range = d.pop("time_range")

    timestamp = d.pop("timestamp")

    def _parse_storage_summary(data: object) -> None | StorageSummary | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        storage_summary_type_0 = StorageSummary.from_dict(data)

        return storage_summary_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | StorageSummary | Unset, data)

    storage_summary = _parse_storage_summary(d.pop("storage_summary", UNSET))

    def _parse_credit_summary(data: object) -> CreditSummary | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        credit_summary_type_0 = CreditSummary.from_dict(data)

        return credit_summary_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(CreditSummary | None | Unset, data)

    credit_summary = _parse_credit_summary(d.pop("credit_summary", UNSET))

    def _parse_performance_insights(data: object) -> None | PerformanceInsights | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        performance_insights_type_0 = PerformanceInsights.from_dict(data)

        return performance_insights_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | PerformanceInsights | Unset, data)

    performance_insights = _parse_performance_insights(
      d.pop("performance_insights", UNSET)
    )

    _recent_events = d.pop("recent_events", UNSET)
    recent_events: list[GraphUsageResponseRecentEventsItem] | Unset = UNSET
    if _recent_events is not UNSET:
      recent_events = []
      for recent_events_item_data in _recent_events:
        recent_events_item = GraphUsageResponseRecentEventsItem.from_dict(
          recent_events_item_data
        )

        recent_events.append(recent_events_item)

    graph_usage_response = cls(
      graph_id=graph_id,
      time_range=time_range,
      timestamp=timestamp,
      storage_summary=storage_summary,
      credit_summary=credit_summary,
      performance_insights=performance_insights,
      recent_events=recent_events,
    )

    graph_usage_response.additional_properties = d
    return graph_usage_response

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
