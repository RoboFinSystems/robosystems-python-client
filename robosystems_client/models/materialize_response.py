from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.materialize_response_limit_check_type_0 import (
    MaterializeResponseLimitCheckType0,
  )


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
      limit_check (MaterializeResponseLimitCheckType0 | None | Unset): Limit check results (only present for dry_run
          requests)
  """

  graph_id: str
  operation_id: str
  message: str
  status: str | Unset = "queued"
  limit_check: MaterializeResponseLimitCheckType0 | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.materialize_response_limit_check_type_0 import (
      MaterializeResponseLimitCheckType0,
    )

    graph_id = self.graph_id

    operation_id = self.operation_id

    message = self.message

    status = self.status

    limit_check: dict[str, Any] | None | Unset
    if isinstance(self.limit_check, Unset):
      limit_check = UNSET
    elif isinstance(self.limit_check, MaterializeResponseLimitCheckType0):
      limit_check = self.limit_check.to_dict()
    else:
      limit_check = self.limit_check

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
    if limit_check is not UNSET:
      field_dict["limit_check"] = limit_check

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.materialize_response_limit_check_type_0 import (
      MaterializeResponseLimitCheckType0,
    )

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    operation_id = d.pop("operation_id")

    message = d.pop("message")

    status = d.pop("status", UNSET)

    def _parse_limit_check(
      data: object,
    ) -> MaterializeResponseLimitCheckType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        limit_check_type_0 = MaterializeResponseLimitCheckType0.from_dict(data)

        return limit_check_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(MaterializeResponseLimitCheckType0 | None | Unset, data)

    limit_check = _parse_limit_check(d.pop("limit_check", UNSET))

    materialize_response = cls(
      graph_id=graph_id,
      operation_id=operation_id,
      message=message,
      status=status,
      limit_check=limit_check,
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
