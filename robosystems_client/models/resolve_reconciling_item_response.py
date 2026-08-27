from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resolve_reconciling_item_response_disposition import (
  ResolveReconcilingItemResponseDisposition,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.reconciling_item_catch_up import ReconcilingItemCatchUp
  from ..models.reconciling_item_delta_line import ReconcilingItemDeltaLine
  from ..models.reconciling_item_regenerated import ReconcilingItemRegenerated


T = TypeVar("T", bound="ResolveReconcilingItemResponse")


@_attrs_define
class ResolveReconcilingItemResponse:
  """The outcome of resolving one reconciling item.

  Attributes:
      event_id (str):
      disposition (ResolveReconcilingItemResponseDisposition):
      resolved_at (datetime.datetime):
      resolved_by (str):
      external_id (None | str | Unset):
      delta (list[ReconcilingItemDeltaLine] | Unset):
      no_gl_effect (bool | Unset):  Default: False.
      catch_up (None | ReconcilingItemCatchUp | Unset): Present when the disposition posted a catch-up entry
      regenerated (None | ReconcilingItemRegenerated | Unset): Present when the disposition rebuilt the event's
          entries
      reference_event_id (None | str | Unset):
      note (None | str | Unset):
  """

  event_id: str
  disposition: ResolveReconcilingItemResponseDisposition
  resolved_at: datetime.datetime
  resolved_by: str
  external_id: None | str | Unset = UNSET
  delta: list[ReconcilingItemDeltaLine] | Unset = UNSET
  no_gl_effect: bool | Unset = False
  catch_up: None | ReconcilingItemCatchUp | Unset = UNSET
  regenerated: None | ReconcilingItemRegenerated | Unset = UNSET
  reference_event_id: None | str | Unset = UNSET
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.reconciling_item_catch_up import ReconcilingItemCatchUp
    from ..models.reconciling_item_regenerated import ReconcilingItemRegenerated

    event_id = self.event_id

    disposition = self.disposition.value

    resolved_at = self.resolved_at.isoformat()

    resolved_by = self.resolved_by

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

    delta: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.delta, Unset):
      delta = []
      for delta_item_data in self.delta:
        delta_item = delta_item_data.to_dict()
        delta.append(delta_item)

    no_gl_effect = self.no_gl_effect

    catch_up: dict[str, Any] | None | Unset
    if isinstance(self.catch_up, Unset):
      catch_up = UNSET
    elif isinstance(self.catch_up, ReconcilingItemCatchUp):
      catch_up = self.catch_up.to_dict()
    else:
      catch_up = self.catch_up

    regenerated: dict[str, Any] | None | Unset
    if isinstance(self.regenerated, Unset):
      regenerated = UNSET
    elif isinstance(self.regenerated, ReconcilingItemRegenerated):
      regenerated = self.regenerated.to_dict()
    else:
      regenerated = self.regenerated

    reference_event_id: None | str | Unset
    if isinstance(self.reference_event_id, Unset):
      reference_event_id = UNSET
    else:
      reference_event_id = self.reference_event_id

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
        "disposition": disposition,
        "resolved_at": resolved_at,
        "resolved_by": resolved_by,
      }
    )
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if delta is not UNSET:
      field_dict["delta"] = delta
    if no_gl_effect is not UNSET:
      field_dict["no_gl_effect"] = no_gl_effect
    if catch_up is not UNSET:
      field_dict["catch_up"] = catch_up
    if regenerated is not UNSET:
      field_dict["regenerated"] = regenerated
    if reference_event_id is not UNSET:
      field_dict["reference_event_id"] = reference_event_id
    if note is not UNSET:
      field_dict["note"] = note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.reconciling_item_catch_up import ReconcilingItemCatchUp
    from ..models.reconciling_item_delta_line import ReconcilingItemDeltaLine
    from ..models.reconciling_item_regenerated import ReconcilingItemRegenerated

    d = dict(src_dict)
    event_id = d.pop("event_id")

    disposition = ResolveReconcilingItemResponseDisposition(d.pop("disposition"))

    resolved_at = datetime.datetime.fromisoformat(d.pop("resolved_at"))

    resolved_by = d.pop("resolved_by")

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

    _delta = d.pop("delta", UNSET)
    delta: list[ReconcilingItemDeltaLine] | Unset = UNSET
    if _delta is not UNSET:
      delta = []
      for delta_item_data in _delta:
        delta_item = ReconcilingItemDeltaLine.from_dict(delta_item_data)

        delta.append(delta_item)

    no_gl_effect = d.pop("no_gl_effect", UNSET)

    def _parse_catch_up(data: object) -> None | ReconcilingItemCatchUp | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        catch_up_type_0 = ReconcilingItemCatchUp.from_dict(data)

        return catch_up_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ReconcilingItemCatchUp | Unset, data)

    catch_up = _parse_catch_up(d.pop("catch_up", UNSET))

    def _parse_regenerated(data: object) -> None | ReconcilingItemRegenerated | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        regenerated_type_0 = ReconcilingItemRegenerated.from_dict(data)

        return regenerated_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ReconcilingItemRegenerated | Unset, data)

    regenerated = _parse_regenerated(d.pop("regenerated", UNSET))

    def _parse_reference_event_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reference_event_id = _parse_reference_event_id(d.pop("reference_event_id", UNSET))

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    resolve_reconciling_item_response = cls(
      event_id=event_id,
      disposition=disposition,
      resolved_at=resolved_at,
      resolved_by=resolved_by,
      external_id=external_id,
      delta=delta,
      no_gl_effect=no_gl_effect,
      catch_up=catch_up,
      regenerated=regenerated,
      reference_event_id=reference_event_id,
      note=note,
    )

    resolve_reconciling_item_response.additional_properties = d
    return resolve_reconciling_item_response

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
