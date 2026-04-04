from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.schedule_summary_response import ScheduleSummaryResponse


T = TypeVar("T", bound="ScheduleListResponse")


@_attrs_define
class ScheduleListResponse:
  """
  Attributes:
      schedules (list[ScheduleSummaryResponse]):
  """

  schedules: list[ScheduleSummaryResponse]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    schedules = []
    for schedules_item_data in self.schedules:
      schedules_item = schedules_item_data.to_dict()
      schedules.append(schedules_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "schedules": schedules,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.schedule_summary_response import ScheduleSummaryResponse

    d = dict(src_dict)
    schedules = []
    _schedules = d.pop("schedules")
    for schedules_item_data in _schedules:
      schedules_item = ScheduleSummaryResponse.from_dict(schedules_item_data)

      schedules.append(schedules_item)

    schedule_list_response = cls(
      schedules=schedules,
    )

    schedule_list_response.additional_properties = d
    return schedule_list_response

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
