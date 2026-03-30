from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FactRowResponse")


@_attrs_define
class FactRowResponse:
  """
  Attributes:
      element_id (str):
      element_qname (str):
      element_name (str):
      classification (str):
      current_value (float):
      prior_value (float | None | Unset):
      is_subtotal (bool | Unset):  Default: False.
      depth (int | Unset):  Default: 0.
  """

  element_id: str
  element_qname: str
  element_name: str
  classification: str
  current_value: float
  prior_value: float | None | Unset = UNSET
  is_subtotal: bool | Unset = False
  depth: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    element_qname = self.element_qname

    element_name = self.element_name

    classification = self.classification

    current_value = self.current_value

    prior_value: float | None | Unset
    if isinstance(self.prior_value, Unset):
      prior_value = UNSET
    else:
      prior_value = self.prior_value

    is_subtotal = self.is_subtotal

    depth = self.depth

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "element_qname": element_qname,
        "element_name": element_name,
        "classification": classification,
        "current_value": current_value,
      }
    )
    if prior_value is not UNSET:
      field_dict["prior_value"] = prior_value
    if is_subtotal is not UNSET:
      field_dict["is_subtotal"] = is_subtotal
    if depth is not UNSET:
      field_dict["depth"] = depth

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    element_qname = d.pop("element_qname")

    element_name = d.pop("element_name")

    classification = d.pop("classification")

    current_value = d.pop("current_value")

    def _parse_prior_value(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    prior_value = _parse_prior_value(d.pop("prior_value", UNSET))

    is_subtotal = d.pop("is_subtotal", UNSET)

    depth = d.pop("depth", UNSET)

    fact_row_response = cls(
      element_id=element_id,
      element_qname=element_qname,
      element_name=element_name,
      classification=classification,
      current_value=current_value,
      prior_value=prior_value,
      is_subtotal=is_subtotal,
      depth=depth,
    )

    fact_row_response.additional_properties = d
    return fact_row_response

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
