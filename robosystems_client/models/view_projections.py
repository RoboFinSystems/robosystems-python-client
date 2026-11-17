from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.chart_lite import ChartLite
  from ..models.rendering_lite import RenderingLite


T = TypeVar("T", bound="ViewProjections")


@_attrs_define
class ViewProjections:
  """The server-computed View projections of an Information Block,
  surfaced at the envelope boundary.

  Two are computed at envelope-build time when their source data is
  available: `rendering` (the rendered rows and periods) for the
  statement family, disclosures, metrics, forecasts and reconciliations,
  and `chart` (panel/series config over the rendering's rows and
  periods) for metric blocks. The other views a client shows are
  derived from the envelope itself — a fact table from
  `InformationBlockEnvelope.facts`, rule outcomes from its rules and
  verification results.

      Attributes:
          rendering (None | RenderingLite | Unset):
          chart (ChartLite | None | Unset):
  """

  rendering: None | RenderingLite | Unset = UNSET
  chart: ChartLite | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.chart_lite import ChartLite
    from ..models.rendering_lite import RenderingLite

    rendering: dict[str, Any] | None | Unset
    if isinstance(self.rendering, Unset):
      rendering = UNSET
    elif isinstance(self.rendering, RenderingLite):
      rendering = self.rendering.to_dict()
    else:
      rendering = self.rendering

    chart: dict[str, Any] | None | Unset
    if isinstance(self.chart, Unset):
      chart = UNSET
    elif isinstance(self.chart, ChartLite):
      chart = self.chart.to_dict()
    else:
      chart = self.chart

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if rendering is not UNSET:
      field_dict["rendering"] = rendering
    if chart is not UNSET:
      field_dict["chart"] = chart

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.chart_lite import ChartLite
    from ..models.rendering_lite import RenderingLite

    d = dict(src_dict)

    def _parse_rendering(data: object) -> None | RenderingLite | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        rendering_type_0 = RenderingLite.from_dict(data)

        return rendering_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | RenderingLite | Unset, data)

    rendering = _parse_rendering(d.pop("rendering", UNSET))

    def _parse_chart(data: object) -> ChartLite | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        chart_type_0 = ChartLite.from_dict(data)

        return chart_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(ChartLite | None | Unset, data)

    chart = _parse_chart(d.pop("chart", UNSET))

    view_projections = cls(
      rendering=rendering,
      chart=chart,
    )

    view_projections.additional_properties = d
    return view_projections

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
