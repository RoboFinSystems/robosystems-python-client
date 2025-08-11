from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AvailableExtension")


@_attrs_define
class AvailableExtension:
  """
  Attributes:
      name (str): Extension name (e.g., 'roboledger')
      display_name (str): Human-readable name (e.g., 'RoboLedger - Financial Reporting')
      description (str): Description of what this extension provides
      node_count (int): Number of node types this extension adds
      relationship_count (int): Number of relationship types this extension adds
  """

  name: str
  display_name: str
  description: str
  node_count: int
  relationship_count: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    display_name = self.display_name

    description = self.description

    node_count = self.node_count

    relationship_count = self.relationship_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "display_name": display_name,
        "description": description,
        "node_count": node_count,
        "relationship_count": relationship_count,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    display_name = d.pop("display_name")

    description = d.pop("description")

    node_count = d.pop("node_count")

    relationship_count = d.pop("relationship_count")

    available_extension = cls(
      name=name,
      display_name=display_name,
      description=description,
      node_count=node_count,
      relationship_count=relationship_count,
    )

    available_extension.additional_properties = d
    return available_extension

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
