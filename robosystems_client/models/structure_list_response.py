from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.structure_response import StructureResponse


T = TypeVar("T", bound="StructureListResponse")


@_attrs_define
class StructureListResponse:
  """
  Attributes:
      structures (list[StructureResponse]):
  """

  structures: list[StructureResponse]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structures = []
    for structures_item_data in self.structures:
      structures_item = structures_item_data.to_dict()
      structures.append(structures_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structures": structures,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.structure_response import StructureResponse

    d = dict(src_dict)
    structures = []
    _structures = d.pop("structures")
    for structures_item_data in _structures:
      structures_item = StructureResponse.from_dict(structures_item_data)

      structures.append(structures_item)

    structure_list_response = cls(
      structures=structures,
    )

    structure_list_response.additional_properties = d
    return structure_list_response

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
