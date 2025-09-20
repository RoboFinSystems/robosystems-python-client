from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseHealthResponse")


@_attrs_define
class DatabaseHealthResponse:
  """Response model for database health check.

  Attributes:
      graph_id (str): Graph database identifier
      status (str): Overall health status
      connection_status (str): Database connection status
      uptime_seconds (float): Database uptime in seconds
      query_count_24h (int): Number of queries executed in last 24 hours
      avg_query_time_ms (float): Average query execution time in milliseconds
      error_rate_24h (float): Error rate in last 24 hours (percentage)
      last_query_time (Union[None, Unset, str]): Timestamp of last query execution
      memory_usage_mb (Union[None, Unset, float]): Memory usage in MB
      storage_usage_mb (Union[None, Unset, float]): Storage usage in MB
      alerts (Union[Unset, list[str]]): Active alerts or warnings
  """

  graph_id: str
  status: str
  connection_status: str
  uptime_seconds: float
  query_count_24h: int
  avg_query_time_ms: float
  error_rate_24h: float
  last_query_time: Union[None, Unset, str] = UNSET
  memory_usage_mb: Union[None, Unset, float] = UNSET
  storage_usage_mb: Union[None, Unset, float] = UNSET
  alerts: Union[Unset, list[str]] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    status = self.status

    connection_status = self.connection_status

    uptime_seconds = self.uptime_seconds

    query_count_24h = self.query_count_24h

    avg_query_time_ms = self.avg_query_time_ms

    error_rate_24h = self.error_rate_24h

    last_query_time: Union[None, Unset, str]
    if isinstance(self.last_query_time, Unset):
      last_query_time = UNSET
    else:
      last_query_time = self.last_query_time

    memory_usage_mb: Union[None, Unset, float]
    if isinstance(self.memory_usage_mb, Unset):
      memory_usage_mb = UNSET
    else:
      memory_usage_mb = self.memory_usage_mb

    storage_usage_mb: Union[None, Unset, float]
    if isinstance(self.storage_usage_mb, Unset):
      storage_usage_mb = UNSET
    else:
      storage_usage_mb = self.storage_usage_mb

    alerts: Union[Unset, list[str]] = UNSET
    if not isinstance(self.alerts, Unset):
      alerts = self.alerts

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "status": status,
        "connection_status": connection_status,
        "uptime_seconds": uptime_seconds,
        "query_count_24h": query_count_24h,
        "avg_query_time_ms": avg_query_time_ms,
        "error_rate_24h": error_rate_24h,
      }
    )
    if last_query_time is not UNSET:
      field_dict["last_query_time"] = last_query_time
    if memory_usage_mb is not UNSET:
      field_dict["memory_usage_mb"] = memory_usage_mb
    if storage_usage_mb is not UNSET:
      field_dict["storage_usage_mb"] = storage_usage_mb
    if alerts is not UNSET:
      field_dict["alerts"] = alerts

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    status = d.pop("status")

    connection_status = d.pop("connection_status")

    uptime_seconds = d.pop("uptime_seconds")

    query_count_24h = d.pop("query_count_24h")

    avg_query_time_ms = d.pop("avg_query_time_ms")

    error_rate_24h = d.pop("error_rate_24h")

    def _parse_last_query_time(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    last_query_time = _parse_last_query_time(d.pop("last_query_time", UNSET))

    def _parse_memory_usage_mb(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    memory_usage_mb = _parse_memory_usage_mb(d.pop("memory_usage_mb", UNSET))

    def _parse_storage_usage_mb(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    storage_usage_mb = _parse_storage_usage_mb(d.pop("storage_usage_mb", UNSET))

    alerts = cast(list[str], d.pop("alerts", UNSET))

    database_health_response = cls(
      graph_id=graph_id,
      status=status,
      connection_status=connection_status,
      uptime_seconds=uptime_seconds,
      query_count_24h=query_count_24h,
      avg_query_time_ms=avg_query_time_ms,
      error_rate_24h=error_rate_24h,
      last_query_time=last_query_time,
      memory_usage_mb=memory_usage_mb,
      storage_usage_mb=storage_usage_mb,
      alerts=alerts,
    )

    database_health_response.additional_properties = d
    return database_health_response

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
