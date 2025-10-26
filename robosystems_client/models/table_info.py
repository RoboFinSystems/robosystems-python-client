from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableInfo")


@_attrs_define
class TableInfo:
  """
  Attributes:
      table_name (str): Table name
      row_count (int): Approximate row count
      file_count (Union[Unset, int]): Number of files Default: 0.
      total_size_bytes (Union[Unset, int]): Total size in bytes Default: 0.
      s3_location (Union[None, Unset, str]): S3 location for external tables
  """

  table_name: str
  row_count: int
  file_count: Union[Unset, int] = 0
  total_size_bytes: Union[Unset, int] = 0
  s3_location: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    table_name = self.table_name

    row_count = self.row_count

    file_count = self.file_count

    total_size_bytes = self.total_size_bytes

    s3_location: Union[None, Unset, str]
    if isinstance(self.s3_location, Unset):
      s3_location = UNSET
    else:
      s3_location = self.s3_location

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "table_name": table_name,
        "row_count": row_count,
      }
    )
    if file_count is not UNSET:
      field_dict["file_count"] = file_count
    if total_size_bytes is not UNSET:
      field_dict["total_size_bytes"] = total_size_bytes
    if s3_location is not UNSET:
      field_dict["s3_location"] = s3_location

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    table_name = d.pop("table_name")

    row_count = d.pop("row_count")

    file_count = d.pop("file_count", UNSET)

    total_size_bytes = d.pop("total_size_bytes", UNSET)

    def _parse_s3_location(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    s3_location = _parse_s3_location(d.pop("s3_location", UNSET))

    table_info = cls(
      table_name=table_name,
      row_count=row_count,
      file_count=file_count,
      total_size_bytes=total_size_bytes,
      s3_location=s3_location,
    )

    table_info.additional_properties = d
    return table_info

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
