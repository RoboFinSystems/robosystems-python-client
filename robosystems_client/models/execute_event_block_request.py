from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteEventBlockRequest")


@_attrs_define
class ExecuteEventBlockRequest:
  """Request to publish an event to the source-of-truth system.

  For events on a connection with `write_policy='qb_authoritative'`
  (or `'hybrid'`), this triggers a synchronous write to QuickBooks
  via the QB API. The returned `qb_txn_id` lands on
  `event.metadata.qb_external_id` and the event transitions to
  `committed` (in flight) → `fulfilled` (QB accepted) or `pending`
  (QB rejected).

  `'native'`-policy events fast-path through with no QB write —
  RoboSystems IS the source of truth, no outbound publish needed.

      Attributes:
          event_id (str): Event ID (`evt_*` ULID) to publish. The event's `metadata.connection_id` determines which QB
              connection to write to; the connection's `write_policy` governs whether a write fires.
          connection_id (None | str | Unset): Override for the connection to route the write through. Used by the close-
              period batch path where schedule-originated events don't carry `connection_id` in their metadata. When unset,
              the command reads `event.metadata.connection_id`.
  """

  event_id: str
  connection_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_id = self.event_id

    connection_id: None | str | Unset
    if isinstance(self.connection_id, Unset):
      connection_id = UNSET
    else:
      connection_id = self.connection_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
      }
    )
    if connection_id is not UNSET:
      field_dict["connection_id"] = connection_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    event_id = d.pop("event_id")

    def _parse_connection_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    connection_id = _parse_connection_id(d.pop("connection_id", UNSET))

    execute_event_block_request = cls(
      event_id=event_id,
      connection_id=connection_id,
    )

    execute_event_block_request.additional_properties = d
    return execute_event_block_request

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
