from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.chart_panel_lite import ChartPanelLite


T = TypeVar("T", bound="ChartLite")


@_attrs_define
class ChartLite:
  """Server-shaped chart projection — panel/series CONFIG, never values.

  The second real server-computed View arm (after ``rendering``). Values
  come from ``rendering.rows`` joined by ``element_id``; the x-axis is
  ``rendering.periods``. Renderers (report-components) turn one panel
  into one chart.

      Attributes:
          panels (list[ChartPanelLite] | Unset):
  """

  panels: list[ChartPanelLite] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    panels: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.panels, Unset):
      panels = []
      for panels_item_data in self.panels:
        panels_item = panels_item_data.to_dict()
        panels.append(panels_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if panels is not UNSET:
      field_dict["panels"] = panels

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.chart_panel_lite import ChartPanelLite

    d = dict(src_dict)
    _panels = d.pop("panels", UNSET)
    panels: list[ChartPanelLite] | Unset = UNSET
    if _panels is not UNSET:
      panels = []
      for panels_item_data in _panels:
        panels_item = ChartPanelLite.from_dict(panels_item_data)

        panels.append(panels_item)

    chart_lite = cls(
      panels=panels,
    )

    chart_lite.additional_properties = d
    return chart_lite

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
