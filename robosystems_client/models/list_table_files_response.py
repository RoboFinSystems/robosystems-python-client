from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.file_info import FileInfo


T = TypeVar("T", bound="ListTableFilesResponse")


@_attrs_define
class ListTableFilesResponse:
  """
  Attributes:
      graph_id (str): Graph database identifier
      table_name (str): Table name
      files (list['FileInfo']): List of files in the table
      total_files (int): Total number of files
      total_size_bytes (int): Total size of all files in bytes
  """

  graph_id: str
  table_name: str
  files: list["FileInfo"]
  total_files: int
  total_size_bytes: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    table_name = self.table_name

    files = []
    for files_item_data in self.files:
      files_item = files_item_data.to_dict()
      files.append(files_item)

    total_files = self.total_files

    total_size_bytes = self.total_size_bytes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "table_name": table_name,
        "files": files,
        "total_files": total_files,
        "total_size_bytes": total_size_bytes,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.file_info import FileInfo

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    table_name = d.pop("table_name")

    files = []
    _files = d.pop("files")
    for files_item_data in _files:
      files_item = FileInfo.from_dict(files_item_data)

      files.append(files_item)

    total_files = d.pop("total_files")

    total_size_bytes = d.pop("total_size_bytes")

    list_table_files_response = cls(
      graph_id=graph_id,
      table_name=table_name,
      files=files,
      total_files=total_files,
      total_size_bytes=total_size_bytes,
    )

    list_table_files_response.additional_properties = d
    return list_table_files_response

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
