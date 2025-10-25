from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileUploadResponse")


@_attrs_define
class FileUploadResponse:
  """
  Attributes:
      upload_url (str): Presigned S3 upload URL
      expires_in (int): URL expiration time in seconds
      file_id (str): File tracking ID
      s3_key (str): S3 object key
  """

  upload_url: str
  expires_in: int
  file_id: str
  s3_key: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    upload_url = self.upload_url

    expires_in = self.expires_in

    file_id = self.file_id

    s3_key = self.s3_key

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "upload_url": upload_url,
        "expires_in": expires_in,
        "file_id": file_id,
        "s3_key": s3_key,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    upload_url = d.pop("upload_url")

    expires_in = d.pop("expires_in")

    file_id = d.pop("file_id")

    s3_key = d.pop("s3_key")

    file_upload_response = cls(
      upload_url=upload_url,
      expires_in=expires_in,
      file_id=file_id,
      s3_key=s3_key,
    )

    file_upload_response.additional_properties = d
    return file_upload_response

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
