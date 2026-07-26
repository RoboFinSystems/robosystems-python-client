from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GraphMetricsResponseStorage")


@_attrs_define
class GraphMetricsResponseStorage:
  """Measured on-disk storage: total_bytes/kb/mb/gb plus itemized `items` (graph, memory, subgraph, vectors, staging).
  Carries `error` instead if the instance could not be reached — the fields are absent rather than estimated.

  """

  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_metrics_response_storage = cls()

    graph_metrics_response_storage.additional_properties = d
    return graph_metrics_response_storage

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
