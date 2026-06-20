from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RebuildScheduleRequest")


@_attrs_define
class RebuildScheduleRequest:
  """Re-run the schedule generator in place on an existing schedule.

  Atomic alternative to delete-then-recreate: the structure id and its
  element associations are preserved, the old pending obligation chain
  is voided, the old facts + rules are deleted, and a fresh set of
  forward facts + a fresh obligation chain are regenerated from the
  schedule's stored definition (entry_template / schedule_metadata /
  monthly_amount / period bounds on the Structure's metadata).

  The historical-vs-in-scope split is re-derived from the CURRENT fiscal
  calendar `closed_through`, so a rebuild re-scopes the schedule to
  today's close state. Use this to pick up a fixed generator (e.g. the
  roll-forward direction fix) without orphaning obligations.

      Attributes:
          structure_id (str): The schedule structure to regenerate in place.
  """

  structure_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    rebuild_schedule_request = cls(
      structure_id=structure_id,
    )

    rebuild_schedule_request.additional_properties = d
    return rebuild_schedule_request

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
