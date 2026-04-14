from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_envelope_status import OperationEnvelopeStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.operation_envelope_result_type_0 import OperationEnvelopeResultType0


T = TypeVar("T", bound="OperationEnvelope")


@_attrs_define
class OperationEnvelope:
  """Uniform response shape for every extensions operation endpoint.

  Every dispatch through `/extensions/{domain}/{graph_id}/operations/{op}`
  returns an envelope carrying an `op_<ULID>` operation_id. That id is the
  bridge to the platform's monitoring surface: pass it to
  `GET /v1/operations/{operation_id}/stream` (see `routers/operations.py`)
  to subscribe to SSE progress events. Sync commands complete in the
  envelope itself; async commands (`status: "pending"`, HTTP 202) hand off
  to a background worker and stream their tail through the same SSE
  endpoint until completion. Failed dispatches still mint an `operation_id`
  so the audit log and any partial SSE events stay correlatable.

  Fields:
  - `operation`: kebab-case command name (e.g. `close-period`)
  - `operation_id`: `op_`-prefixed ULID; always present, usable for audit
    correlation and — for async commands — SSE subscription via
    `/v1/operations/{operation_id}/stream`
  - `status`: `"completed"` (sync, HTTP 200), `"pending"` (async, HTTP 202),
    or `"failed"` (error responses)
  - `result`: the domain-specific payload (the original Pydantic response)
    or `None` for async/failed cases
  - `at`: ISO-8601 UTC timestamp of when the envelope was minted

      Attributes:
          operation (str): Kebab-case operation name
          operation_id (str): op_-prefixed ULID for audit and SSE correlation
          status (OperationEnvelopeStatus): Operation lifecycle state
          at (str): ISO-8601 UTC timestamp
          result (list[Any] | None | OperationEnvelopeResultType0 | Unset): Command-specific result payload
  """

  operation: str
  operation_id: str
  status: OperationEnvelopeStatus
  at: str
  result: list[Any] | None | OperationEnvelopeResultType0 | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.operation_envelope_result_type_0 import OperationEnvelopeResultType0

    operation = self.operation

    operation_id = self.operation_id

    status = self.status.value

    at = self.at

    result: dict[str, Any] | list[Any] | None | Unset
    if isinstance(self.result, Unset):
      result = UNSET
    elif isinstance(self.result, OperationEnvelopeResultType0):
      result = self.result.to_dict()
    elif isinstance(self.result, list):
      result = self.result

    else:
      result = self.result

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

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.operation_envelope_result_type_0 import OperationEnvelopeResultType0

    d = dict(src_dict)
    operation = d.pop("operation")

    operation_id = d.pop("operationId")

    status = OperationEnvelopeStatus(d.pop("status"))

    at = d.pop("at")

    def _parse_result(
      data: object,
    ) -> list[Any] | None | OperationEnvelopeResultType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        result_type_0 = OperationEnvelopeResultType0.from_dict(data)

        return result_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      try:
        if not isinstance(data, list):
          raise TypeError()
        result_type_1 = cast(list[Any], data)

        return result_type_1
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[Any] | None | OperationEnvelopeResultType0 | Unset, data)

    result = _parse_result(d.pop("result", UNSET))

    operation_envelope = cls(
      operation=operation,
      operation_id=operation_id,
      status=status,
      at=at,
      result=result,
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
