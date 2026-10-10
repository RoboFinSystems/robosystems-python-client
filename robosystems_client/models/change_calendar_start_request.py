from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeCalendarStartRequest")


@_attrs_define
class ChangeCalendarStartRequest:
  """Move where an entity's calendar starts, before its first close.

  Earlier adds open months back to `first_open_period`, for history that
  predates the start (a bank feed's backfill, a cutover moved earlier).
  Later removes empty leading months. Refused once any month has closed,
  and when moving later would drop months that hold entries or unposted
  source lines.

      Attributes:
          first_open_period (str): YYYY-MM: the new first month of the calendar, open.
          entity_id (None | str | Unset): The entity whose books this acts on, by id. Omit for the group parent — the
              single-entity default.
          note (None | str | Unset): Free-form note attached to the audit event
  """

  first_open_period: str
  entity_id: None | str | Unset = UNSET
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    first_open_period = self.first_open_period

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "first_open_period": first_open_period,
      }
    )
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if note is not UNSET:
      field_dict["note"] = note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    first_open_period = d.pop("first_open_period")

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    change_calendar_start_request = cls(
      first_open_period=first_open_period,
      entity_id=entity_id,
      note=note,
    )

    change_calendar_start_request.additional_properties = d
    return change_calendar_start_request

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
