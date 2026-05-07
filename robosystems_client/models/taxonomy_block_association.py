from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxonomyBlockAssociation")


@_attrs_define
class TaxonomyBlockAssociation:
  """Association projection for the Taxonomy Block envelope.

  Attributes:
      id (str):
      structure_id (str):
      from_element_qname (str):
      to_element_qname (str):
      association_type (str):
      order_value (float | None | Unset):
      arcrole (None | str | Unset):
      weight (float | None | Unset):
  """

  id: str
  structure_id: str
  from_element_qname: str
  to_element_qname: str
  association_type: str
  order_value: float | None | Unset = UNSET
  arcrole: None | str | Unset = UNSET
  weight: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    structure_id = self.structure_id

    from_element_qname = self.from_element_qname

    to_element_qname = self.to_element_qname

    association_type = self.association_type

    order_value: float | None | Unset
    if isinstance(self.order_value, Unset):
      order_value = UNSET
    else:
      order_value = self.order_value

    arcrole: None | str | Unset
    if isinstance(self.arcrole, Unset):
      arcrole = UNSET
    else:
      arcrole = self.arcrole

    weight: float | None | Unset
    if isinstance(self.weight, Unset):
      weight = UNSET
    else:
      weight = self.weight

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "structure_id": structure_id,
        "from_element_qname": from_element_qname,
        "to_element_qname": to_element_qname,
        "association_type": association_type,
      }
    )
    if order_value is not UNSET:
      field_dict["order_value"] = order_value
    if arcrole is not UNSET:
      field_dict["arcrole"] = arcrole
    if weight is not UNSET:
      field_dict["weight"] = weight

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    structure_id = d.pop("structure_id")

    from_element_qname = d.pop("from_element_qname")

    to_element_qname = d.pop("to_element_qname")

    association_type = d.pop("association_type")

    def _parse_order_value(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    order_value = _parse_order_value(d.pop("order_value", UNSET))

    def _parse_arcrole(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    arcrole = _parse_arcrole(d.pop("arcrole", UNSET))

    def _parse_weight(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    weight = _parse_weight(d.pop("weight", UNSET))

    taxonomy_block_association = cls(
      id=id,
      structure_id=structure_id,
      from_element_qname=from_element_qname,
      to_element_qname=to_element_qname,
      association_type=association_type,
      order_value=order_value,
      arcrole=arcrole,
      weight=weight,
    )

    taxonomy_block_association.additional_properties = d
    return taxonomy_block_association

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
