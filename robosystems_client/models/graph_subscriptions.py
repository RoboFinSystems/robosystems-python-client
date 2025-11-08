from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.graph_subscription_tier import GraphSubscriptionTier
  from ..models.storage_info import StorageInfo


T = TypeVar("T", bound="GraphSubscriptions")


@_attrs_define
class GraphSubscriptions:
  """Graph subscription offerings.

  Graph subscriptions are per-graph, not per-organization. Each graph
  created by an organization has its own subscription with its own
  infrastructure tier, pricing, and credit allocation.

      Attributes:
          description (str): Description of graph subscriptions
          pricing_model (str): Pricing model type (per_graph or per_organization)
          tiers (list['GraphSubscriptionTier']): Available infrastructure tiers
          storage (StorageInfo): Storage pricing information.
          notes (list[str]): Important notes
  """

  description: str
  pricing_model: str
  tiers: list["GraphSubscriptionTier"]
  storage: "StorageInfo"
  notes: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    description = self.description

    pricing_model = self.pricing_model

    tiers = []
    for tiers_item_data in self.tiers:
      tiers_item = tiers_item_data.to_dict()
      tiers.append(tiers_item)

    storage = self.storage.to_dict()

    notes = self.notes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "description": description,
        "pricing_model": pricing_model,
        "tiers": tiers,
        "storage": storage,
        "notes": notes,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_subscription_tier import GraphSubscriptionTier
    from ..models.storage_info import StorageInfo

    d = dict(src_dict)
    description = d.pop("description")

    pricing_model = d.pop("pricing_model")

    tiers = []
    _tiers = d.pop("tiers")
    for tiers_item_data in _tiers:
      tiers_item = GraphSubscriptionTier.from_dict(tiers_item_data)

      tiers.append(tiers_item)

    storage = StorageInfo.from_dict(d.pop("storage"))

    notes = cast(list[str], d.pop("notes"))

    graph_subscriptions = cls(
      description=description,
      pricing_model=pricing_model,
      tiers=tiers,
      storage=storage,
      notes=notes,
    )

    graph_subscriptions.additional_properties = d
    return graph_subscriptions

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
