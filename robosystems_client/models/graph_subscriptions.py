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

  Attributes:
      description (str): Description of graph subscriptions
      tiers (list['GraphSubscriptionTier']): Available tiers
      storage (StorageInfo): Storage pricing information.
      notes (list[str]): Important notes
  """

  description: str
  tiers: list["GraphSubscriptionTier"]
  storage: "StorageInfo"
  notes: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    description = self.description

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

    tiers = []
    _tiers = d.pop("tiers")
    for tiers_item_data in _tiers:
      tiers_item = GraphSubscriptionTier.from_dict(tiers_item_data)

      tiers.append(tiers_item)

    storage = StorageInfo.from_dict(d.pop("storage"))

    notes = cast(list[str], d.pop("notes"))

    graph_subscriptions = cls(
      description=description,
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
