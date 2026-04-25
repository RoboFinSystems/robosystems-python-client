from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_event_block_request_transition_to_type_0 import (
  UpdateEventBlockRequestTransitionToType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.update_event_block_request_metadata_patch import (
    UpdateEventBlockRequestMetadataPatch,
  )


T = TypeVar("T", bound="UpdateEventBlockRequest")


@_attrs_define
class UpdateEventBlockRequest:
  """Status transitions and field corrections for an event block.

  All fields except event_id are optional — only supplied fields are updated.

      Attributes:
          event_id (str):
          transition_to (None | Unset | UpdateEventBlockRequestTransitionToType0): Status transition. Valid moves depend
              on current status: captured → committed | voided; classified → committed | pending | fulfilled | voided;
              committed → pending | fulfilled | voided; pending → fulfilled | voided. Terminal states (fulfilled, voided,
              superseded) accept no further transitions. Note: classified and fulfilled are usually set by handlers, not by
              callers, but the transition is allowed for corrections.
          superseded_by_id (None | str | Unset): New event id that replaces this one. Required when
              transition_to='superseded'.
          description (None | str | Unset):
          effective_at (datetime.datetime | None | Unset):
          metadata_patch (UpdateEventBlockRequestMetadataPatch | Unset): Key-value pairs merged into existing metadata
              (additive patch, not replace).
  """

  event_id: str
  transition_to: None | Unset | UpdateEventBlockRequestTransitionToType0 = UNSET
  superseded_by_id: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  effective_at: datetime.datetime | None | Unset = UNSET
  metadata_patch: UpdateEventBlockRequestMetadataPatch | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_id = self.event_id

    transition_to: None | str | Unset
    if isinstance(self.transition_to, Unset):
      transition_to = UNSET
    elif isinstance(self.transition_to, UpdateEventBlockRequestTransitionToType0):
      transition_to = self.transition_to.value
    else:
      transition_to = self.transition_to

    superseded_by_id: None | str | Unset
    if isinstance(self.superseded_by_id, Unset):
      superseded_by_id = UNSET
    else:
      superseded_by_id = self.superseded_by_id

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    effective_at: None | str | Unset
    if isinstance(self.effective_at, Unset):
      effective_at = UNSET
    elif isinstance(self.effective_at, datetime.datetime):
      effective_at = self.effective_at.isoformat()
    else:
      effective_at = self.effective_at

    metadata_patch: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata_patch, Unset):
      metadata_patch = self.metadata_patch.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
      }
    )
    if transition_to is not UNSET:
      field_dict["transition_to"] = transition_to
    if superseded_by_id is not UNSET:
      field_dict["superseded_by_id"] = superseded_by_id
    if description is not UNSET:
      field_dict["description"] = description
    if effective_at is not UNSET:
      field_dict["effective_at"] = effective_at
    if metadata_patch is not UNSET:
      field_dict["metadata_patch"] = metadata_patch

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.update_event_block_request_metadata_patch import (
      UpdateEventBlockRequestMetadataPatch,
    )

    d = dict(src_dict)
    event_id = d.pop("event_id")

    def _parse_transition_to(
      data: object,
    ) -> None | Unset | UpdateEventBlockRequestTransitionToType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        transition_to_type_0 = UpdateEventBlockRequestTransitionToType0(data)

        return transition_to_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateEventBlockRequestTransitionToType0, data)

    transition_to = _parse_transition_to(d.pop("transition_to", UNSET))

    def _parse_superseded_by_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    superseded_by_id = _parse_superseded_by_id(d.pop("superseded_by_id", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_effective_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        effective_at_type_0 = isoparse(data)

        return effective_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    effective_at = _parse_effective_at(d.pop("effective_at", UNSET))

    _metadata_patch = d.pop("metadata_patch", UNSET)
    metadata_patch: UpdateEventBlockRequestMetadataPatch | Unset
    if isinstance(_metadata_patch, Unset):
      metadata_patch = UNSET
    else:
      metadata_patch = UpdateEventBlockRequestMetadataPatch.from_dict(_metadata_patch)

    update_event_block_request = cls(
      event_id=event_id,
      transition_to=transition_to,
      superseded_by_id=superseded_by_id,
      description=description,
      effective_at=effective_at,
      metadata_patch=metadata_patch,
    )

    update_event_block_request.additional_properties = d
    return update_event_block_request

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
