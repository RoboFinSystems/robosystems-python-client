from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.bulk_association_item import BulkAssociationItem


T = TypeVar("T", bound="BulkCreateAssociationsRequest")


@_attrs_define
class BulkCreateAssociationsRequest:
  """Bulk create associations within a single structure. Atomic — any
  failed row rolls back the whole batch. Handles 50+ presentation arcs,
  25+ calculation arcs, or a full table linkbase in one call.

      Attributes:
          structure_id (str):
          associations (list[BulkAssociationItem]):
  """

  structure_id: str
  associations: list[BulkAssociationItem]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    associations = []
    for associations_item_data in self.associations:
      associations_item = associations_item_data.to_dict()
      associations.append(associations_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "associations": associations,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.bulk_association_item import BulkAssociationItem

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    associations = []
    _associations = d.pop("associations")
    for associations_item_data in _associations:
      associations_item = BulkAssociationItem.from_dict(associations_item_data)

      associations.append(associations_item)

    bulk_create_associations_request = cls(
      structure_id=structure_id,
      associations=associations,
    )

    bulk_create_associations_request.additional_properties = d
    return bulk_create_associations_request

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
