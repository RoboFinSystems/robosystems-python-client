from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_envelope_status import OperationEnvelopeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OperationEnvelope")


@_attrs_define
class OperationEnvelope:
  """Uniform response shape for every operation endpoint.

  Every dispatch carries an ``op_<ULID>`` operation_id, which is the bridge
  to the monitoring surface: pass it to
  ``GET /v1/operations/{operation_id}/stream`` (see ``routers/operations.py``)
  to subscribe to SSE progress events. Sync commands complete in the envelope
  itself (``status: "completed"``, HTTP 200); async commands
  (``status: "pending"``, HTTP 202) hand off to a background worker and stream
  their tail through that SSE endpoint. Failed dispatches still mint an
  ``operation_id`` so the audit log and any partial SSE events stay
  correlatable.

  ``TResult`` parameterizes ``result`` so per-op response shapes surface in
  OpenAPI. Operations that pin ``OperationSpec.result_type`` get
  ``OperationEnvelope[YourEnvelope]`` as their response model; the rest keep
  the default ``Any`` shape (``result: any | null`` on the wire).

      Attributes:
          operation (str): Kebab-case operation name
          operation_id (str): op_-prefixed ULID for audit and SSE correlation
          status (OperationEnvelopeStatus): Operation lifecycle state
          at (str): ISO-8601 UTC timestamp
          result (Any | None | Unset): Command-specific result payload
          created_by (None | str | Unset): User ID that initiated the operation (null for legacy callers)
          idempotent_replay (bool | Unset): True when this envelope came from the idempotency cache — the underlying
              command did not execute again. False on fresh executions. Default: False.
  """

  operation: str
  operation_id: str
  status: OperationEnvelopeStatus
  at: str
  result: Any | None | Unset = UNSET
  created_by: None | str | Unset = UNSET
  idempotent_replay: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    operation = self.operation

    operation_id = self.operation_id

    status = self.status.value

    at = self.at

    result: Any | None | Unset
    if isinstance(self.result, Unset):
      result = UNSET
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
    d = dict(src_dict)
    operation = d.pop("operation")

    operation_id = d.pop("operationId")

    status = OperationEnvelopeStatus(d.pop("status"))

    at = d.pop("at")

    def _parse_result(data: object) -> Any | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Any | None | Unset, data)

    result = _parse_result(d.pop("result", UNSET))

    def _parse_created_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    created_by = _parse_created_by(d.pop("createdBy", UNSET))

    idempotent_replay = d.pop("idempotentReplay", UNSET)

    operation_envelope = cls(
      operation=operation,
      operation_id=operation_id,
      status=status,
      at=at,
      result=result,
      created_by=created_by,
      idempotent_replay=idempotent_replay,
    )

    operation_envelope.additional_properties = d
    return operation_envelope

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
