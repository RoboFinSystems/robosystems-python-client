from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateGraphMetadataOp")


@_attrs_define
class UpdateGraphMetadataOp:
  """Body for the update-graph-metadata operation.

  Partial update — only supplied (non-null) fields change, so a caller
  editing just the display name need not resend the description and tags.
  Because ``None`` means "leave alone", clearing a field uses its empty
  value instead: pass ``""`` to clear the description and ``[]`` to clear
  the tags. ``graph_name`` cannot be cleared; it is the graph's label
  everywhere it is listed.

  This is the platform-level label for the graph, independent of the
  entity name shown on financial statements — change that through
  ``POST /extensions/roboledger/{graph_id}/operations/update-entity``.

      Attributes:
          graph_name (None | str | Unset): New display name. Omit to leave unchanged; cannot be cleared.
          description (None | str | Unset): New description. Omit to leave unchanged; pass '' to clear.
          tags (list[str] | None | Unset): Replaces the full tag list (not a merge). Omit to leave unchanged; pass [] to
              clear. Tags are trimmed, de-duplicated, and capped at 50 characters each.
  """

  graph_name: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  tags: list[str] | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_name: None | str | Unset
    if isinstance(self.graph_name, Unset):
      graph_name = UNSET
    else:
      graph_name = self.graph_name

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    tags: list[str] | None | Unset
    if isinstance(self.tags, Unset):
      tags = UNSET
    elif isinstance(self.tags, list):
      tags = self.tags

    else:
      tags = self.tags

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if graph_name is not UNSET:
      field_dict["graph_name"] = graph_name
    if description is not UNSET:
      field_dict["description"] = description
    if tags is not UNSET:
      field_dict["tags"] = tags

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_graph_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    graph_name = _parse_graph_name(d.pop("graph_name", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_tags(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        tags_type_0 = cast(list[str], data)

        return tags_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    tags = _parse_tags(d.pop("tags", UNSET))

    update_graph_metadata_op = cls(
      graph_name=graph_name,
      description=description,
      tags=tags,
    )

    update_graph_metadata_op.additional_properties = d
    return update_graph_metadata_op

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
