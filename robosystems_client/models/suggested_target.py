from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SuggestedTarget")


@_attrs_define
class SuggestedTarget:
  """A suggested mapping target from the reporting taxonomy.

  Attributes:
      element_id (str):
      qname (str):
      name (str):
      confidence (float | None | Unset):
  """

  element_id: str
  qname: str
  name: str
  confidence: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    qname = self.qname

    name = self.name

    confidence: float | None | Unset
    if isinstance(self.confidence, Unset):
      confidence = UNSET
    else:
      confidence = self.confidence

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "qname": qname,
        "name": name,
      }
    )
    if confidence is not UNSET:
      field_dict["confidence"] = confidence

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    qname = d.pop("qname")

    name = d.pop("name")

    def _parse_confidence(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    confidence = _parse_confidence(d.pop("confidence", UNSET))

    suggested_target = cls(
      element_id=element_id,
      qname=qname,
      name=name,
      confidence=confidence,
    )

    suggested_target.additional_properties = d
    return suggested_target

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
