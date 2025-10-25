from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileUpdateRequest")


@_attrs_define
class FileUpdateRequest:
  """
  Attributes:
      file_size_bytes (int): Actual uploaded file size in bytes
      row_count (Union[None, Unset, int]): Number of rows in the file
  """

  file_size_bytes: int
  row_count: Union[None, Unset, int] = UNSET

  def to_dict(self) -> dict[str, Any]:
    file_size_bytes = self.file_size_bytes

    row_count: Union[None, Unset, int]
    if isinstance(self.row_count, Unset):
      row_count = UNSET
    else:
      row_count = self.row_count

    field_dict: dict[str, Any] = {}

    field_dict.update(
      {
        "file_size_bytes": file_size_bytes,
      }
    )
    if row_count is not UNSET:
      field_dict["row_count"] = row_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    file_size_bytes = d.pop("file_size_bytes")

    def _parse_row_count(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    row_count = _parse_row_count(d.pop("row_count", UNSET))

    file_update_request = cls(
      file_size_bytes=file_size_bytes,
      row_count=row_count,
    )

    return file_update_request
