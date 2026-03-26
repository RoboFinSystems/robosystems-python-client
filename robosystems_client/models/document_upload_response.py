from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DocumentUploadResponse")


@_attrs_define
class DocumentUploadResponse:
  """Response from document upload.

  Attributes:
      document_id (str):
      sections_indexed (int):
      total_content_length (int):
      section_ids (list[str]):
  """

  document_id: str
  sections_indexed: int
  total_content_length: int
  section_ids: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    document_id = self.document_id

    sections_indexed = self.sections_indexed

    total_content_length = self.total_content_length

    section_ids = self.section_ids

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "document_id": document_id,
        "sections_indexed": sections_indexed,
        "total_content_length": total_content_length,
        "section_ids": section_ids,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    document_id = d.pop("document_id")

    sections_indexed = d.pop("sections_indexed")

    total_content_length = d.pop("total_content_length")

    section_ids = cast(list[str], d.pop("section_ids"))

    document_upload_response = cls(
      document_id=document_id,
      sections_indexed=sections_indexed,
      total_content_length=total_content_length,
      section_ids=section_ids,
    )

    document_upload_response.additional_properties = d
    return document_upload_response

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
