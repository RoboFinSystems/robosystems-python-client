from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.fiscal_calendar_response import FiscalCalendarResponse


T = TypeVar("T", bound="InitializeLedgerResponse")


@_attrs_define
class InitializeLedgerResponse:
  """
  Attributes:
      fiscal_calendar (FiscalCalendarResponse): Current fiscal calendar state for a graph.
      periods_created (int | Unset): Number of FiscalPeriod rows created by initialization Default: 0.
      warnings (list[str] | Unset): Non-fatal warnings (e.g., auto_seed_schedules not implemented)
  """

  fiscal_calendar: FiscalCalendarResponse
  periods_created: int | Unset = 0
  warnings: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    fiscal_calendar = self.fiscal_calendar.to_dict()

    periods_created = self.periods_created

    warnings: list[str] | Unset = UNSET
    if not isinstance(self.warnings, Unset):
      warnings = self.warnings

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "fiscal_calendar": fiscal_calendar,
      }
    )
    if periods_created is not UNSET:
      field_dict["periods_created"] = periods_created
    if warnings is not UNSET:
      field_dict["warnings"] = warnings

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.fiscal_calendar_response import FiscalCalendarResponse

    d = dict(src_dict)
    fiscal_calendar = FiscalCalendarResponse.from_dict(d.pop("fiscal_calendar"))

    periods_created = d.pop("periods_created", UNSET)

    warnings = cast(list[str], d.pop("warnings", UNSET))

    initialize_ledger_response = cls(
      fiscal_calendar=fiscal_calendar,
      periods_created=periods_created,
      warnings=warnings,
    )

    initialize_ledger_response.additional_properties = d
    return initialize_ledger_response

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
