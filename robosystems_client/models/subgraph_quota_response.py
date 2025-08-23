from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubgraphQuotaResponse")


@_attrs_define
class SubgraphQuotaResponse:
  """Response model for subgraph quota information.

  Attributes:
      parent_graph_id (str): Parent graph identifier
      tier (str): Graph tier
      current_count (int): Current number of subgraphs
      max_allowed (Union[None, Unset, int]): Maximum allowed subgraphs (None = unlimited)
      remaining (Union[None, Unset, int]): Remaining subgraphs that can be created
      total_size_mb (Union[None, Unset, float]): Total size of all subgraphs
      max_size_mb (Union[None, Unset, float]): Maximum allowed total size
  """

  parent_graph_id: str
  tier: str
  current_count: int
  max_allowed: Union[None, Unset, int] = UNSET
  remaining: Union[None, Unset, int] = UNSET
  total_size_mb: Union[None, Unset, float] = UNSET
  max_size_mb: Union[None, Unset, float] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    parent_graph_id = self.parent_graph_id

    tier = self.tier

    current_count = self.current_count

    max_allowed: Union[None, Unset, int]
    if isinstance(self.max_allowed, Unset):
      max_allowed = UNSET
    else:
      max_allowed = self.max_allowed

    remaining: Union[None, Unset, int]
    if isinstance(self.remaining, Unset):
      remaining = UNSET
    else:
      remaining = self.remaining

    total_size_mb: Union[None, Unset, float]
    if isinstance(self.total_size_mb, Unset):
      total_size_mb = UNSET
    else:
      total_size_mb = self.total_size_mb

    max_size_mb: Union[None, Unset, float]
    if isinstance(self.max_size_mb, Unset):
      max_size_mb = UNSET
    else:
      max_size_mb = self.max_size_mb

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "parent_graph_id": parent_graph_id,
        "tier": tier,
        "current_count": current_count,
      }
    )
    if max_allowed is not UNSET:
      field_dict["max_allowed"] = max_allowed
    if remaining is not UNSET:
      field_dict["remaining"] = remaining
    if total_size_mb is not UNSET:
      field_dict["total_size_mb"] = total_size_mb
    if max_size_mb is not UNSET:
      field_dict["max_size_mb"] = max_size_mb

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    parent_graph_id = d.pop("parent_graph_id")

    tier = d.pop("tier")

    current_count = d.pop("current_count")

    def _parse_max_allowed(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    max_allowed = _parse_max_allowed(d.pop("max_allowed", UNSET))

    def _parse_remaining(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    remaining = _parse_remaining(d.pop("remaining", UNSET))

    def _parse_total_size_mb(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    total_size_mb = _parse_total_size_mb(d.pop("total_size_mb", UNSET))

    def _parse_max_size_mb(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    max_size_mb = _parse_max_size_mb(d.pop("max_size_mb", UNSET))

    subgraph_quota_response = cls(
      parent_graph_id=parent_graph_id,
      tier=tier,
      current_count=current_count,
      max_allowed=max_allowed,
      remaining=remaining,
      total_size_mb=total_size_mb,
      max_size_mb=max_size_mb,
    )

    subgraph_quota_response.additional_properties = d
    return subgraph_quota_response

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
