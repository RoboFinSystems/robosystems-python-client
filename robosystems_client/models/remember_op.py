from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.remember_op_provenance_type_0 import RememberOpProvenanceType0


T = TypeVar("T", bound="RememberOp")


@_attrs_define
class RememberOp:
  """Body for the remember operation (write a semantic memory).

  Attributes:
      text (str): Memory content
      source (str | Unset): Origin of the memory Default: 'api'.
      memory_type (str | Unset): Freeform classifier Default: 'note'.
      tags (list[str] | None | Unset): Optional labels
      source_ref (None | str | Unset): Optional external reference/URI
      provenance (None | RememberOpProvenanceType0 | Unset): Opaque provenance metadata
  """

  text: str
  source: str | Unset = "api"
  memory_type: str | Unset = "note"
  tags: list[str] | None | Unset = UNSET
  source_ref: None | str | Unset = UNSET
  provenance: None | RememberOpProvenanceType0 | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.remember_op_provenance_type_0 import RememberOpProvenanceType0

    text = self.text

    source = self.source

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
    elif isinstance(self.provenance, RememberOpProvenanceType0):
      provenance = self.provenance.to_dict()
    else:
      provenance = self.provenance

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
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

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.remember_op_provenance_type_0 import RememberOpProvenanceType0

    d = dict(src_dict)
    text = d.pop("text")

    source = d.pop("source", UNSET)

    memory_type = d.pop("memory_type", UNSET)

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

    def _parse_provenance(data: object) -> None | RememberOpProvenanceType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        provenance_type_0 = RememberOpProvenanceType0.from_dict(data)

        return provenance_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | RememberOpProvenanceType0 | Unset, data)

    provenance = _parse_provenance(d.pop("provenance", UNSET))

    remember_op = cls(
      text=text,
      source=source,
      memory_type=memory_type,
      tags=tags,
      source_ref=source_ref,
      provenance=provenance,
    )

    remember_op.additional_properties = d
    return remember_op

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
