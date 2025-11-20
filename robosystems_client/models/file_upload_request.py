from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileUploadRequest")


@_attrs_define
class FileUploadRequest:
  """
  Attributes:
      file_name (str): File name to upload
      content_type (str | Unset): File MIME type Default: 'application/x-parquet'.
      table_name (None | str | Unset): Table name to associate file with (required for first-class /files endpoint)
  """

  file_name: str
  content_type: str | Unset = "application/x-parquet"
  table_name: None | str | Unset = UNSET

  def to_dict(self) -> dict[str, Any]:
    file_name = self.file_name

    content_type = self.content_type

    table_name: None | str | Unset
    if isinstance(self.table_name, Unset):
      table_name = UNSET
    else:
      table_name = self.table_name

    field_dict: dict[str, Any] = {}

    field_dict.update(
      {
        "file_name": file_name,
      }
    )
    if content_type is not UNSET:
      field_dict["content_type"] = content_type
    if table_name is not UNSET:
      field_dict["table_name"] = table_name

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    file_name = d.pop("file_name")

    content_type = d.pop("content_type", UNSET)

    def _parse_table_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    table_name = _parse_table_name(d.pop("table_name", UNSET))

    file_upload_request = cls(
      file_name=file_name,
      content_type=content_type,
      table_name=table_name,
    )

    return file_upload_request
