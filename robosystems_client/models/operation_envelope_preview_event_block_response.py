from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_envelope_preview_event_block_response_status import (
  OperationEnvelopePreviewEventBlockResponseStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.preview_event_block_response import PreviewEventBlockResponse


T = TypeVar("T", bound="OperationEnvelopePreviewEventBlockResponse")


@_attrs_define
class OperationEnvelopePreviewEventBlockResponse:
  """
  Attributes:
      operation (str): Kebab-case operation name
      operation_id (str): op_-prefixed ULID for audit and SSE correlation
      status (OperationEnvelopePreviewEventBlockResponseStatus): Operation lifecycle state
      at (str): ISO-8601 UTC timestamp
      result (None | PreviewEventBlockResponse | Unset): Command-specific result payload
      created_by (None | str | Unset): User ID that initiated the operation (null for legacy callers)
      idempotent_replay (bool | Unset): True when this envelope came from the idempotency cache — the underlying
          command did not execute again. False on fresh executions. Default: False.
  """

  operation: str
  operation_id: str
  status: OperationEnvelopePreviewEventBlockResponseStatus
  at: str
  result: None | PreviewEventBlockResponse | Unset = UNSET
  created_by: None | str | Unset = UNSET
  idempotent_replay: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.preview_event_block_response import PreviewEventBlockResponse

    operation = self.operation

    operation_id = self.operation_id

    status = self.status.value

    at = self.at

    result: dict[str, Any] | None | Unset
    if isinstance(self.result, Unset):
      result = UNSET
    elif isinstance(self.result, PreviewEventBlockResponse):
      result = self.result.to_dict()
    else:
      result = self.result

    created_by: None | str | Unset
    if isinstance(self.created_by, Unset):
      created_by = UNSET
    else:
      created_by = self.created_by

    idempotent_replay = self.idempotent_replay

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "operation": operation,
        "operationId": operation_id,
        "status": status,
        "at": at,
      }
    )
    if result is not UNSET:
      field_dict["result"] = result
    if created_by is not UNSET:
      field_dict["createdBy"] = created_by
    if idempotent_replay is not UNSET:
      field_dict["idempotentReplay"] = idempotent_replay

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.preview_event_block_response import PreviewEventBlockResponse

    d = dict(src_dict)
    operation = d.pop("operation")

    operation_id = d.pop("operationId")

    status = OperationEnvelopePreviewEventBlockResponseStatus(d.pop("status"))

    at = d.pop("at")

    def _parse_result(data: object) -> None | PreviewEventBlockResponse | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        result_type_0 = PreviewEventBlockResponse.from_dict(data)

        return result_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | PreviewEventBlockResponse | Unset, data)

    result = _parse_result(d.pop("result", UNSET))

    def _parse_created_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    created_by = _parse_created_by(d.pop("createdBy", UNSET))

    idempotent_replay = d.pop("idempotentReplay", UNSET)

    operation_envelope_preview_event_block_response = cls(
      operation=operation,
      operation_id=operation_id,
      status=status,
      at=at,
      result=result,
      created_by=created_by,
      idempotent_replay=idempotent_replay,
    )

    operation_envelope_preview_event_block_response.additional_properties = d
    return operation_envelope_preview_event_block_response

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
