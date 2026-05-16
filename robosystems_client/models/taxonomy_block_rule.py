from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxonomyBlockRule")


@_attrs_define
class TaxonomyBlockRule:
  """Rule projection for the Taxonomy Block envelope.

  Exactly one of ``rule_pattern`` (arithmetic) or ``rule_check_kind``
  (model-structure) is non-null per row, enforced by the
  ``check_rule_pattern_kind_xor`` DB constraint. See
  information-block.md §5.2.2.

      Attributes:
          id (str):
          name (str):
          rule_category (str):
          rule_expression (str):
          rule_pattern (None | str | Unset):
          rule_check_kind (None | str | Unset):
          severity (str | Unset):  Default: 'error'.
          origin (str | Unset): 'forked' | 'native' | 'auto' — matches DB CHECK. Default: 'native'.
          target_kind (None | str | Unset):
          target_ref (None | str | Unset): Polymorphic display string — structure_id, element qname, association_id, or
              taxonomy_id depending on ``target_kind``.
  """

  id: str
  name: str
  rule_category: str
  rule_expression: str
  rule_pattern: None | str | Unset = UNSET
  rule_check_kind: None | str | Unset = UNSET
  severity: str | Unset = "error"
  origin: str | Unset = "native"
  target_kind: None | str | Unset = UNSET
  target_ref: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    rule_category = self.rule_category

    rule_expression = self.rule_expression

    rule_pattern: None | str | Unset
    if isinstance(self.rule_pattern, Unset):
      rule_pattern = UNSET
    else:
      rule_pattern = self.rule_pattern

    rule_check_kind: None | str | Unset
    if isinstance(self.rule_check_kind, Unset):
      rule_check_kind = UNSET
    else:
      rule_check_kind = self.rule_check_kind

    severity = self.severity

    origin = self.origin

    target_kind: None | str | Unset
    if isinstance(self.target_kind, Unset):
      target_kind = UNSET
    else:
      target_kind = self.target_kind

    target_ref: None | str | Unset
    if isinstance(self.target_ref, Unset):
      target_ref = UNSET
    else:
      target_ref = self.target_ref

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "rule_category": rule_category,
        "rule_expression": rule_expression,
      }
    )
    if rule_pattern is not UNSET:
      field_dict["rule_pattern"] = rule_pattern
    if rule_check_kind is not UNSET:
      field_dict["rule_check_kind"] = rule_check_kind
    if severity is not UNSET:
      field_dict["severity"] = severity
    if origin is not UNSET:
      field_dict["origin"] = origin
    if target_kind is not UNSET:
      field_dict["target_kind"] = target_kind
    if target_ref is not UNSET:
      field_dict["target_ref"] = target_ref

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    rule_category = d.pop("rule_category")

    rule_expression = d.pop("rule_expression")

    def _parse_rule_pattern(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    rule_pattern = _parse_rule_pattern(d.pop("rule_pattern", UNSET))

    def _parse_rule_check_kind(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    rule_check_kind = _parse_rule_check_kind(d.pop("rule_check_kind", UNSET))

    severity = d.pop("severity", UNSET)

    origin = d.pop("origin", UNSET)

    def _parse_target_kind(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    target_kind = _parse_target_kind(d.pop("target_kind", UNSET))

    def _parse_target_ref(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    target_ref = _parse_target_ref(d.pop("target_ref", UNSET))

    taxonomy_block_rule = cls(
      id=id,
      name=name,
      rule_category=rule_category,
      rule_expression=rule_expression,
      rule_pattern=rule_pattern,
      rule_check_kind=rule_check_kind,
      severity=severity,
      origin=origin,
      target_kind=target_kind,
      target_ref=target_ref,
    )

    taxonomy_block_rule.additional_properties = d
    return taxonomy_block_rule

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
