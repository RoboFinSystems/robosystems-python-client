from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentListItem")


@_attrs_define
class DocumentListItem:
  """A document in the document list.

  Attributes:
      document_title (str):
      section_count (int):
      source_type (str):
      folder (None | str | Unset):
      tags (list[str] | None | Unset):
      last_indexed (None | str | Unset):
  """

  document_title: str
  section_count: int
  source_type: str
  folder: None | str | Unset = UNSET
  tags: list[str] | None | Unset = UNSET
  last_indexed: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    document_title = self.document_title

    section_count = self.section_count

    source_type = self.source_type

    folder: None | str | Unset
    if isinstance(self.folder, Unset):
      folder = UNSET
    else:
      folder = self.folder

    tags: list[str] | None | Unset
    if isinstance(self.tags, Unset):
      tags = UNSET
    elif isinstance(self.tags, list):
      tags = self.tags

    else:
      tags = self.tags

    last_indexed: None | str | Unset
    if isinstance(self.last_indexed, Unset):
      last_indexed = UNSET
    else:
      last_indexed = self.last_indexed

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "document_title": document_title,
        "section_count": section_count,
        "source_type": source_type,
      }
    )
    if folder is not UNSET:
      field_dict["folder"] = folder
    if tags is not UNSET:
      field_dict["tags"] = tags
    if last_indexed is not UNSET:
      field_dict["last_indexed"] = last_indexed

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    document_title = d.pop("document_title")

    section_count = d.pop("section_count")

    source_type = d.pop("source_type")

    def _parse_folder(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    folder = _parse_folder(d.pop("folder", UNSET))

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

    def _parse_last_indexed(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    last_indexed = _parse_last_indexed(d.pop("last_indexed", UNSET))

    document_list_item = cls(
      document_title=document_title,
      section_count=section_count,
      source_type=source_type,
      folder=folder,
      tags=tags,
      last_indexed=last_indexed,
    )

    document_list_item.additional_properties = d
    return document_list_item

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
