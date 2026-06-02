from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromoteObligationsRequest")


@_attrs_define
class PromoteObligationsRequest:
  """On-demand trigger for the obligation-promotion sweep.

  Mirrors what the ``scheduled_obligation_promoter`` Dagster sensor does
  on its tick, but lets an interactive caller or an MCP close co-pilot
  run it now instead of waiting for the background cadence — required to
  drive a schedule-driven close to completion in a single session.
  Flips matured ``pending`` ``schedule_entry_due`` events (period boundary
  passed) to ``classified``; with ``dispatch_handlers`` it also drafts the
  closing entries in the same transaction (idempotent — reconciles to an
  existing draft).

      Attributes:
          dispatch_handlers (bool | Unset): When True (default), also fire the schedule_entry_due handler for each
              promoted obligation so the draft closing entry materializes immediately (autopilot). When False, flip status
              only (co-pilot) — the draft is created separately. Default: True.
  """

  dispatch_handlers: bool | Unset = True
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    dispatch_handlers = self.dispatch_handlers

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if dispatch_handlers is not UNSET:
      field_dict["dispatch_handlers"] = dispatch_handlers

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    dispatch_handlers = d.pop("dispatch_handlers", UNSET)

    promote_obligations_request = cls(
      dispatch_handlers=dispatch_handlers,
    )

    promote_obligations_request.additional_properties = d
    return promote_obligations_request

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
