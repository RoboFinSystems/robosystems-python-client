from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaterializeResponse")


@_attrs_define
class MaterializeResponse:
  """
  Attributes:
      status (str): Materialization status
      graph_id (str): Graph database identifier
      was_stale (bool): Whether graph was stale before materialization
      tables_materialized (list[str]): List of tables successfully materialized
      total_rows (int): Total rows materialized across all tables
      execution_time_ms (float): Total materialization time
      message (str): Human-readable status message
      stale_reason (None | str | Unset): Reason graph was stale
  """

  status: str
  graph_id: str
  was_stale: bool
  tables_materialized: list[str]
  total_rows: int
  execution_time_ms: float
  message: str
  stale_reason: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    status = self.status

    graph_id = self.graph_id

    was_stale = self.was_stale

    tables_materialized = self.tables_materialized

    total_rows = self.total_rows

    execution_time_ms = self.execution_time_ms

    message = self.message

    stale_reason: None | str | Unset
    if isinstance(self.stale_reason, Unset):
      stale_reason = UNSET
    else:
      stale_reason = self.stale_reason

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "status": status,
        "graph_id": graph_id,
        "was_stale": was_stale,
        "tables_materialized": tables_materialized,
        "total_rows": total_rows,
        "execution_time_ms": execution_time_ms,
        "message": message,
      }
    )
    if stale_reason is not UNSET:
      field_dict["stale_reason"] = stale_reason

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    status = d.pop("status")

    graph_id = d.pop("graph_id")

    was_stale = d.pop("was_stale")

    tables_materialized = cast(list[str], d.pop("tables_materialized"))

    total_rows = d.pop("total_rows")

    execution_time_ms = d.pop("execution_time_ms")

    message = d.pop("message")

    def _parse_stale_reason(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    stale_reason = _parse_stale_reason(d.pop("stale_reason", UNSET))

    materialize_response = cls(
      status=status,
      graph_id=graph_id,
      was_stale=was_stale,
      tables_materialized=tables_materialized,
      total_rows=total_rows,
      execution_time_ms=execution_time_ms,
      message=message,
      stale_reason=stale_reason,
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
