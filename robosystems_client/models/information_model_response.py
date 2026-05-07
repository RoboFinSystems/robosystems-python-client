from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InformationModelResponse")


@_attrs_define
class InformationModelResponse:
  """The block's intrinsic shape — concept + member arrangement patterns.

  Attributes:
      concept_arrangement (None | str | Unset): roll_up | roll_forward | variance | adjustment | set | arithmetic |
          textblock. Null for block types where the concept arrangement is implicit in their mechanics.
      member_arrangement (None | str | Unset): aggregation | nonaggregation, or null if non-hypercube.
  """

  concept_arrangement: None | str | Unset = UNSET
  member_arrangement: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    concept_arrangement: None | str | Unset
    if isinstance(self.concept_arrangement, Unset):
      concept_arrangement = UNSET
    else:
      concept_arrangement = self.concept_arrangement

    member_arrangement: None | str | Unset
    if isinstance(self.member_arrangement, Unset):
      member_arrangement = UNSET
    else:
      member_arrangement = self.member_arrangement

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if concept_arrangement is not UNSET:
      field_dict["concept_arrangement"] = concept_arrangement
    if member_arrangement is not UNSET:
      field_dict["member_arrangement"] = member_arrangement

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_concept_arrangement(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    concept_arrangement = _parse_concept_arrangement(
      d.pop("concept_arrangement", UNSET)
    )

    def _parse_member_arrangement(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    member_arrangement = _parse_member_arrangement(d.pop("member_arrangement", UNSET))

    information_model_response = cls(
      concept_arrangement=concept_arrangement,
      member_arrangement=member_arrangement,
    )

    information_model_response.additional_properties = d
    return information_model_response

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
