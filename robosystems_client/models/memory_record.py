from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.memory_record_provenance_type_0 import MemoryRecordProvenanceType0


T = TypeVar("T", bound="MemoryRecord")


@_attrs_define
class MemoryRecord:
  """A stored memory (never includes the raw embedding vector).

  Attributes:
      id (str):
      text (str):
      source (None | str | Unset):
      memory_type (None | str | Unset):
      tags (list[str] | None | Unset):
      source_ref (None | str | Unset):
      provenance (MemoryRecordProvenanceType0 | None | Unset):
      created_by (None | str | Unset):
      created_at (datetime.datetime | None | Unset):
      updated_at (datetime.datetime | None | Unset):
  """

  id: str
  text: str
  source: None | str | Unset = UNSET
  memory_type: None | str | Unset = UNSET
  tags: list[str] | None | Unset = UNSET
  source_ref: None | str | Unset = UNSET
  provenance: MemoryRecordProvenanceType0 | None | Unset = UNSET
  created_by: None | str | Unset = UNSET
  created_at: datetime.datetime | None | Unset = UNSET
  updated_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.memory_record_provenance_type_0 import MemoryRecordProvenanceType0

    id = self.id

    text = self.text

    source: None | str | Unset
    if isinstance(self.source, Unset):
      source = UNSET
    else:
      source = self.source

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
    elif isinstance(self.provenance, MemoryRecordProvenanceType0):
      provenance = self.provenance.to_dict()
    else:
      provenance = self.provenance

    created_by: None | str | Unset
    if isinstance(self.created_by, Unset):
      created_by = UNSET
    else:
      created_by = self.created_by

    created_at: None | str | Unset
    if isinstance(self.created_at, Unset):
      created_at = UNSET
    elif isinstance(self.created_at, datetime.datetime):
      created_at = self.created_at.isoformat()
    else:
      created_at = self.created_at

    updated_at: None | str | Unset
    if isinstance(self.updated_at, Unset):
      updated_at = UNSET
    elif isinstance(self.updated_at, datetime.datetime):
      updated_at = self.updated_at.isoformat()
    else:
      updated_at = self.updated_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "text": text,
      }
    )
    if source is not UNSET:
      field_dict["source"] = source
    if memory_type is not UNSET:
      field_dict["memory_type"] = memory_type
    if tags is not UNSET:
      field_dict["tags"] = tags
    if source_ref is not UNSET:
      field_dict["source_ref"] = source_ref
    if provenance is not UNSET:
      field_dict["provenance"] = provenance
    if created_by is not UNSET:
      field_dict["created_by"] = created_by
    if created_at is not UNSET:
      field_dict["created_at"] = created_at
    if updated_at is not UNSET:
      field_dict["updated_at"] = updated_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.memory_record_provenance_type_0 import MemoryRecordProvenanceType0

    d = dict(src_dict)
    id = d.pop("id")

    text = d.pop("text")

    def _parse_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source = _parse_source(d.pop("source", UNSET))

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

    def _parse_provenance(data: object) -> MemoryRecordProvenanceType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        provenance_type_0 = MemoryRecordProvenanceType0.from_dict(data)

        return provenance_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(MemoryRecordProvenanceType0 | None | Unset, data)

    provenance = _parse_provenance(d.pop("provenance", UNSET))

    def _parse_created_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    created_by = _parse_created_by(d.pop("created_by", UNSET))

    def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        created_at_type_0 = isoparse(data)

        return created_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    created_at = _parse_created_at(d.pop("created_at", UNSET))

    def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        updated_at_type_0 = isoparse(data)

        return updated_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

    memory_record = cls(
      id=id,
      text=text,
      source=source,
      memory_type=memory_type,
      tags=tags,
      source_ref=source_ref,
      provenance=provenance,
      created_by=created_by,
      created_at=created_at,
      updated_at=updated_at,
    )

    memory_record.additional_properties = d
    return memory_record

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
