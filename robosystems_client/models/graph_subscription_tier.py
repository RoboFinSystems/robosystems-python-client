from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphSubscriptionTier")


@_attrs_define
class GraphSubscriptionTier:
  """Information about a graph infrastructure tier.

  Each tier represents a per-graph subscription option with specific
  infrastructure, performance, and pricing characteristics.

      Attributes:
          name (str): Infrastructure tier identifier (e.g., kuzu-standard)
          display_name (str): Display name for UI
          description (str): Tier description
          monthly_price_per_graph (float): Monthly price in USD per graph
          monthly_credits_per_graph (int): Monthly AI credits per graph
          storage_included_gb (int): Storage included in GB
          storage_overage_per_gb (float): Overage cost per GB per month
          infrastructure (str): Infrastructure description
          features (list[str]): List of features
          backup_retention_days (int): Backup retention in days
          priority_support (bool): Whether priority support is included
          api_rate_multiplier (float): API rate multiplier
          backend (str): Database backend (kuzu or neo4j)
          max_queries_per_hour (Union[None, Unset, int]): Maximum queries per hour
          max_subgraphs (Union[Unset, int]): Maximum subgraphs supported Default: 0.
          instance_type (Union[None, Unset, str]): Instance type
  """

  name: str
  display_name: str
  description: str
  monthly_price_per_graph: float
  monthly_credits_per_graph: int
  storage_included_gb: int
  storage_overage_per_gb: float
  infrastructure: str
  features: list[str]
  backup_retention_days: int
  priority_support: bool
  api_rate_multiplier: float
  backend: str
  max_queries_per_hour: Union[None, Unset, int] = UNSET
  max_subgraphs: Union[Unset, int] = 0
  instance_type: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    display_name = self.display_name

    description = self.description

    monthly_price_per_graph = self.monthly_price_per_graph

    monthly_credits_per_graph = self.monthly_credits_per_graph

    storage_included_gb = self.storage_included_gb

    storage_overage_per_gb = self.storage_overage_per_gb

    infrastructure = self.infrastructure

    features = self.features

    backup_retention_days = self.backup_retention_days

    priority_support = self.priority_support

    api_rate_multiplier = self.api_rate_multiplier

    backend = self.backend

    max_queries_per_hour: Union[None, Unset, int]
    if isinstance(self.max_queries_per_hour, Unset):
      max_queries_per_hour = UNSET
    else:
      max_queries_per_hour = self.max_queries_per_hour

    max_subgraphs = self.max_subgraphs

    instance_type: Union[None, Unset, str]
    if isinstance(self.instance_type, Unset):
      instance_type = UNSET
    else:
      instance_type = self.instance_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "display_name": display_name,
        "description": description,
        "monthly_price_per_graph": monthly_price_per_graph,
        "monthly_credits_per_graph": monthly_credits_per_graph,
        "storage_included_gb": storage_included_gb,
        "storage_overage_per_gb": storage_overage_per_gb,
        "infrastructure": infrastructure,
        "features": features,
        "backup_retention_days": backup_retention_days,
        "priority_support": priority_support,
        "api_rate_multiplier": api_rate_multiplier,
        "backend": backend,
      }
    )
    if max_queries_per_hour is not UNSET:
      field_dict["max_queries_per_hour"] = max_queries_per_hour
    if max_subgraphs is not UNSET:
      field_dict["max_subgraphs"] = max_subgraphs
    if instance_type is not UNSET:
      field_dict["instance_type"] = instance_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    display_name = d.pop("display_name")

    description = d.pop("description")

    monthly_price_per_graph = d.pop("monthly_price_per_graph")

    monthly_credits_per_graph = d.pop("monthly_credits_per_graph")

    storage_included_gb = d.pop("storage_included_gb")

    storage_overage_per_gb = d.pop("storage_overage_per_gb")

    infrastructure = d.pop("infrastructure")

    features = cast(list[str], d.pop("features"))

    backup_retention_days = d.pop("backup_retention_days")

    priority_support = d.pop("priority_support")

    api_rate_multiplier = d.pop("api_rate_multiplier")

    backend = d.pop("backend")

    def _parse_max_queries_per_hour(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    max_queries_per_hour = _parse_max_queries_per_hour(
      d.pop("max_queries_per_hour", UNSET)
    )

    max_subgraphs = d.pop("max_subgraphs", UNSET)

    def _parse_instance_type(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    instance_type = _parse_instance_type(d.pop("instance_type", UNSET))

    graph_subscription_tier = cls(
      name=name,
      display_name=display_name,
      description=description,
      monthly_price_per_graph=monthly_price_per_graph,
      monthly_credits_per_graph=monthly_credits_per_graph,
      storage_included_gb=storage_included_gb,
      storage_overage_per_gb=storage_overage_per_gb,
      infrastructure=infrastructure,
      features=features,
      backup_retention_days=backup_retention_days,
      priority_support=priority_support,
      api_rate_multiplier=api_rate_multiplier,
      backend=backend,
      max_queries_per_hour=max_queries_per_hour,
      max_subgraphs=max_subgraphs,
      instance_type=instance_type,
    )

    graph_subscription_tier.additional_properties = d
    return graph_subscription_tier

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
