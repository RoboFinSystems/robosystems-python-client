from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphMetadataResult")


@_attrs_define
class GraphMetadataResult:
  """Result payload for the update-graph-metadata operation.

  Attributes:
      graph_id (str): Graph the metadata belongs to
      graph_name (str): Display name after the update
      description (str | Unset): Description after the update ('' when unset) Default: ''.
      tags (list[str] | Unset): Tags after the update (empty when unset)
      updated_fields (list[str] | Unset): Fields this call actually changed. Empty when the submitted values already
          matched what was stored.
  """

  graph_id: str
  graph_name: str
  description: str | Unset = ""
  tags: list[str] | Unset = UNSET
  updated_fields: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    graph_name = self.graph_name

    description = self.description

    tags: list[str] | Unset = UNSET
    if not isinstance(self.tags, Unset):
      tags = self.tags

    updated_fields: list[str] | Unset = UNSET
    if not isinstance(self.updated_fields, Unset):
      updated_fields = self.updated_fields

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "graph_name": graph_name,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if tags is not UNSET:
      field_dict["tags"] = tags
    if updated_fields is not UNSET:
      field_dict["updated_fields"] = updated_fields

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    graph_name = d.pop("graph_name")

    description = d.pop("description", UNSET)

    tags = cast(list[str], d.pop("tags", UNSET))

    updated_fields = cast(list[str], d.pop("updated_fields", UNSET))

    graph_metadata_result = cls(
      graph_id=graph_id,
      graph_name=graph_name,
      description=description,
      tags=tags,
      updated_fields=updated_fields,
    )

    graph_metadata_result.additional_properties = d
    return graph_metadata_result

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
