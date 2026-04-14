from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClosePeriodOperation")


@_attrs_define
class ClosePeriodOperation:
  """
  Attributes:
      period (str):
      note (None | str | Unset): Free-form note attached to the close event
      allow_stale_sync (bool | Unset): Override the sync-currency gate. Only use when you have manually verified that
          the source data for the period is complete. Default: False.
  """

  period: str
  note: None | str | Unset = UNSET
  allow_stale_sync: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    allow_stale_sync = self.allow_stale_sync

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
      }
    )
    if note is not UNSET:
      field_dict["note"] = note
    if allow_stale_sync is not UNSET:
      field_dict["allow_stale_sync"] = allow_stale_sync

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    period = d.pop("period")

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    allow_stale_sync = d.pop("allow_stale_sync", UNSET)

    close_period_operation = cls(
      period=period,
      note=note,
      allow_stale_sync=allow_stale_sync,
    )

    close_period_operation.additional_properties = d
    return close_period_operation

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
