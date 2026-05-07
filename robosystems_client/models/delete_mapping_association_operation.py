from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteMappingAssociationOperation")


@_attrs_define
class DeleteMappingAssociationOperation:
  """Delete a single CoA → reporting-concept mapping edge.

  Attributes:
      mapping_id (str): The mapping structure containing the association.
      association_id (str): The association edge to delete.
  """

  mapping_id: str
  association_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    mapping_id = self.mapping_id

    association_id = self.association_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "mapping_id": mapping_id,
        "association_id": association_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    mapping_id = d.pop("mapping_id")

    association_id = d.pop("association_id")

    delete_mapping_association_operation = cls(
      mapping_id=mapping_id,
      association_id=association_id,
    )

    delete_mapping_association_operation.additional_properties = d
    return delete_mapping_association_operation

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
