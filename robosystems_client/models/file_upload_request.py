from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileUploadRequest")


@_attrs_define
class FileUploadRequest:
  """
  Attributes:
      file_name (str): File name to upload
      content_type (Union[Unset, str]): File MIME type Default: 'application/x-parquet'.
  """

  file_name: str
  content_type: Union[Unset, str] = "application/x-parquet"

  def to_dict(self) -> dict[str, Any]:
    file_name = self.file_name

    content_type = self.content_type

    field_dict: dict[str, Any] = {}

    field_dict.update(
      {
        "file_name": file_name,
      }
    )
    if content_type is not UNSET:
      field_dict["content_type"] = content_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    file_name = d.pop("file_name")

    content_type = d.pop("content_type", UNSET)

    file_upload_request = cls(
      file_name=file_name,
      content_type=content_type,
    )

    return file_upload_request
