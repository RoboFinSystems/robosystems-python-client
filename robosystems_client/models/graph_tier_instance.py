from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GraphTierInstance")


@_attrs_define
class GraphTierInstance:
  """Instance specifications for a tier.

  Attributes:
      type_ (str): Instance type identifier
      memory_mb (int): Memory allocated to your graph in megabytes
      is_multitenant (bool): Whether this tier shares infrastructure with other graphs
  """

  type_: str
  memory_mb: int
  is_multitenant: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    type_ = self.type_

    memory_mb = self.memory_mb

    is_multitenant = self.is_multitenant

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "type": type_,
        "memory_mb": memory_mb,
        "is_multitenant": is_multitenant,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    type_ = d.pop("type")

    memory_mb = d.pop("memory_mb")

    is_multitenant = d.pop("is_multitenant")

    graph_tier_instance = cls(
      type_=type_,
      memory_mb=memory_mb,
      is_multitenant=is_multitenant,
    )

    graph_tier_instance.additional_properties = d
    return graph_tier_instance

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
