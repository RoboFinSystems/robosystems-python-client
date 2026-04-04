from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.association_response import AssociationResponse


T = TypeVar("T", bound="MappingDetailResponse")


@_attrs_define
class MappingDetailResponse:
  """A mapping structure with all its associations.

  Attributes:
      id (str):
      name (str):
      structure_type (str):
      taxonomy_id (str):
      associations (list[AssociationResponse]):
      total_associations (int):
  """

  id: str
  name: str
  structure_type: str
  taxonomy_id: str
  associations: list[AssociationResponse]
  total_associations: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    structure_type = self.structure_type

    taxonomy_id = self.taxonomy_id

    associations = []
    for associations_item_data in self.associations:
      associations_item = associations_item_data.to_dict()
      associations.append(associations_item)

    total_associations = self.total_associations

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "structure_type": structure_type,
        "taxonomy_id": taxonomy_id,
        "associations": associations,
        "total_associations": total_associations,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.association_response import AssociationResponse

    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    structure_type = d.pop("structure_type")

    taxonomy_id = d.pop("taxonomy_id")

    associations = []
    _associations = d.pop("associations")
    for associations_item_data in _associations:
      associations_item = AssociationResponse.from_dict(associations_item_data)

      associations.append(associations_item)

    total_associations = d.pop("total_associations")

    mapping_detail_response = cls(
      id=id,
      name=name,
      structure_type=structure_type,
      taxonomy_id=taxonomy_id,
      associations=associations,
      total_associations=total_associations,
    )

    mapping_detail_response.additional_properties = d
    return mapping_detail_response

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
