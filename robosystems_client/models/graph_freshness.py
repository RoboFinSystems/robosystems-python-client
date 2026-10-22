from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphFreshness")


@_attrs_define
class GraphFreshness:
  """Whether a ledger's graph is current with its books.

  A ledger's graph is a projection of its database, rebuilt after writes;
  until a rebuild finishes, graph-backed reads answer from the previous one.

      Attributes:
          stale (bool): True when the books have changed since the graph was last rebuilt, so this answer can be behind
              them. A rebuild is queued automatically.
          stale_since (None | str | Unset): When the graph first fell behind the books (ISO 8601); null when current.
          stale_reason (None | str | Unset): The latest write that left the graph behind (e.g. 'period_closed').
          last_materialized_at (None | str | Unset): When the graph was last rebuilt (ISO 8601).
  """

  stale: bool
  stale_since: None | str | Unset = UNSET
  stale_reason: None | str | Unset = UNSET
  last_materialized_at: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    stale = self.stale

    stale_since: None | str | Unset
    if isinstance(self.stale_since, Unset):
      stale_since = UNSET
    else:
      stale_since = self.stale_since

    stale_reason: None | str | Unset
    if isinstance(self.stale_reason, Unset):
      stale_reason = UNSET
    else:
      stale_reason = self.stale_reason

    last_materialized_at: None | str | Unset
    if isinstance(self.last_materialized_at, Unset):
      last_materialized_at = UNSET
    else:
      last_materialized_at = self.last_materialized_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "stale": stale,
      }
    )
    if stale_since is not UNSET:
      field_dict["stale_since"] = stale_since
    if stale_reason is not UNSET:
      field_dict["stale_reason"] = stale_reason
    if last_materialized_at is not UNSET:
      field_dict["last_materialized_at"] = last_materialized_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    stale = d.pop("stale")

    def _parse_stale_since(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    stale_since = _parse_stale_since(d.pop("stale_since", UNSET))

    def _parse_stale_reason(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    stale_reason = _parse_stale_reason(d.pop("stale_reason", UNSET))

    def _parse_last_materialized_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    last_materialized_at = _parse_last_materialized_at(
      d.pop("last_materialized_at", UNSET)
    )

    graph_freshness = cls(
      stale=stale,
      stale_since=stale_since,
      stale_reason=stale_reason,
      last_materialized_at=last_materialized_at,
    )

    graph_freshness.additional_properties = d
    return graph_freshness

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
