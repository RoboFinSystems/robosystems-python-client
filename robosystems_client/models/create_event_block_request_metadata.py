from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateEventBlockRequestMetadata")


@_attrs_define
class CreateEventBlockRequestMetadata:
  """Free-form payload, opaque to the event surface. When `apply_handlers=True`, the matched handler's metadata schema
  validates this dict — required keys depend on the handler registered for `event_type`. Use `preview-event-block` to
  discover the expected shape without writing.

  """

  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    create_event_block_request_metadata = cls()

    create_event_block_request_metadata.additional_properties = d
    return create_event_block_request_metadata

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
