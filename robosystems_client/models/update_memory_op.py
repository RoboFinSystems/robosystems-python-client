from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.update_memory_op_provenance_type_0 import UpdateMemoryOpProvenanceType0


T = TypeVar("T", bound="UpdateMemoryOp")


@_attrs_define
class UpdateMemoryOp:
  """Body for the update-memory operation (partial update of a stored memory).

  Only supplied fields are changed; the memory is re-embedded when ``text``
  changes.

      Attributes:
          memory_id (str): Server-generated memory id to update
          text (None | str | Unset): New memory content
          memory_type (None | str | Unset): Freeform classifier
          tags (list[str] | None | Unset): Optional labels
          source_ref (None | str | Unset): Optional external reference/URI
          provenance (None | Unset | UpdateMemoryOpProvenanceType0): Opaque provenance metadata
  """

  memory_id: str
  text: None | str | Unset = UNSET
  memory_type: None | str | Unset = UNSET
  tags: list[str] | None | Unset = UNSET
  source_ref: None | str | Unset = UNSET
  provenance: None | Unset | UpdateMemoryOpProvenanceType0 = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.update_memory_op_provenance_type_0 import (
      UpdateMemoryOpProvenanceType0,
    )

    memory_id = self.memory_id

    text: None | str | Unset
    if isinstance(self.text, Unset):
      text = UNSET
    else:
      text = self.text

    memory_type: None | str | Unset
    if isinstance(self.memory_type, Unset):
      memory_type = UNSET
    else:
      memory_type = self.memory_type

    tags: list[str] | None | Unset
    if isinstance(self.tags, Unset):
      tags = UNSET
    elif isinstance(self.tags, list):
      tags = self.tags

    else:
      tags = self.tags

    source_ref: None | str | Unset
    if isinstance(self.source_ref, Unset):
      source_ref = UNSET
    else:
      source_ref = self.source_ref

    provenance: dict[str, Any] | None | Unset
    if isinstance(self.provenance, Unset):
      provenance = UNSET
    elif isinstance(self.provenance, UpdateMemoryOpProvenanceType0):
      provenance = self.provenance.to_dict()
    else:
      provenance = self.provenance

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "memory_id": memory_id,
      }
    )
    if text is not UNSET:
      field_dict["text"] = text
    if memory_type is not UNSET:
      field_dict["memory_type"] = memory_type
    if tags is not UNSET:
      field_dict["tags"] = tags
    if source_ref is not UNSET:
      field_dict["source_ref"] = source_ref
    if provenance is not UNSET:
      field_dict["provenance"] = provenance

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.update_memory_op_provenance_type_0 import (
      UpdateMemoryOpProvenanceType0,
    )

    d = dict(src_dict)
    memory_id = d.pop("memory_id")

    def _parse_text(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    text = _parse_text(d.pop("text", UNSET))

    def _parse_memory_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    memory_type = _parse_memory_type(d.pop("memory_type", UNSET))

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

    def _parse_source_ref(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_ref = _parse_source_ref(d.pop("source_ref", UNSET))

    def _parse_provenance(data: object) -> None | Unset | UpdateMemoryOpProvenanceType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        provenance_type_0 = UpdateMemoryOpProvenanceType0.from_dict(data)

        return provenance_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateMemoryOpProvenanceType0, data)

    provenance = _parse_provenance(d.pop("provenance", UNSET))

    update_memory_op = cls(
      memory_id=memory_id,
      text=text,
      memory_type=memory_type,
      tags=tags,
      source_ref=source_ref,
      provenance=provenance,
    )

    update_memory_op.additional_properties = d
    return update_memory_op

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
