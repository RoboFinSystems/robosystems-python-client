from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RuleTargetLite")


@_attrs_define
class RuleTargetLite:
  """Polymorphic rule target — points at the atom the rule is scoped to.

  Attributes:
      target_kind (str): Which atom type the rule targets — 'structure' | 'element' | 'association' | 'taxonomy'. Enum
          closure enforced by the ``public.rules`` CHECK constraint.
      target_ref_id (str): UUID of the target atom — structure_id, element_id, association_id, or taxonomy_id
          depending on ``target_kind``.
  """

  target_kind: str
  target_ref_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    target_kind = self.target_kind

    target_ref_id = self.target_ref_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "target_kind": target_kind,
        "target_ref_id": target_ref_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    target_kind = d.pop("target_kind")

    target_ref_id = d.pop("target_ref_id")

    rule_target_lite = cls(
      target_kind=target_kind,
      target_ref_id=target_ref_id,
    )

    rule_target_lite.additional_properties = d
    return rule_target_lite

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
