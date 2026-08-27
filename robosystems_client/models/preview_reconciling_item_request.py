from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PreviewReconcilingItemRequest")


@_attrs_define
class PreviewReconcilingItemRequest:
  """Read what changed on a reconciling item, and what resolving it would do.

  Attributes:
      event_id (str): Event id (evt_ prefixed) to inspect
  """

  event_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_id = self.event_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    event_id = d.pop("event_id")

    preview_reconciling_item_request = cls(
      event_id=event_id,
    )

    preview_reconciling_item_request.additional_properties = d
    return preview_reconciling_item_request

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
