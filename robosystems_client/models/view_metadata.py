from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.graph_freshness import GraphFreshness


T = TypeVar("T", bound="ViewMetadata")


@_attrs_define
class ViewMetadata:
  """
  Attributes:
      view_id (str): Unique view identifier
      facts_processed (int): Number of facts processed
      construction_time_ms (float): Time to build view in milliseconds
      source (str): Data source type
      period_start (None | str | Unset): Period start date
      period_end (None | str | Unset): Period end date
      truncated (bool | Unset): True when more facts matched than `limit` allowed. The returned facts are the most
          recent by period; narrow the filters or raise `limit` to see the rest. Default: False.
      graph_freshness (GraphFreshness | None | Unset): On a ledger's graph, whether the graph is current with the
          books; null on shared repositories, which are not rebuilt from a ledger.
  """

  view_id: str
  facts_processed: int
  construction_time_ms: float
  source: str
  period_start: None | str | Unset = UNSET
  period_end: None | str | Unset = UNSET
  truncated: bool | Unset = False
  graph_freshness: GraphFreshness | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.graph_freshness import GraphFreshness

    view_id = self.view_id

    facts_processed = self.facts_processed

    construction_time_ms = self.construction_time_ms

    source = self.source

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    else:
      period_start = self.period_start

    period_end: None | str | Unset
    if isinstance(self.period_end, Unset):
      period_end = UNSET
    else:
      period_end = self.period_end

    truncated = self.truncated

    graph_freshness: dict[str, Any] | None | Unset
    if isinstance(self.graph_freshness, Unset):
      graph_freshness = UNSET
    elif isinstance(self.graph_freshness, GraphFreshness):
      graph_freshness = self.graph_freshness.to_dict()
    else:
      graph_freshness = self.graph_freshness

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "view_id": view_id,
        "facts_processed": facts_processed,
        "construction_time_ms": construction_time_ms,
        "source": source,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if truncated is not UNSET:
      field_dict["truncated"] = truncated
    if graph_freshness is not UNSET:
      field_dict["graph_freshness"] = graph_freshness

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_freshness import GraphFreshness

    d = dict(src_dict)
    view_id = d.pop("view_id")

    facts_processed = d.pop("facts_processed")

    construction_time_ms = d.pop("construction_time_ms")

    source = d.pop("source")

    def _parse_period_start(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_start = _parse_period_start(d.pop("period_start", UNSET))

    def _parse_period_end(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_end = _parse_period_end(d.pop("period_end", UNSET))

    truncated = d.pop("truncated", UNSET)

    def _parse_graph_freshness(data: object) -> GraphFreshness | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        graph_freshness_type_0 = GraphFreshness.from_dict(data)

        return graph_freshness_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(GraphFreshness | None | Unset, data)

    graph_freshness = _parse_graph_freshness(d.pop("graph_freshness", UNSET))

    view_metadata = cls(
      view_id=view_id,
      facts_processed=facts_processed,
      construction_time_ms=construction_time_ms,
      source=source,
      period_start=period_start,
      period_end=period_end,
      truncated=truncated,
      graph_freshness=graph_freshness,
    )

    view_metadata.additional_properties = d
    return view_metadata

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
