from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.document_file_info import DocumentFileInfo


T = TypeVar("T", bound="DocumentFileDownloadResponse")


@_attrs_define
class DocumentFileDownloadResponse:
  """A short-lived link to a stored document file.

  Attributes:
      document_id (str):
      download_url (str): Presigned URL to GET the file.
      expires_in (int): Seconds until the URL expires.
      file (DocumentFileInfo): The stored file behind a document, when it is one.
  """

  document_id: str
  download_url: str
  expires_in: int
  file: DocumentFileInfo
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    document_id = self.document_id

    download_url = self.download_url

    expires_in = self.expires_in

    file = self.file.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "document_id": document_id,
        "download_url": download_url,
        "expires_in": expires_in,
        "file": file,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.document_file_info import DocumentFileInfo

    d = dict(src_dict)
    document_id = d.pop("document_id")

    download_url = d.pop("download_url")

    expires_in = d.pop("expires_in")

    file = DocumentFileInfo.from_dict(d.pop("file"))

    document_file_download_response = cls(
      document_id=document_id,
      download_url=download_url,
      expires_in=expires_in,
      file=file,
    )

    document_file_download_response.additional_properties = d
    return document_file_download_response

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
