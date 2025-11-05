from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceOfferingSummary")


@_attrs_define
class ServiceOfferingSummary:
  """Summary of service offerings.

  Attributes:
      total_graph_tiers (int): Total number of graph tiers
      total_repositories (int): Total number of repositories
      enabled_repositories (int): Number of enabled repositories
      coming_soon_repositories (int): Number of coming soon repositories
  """

  total_graph_tiers: int
  total_repositories: int
  enabled_repositories: int
  coming_soon_repositories: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    total_graph_tiers = self.total_graph_tiers

    total_repositories = self.total_repositories

    enabled_repositories = self.enabled_repositories

    coming_soon_repositories = self.coming_soon_repositories

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "total_graph_tiers": total_graph_tiers,
        "total_repositories": total_repositories,
        "enabled_repositories": enabled_repositories,
        "coming_soon_repositories": coming_soon_repositories,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    total_graph_tiers = d.pop("total_graph_tiers")

    total_repositories = d.pop("total_repositories")

    enabled_repositories = d.pop("enabled_repositories")

    coming_soon_repositories = d.pop("coming_soon_repositories")

    service_offering_summary = cls(
      total_graph_tiers=total_graph_tiers,
      total_repositories=total_repositories,
      enabled_repositories=enabled_repositories,
      coming_soon_repositories=coming_soon_repositories,
    )

    service_offering_summary.additional_properties = d
    return service_offering_summary

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
