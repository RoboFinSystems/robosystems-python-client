from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.document_file_info import DocumentFileInfo


T = TypeVar("T", bound="DocumentListItem")


@_attrs_define
class DocumentListItem:
  """A document in the document list.

  Attributes:
      id (str):
      document_title (str):
      section_count (int):
      source_type (str):
      created_at (str):
      updated_at (str):
      folder (None | str | Unset):
      tags (list[str] | None | Unset):
      file (DocumentFileInfo | None | Unset): The stored file, for a document that is one.
  """

  id: str
  document_title: str
  section_count: int
  source_type: str
  created_at: str
  updated_at: str
  folder: None | str | Unset = UNSET
  tags: list[str] | None | Unset = UNSET
  file: DocumentFileInfo | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.document_file_info import DocumentFileInfo

    id = self.id

    document_title = self.document_title

    section_count = self.section_count

    source_type = self.source_type

    created_at = self.created_at

    updated_at = self.updated_at

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

    file: dict[str, Any] | None | Unset
    if isinstance(self.file, Unset):
      file = UNSET
    elif isinstance(self.file, DocumentFileInfo):
      file = self.file.to_dict()
    else:
      file = self.file

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "document_title": document_title,
        "section_count": section_count,
        "source_type": source_type,
        "created_at": created_at,
        "updated_at": updated_at,
      }
    )
    if folder is not UNSET:
      field_dict["folder"] = folder
    if tags is not UNSET:
      field_dict["tags"] = tags
    if file is not UNSET:
      field_dict["file"] = file

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.document_file_info import DocumentFileInfo

    d = dict(src_dict)
    id = d.pop("id")

    document_title = d.pop("document_title")

    section_count = d.pop("section_count")

    source_type = d.pop("source_type")

    created_at = d.pop("created_at")

    updated_at = d.pop("updated_at")

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

    def _parse_file(data: object) -> DocumentFileInfo | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        file_type_0 = DocumentFileInfo.from_dict(data)

        return file_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(DocumentFileInfo | None | Unset, data)

    file = _parse_file(d.pop("file", UNSET))

    document_list_item = cls(
      id=id,
      document_title=document_title,
      section_count=section_count,
      source_type=source_type,
      created_at=created_at,
      updated_at=updated_at,
      folder=folder,
      tags=tags,
      file=file,
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
