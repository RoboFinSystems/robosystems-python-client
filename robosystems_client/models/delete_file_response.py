from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteFileResponse")


@_attrs_define
class DeleteFileResponse:
  """
  Attributes:
      status (str): Deletion status
      file_id (str): Deleted file ID
      file_name (str): Deleted file name
      message (str): Operation message
  """

  status: str
  file_id: str
  file_name: str
  message: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    status = self.status

    file_id = self.file_id

    file_name = self.file_name

    message = self.message

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "status": status,
        "file_id": file_id,
        "file_name": file_name,
        "message": message,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    status = d.pop("status")

    file_id = d.pop("file_id")

    file_name = d.pop("file_name")

    message = d.pop("message")

    delete_file_response = cls(
      status=status,
      file_id=file_id,
      file_name=file_name,
      message=message,
    )

    delete_file_response.additional_properties = d
    return delete_file_response

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
