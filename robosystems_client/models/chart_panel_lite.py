from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.chart_series_lite import ChartSeriesLite


T = TypeVar("T", bound="ChartPanelLite")


@_attrs_define
class ChartPanelLite:
  """One chart panel — series sharing a y-axis format family.

  Mixed-unit catalogs are unplottable on one axis, so the server groups
  rows into panels by ``item_type`` family (NULL falls back to
  ``is_monetary``). The x-axis is always ``rendering.periods``.

      Attributes:
          label (None | str | Unset): Panel heading — e.g. 'Monetary', 'Ratios'.
          item_type (None | str | Unset): Format family shared by the panel's series (monetary | ratio | percent |
              multiple | days); None for the untyped fallback panel.
          kind (str | Unset): Per-panel mark — 'line' or 'bar'. Default: 'line'.
          series (list[ChartSeriesLite] | Unset):
  """

  label: None | str | Unset = UNSET
  item_type: None | str | Unset = UNSET
  kind: str | Unset = "line"
  series: list[ChartSeriesLite] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    label: None | str | Unset
    if isinstance(self.label, Unset):
      label = UNSET
    else:
      label = self.label

    item_type: None | str | Unset
    if isinstance(self.item_type, Unset):
      item_type = UNSET
    else:
      item_type = self.item_type

    kind = self.kind

    series: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.series, Unset):
      series = []
      for series_item_data in self.series:
        series_item = series_item_data.to_dict()
        series.append(series_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if label is not UNSET:
      field_dict["label"] = label
    if item_type is not UNSET:
      field_dict["item_type"] = item_type
    if kind is not UNSET:
      field_dict["kind"] = kind
    if series is not UNSET:
      field_dict["series"] = series

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.chart_series_lite import ChartSeriesLite

    d = dict(src_dict)

    def _parse_label(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    label = _parse_label(d.pop("label", UNSET))

    def _parse_item_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    item_type = _parse_item_type(d.pop("item_type", UNSET))

    kind = d.pop("kind", UNSET)

    _series = d.pop("series", UNSET)
    series: list[ChartSeriesLite] | Unset = UNSET
    if _series is not UNSET:
      series = []
      for series_item_data in _series:
        series_item = ChartSeriesLite.from_dict(series_item_data)

        series.append(series_item)

    chart_panel_lite = cls(
      label=label,
      item_type=item_type,
      kind=kind,
      series=series,
    )

    chart_panel_lite.additional_properties = d
    return chart_panel_lite

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
