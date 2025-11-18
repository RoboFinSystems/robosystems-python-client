from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveViewRequest")


@_attrs_define
class SaveViewRequest:
  """
  Attributes:
      report_type (str): Type of report (e.g., 'Annual Report', 'Quarterly Report', '10-K')
      period_start (str): Period start date (YYYY-MM-DD)
      period_end (str): Period end date (YYYY-MM-DD)
      report_id (None | str | Unset): Existing report ID to update (if provided, deletes existing facts/structures and
          creates new ones)
      entity_id (None | str | Unset): Entity identifier (defaults to primary entity)
      include_presentation (bool | Unset): Create presentation structures Default: True.
      include_calculation (bool | Unset): Create calculation structures Default: True.
  """

  report_type: str
  period_start: str
  period_end: str
  report_id: None | str | Unset = UNSET
  entity_id: None | str | Unset = UNSET
  include_presentation: bool | Unset = True
  include_calculation: bool | Unset = True
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    report_type = self.report_type

    period_start = self.period_start

    period_end = self.period_end

    report_id: None | str | Unset
    if isinstance(self.report_id, Unset):
      report_id = UNSET
    else:
      report_id = self.report_id

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    include_presentation = self.include_presentation

    include_calculation = self.include_calculation

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "report_type": report_type,
        "period_start": period_start,
        "period_end": period_end,
      }
    )
    if report_id is not UNSET:
      field_dict["report_id"] = report_id
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if include_presentation is not UNSET:
      field_dict["include_presentation"] = include_presentation
    if include_calculation is not UNSET:
      field_dict["include_calculation"] = include_calculation

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    report_type = d.pop("report_type")

    period_start = d.pop("period_start")

    period_end = d.pop("period_end")

    def _parse_report_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    report_id = _parse_report_id(d.pop("report_id", UNSET))

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    include_presentation = d.pop("include_presentation", UNSET)

    include_calculation = d.pop("include_calculation", UNSET)

    save_view_request = cls(
      report_type=report_type,
      period_start=period_start,
      period_end=period_end,
      report_id=report_id,
      entity_id=entity_id,
      include_presentation=include_presentation,
      include_calculation=include_calculation,
    )

    save_view_request.additional_properties = d
    return save_view_request

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
