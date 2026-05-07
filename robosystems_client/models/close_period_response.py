from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.fiscal_calendar_response import FiscalCalendarResponse


T = TypeVar("T", bound="ClosePeriodResponse")


@_attrs_define
class ClosePeriodResponse:
  """Response from a single-period close operation.

  Attributes:
      fiscal_calendar (FiscalCalendarResponse): Current fiscal calendar state for a graph.
      period (str):
      entries_posted (int | Unset): Number of draft entries transitioned to posted Default: 0.
      target_auto_advanced (bool | Unset): Whether close_target was auto-advanced because it was reached Default:
          False.
  """

  fiscal_calendar: FiscalCalendarResponse
  period: str
  entries_posted: int | Unset = 0
  target_auto_advanced: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    fiscal_calendar = self.fiscal_calendar.to_dict()

    period = self.period

    entries_posted = self.entries_posted

    target_auto_advanced = self.target_auto_advanced

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "fiscal_calendar": fiscal_calendar,
        "period": period,
      }
    )
    if entries_posted is not UNSET:
      field_dict["entries_posted"] = entries_posted
    if target_auto_advanced is not UNSET:
      field_dict["target_auto_advanced"] = target_auto_advanced

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.fiscal_calendar_response import FiscalCalendarResponse

    d = dict(src_dict)
    fiscal_calendar = FiscalCalendarResponse.from_dict(d.pop("fiscal_calendar"))

    period = d.pop("period")

    entries_posted = d.pop("entries_posted", UNSET)

    target_auto_advanced = d.pop("target_auto_advanced", UNSET)

    close_period_response = cls(
      fiscal_calendar=fiscal_calendar,
      period=period,
      entries_posted=entries_posted,
      target_auto_advanced=target_auto_advanced,
    )

    close_period_response.additional_properties = d
    return close_period_response

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
