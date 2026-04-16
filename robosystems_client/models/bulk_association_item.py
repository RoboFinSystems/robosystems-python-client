from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_association_item_association_type import (
  BulkAssociationItemAssociationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkAssociationItem")


@_attrs_define
class BulkAssociationItem:
  """A single association within a bulk-create payload. The parent
  `structure_id` is set once on the request envelope, not repeated
  per item.

      Attributes:
          from_element_id (str):
          to_element_id (str):
          association_type (BulkAssociationItemAssociationType | Unset):  Default:
              BulkAssociationItemAssociationType.PRESENTATION.
          arcrole (None | str | Unset):
          order_value (float | None | Unset):  Default: 0.0.
          weight (float | None | Unset):
          confidence (float | None | Unset):
          suggested_by (None | str | Unset):
  """

  from_element_id: str
  to_element_id: str
  association_type: BulkAssociationItemAssociationType | Unset = (
    BulkAssociationItemAssociationType.PRESENTATION
  )
  arcrole: None | str | Unset = UNSET
  order_value: float | None | Unset = 0.0
  weight: float | None | Unset = UNSET
  confidence: float | None | Unset = UNSET
  suggested_by: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from_element_id = self.from_element_id

    to_element_id = self.to_element_id

    association_type: str | Unset = UNSET
    if not isinstance(self.association_type, Unset):
      association_type = self.association_type.value

    arcrole: None | str | Unset
    if isinstance(self.arcrole, Unset):
      arcrole = UNSET
    else:
      arcrole = self.arcrole

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

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "from_element_id": from_element_id,
        "to_element_id": to_element_id,
      }
    )
    if association_type is not UNSET:
      field_dict["association_type"] = association_type
    if arcrole is not UNSET:
      field_dict["arcrole"] = arcrole
    if order_value is not UNSET:
      field_dict["order_value"] = order_value
    if weight is not UNSET:
      field_dict["weight"] = weight
    if confidence is not UNSET:
      field_dict["confidence"] = confidence
    if suggested_by is not UNSET:
      field_dict["suggested_by"] = suggested_by

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    from_element_id = d.pop("from_element_id")

    to_element_id = d.pop("to_element_id")

    _association_type = d.pop("association_type", UNSET)
    association_type: BulkAssociationItemAssociationType | Unset
    if isinstance(_association_type, Unset):
      association_type = UNSET
    else:
      association_type = BulkAssociationItemAssociationType(_association_type)

    def _parse_arcrole(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    arcrole = _parse_arcrole(d.pop("arcrole", UNSET))

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

    bulk_association_item = cls(
      from_element_id=from_element_id,
      to_element_id=to_element_id,
      association_type=association_type,
      arcrole=arcrole,
      order_value=order_value,
      weight=weight,
      confidence=confidence,
      suggested_by=suggested_by,
    )

    bulk_association_item.additional_properties = d
    return bulk_association_item

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
