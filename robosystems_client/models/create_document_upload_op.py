from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_document_upload_op_content_type import (
  CreateDocumentUploadOpContentType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDocumentUploadOp")


@_attrs_define
class CreateDocumentUploadOp:
  """Body for create-document-upload: where to upload a document's file.

  Attributes:
      file_name (str): The file's name, ending in its type's extension (`.pdf`, `.png`, `.jpg` or `.jpeg`).
      content_type (CreateDocumentUploadOpContentType | Unset): The file's media type. Default:
          CreateDocumentUploadOpContentType.APPLICATIONPDF.
      file_size_bytes (int | None | Unset): The file's exact size in bytes, at most 25 MB. When given it is signed
          into the upload URL, so an upload of any other size fails. Completing the upload checks the size either way.
  """

  file_name: str
  content_type: CreateDocumentUploadOpContentType | Unset = (
    CreateDocumentUploadOpContentType.APPLICATIONPDF
  )
  file_size_bytes: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    file_name = self.file_name

    content_type: str | Unset = UNSET
    if not isinstance(self.content_type, Unset):
      content_type = self.content_type.value

    file_size_bytes: int | None | Unset
    if isinstance(self.file_size_bytes, Unset):
      file_size_bytes = UNSET
    else:
      file_size_bytes = self.file_size_bytes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "file_name": file_name,
      }
    )
    if content_type is not UNSET:
      field_dict["content_type"] = content_type
    if file_size_bytes is not UNSET:
      field_dict["file_size_bytes"] = file_size_bytes

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    file_name = d.pop("file_name")

    _content_type = d.pop("content_type", UNSET)
    content_type: CreateDocumentUploadOpContentType | Unset
    if isinstance(_content_type, Unset):
      content_type = UNSET
    else:
      content_type = CreateDocumentUploadOpContentType(_content_type)

    def _parse_file_size_bytes(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    file_size_bytes = _parse_file_size_bytes(d.pop("file_size_bytes", UNSET))

    create_document_upload_op = cls(
      file_name=file_name,
      content_type=content_type,
      file_size_bytes=file_size_bytes,
    )

    create_document_upload_op.additional_properties = d
    return create_document_upload_op

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
