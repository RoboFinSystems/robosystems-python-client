from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DocumentEvidence")


@_attrs_define
class DocumentEvidence:
  """A live event on the books that names the document as its evidence.

  Attributes:
      event_id (str):
      event_type (str):
      status (str):
      occurred_at (str):
  """

  event_id: str
  event_type: str
  status: str
  occurred_at: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_id = self.event_id

    event_type = self.event_type

    status = self.status

    occurred_at = self.occurred_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
        "event_type": event_type,
        "status": status,
        "occurred_at": occurred_at,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    event_id = d.pop("event_id")

    event_type = d.pop("event_type")

    status = d.pop("status")

    occurred_at = d.pop("occurred_at")

    document_evidence = cls(
      event_id=event_id,
      event_type=event_type,
      status=status,
      occurred_at=occurred_at,
    )

    document_evidence.additional_properties = d
    return document_evidence

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
