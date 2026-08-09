from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockedSourceGraphResponse")


@_attrs_define
class BlockedSourceGraphResponse:
  """One blocked source graph.

  Attributes:
      id (str): Block row identifier (ULID).
      source_graph_id (str): The blocked sender's graph ID.
      blocked_by (str): User ID that created the block.
      blocked_at (datetime.datetime): When the block was created.
      source_graph_name (None | str | Unset): Display name of the blocked graph (if known).
      reason (None | str | Unset): Recipient's own note, if given.
  """

  id: str
  source_graph_id: str
  blocked_by: str
  blocked_at: datetime.datetime
  source_graph_name: None | str | Unset = UNSET
  reason: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    source_graph_id = self.source_graph_id

    blocked_by = self.blocked_by

    blocked_at = self.blocked_at.isoformat()

    source_graph_name: None | str | Unset
    if isinstance(self.source_graph_name, Unset):
      source_graph_name = UNSET
    else:
      source_graph_name = self.source_graph_name

    reason: None | str | Unset
    if isinstance(self.reason, Unset):
      reason = UNSET
    else:
      reason = self.reason

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "source_graph_id": source_graph_id,
        "blocked_by": blocked_by,
        "blocked_at": blocked_at,
      }
    )
    if source_graph_name is not UNSET:
      field_dict["source_graph_name"] = source_graph_name
    if reason is not UNSET:
      field_dict["reason"] = reason

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    source_graph_id = d.pop("source_graph_id")

    blocked_by = d.pop("blocked_by")

    blocked_at = datetime.datetime.fromisoformat(d.pop("blocked_at"))

    def _parse_source_graph_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_graph_name = _parse_source_graph_name(d.pop("source_graph_name", UNSET))

    def _parse_reason(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reason = _parse_reason(d.pop("reason", UNSET))

    blocked_source_graph_response = cls(
      id=id,
      source_graph_id=source_graph_id,
      blocked_by=blocked_by,
      blocked_at=blocked_at,
      source_graph_name=source_graph_name,
      reason=reason,
    )

    blocked_source_graph_response.additional_properties = d
    return blocked_source_graph_response

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
