from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.document_evidence import DocumentEvidence
  from ..models.document_file_info import DocumentFileInfo


T = TypeVar("T", bound="DocumentDetailResponse")


@_attrs_define
class DocumentDetailResponse:
  """Full document detail with raw content.

  Attributes:
      id (str):
      graph_id (str):
      user_id (str):
      title (str):
      content (str):
      source_type (str):
      sections_indexed (int):
      created_at (str):
      updated_at (str):
      tags (list[str] | None | Unset):
      folder (None | str | Unset):
      external_id (None | str | Unset):
      source_provider (None | str | Unset):
      file (DocumentFileInfo | None | Unset): The stored file, for a document that is one; its `content` is empty.
          Download it from `GET /documents/{document_id}/file`.
      evidence_for (list[DocumentEvidence] | Unset): The live events that name this document as their evidence (an
          invoice, a bill, a statement balance), newest first, at most 50. While any are listed, the document cannot be
          deleted.
  """

  id: str
  graph_id: str
  user_id: str
  title: str
  content: str
  source_type: str
  sections_indexed: int
  created_at: str
  updated_at: str
  tags: list[str] | None | Unset = UNSET
  folder: None | str | Unset = UNSET
  external_id: None | str | Unset = UNSET
  source_provider: None | str | Unset = UNSET
  file: DocumentFileInfo | None | Unset = UNSET
  evidence_for: list[DocumentEvidence] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.document_file_info import DocumentFileInfo

    id = self.id

    graph_id = self.graph_id

    user_id = self.user_id

    title = self.title

    content = self.content

    source_type = self.source_type

    sections_indexed = self.sections_indexed

    created_at = self.created_at

    updated_at = self.updated_at

    tags: list[str] | None | Unset
    if isinstance(self.tags, Unset):
      tags = UNSET
    elif isinstance(self.tags, list):
      tags = self.tags

    else:
      tags = self.tags

    folder: None | str | Unset
    if isinstance(self.folder, Unset):
      folder = UNSET
    else:
      folder = self.folder

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

    source_provider: None | str | Unset
    if isinstance(self.source_provider, Unset):
      source_provider = UNSET
    else:
      source_provider = self.source_provider

    file: dict[str, Any] | None | Unset
    if isinstance(self.file, Unset):
      file = UNSET
    elif isinstance(self.file, DocumentFileInfo):
      file = self.file.to_dict()
    else:
      file = self.file

    evidence_for: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.evidence_for, Unset):
      evidence_for = []
      for evidence_for_item_data in self.evidence_for:
        evidence_for_item = evidence_for_item_data.to_dict()
        evidence_for.append(evidence_for_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "graph_id": graph_id,
        "user_id": user_id,
        "title": title,
        "content": content,
        "source_type": source_type,
        "sections_indexed": sections_indexed,
        "created_at": created_at,
        "updated_at": updated_at,
      }
    )
    if tags is not UNSET:
      field_dict["tags"] = tags
    if folder is not UNSET:
      field_dict["folder"] = folder
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if source_provider is not UNSET:
      field_dict["source_provider"] = source_provider
    if file is not UNSET:
      field_dict["file"] = file
    if evidence_for is not UNSET:
      field_dict["evidence_for"] = evidence_for

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.document_evidence import DocumentEvidence
    from ..models.document_file_info import DocumentFileInfo

    d = dict(src_dict)
    id = d.pop("id")

    graph_id = d.pop("graph_id")

    user_id = d.pop("user_id")

    title = d.pop("title")

    content = d.pop("content")

    source_type = d.pop("source_type")

    sections_indexed = d.pop("sections_indexed")

    created_at = d.pop("created_at")

    updated_at = d.pop("updated_at")

    def _parse_tags(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        tags_type_0 = cast(list[str], data)

        return tags_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    tags = _parse_tags(d.pop("tags", UNSET))

    def _parse_folder(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    folder = _parse_folder(d.pop("folder", UNSET))

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

    def _parse_source_provider(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source_provider = _parse_source_provider(d.pop("source_provider", UNSET))

    def _parse_file(data: object) -> DocumentFileInfo | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        file_type_0 = DocumentFileInfo.from_dict(data)

        return file_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(DocumentFileInfo | None | Unset, data)

    file = _parse_file(d.pop("file", UNSET))

    _evidence_for = d.pop("evidence_for", UNSET)
    evidence_for: list[DocumentEvidence] | Unset = UNSET
    if _evidence_for is not UNSET:
      evidence_for = []
      for evidence_for_item_data in _evidence_for:
        evidence_for_item = DocumentEvidence.from_dict(evidence_for_item_data)

        evidence_for.append(evidence_for_item)

    document_detail_response = cls(
      id=id,
      graph_id=graph_id,
      user_id=user_id,
      title=title,
      content=content,
      source_type=source_type,
      sections_indexed=sections_indexed,
      created_at=created_at,
      updated_at=updated_at,
      tags=tags,
      folder=folder,
      external_id=external_id,
      source_provider=source_provider,
      file=file,
      evidence_for=evidence_for,
    )

    document_detail_response.additional_properties = d
    return document_detail_response

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
