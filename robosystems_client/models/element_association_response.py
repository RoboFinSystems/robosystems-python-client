from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ElementAssociationResponse")


@_attrs_define
class ElementAssociationResponse:
  """
  Attributes:
      id (str):
      structure_id (str):
      from_element_id (str):
      to_element_id (str):
      association_type (str):
      from_element_name (None | str | Unset):
      from_element_qname (None | str | Unset):
      to_element_name (None | str | Unset):
      to_element_qname (None | str | Unset):
      order_value (float | None | Unset):
      weight (float | None | Unset):
      confidence (float | None | Unset):
      suggested_by (None | str | Unset):
      approved_by (None | str | Unset):
  """

  id: str
  structure_id: str
  from_element_id: str
  to_element_id: str
  association_type: str
  from_element_name: None | str | Unset = UNSET
  from_element_qname: None | str | Unset = UNSET
  to_element_name: None | str | Unset = UNSET
  to_element_qname: None | str | Unset = UNSET
  order_value: float | None | Unset = UNSET
  weight: float | None | Unset = UNSET
  confidence: float | None | Unset = UNSET
  suggested_by: None | str | Unset = UNSET
  approved_by: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    structure_id = self.structure_id

    from_element_id = self.from_element_id

    to_element_id = self.to_element_id

    association_type = self.association_type

    from_element_name: None | str | Unset
    if isinstance(self.from_element_name, Unset):
      from_element_name = UNSET
    else:
      from_element_name = self.from_element_name

    from_element_qname: None | str | Unset
    if isinstance(self.from_element_qname, Unset):
      from_element_qname = UNSET
    else:
      from_element_qname = self.from_element_qname

    to_element_name: None | str | Unset
    if isinstance(self.to_element_name, Unset):
      to_element_name = UNSET
    else:
      to_element_name = self.to_element_name

    to_element_qname: None | str | Unset
    if isinstance(self.to_element_qname, Unset):
      to_element_qname = UNSET
    else:
      to_element_qname = self.to_element_qname

    order_value: float | None | Unset
    if isinstance(self.order_value, Unset):
      order_value = UNSET
    else:
      order_value = self.order_value

    weight: float | None | Unset
    if isinstance(self.weight, Unset):
      weight = UNSET
    else:
      weight = self.weight

    confidence: float | None | Unset
    if isinstance(self.confidence, Unset):
      confidence = UNSET
    else:
      confidence = self.confidence

    suggested_by: None | str | Unset
    if isinstance(self.suggested_by, Unset):
      suggested_by = UNSET
    else:
      suggested_by = self.suggested_by

    approved_by: None | str | Unset
    if isinstance(self.approved_by, Unset):
      approved_by = UNSET
    else:
      approved_by = self.approved_by

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "structure_id": structure_id,
        "from_element_id": from_element_id,
        "to_element_id": to_element_id,
        "association_type": association_type,
      }
    )
    if from_element_name is not UNSET:
      field_dict["from_element_name"] = from_element_name
    if from_element_qname is not UNSET:
      field_dict["from_element_qname"] = from_element_qname
    if to_element_name is not UNSET:
      field_dict["to_element_name"] = to_element_name
    if to_element_qname is not UNSET:
      field_dict["to_element_qname"] = to_element_qname
    if order_value is not UNSET:
      field_dict["order_value"] = order_value
    if weight is not UNSET:
      field_dict["weight"] = weight
    if confidence is not UNSET:
      field_dict["confidence"] = confidence
    if suggested_by is not UNSET:
      field_dict["suggested_by"] = suggested_by
    if approved_by is not UNSET:
      field_dict["approved_by"] = approved_by

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    structure_id = d.pop("structure_id")

    from_element_id = d.pop("from_element_id")

    to_element_id = d.pop("to_element_id")

    association_type = d.pop("association_type")

    def _parse_from_element_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    from_element_name = _parse_from_element_name(d.pop("from_element_name", UNSET))

    def _parse_from_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    from_element_qname = _parse_from_element_qname(d.pop("from_element_qname", UNSET))

    def _parse_to_element_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    to_element_name = _parse_to_element_name(d.pop("to_element_name", UNSET))

    def _parse_to_element_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    to_element_qname = _parse_to_element_qname(d.pop("to_element_qname", UNSET))

    def _parse_order_value(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    order_value = _parse_order_value(d.pop("order_value", UNSET))

    def _parse_weight(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    weight = _parse_weight(d.pop("weight", UNSET))

    def _parse_confidence(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    confidence = _parse_confidence(d.pop("confidence", UNSET))

    def _parse_suggested_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    suggested_by = _parse_suggested_by(d.pop("suggested_by", UNSET))

    def _parse_approved_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    approved_by = _parse_approved_by(d.pop("approved_by", UNSET))

    element_association_response = cls(
      id=id,
      structure_id=structure_id,
      from_element_id=from_element_id,
      to_element_id=to_element_id,
      association_type=association_type,
      from_element_name=from_element_name,
      from_element_qname=from_element_qname,
      to_element_name=to_element_name,
      to_element_qname=to_element_qname,
      order_value=order_value,
      weight=weight,
      confidence=confidence,
      suggested_by=suggested_by,
      approved_by=approved_by,
    )

    element_association_response.additional_properties = d
    return element_association_response

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
