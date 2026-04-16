from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAssociationRequest")


@_attrs_define
class UpdateAssociationRequest:
  """Update mutable fields on an association. `from_element_id`,
  `to_element_id`, and `association_type` are immutable — delete and
  recreate instead.

      Attributes:
          association_id (str):
          order_value (float | None | Unset):
          weight (float | None | Unset):
          confidence (float | None | Unset):
          approved_by (None | str | Unset):
  """

  association_id: str
  order_value: float | None | Unset = UNSET
  weight: float | None | Unset = UNSET
  confidence: float | None | Unset = UNSET
  approved_by: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    association_id = self.association_id

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

    approved_by: None | str | Unset
    if isinstance(self.approved_by, Unset):
      approved_by = UNSET
    else:
      approved_by = self.approved_by

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "association_id": association_id,
      }
    )
    if order_value is not UNSET:
      field_dict["order_value"] = order_value
    if weight is not UNSET:
      field_dict["weight"] = weight
    if confidence is not UNSET:
      field_dict["confidence"] = confidence
    if approved_by is not UNSET:
      field_dict["approved_by"] = approved_by

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    association_id = d.pop("association_id")

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

    def _parse_approved_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    approved_by = _parse_approved_by(d.pop("approved_by", UNSET))

    update_association_request = cls(
      association_id=association_id,
      order_value=order_value,
      weight=weight,
      confidence=confidence,
      approved_by=approved_by,
    )

    update_association_request.additional_properties = d
    return update_association_request

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
