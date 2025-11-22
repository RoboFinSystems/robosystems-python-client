from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.graph_tier_instance import GraphTierInstance
  from ..models.graph_tier_limits import GraphTierLimits


T = TypeVar("T", bound="GraphTierInfo")


@_attrs_define
class GraphTierInfo:
  """Complete information about a graph database tier.

  Attributes:
      tier (str): Tier identifier
      name (str): Tier name
      display_name (str): Display name for UI
      description (str): Tier description
      backend (str): Database backend (ladybug or neo4j)
      enabled (bool): Whether tier is available
      max_subgraphs (int | None): Maximum subgraphs allowed
      storage_limit_gb (int): Storage limit in GB
      monthly_credits (int): Monthly AI credits
      api_rate_multiplier (float): API rate limit multiplier
      features (list[str]): List of tier features
      instance (GraphTierInstance): Instance specifications for a tier.
      limits (GraphTierLimits): Resource limits for a tier.
      monthly_price (float | None | Unset): Monthly price in USD
  """

  tier: str
  name: str
  display_name: str
  description: str
  backend: str
  enabled: bool
  max_subgraphs: int | None
  storage_limit_gb: int
  monthly_credits: int
  api_rate_multiplier: float
  features: list[str]
  instance: GraphTierInstance
  limits: GraphTierLimits
  monthly_price: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    tier = self.tier

    name = self.name

    display_name = self.display_name

    description = self.description

    backend = self.backend

    enabled = self.enabled

    max_subgraphs: int | None
    max_subgraphs = self.max_subgraphs

    storage_limit_gb = self.storage_limit_gb

    monthly_credits = self.monthly_credits

    api_rate_multiplier = self.api_rate_multiplier

    features = self.features

    instance = self.instance.to_dict()

    limits = self.limits.to_dict()

    monthly_price: float | None | Unset
    if isinstance(self.monthly_price, Unset):
      monthly_price = UNSET
    else:
      monthly_price = self.monthly_price

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "tier": tier,
        "name": name,
        "display_name": display_name,
        "description": description,
        "backend": backend,
        "enabled": enabled,
        "max_subgraphs": max_subgraphs,
        "storage_limit_gb": storage_limit_gb,
        "monthly_credits": monthly_credits,
        "api_rate_multiplier": api_rate_multiplier,
        "features": features,
        "instance": instance,
        "limits": limits,
      }
    )
    if monthly_price is not UNSET:
      field_dict["monthly_price"] = monthly_price

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_tier_instance import GraphTierInstance
    from ..models.graph_tier_limits import GraphTierLimits

    d = dict(src_dict)
    tier = d.pop("tier")

    name = d.pop("name")

    display_name = d.pop("display_name")

    description = d.pop("description")

    backend = d.pop("backend")

    enabled = d.pop("enabled")

    def _parse_max_subgraphs(data: object) -> int | None:
      if data is None:
        return data
      return cast(int | None, data)

    max_subgraphs = _parse_max_subgraphs(d.pop("max_subgraphs"))

    storage_limit_gb = d.pop("storage_limit_gb")

    monthly_credits = d.pop("monthly_credits")

    api_rate_multiplier = d.pop("api_rate_multiplier")

    features = cast(list[str], d.pop("features"))

    instance = GraphTierInstance.from_dict(d.pop("instance"))

    limits = GraphTierLimits.from_dict(d.pop("limits"))

    def _parse_monthly_price(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    monthly_price = _parse_monthly_price(d.pop("monthly_price", UNSET))

    graph_tier_info = cls(
      tier=tier,
      name=name,
      display_name=display_name,
      description=description,
      backend=backend,
      enabled=enabled,
      max_subgraphs=max_subgraphs,
      storage_limit_gb=storage_limit_gb,
      monthly_credits=monthly_credits,
      api_rate_multiplier=api_rate_multiplier,
      features=features,
      instance=instance,
      limits=limits,
      monthly_price=monthly_price,
    )

    graph_tier_info.additional_properties = d
    return graph_tier_info

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
