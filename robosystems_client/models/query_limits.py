from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueryLimits")


@_attrs_define
class QueryLimits:
  """Query operation limits.

  Attributes:
      max_timeout_seconds (int): Maximum query timeout in seconds
      chunk_size (int): Maximum chunk size for result streaming
      max_rows_per_query (int): Maximum rows returned per query
      concurrent_queries (int): Maximum concurrent queries allowed
  """

  max_timeout_seconds: int
  chunk_size: int
  max_rows_per_query: int
  concurrent_queries: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    max_timeout_seconds = self.max_timeout_seconds

    chunk_size = self.chunk_size

    max_rows_per_query = self.max_rows_per_query

    concurrent_queries = self.concurrent_queries

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "max_timeout_seconds": max_timeout_seconds,
        "chunk_size": chunk_size,
        "max_rows_per_query": max_rows_per_query,
        "concurrent_queries": concurrent_queries,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    max_timeout_seconds = d.pop("max_timeout_seconds")

    chunk_size = d.pop("chunk_size")

    max_rows_per_query = d.pop("max_rows_per_query")

    concurrent_queries = d.pop("concurrent_queries")

    query_limits = cls(
      max_timeout_seconds=max_timeout_seconds,
      chunk_size=chunk_size,
      max_rows_per_query=max_rows_per_query,
      concurrent_queries=concurrent_queries,
    )

    query_limits.additional_properties = d
    return query_limits

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
