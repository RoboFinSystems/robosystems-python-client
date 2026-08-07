from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubgraphLimits")


@_attrs_define
class SubgraphLimits:
  """Subgraph count against the parent graph tier's cap.

  Subgraphs are refused at the tier cap regardless of how small they are,
  so this is a count axis independent of the storage one — ``instance``
  already itemizes their footprint.

      Attributes:
          current_count (int): Subgraphs currently provisioned under this graph
          approaching_limit (bool): Whether approaching subgraph limit (>80%)
          max_allowed (int | None | Unset): Maximum subgraphs for this tier (null when uncapped)
          remaining (int | None | Unset): Subgraphs that can still be created (null when uncapped)
  """

  current_count: int
  approaching_limit: bool
  max_allowed: int | None | Unset = UNSET
  remaining: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    current_count = self.current_count

    approaching_limit = self.approaching_limit

    max_allowed: int | None | Unset
    if isinstance(self.max_allowed, Unset):
      max_allowed = UNSET
    else:
      max_allowed = self.max_allowed

    remaining: int | None | Unset
    if isinstance(self.remaining, Unset):
      remaining = UNSET
    else:
      remaining = self.remaining

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "current_count": current_count,
        "approaching_limit": approaching_limit,
      }
    )
    if max_allowed is not UNSET:
      field_dict["max_allowed"] = max_allowed
    if remaining is not UNSET:
      field_dict["remaining"] = remaining

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    current_count = d.pop("current_count")

    approaching_limit = d.pop("approaching_limit")

    def _parse_max_allowed(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    max_allowed = _parse_max_allowed(d.pop("max_allowed", UNSET))

    def _parse_remaining(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    remaining = _parse_remaining(d.pop("remaining", UNSET))

    subgraph_limits = cls(
      current_count=current_count,
      approaching_limit=approaching_limit,
      max_allowed=max_allowed,
      remaining=remaining,
    )

    subgraph_limits.additional_properties = d
    return subgraph_limits

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
