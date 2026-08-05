from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentLimits")


@_attrs_define
class DocumentLimits:
  """Knowledge-base document usage against the tier's cap.

  Attributes:
      current_count (int): Uploaded documents currently stored for this graph
      approaching_limit (bool): Whether approaching document limit (>80%)
      max_documents (int | None | Unset): Maximum uploaded documents for this tier (null when uncapped)
  """

  current_count: int
  approaching_limit: bool
  max_documents: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    current_count = self.current_count

    approaching_limit = self.approaching_limit

    max_documents: int | None | Unset
    if isinstance(self.max_documents, Unset):
      max_documents = UNSET
    else:
      max_documents = self.max_documents

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "current_count": current_count,
        "approaching_limit": approaching_limit,
      }
    )
    if max_documents is not UNSET:
      field_dict["max_documents"] = max_documents

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    current_count = d.pop("current_count")

    approaching_limit = d.pop("approaching_limit")

    def _parse_max_documents(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    max_documents = _parse_max_documents(d.pop("max_documents", UNSET))

    document_limits = cls(
      current_count=current_count,
      approaching_limit=approaching_limit,
      max_documents=max_documents,
    )

    document_limits.additional_properties = d
    return document_limits

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
