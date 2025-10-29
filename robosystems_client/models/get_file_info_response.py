from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFileInfoResponse")


@_attrs_define
class GetFileInfoResponse:
  """
  Attributes:
      file_id (str): Unique file identifier
      graph_id (str): Graph database identifier
      table_id (str): Table identifier
      file_name (str): Original file name
      file_format (str): File format (parquet, csv, etc.)
      size_bytes (int): File size in bytes
      upload_status (str): Current upload status
      upload_method (str): Upload method used
      s3_key (str): S3 object key
      table_name (Union[None, Unset, str]): Table name
      row_count (Union[None, Unset, int]): Estimated row count
      created_at (Union[None, Unset, str]): File creation timestamp
      uploaded_at (Union[None, Unset, str]): File upload completion timestamp
  """

  file_id: str
  graph_id: str
  table_id: str
  file_name: str
  file_format: str
  size_bytes: int
  upload_status: str
  upload_method: str
  s3_key: str
  table_name: Union[None, Unset, str] = UNSET
  row_count: Union[None, Unset, int] = UNSET
  created_at: Union[None, Unset, str] = UNSET
  uploaded_at: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    file_id = self.file_id

    graph_id = self.graph_id

    table_id = self.table_id

    file_name = self.file_name

    file_format = self.file_format

    size_bytes = self.size_bytes

    upload_status = self.upload_status

    upload_method = self.upload_method

    s3_key = self.s3_key

    table_name: Union[None, Unset, str]
    if isinstance(self.table_name, Unset):
      table_name = UNSET
    else:
      table_name = self.table_name

    row_count: Union[None, Unset, int]
    if isinstance(self.row_count, Unset):
      row_count = UNSET
    else:
      row_count = self.row_count

    created_at: Union[None, Unset, str]
    if isinstance(self.created_at, Unset):
      created_at = UNSET
    else:
      created_at = self.created_at

    uploaded_at: Union[None, Unset, str]
    if isinstance(self.uploaded_at, Unset):
      uploaded_at = UNSET
    else:
      uploaded_at = self.uploaded_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "file_id": file_id,
        "graph_id": graph_id,
        "table_id": table_id,
        "file_name": file_name,
        "file_format": file_format,
        "size_bytes": size_bytes,
        "upload_status": upload_status,
        "upload_method": upload_method,
        "s3_key": s3_key,
      }
    )
    if table_name is not UNSET:
      field_dict["table_name"] = table_name
    if row_count is not UNSET:
      field_dict["row_count"] = row_count
    if created_at is not UNSET:
      field_dict["created_at"] = created_at
    if uploaded_at is not UNSET:
      field_dict["uploaded_at"] = uploaded_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    file_id = d.pop("file_id")

    graph_id = d.pop("graph_id")

    table_id = d.pop("table_id")

    file_name = d.pop("file_name")

    file_format = d.pop("file_format")

    size_bytes = d.pop("size_bytes")

    upload_status = d.pop("upload_status")

    upload_method = d.pop("upload_method")

    s3_key = d.pop("s3_key")

    def _parse_table_name(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    table_name = _parse_table_name(d.pop("table_name", UNSET))

    def _parse_row_count(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    row_count = _parse_row_count(d.pop("row_count", UNSET))

    def _parse_created_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    created_at = _parse_created_at(d.pop("created_at", UNSET))

    def _parse_uploaded_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    uploaded_at = _parse_uploaded_at(d.pop("uploaded_at", UNSET))

    get_file_info_response = cls(
      file_id=file_id,
      graph_id=graph_id,
      table_id=table_id,
      file_name=file_name,
      file_format=file_format,
      size_bytes=size_bytes,
      upload_status=upload_status,
      upload_method=upload_method,
      s3_key=s3_key,
      table_name=table_name,
      row_count=row_count,
      created_at=created_at,
      uploaded_at=uploaded_at,
    )

    get_file_info_response.additional_properties = d
    return get_file_info_response

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
