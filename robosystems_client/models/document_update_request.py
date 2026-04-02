from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentUpdateRequest")


@_attrs_define
class DocumentUpdateRequest:
  """Update a document's metadata and/or content.

  Attributes:
      title (None | str | Unset):
      content (None | str | Unset):
      tags (list[str] | None | Unset):
      folder (None | str | Unset):
  """

  title: None | str | Unset = UNSET
  content: None | str | Unset = UNSET
  tags: list[str] | None | Unset = UNSET
  folder: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
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

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if title is not UNSET:
      field_dict["title"] = title
    if content is not UNSET:
      field_dict["content"] = content
    if tags is not UNSET:
      field_dict["tags"] = tags
    if folder is not UNSET:
      field_dict["folder"] = folder

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

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

    document_update_request = cls(
      title=title,
      content=content,
      tags=tags,
      folder=folder,
    )

    document_update_request.additional_properties = d
    return document_update_request

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
