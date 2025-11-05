from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.graph_tier_info import GraphTierInfo


T = TypeVar("T", bound="AvailableGraphTiersResponse")


@_attrs_define
class AvailableGraphTiersResponse:
  """Response containing available graph tiers.

  Attributes:
      tiers (list['GraphTierInfo']): List of available tiers
  """

  tiers: list["GraphTierInfo"]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    tiers = []
    for tiers_item_data in self.tiers:
      tiers_item = tiers_item_data.to_dict()
      tiers.append(tiers_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "tiers": tiers,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_tier_info import GraphTierInfo

    d = dict(src_dict)
    tiers = []
    _tiers = d.pop("tiers")
    for tiers_item_data in _tiers:
      tiers_item = GraphTierInfo.from_dict(tiers_item_data)

      tiers.append(tiers_item)

    available_graph_tiers_response = cls(
      tiers=tiers,
    )

    available_graph_tiers_response.additional_properties = d
    return available_graph_tiers_response

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
