from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.document_upload_request import DocumentUploadRequest


T = TypeVar("T", bound="BulkDocumentUploadRequest")


@_attrs_define
class BulkDocumentUploadRequest:
  """Bulk upload multiple markdown documents.

  Attributes:
      documents (list[DocumentUploadRequest]): Documents to upload (max 50)
  """

  documents: list[DocumentUploadRequest]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    documents = []
    for documents_item_data in self.documents:
      documents_item = documents_item_data.to_dict()
      documents.append(documents_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "documents": documents,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.document_upload_request import DocumentUploadRequest

    d = dict(src_dict)
    documents = []
    _documents = d.pop("documents")
    for documents_item_data in _documents:
      documents_item = DocumentUploadRequest.from_dict(documents_item_data)

      documents.append(documents_item)

    bulk_document_upload_request = cls(
      documents=documents,
    )

    bulk_document_upload_request.additional_properties = d
    return bulk_document_upload_request

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
