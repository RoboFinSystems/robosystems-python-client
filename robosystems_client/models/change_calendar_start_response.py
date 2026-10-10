from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.fiscal_calendar_response import FiscalCalendarResponse


T = TypeVar("T", bound="ChangeCalendarStartResponse")


@_attrs_define
class ChangeCalendarStartResponse:
  """
  Attributes:
      fiscal_calendar (FiscalCalendarResponse): Current fiscal calendar state for one entity of a graph.
      periods_created (int | Unset): Open FiscalPeriod rows added by moving the start earlier Default: 0.
      periods_removed (int | Unset): Empty FiscalPeriod rows removed by moving the start later Default: 0.
  """

  fiscal_calendar: FiscalCalendarResponse
  periods_created: int | Unset = 0
  periods_removed: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    fiscal_calendar = self.fiscal_calendar.to_dict()

    periods_created = self.periods_created

    periods_removed = self.periods_removed

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "fiscal_calendar": fiscal_calendar,
      }
    )
    if periods_created is not UNSET:
      field_dict["periods_created"] = periods_created
    if periods_removed is not UNSET:
      field_dict["periods_removed"] = periods_removed

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.fiscal_calendar_response import FiscalCalendarResponse

    d = dict(src_dict)
    fiscal_calendar = FiscalCalendarResponse.from_dict(d.pop("fiscal_calendar"))

    periods_created = d.pop("periods_created", UNSET)

    periods_removed = d.pop("periods_removed", UNSET)

    change_calendar_start_response = cls(
      fiscal_calendar=fiscal_calendar,
      periods_created=periods_created,
      periods_removed=periods_removed,
    )

    change_calendar_start_response.additional_properties = d
    return change_calendar_start_response

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
