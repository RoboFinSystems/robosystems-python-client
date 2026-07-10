from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryRecallRequest")


@_attrs_define
class MemoryRecallRequest:
  """Body for recall (ranked semantic search over memory).

  Attributes:
      query (str): Recall query
      k (int | Unset): Max results to return Default: 10.
      memory_type (None | str | Unset): Filter by memory type
      source (None | str | Unset): Filter by source
  """

  query: str
  k: int | Unset = 10
  memory_type: None | str | Unset = UNSET
  source: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    query = self.query

    k = self.k

    memory_type: None | str | Unset
    if isinstance(self.memory_type, Unset):
      memory_type = UNSET
    else:
      memory_type = self.memory_type

    source: None | str | Unset
    if isinstance(self.source, Unset):
      source = UNSET
    else:
      source = self.source

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "query": query,
      }
    )
    if k is not UNSET:
      field_dict["k"] = k
    if memory_type is not UNSET:
      field_dict["memory_type"] = memory_type
    if source is not UNSET:
      field_dict["source"] = source

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    query = d.pop("query")

    k = d.pop("k", UNSET)

    def _parse_memory_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    memory_type = _parse_memory_type(d.pop("memory_type", UNSET))

    def _parse_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source = _parse_source(d.pop("source", UNSET))

    memory_recall_request = cls(
      query=query,
      k=k,
      memory_type=memory_type,
      source=source,
    )

    memory_recall_request.additional_properties = d
    return memory_recall_request

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
