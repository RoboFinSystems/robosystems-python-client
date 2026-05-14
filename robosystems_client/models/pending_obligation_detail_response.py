from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PendingObligationDetailResponse")


@_attrs_define
class PendingObligationDetailResponse:
  """One pending schedule-derived obligation blocking close.

  Surfaced on `FiscalCalendarResponse` when `pending_obligations` is in
  the blockers list so callers can name which schedules to promote.

      Attributes:
          event_id (str):
          period (str): Period in YYYY-MM format
          schedule_id (None | str | Unset):
          schedule_name (None | str | Unset):
  """

  event_id: str
  period: str
  schedule_id: None | str | Unset = UNSET
  schedule_name: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_id = self.event_id

    period = self.period

    schedule_id: None | str | Unset
    if isinstance(self.schedule_id, Unset):
      schedule_id = UNSET
    else:
      schedule_id = self.schedule_id

    schedule_name: None | str | Unset
    if isinstance(self.schedule_name, Unset):
      schedule_name = UNSET
    else:
      schedule_name = self.schedule_name

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
        "period": period,
      }
    )
    if schedule_id is not UNSET:
      field_dict["schedule_id"] = schedule_id
    if schedule_name is not UNSET:
      field_dict["schedule_name"] = schedule_name

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    event_id = d.pop("event_id")

    period = d.pop("period")

    def _parse_schedule_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    schedule_id = _parse_schedule_id(d.pop("schedule_id", UNSET))

    def _parse_schedule_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    schedule_name = _parse_schedule_name(d.pop("schedule_name", UNSET))

    pending_obligation_detail_response = cls(
      event_id=event_id,
      period=period,
      schedule_id=schedule_id,
      schedule_name=schedule_name,
    )

    pending_obligation_detail_response.additional_properties = d
    return pending_obligation_detail_response

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
