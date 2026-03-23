from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.bulk_document_upload_response_errors_type_0_item import (
    BulkDocumentUploadResponseErrorsType0Item,
  )
  from ..models.document_upload_response import DocumentUploadResponse


T = TypeVar("T", bound="BulkDocumentUploadResponse")


@_attrs_define
class BulkDocumentUploadResponse:
  """Response from bulk document upload.

  Attributes:
      total_documents (int):
      total_sections_indexed (int):
      results (list[DocumentUploadResponse]):
      errors (list[BulkDocumentUploadResponseErrorsType0Item] | None | Unset):
  """

  total_documents: int
  total_sections_indexed: int
  results: list[DocumentUploadResponse]
  errors: list[BulkDocumentUploadResponseErrorsType0Item] | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    total_documents = self.total_documents

    total_sections_indexed = self.total_sections_indexed

    results = []
    for results_item_data in self.results:
      results_item = results_item_data.to_dict()
      results.append(results_item)

    errors: list[dict[str, Any]] | None | Unset
    if isinstance(self.errors, Unset):
      errors = UNSET
    elif isinstance(self.errors, list):
      errors = []
      for errors_type_0_item_data in self.errors:
        errors_type_0_item = errors_type_0_item_data.to_dict()
        errors.append(errors_type_0_item)

    else:
      errors = self.errors

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "total_documents": total_documents,
        "total_sections_indexed": total_sections_indexed,
        "results": results,
      }
    )
    if errors is not UNSET:
      field_dict["errors"] = errors

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.bulk_document_upload_response_errors_type_0_item import (
      BulkDocumentUploadResponseErrorsType0Item,
    )
    from ..models.document_upload_response import DocumentUploadResponse

    d = dict(src_dict)
    total_documents = d.pop("total_documents")

    total_sections_indexed = d.pop("total_sections_indexed")

    results = []
    _results = d.pop("results")
    for results_item_data in _results:
      results_item = DocumentUploadResponse.from_dict(results_item_data)

      results.append(results_item)

    def _parse_errors(
      data: object,
    ) -> list[BulkDocumentUploadResponseErrorsType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        errors_type_0 = []
        _errors_type_0 = data
        for errors_type_0_item_data in _errors_type_0:
          errors_type_0_item = BulkDocumentUploadResponseErrorsType0Item.from_dict(
            errors_type_0_item_data
          )

          errors_type_0.append(errors_type_0_item)

        return errors_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[BulkDocumentUploadResponseErrorsType0Item] | None | Unset, data)

    errors = _parse_errors(d.pop("errors", UNSET))

    bulk_document_upload_response = cls(
      total_documents=total_documents,
      total_sections_indexed=total_sections_indexed,
      results=results,
      errors=errors,
    )

    bulk_document_upload_response.additional_properties = d
    return bulk_document_upload_response

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
