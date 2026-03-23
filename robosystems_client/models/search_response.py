from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.search_hit import SearchHit


T = TypeVar("T", bound="SearchResponse")


@_attrs_define
class SearchResponse:
  """Response model for document search.

  Attributes:
      total (int):
      hits (list[SearchHit]):
      query (str):
      graph_id (str):
  """

  total: int
  hits: list[SearchHit]
  query: str
  graph_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    total = self.total

    hits = []
    for hits_item_data in self.hits:
      hits_item = hits_item_data.to_dict()
      hits.append(hits_item)

    query = self.query

    graph_id = self.graph_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "total": total,
        "hits": hits,
        "query": query,
        "graph_id": graph_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.search_hit import SearchHit

    d = dict(src_dict)
    total = d.pop("total")

    hits = []
    _hits = d.pop("hits")
    for hits_item_data in _hits:
      hits_item = SearchHit.from_dict(hits_item_data)

      hits.append(hits_item)

    query = d.pop("query")

    graph_id = d.pop("graph_id")

    search_response = cls(
      total=total,
      hits=hits,
      query=query,
      graph_id=graph_id,
    )

    search_response.additional_properties = d
    return search_response

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
