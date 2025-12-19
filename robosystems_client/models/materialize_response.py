from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaterializeResponse")


@_attrs_define
class MaterializeResponse:
  """Response for queued materialization operation.

  Example:
      {'graph_id': 'kg_abc123', 'message': 'Materialization queued. Monitor via SSE stream.', 'operation_id':
          '550e8400-e29b-41d4-a716-446655440000', 'status': 'queued'}

  Attributes:
      graph_id (str): Graph database identifier
      operation_id (str): SSE operation ID for progress tracking
      message (str): Human-readable status message
      status (str | Unset): Operation status Default: 'queued'.
  """

  graph_id: str
  operation_id: str
  message: str
  status: str | Unset = "queued"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    operation_id = self.operation_id

    message = self.message

    status = self.status

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "operation_id": operation_id,
        "message": message,
      }
    )
    if status is not UNSET:
      field_dict["status"] = status

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    operation_id = d.pop("operation_id")

    message = d.pop("message")

    status = d.pop("status", UNSET)

    materialize_response = cls(
      graph_id=graph_id,
      operation_id=operation_id,
      message=message,
      status=status,
    )

    materialize_response.additional_properties = d
    return materialize_response

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
