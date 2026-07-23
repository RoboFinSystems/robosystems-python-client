from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChartSeriesLite")


@_attrs_define
class ChartSeriesLite:
  """One plottable series in a chart panel.

  Carries structure and identity only — the values live in the sibling
  ``rendering.rows`` (join on ``element_id``), so the chart arm never
  duplicates the value matrix. ``key`` is the stable series identity for
  client state (colors, toggles); today it equals ``element_id``, and
  future axes (the forecast scenario) arrive as new fields on this
  model, never a new arm shape.

      Attributes:
          key (str): Stable series id — element_id today.
          element_id (str):
          label (str): Display name for legends.
  """

  key: str
  element_id: str
  label: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    key = self.key

    element_id = self.element_id

    label = self.label

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "key": key,
        "element_id": element_id,
        "label": label,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    key = d.pop("key")

    element_id = d.pop("element_id")

    label = d.pop("label")

    chart_series_lite = cls(
      key=key,
      element_id=element_id,
      label=label,
    )

    chart_series_lite.additional_properties = d
    return chart_series_lite

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
