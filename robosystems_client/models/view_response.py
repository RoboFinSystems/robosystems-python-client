from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.dimension import Dimension
  from ..models.fact_record import FactRecord
  from ..models.view_metadata import ViewMetadata
  from ..models.view_response_summary_type_0 import ViewResponseSummaryType0


T = TypeVar("T", bound="ViewResponse")


@_attrs_define
class ViewResponse:
  """Flat, deduplicated facts plus the aspects they span.

  No server-side pivot: each fact is returned as its own record so the
  consumer can arrange cells on the full aspect signature. Summing across
  entities, units, or elements that merely share a local name is a
  presentation decision this endpoint refuses to make on the caller's behalf.

      Attributes:
          metadata (ViewMetadata):
          dimensions (list[Dimension] | Unset): Aspects spanned by the returned facts
          facts (list[FactRecord] | Unset): Deduplicated fact records
          summary (None | Unset | ViewResponseSummaryType0): Per-element aggregates, only when include_summary=true.
              `total` and `average` span every returned period, so they are present for duration elements only — instants omit
              both (a balance summed across periods is not a balance). Overlapping duration windows sharing a period_end
              (quarter + year-to-date) contribute only the narrowest window, so a quarter is never double-counted inside its
              own YTD figure.
  """

  metadata: ViewMetadata
  dimensions: list[Dimension] | Unset = UNSET
  facts: list[FactRecord] | Unset = UNSET
  summary: None | Unset | ViewResponseSummaryType0 = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.view_response_summary_type_0 import ViewResponseSummaryType0

    metadata = self.metadata.to_dict()

    dimensions: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.dimensions, Unset):
      dimensions = []
      for dimensions_item_data in self.dimensions:
        dimensions_item = dimensions_item_data.to_dict()
        dimensions.append(dimensions_item)

    facts: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.facts, Unset):
      facts = []
      for facts_item_data in self.facts:
        facts_item = facts_item_data.to_dict()
        facts.append(facts_item)

    summary: dict[str, Any] | None | Unset
    if isinstance(self.summary, Unset):
      summary = UNSET
    elif isinstance(self.summary, ViewResponseSummaryType0):
      summary = self.summary.to_dict()
    else:
      summary = self.summary

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "metadata": metadata,
      }
    )
    if dimensions is not UNSET:
      field_dict["dimensions"] = dimensions
    if facts is not UNSET:
      field_dict["facts"] = facts
    if summary is not UNSET:
      field_dict["summary"] = summary

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.dimension import Dimension
    from ..models.fact_record import FactRecord
    from ..models.view_metadata import ViewMetadata
    from ..models.view_response_summary_type_0 import ViewResponseSummaryType0

    d = dict(src_dict)
    metadata = ViewMetadata.from_dict(d.pop("metadata"))

    _dimensions = d.pop("dimensions", UNSET)
    dimensions: list[Dimension] | Unset = UNSET
    if _dimensions is not UNSET:
      dimensions = []
      for dimensions_item_data in _dimensions:
        dimensions_item = Dimension.from_dict(dimensions_item_data)

        dimensions.append(dimensions_item)

    _facts = d.pop("facts", UNSET)
    facts: list[FactRecord] | Unset = UNSET
    if _facts is not UNSET:
      facts = []
      for facts_item_data in _facts:
        facts_item = FactRecord.from_dict(facts_item_data)

        facts.append(facts_item)

    def _parse_summary(data: object) -> None | Unset | ViewResponseSummaryType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        summary_type_0 = ViewResponseSummaryType0.from_dict(data)

        return summary_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | ViewResponseSummaryType0, data)

    summary = _parse_summary(d.pop("summary", UNSET))

    view_response = cls(
      metadata=metadata,
      dimensions=dimensions,
      facts=facts,
      summary=summary,
    )

    view_response.additional_properties = d
    return view_response

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
