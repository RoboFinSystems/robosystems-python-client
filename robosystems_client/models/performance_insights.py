from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.performance_insights_operation_stats import (
    PerformanceInsightsOperationStats,
  )
  from ..models.performance_insights_slow_queries_item import (
    PerformanceInsightsSlowQueriesItem,
  )


T = TypeVar("T", bound="PerformanceInsights")


@_attrs_define
class PerformanceInsights:
  """Performance analytics.

  Attributes:
      analysis_period_days (int): Analysis period in days
      total_operations (int): Total operations analyzed
      operation_stats (PerformanceInsightsOperationStats): Performance stats by operation type
      slow_queries (list['PerformanceInsightsSlowQueriesItem']): Top slow queries (over 5 seconds)
      performance_score (int): Performance score (0-100)
  """

  analysis_period_days: int
  total_operations: int
  operation_stats: "PerformanceInsightsOperationStats"
  slow_queries: list["PerformanceInsightsSlowQueriesItem"]
  performance_score: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    analysis_period_days = self.analysis_period_days

    total_operations = self.total_operations

    operation_stats = self.operation_stats.to_dict()

    slow_queries = []
    for slow_queries_item_data in self.slow_queries:
      slow_queries_item = slow_queries_item_data.to_dict()
      slow_queries.append(slow_queries_item)

    performance_score = self.performance_score

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "analysis_period_days": analysis_period_days,
        "total_operations": total_operations,
        "operation_stats": operation_stats,
        "slow_queries": slow_queries,
        "performance_score": performance_score,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.performance_insights_operation_stats import (
      PerformanceInsightsOperationStats,
    )
    from ..models.performance_insights_slow_queries_item import (
      PerformanceInsightsSlowQueriesItem,
    )

    d = dict(src_dict)
    analysis_period_days = d.pop("analysis_period_days")

    total_operations = d.pop("total_operations")

    operation_stats = PerformanceInsightsOperationStats.from_dict(
      d.pop("operation_stats")
    )

    slow_queries = []
    _slow_queries = d.pop("slow_queries")
    for slow_queries_item_data in _slow_queries:
      slow_queries_item = PerformanceInsightsSlowQueriesItem.from_dict(
        slow_queries_item_data
      )

      slow_queries.append(slow_queries_item)

    performance_score = d.pop("performance_score")

    performance_insights = cls(
      analysis_period_days=analysis_period_days,
      total_operations=total_operations,
      operation_stats=operation_stats,
      slow_queries=slow_queries,
      performance_score=performance_score,
    )

    performance_insights.additional_properties = d
    return performance_insights

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
