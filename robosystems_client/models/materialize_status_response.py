from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaterializeStatusResponse")


@_attrs_define
class MaterializeStatusResponse:
  """
  Attributes:
      graph_id (str): Graph database identifier
      is_stale (bool): Whether graph is currently stale
      message (str): Human-readable status summary
      stale_reason (None | str | Unset): Reason for staleness if applicable
      stale_since (None | str | Unset): When graph became stale (ISO timestamp)
      last_materialized_at (None | str | Unset): When graph was last materialized (ISO timestamp)
      materialization_count (int | Unset): Total number of materializations performed Default: 0.
      hours_since_materialization (float | None | Unset): Hours since last materialization
  """

  graph_id: str
  is_stale: bool
  message: str
  stale_reason: None | str | Unset = UNSET
  stale_since: None | str | Unset = UNSET
  last_materialized_at: None | str | Unset = UNSET
  materialization_count: int | Unset = 0
  hours_since_materialization: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    is_stale = self.is_stale

    message = self.message

    stale_reason: None | str | Unset
    if isinstance(self.stale_reason, Unset):
      stale_reason = UNSET
    else:
      stale_reason = self.stale_reason

    stale_since: None | str | Unset
    if isinstance(self.stale_since, Unset):
      stale_since = UNSET
    else:
      stale_since = self.stale_since

    last_materialized_at: None | str | Unset
    if isinstance(self.last_materialized_at, Unset):
      last_materialized_at = UNSET
    else:
      last_materialized_at = self.last_materialized_at

    materialization_count = self.materialization_count

    hours_since_materialization: float | None | Unset
    if isinstance(self.hours_since_materialization, Unset):
      hours_since_materialization = UNSET
    else:
      hours_since_materialization = self.hours_since_materialization

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "is_stale": is_stale,
        "message": message,
      }
    )
    if stale_reason is not UNSET:
      field_dict["stale_reason"] = stale_reason
    if stale_since is not UNSET:
      field_dict["stale_since"] = stale_since
    if last_materialized_at is not UNSET:
      field_dict["last_materialized_at"] = last_materialized_at
    if materialization_count is not UNSET:
      field_dict["materialization_count"] = materialization_count
    if hours_since_materialization is not UNSET:
      field_dict["hours_since_materialization"] = hours_since_materialization

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    is_stale = d.pop("is_stale")

    message = d.pop("message")

    def _parse_stale_reason(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    stale_reason = _parse_stale_reason(d.pop("stale_reason", UNSET))

    def _parse_stale_since(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    stale_since = _parse_stale_since(d.pop("stale_since", UNSET))

    def _parse_last_materialized_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    last_materialized_at = _parse_last_materialized_at(
      d.pop("last_materialized_at", UNSET)
    )

    materialization_count = d.pop("materialization_count", UNSET)

    def _parse_hours_since_materialization(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    hours_since_materialization = _parse_hours_since_materialization(
      d.pop("hours_since_materialization", UNSET)
    )

    materialize_status_response = cls(
      graph_id=graph_id,
      is_stale=is_stale,
      message=message,
      stale_reason=stale_reason,
      stale_since=stale_since,
      last_materialized_at=last_materialized_at,
      materialization_count=materialization_count,
      hours_since_materialization=hours_since_materialization,
    )

    materialize_status_response.additional_properties = d
    return materialize_status_response

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
