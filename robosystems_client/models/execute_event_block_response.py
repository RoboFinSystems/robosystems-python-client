from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.execute_event_block_response_qb_error_type_0 import (
    ExecuteEventBlockResponseQbErrorType0,
  )


T = TypeVar("T", bound="ExecuteEventBlockResponse")


@_attrs_define
class ExecuteEventBlockResponse:
  """Outcome of an `execute-event-block` call.

  Attributes:
      event_id (str): Echo of the event ID.
      status (str): Post-execute event status. `'classified'` when no write fired (native policy or no-op).
          `'committed'` when the QB write was in flight (intermediate state). `'fulfilled'` when QB accepted and local GL
          drafts were promoted to posted. `'pending'` when QB rejected — see `qb_error` for the rejection detail; retry
          after fixing the underlying issue.
      qb_external_id (None | str | Unset): QB-side transaction ID returned by the JournalEntry API. Null when no write
          fired (native policy) or when the write was rejected before getting an ID.
      qb_error (ExecuteEventBlockResponseQbErrorType0 | None | Unset): QB rejection detail when status='pending'.
          Shape: `{code, message, qb_response_at}`. Operator retries after fixing CoA mapping / amount validation /
          closed-period.
  """

  event_id: str
  status: str
  qb_external_id: None | str | Unset = UNSET
  qb_error: ExecuteEventBlockResponseQbErrorType0 | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.execute_event_block_response_qb_error_type_0 import (
      ExecuteEventBlockResponseQbErrorType0,
    )

    event_id = self.event_id

    status = self.status

    qb_external_id: None | str | Unset
    if isinstance(self.qb_external_id, Unset):
      qb_external_id = UNSET
    else:
      qb_external_id = self.qb_external_id

    qb_error: dict[str, Any] | None | Unset
    if isinstance(self.qb_error, Unset):
      qb_error = UNSET
    elif isinstance(self.qb_error, ExecuteEventBlockResponseQbErrorType0):
      qb_error = self.qb_error.to_dict()
    else:
      qb_error = self.qb_error

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
        "status": status,
      }
    )
    if qb_external_id is not UNSET:
      field_dict["qb_external_id"] = qb_external_id
    if qb_error is not UNSET:
      field_dict["qb_error"] = qb_error

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.execute_event_block_response_qb_error_type_0 import (
      ExecuteEventBlockResponseQbErrorType0,
    )

    d = dict(src_dict)
    event_id = d.pop("event_id")

    status = d.pop("status")

    def _parse_qb_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    qb_external_id = _parse_qb_external_id(d.pop("qb_external_id", UNSET))

    def _parse_qb_error(
      data: object,
    ) -> ExecuteEventBlockResponseQbErrorType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        qb_error_type_0 = ExecuteEventBlockResponseQbErrorType0.from_dict(data)

        return qb_error_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(ExecuteEventBlockResponseQbErrorType0 | None | Unset, data)

    qb_error = _parse_qb_error(d.pop("qb_error", UNSET))

    execute_event_block_response = cls(
      event_id=event_id,
      status=status,
      qb_external_id=qb_external_id,
      qb_error=qb_error,
    )

    execute_event_block_response.additional_properties = d
    return execute_event_block_response

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
