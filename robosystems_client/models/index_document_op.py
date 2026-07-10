from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexDocumentOp")


@_attrs_define
class IndexDocumentOp:
  """Body for index-document (corpus content-op).

  Create a new document when ``document_id`` is absent; update the named
  document (partial — only supplied fields) when present.

      Attributes:
          document_id (None | str | Unset): Present → update that document; absent → create a new one
          title (None | str | Unset): Required when creating
          content (None | str | Unset): Required when creating
          tags (list[str] | None | Unset): Optional labels
          folder (None | str | Unset): Optional folder
          external_id (None | str | Unset): Upsert key (create): re-indexing the same id replaces
  """

  document_id: None | str | Unset = UNSET
  title: None | str | Unset = UNSET
  content: None | str | Unset = UNSET
  tags: list[str] | None | Unset = UNSET
  folder: None | str | Unset = UNSET
  external_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    document_id: None | str | Unset
    if isinstance(self.document_id, Unset):
      document_id = UNSET
    else:
      document_id = self.document_id

    title: None | str | Unset
    if isinstance(self.title, Unset):
      title = UNSET
    else:
      title = self.title

    content: None | str | Unset
    if isinstance(self.content, Unset):
      content = UNSET
    else:
      content = self.content

    tags: list[str] | None | Unset
    if isinstance(self.tags, Unset):
      tags = UNSET
    elif isinstance(self.tags, list):
      tags = self.tags

    else:
      tags = self.tags

    folder: None | str | Unset
    if isinstance(self.folder, Unset):
      folder = UNSET
    else:
      folder = self.folder

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if document_id is not UNSET:
      field_dict["document_id"] = document_id
    if title is not UNSET:
      field_dict["title"] = title
    if content is not UNSET:
      field_dict["content"] = content
    if tags is not UNSET:
      field_dict["tags"] = tags
    if folder is not UNSET:
      field_dict["folder"] = folder
    if external_id is not UNSET:
      field_dict["external_id"] = external_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_document_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    document_id = _parse_document_id(d.pop("document_id", UNSET))

    def _parse_title(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    title = _parse_title(d.pop("title", UNSET))

    def _parse_content(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    content = _parse_content(d.pop("content", UNSET))

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

    def _parse_folder(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    folder = _parse_folder(d.pop("folder", UNSET))

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

    index_document_op = cls(
      document_id=document_id,
      title=title,
      content=content,
      tags=tags,
      folder=folder,
      external_id=external_id,
    )

    index_document_op.additional_properties = d
    return index_document_op

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
